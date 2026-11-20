"""HTTP integration checks against an isolated PHP server and disposable SQLite DB."""
from pathlib import Path
from html.parser import HTMLParser
import collections
import http.cookiejar
import json
import os
import re
import secrets
import shutil
import socket
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
PHP=shutil.which('php')

class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.ids=[];self.links=[];self.forms=[];self.form=None;self.labels=[];self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag in ('a','link','script','img'):
            url=a.get('href',a.get('src',''))
            if url:self.links.append(url)
        if tag=='form':self.form={'attrs':a,'fields':[]};self.forms.append(self.form)
        if tag in ('input','select','textarea') and self.form is not None:self.form['fields'].append(a)
        if tag=='label' and a.get('for'):self.labels.append(a['for'])
    def handle_endtag(self,tag):
        if tag=='form':self.form=None

def main():
    passed=0
    def check(condition,message):
        nonlocal passed
        if not condition:raise AssertionError(message)
        passed+=1
    with tempfile.TemporaryDirectory(prefix='runtime-',dir=ROOT/'tests') as temp:
        env=os.environ.copy();env['FOREST_STORAGE_DIR']=str(Path(temp)/'storage')
        flags=getattr(subprocess,'CREATE_NO_WINDOW',0)
        def fixture(action,**values):
            result=subprocess.run([PHP,'-d',f'xdebug.log={temp}/xdebug.log',str(ROOT/'tests/db-fixture.php')],input=json.dumps({'action':action,**values}),capture_output=True,text=True,encoding='utf-8',env=env,creationflags=flags,check=True)
            return json.loads(result.stdout)
        password=secrets.token_urlsafe(24);fixture('create-admin',username='test-admin',password=password)
        with socket.socket() as sock:sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
        base=f'http://127.0.0.1:{port}/'
        log=open(Path(temp)/'server.log','w',encoding='utf-8')
        process=subprocess.Popen([PHP,'-d',f'xdebug.log={temp}/xdebug.log','-d','display_errors=0','-S',f'127.0.0.1:{port}','-t',str(ROOT),str(ROOT/'router.php')],stdout=log,stderr=log,env=env,cwd=ROOT,creationflags=flags)
        cookies=http.cookiejar.CookieJar();client=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookies))
        def request(path,data=None,json_body=False,headers=None,opener=client):
            h=headers or {}
            if data is not None:
                if json_body:data=json.dumps(data).encode();h={**h,'Content-Type':'application/json','Accept':'application/json'}
                else:data=urllib.parse.urlencode(data).encode()
            req=urllib.request.Request(urllib.parse.urljoin(base,path),data=data,headers=h)
            try:r=opener.open(req,timeout=10)
            except urllib.error.HTTPError as error:r=error
            content=r.read();return r.status,content.decode('utf-8',errors='replace'),r.headers,r.geturl()
        try:
            for _ in range(50):
                try:request('index.php');break
                except urllib.error.URLError:time.sleep(.1)
            else:raise RuntimeError('PHP server did not start')
            pages=json.loads((ROOT/'data/pages.json').read_text(encoding='utf-8'))
            local_assets=set()
            for slug in pages:
                status,text,headers,_=request(slug+'.php');doc=Page(text)
                check(status==200,f'{slug} HTTP status {status}')
                check(not re_error(text),f'{slug} exposes a PHP error')
                check(len(doc.ids)==len(set(doc.ids)),f'{slug}: duplicate IDs')
                check('main-content' in doc.ids,f'{slug}: missing main landmark')
                check('<html lang="en">' in text,f'{slug}: page language must be English')
                check(not re.search(r'[\u0d80-\u0dff]|data-lang=|data-lang-choice=|language-switch',text),f'{slug}: non-English content or language controls remain')
                check("script-src 'self'" in headers.get('Content-Security-Policy',''),f'{slug}: CSP missing')
                for link in doc.links:
                    url=urllib.parse.urlsplit(link)
                    if url.scheme or url.netloc:continue
                    if not url.path:
                        check(not url.fragment or url.fragment in doc.ids,f'{slug}: broken anchor {link}')
                    elif url.path.startswith('assets/'):local_assets.add(url.path)
                    elif url.path.endswith('.php'):
                        target=ROOT/url.path
                        check(target.is_file(),f'{slug}: broken link {link}')
                for form in doc.forms:
                    check('data-inquiry' in form['attrs'],f'{slug}: form has no submission handler')
                    names=[field.get('name') for field in form['fields']]
                    check(all(names),f'{slug}: unnamed form field')
                    check(len(names)==len(set(names)),f'{slug}: duplicate form fields')
                    check({'csrf_token','type','request_id','consent'}.issubset(names),f'{slug}: form security missing')
            for asset in local_assets:
                status,text,_,_=request(asset);check(status==200,f'Missing asset {asset}')
            status,text,_,url=request('about.html?source=legacy');check(status==200 and 'about.php?source=legacy' in url,'Legacy URL redirect failed')
            for path in ['storage/forest-lanka.sqlite','data/products.json','includes/bootstrap.php','tools/create-admin.php','tests/db-fixture.php','.cache/npm/','node_modules/tailwindcss/index.css','config.php','base_templates.py']:
                status,*_=request(path);check(status==403,f'Private path exposed: {path}, {status}')
            status,text,_,_=request('not-a-page');check(status==404 and 'back on track' in text,'Missing page handling failed')
            status,text,headers,_=request('api/inquiries.php',headers={'Accept':'application/json'});check(status==405 and headers.get('Allow')=='POST','API method restriction failed')
            status,text,_,_=request('contact.php');doc=Page(text)
            form=next(form for form in doc.forms if form['attrs'].get('data-inquiry')=='contact')
            hidden={field['name']:field.get('value','') for field in form['fields'] if field.get('type')=='hidden'}
            payload={**hidden,'name':'Integration Test','company':'Test Company','country':'Sri Lanka','email':'test@example.test','phone':'+94712345678','inquiry_type':'other','industry':'ind_poultry','message':'Test quotation request.','consent':'1'}
            def submit(values):
                status,text,headers,_=request('api/inquiries.php',values,True);return status,json.loads(text),headers
            status,result,_=submit({**payload,'csrf_token':'bad'});check(status==419 and not result['ok'],'CSRF bypass')
            status,result,_=submit({**payload,'email':'invalid','phone':'abc','industry':'unknown','consent':'0'});check(status==422 and {'email','phone','industry','consent'}.issubset(result['errors']),'Validation failed')
            status,result,_=submit({**payload,'name':['unsafe']});check(status==422,'Array field should be rejected')
            status,result,_=submit({**payload,'website':'https://spam.test'});check(status==422,'Spam honeypot failed')
            status,result,_=submit(payload);check(status==201 and result['reference'].startswith('INQ-'),'Contact save failed');reference=result['reference']
            status,result,_=submit(payload);check(status==201 and result['reference']==reference and len(fixture('records'))==1,'Retry created duplicate')
            order={**hidden,'type':'order','request_id':secrets.token_hex(16),'name':'Order Test','phone':'+94712345678','city':'Colombo','address':'Test Address','payment_method':'b2b_quotation','consent':'1','items':[{'id':'FL-EGG-30','quantity':2,'price':1}]}
            status,result,_=submit(order);check(status==201 and result['estimated_total']==2700,'Server trusted a tampered price')
            status,result,_=submit({**order,'request_id':secrets.token_hex(16),'items':[{'id':'UNKNOWN','quantity':1}]});check(status==422,'Unknown product accepted')
            schemas=json.loads((ROOT/'data/forms.json').read_text(encoding='utf-8'))
            fixture('reset-rates')
            for kind in ['export','investment','partner','sector']:
                values={**hidden,'type':kind,'request_id':secrets.token_hex(16),'consent':'1'}
                for name,rules in schemas[kind].items():
                    values[name]=next((v for v in rules.get('options',[]) if v),'Test value')
                    if name=='email':values[name]='test@example.test'
                    if name=='phone':values[name]='+94712345678'
                    if name=='sample':values[name]='1'
                status,result,_=submit(values);check(status==201,f'{kind} submission failed: {result}')
            status,text,_,_=request('admin/?download=csv');check('Welcome back.' in text and reference not in text,'Anonymous access exposed records')
            for private in ['admin/catalog.php','admin/industries.php','admin/site.php']:
                status,text,_,_=request(private);check(status==200 and 'Welcome back.' in text,f'Unauthenticated access to {private}')
            status,text,_,_=request('admin/')
            admin=Page(text);token=next(f['value'] for f in admin.forms[0]['fields'] if f['name']=='csrf_token')
            status,text,_,_=request('admin/',{'action':'login','csrf_token':token,'username':'test-admin','password':password});check(status==200 and 'Your inquiry desk' in text,'Admin login failed')
            check(reference in text,'Saved inquiry absent in dashboard')
            record=fixture('records')[0]
            status,text,_,_=request('admin/?id='+str(record['id']));admin=Page(text)
            security=next(f['value'] for f in admin.forms[0]['fields'] if f['name']=='csrf_token')
            status,text,_,_=request('admin/',{'action':'update','csrf_token':security,'id':record['id'],'status':'in_progress','notes':'Reviewed during test'});check(status==200 and 'Request updated.' in text,'Admin update failed')
            check(fixture('records')[0]['status']=='in_progress','Status update not persisted')
            status,text,_,_=request('admin/?q=Integration');check(reference in text and 'Order Test' not in text,'Admin search failed')
            status,text,_,_=request('admin/?download=csv&token='+security);check(status==200 and reference in text and "'+947" in text,'CSV export or formula protection failed')
            status,text,_,_=request('admin/?download=csv&token=bad');check(status==403,'CSV token bypass')
            status,text,_,_=request('admin/catalog.php?new=1');check(status==200 and 'New product' in text,'Catalog editor failed')
            managed={'action':'save','is_new':'1','csrf_token':security,'sku':'FL-TEST-PDF','category':'poultry','name':'Test product','title':'Test catalog product','description':'A test description.','detail_text':'<script>alert(1)</script>','variant':'Test pack','price':'1250','price_type':'fixed','minimum_order':'5','availability':'on_request','publication':'published','featured':'1','image':'assets/images/industries/eggs.jpg','seo_description':'Test product information.'}
            status,text,_,_=request('admin/catalog.php?new=1',{**managed,'csrf_token':'bad'});check(status==419,'Catalog CSRF bypass')
            status,text,_,_=request('admin/catalog.php?new=1',managed);check(status==200 and 'Catalog changes saved.' in text,'Product creation failed')
            status,text,_,_=request('product.php?sku=FL-TEST-PDF');check(status==200 and 'Test catalog product' in text and '&lt;script&gt;alert(1)&lt;/script&gt;' in text and '<script>alert(1)</script>' not in text,'Product detail or output escaping failed')
            check('Minimum order' in text and 'canonical' in text,'Product metadata or minimum missing')
            fixture('reset-rates')
            test_order={**order,'csrf_token':security,'request_id':secrets.token_hex(16),'items':[{'id':'FL-TEST-PDF','quantity':4}]}
            status,result,_=submit(test_order);check(status==422 and 'minimum quantity' in result['errors']['items'],'Product order minimum bypass')
            status,result,_=submit({**test_order,'request_id':secrets.token_hex(16),'items':[{'id':'FL-TEST-PDF','quantity':5,'price':1}]});check(status==201 and result['estimated_total']==6250,'Managed price was not used')
            managed.update({'is_new':'0','price':'1500','availability':'unavailable'})
            status,text,_,_=request('admin/catalog.php?sku=FL-TEST-PDF',managed);check(status==200,'Product editing failed')
            status,result,_=submit({**test_order,'request_id':secrets.token_hex(16),'items':[{'id':'FL-TEST-PDF','quantity':5}]});check(status==422,'Unavailable product accepted')
            managed['publication']='draft'
            request('admin/catalog.php?sku=FL-TEST-PDF',managed)
            status,text,_,_=request('product.php?sku=FL-TEST-PDF');check(status==404,'Draft product is public')
            managed.update({'publication':'published','availability':'available'})
            request('admin/catalog.php?sku=FL-TEST-PDF',managed)
            status,result,_=submit({**test_order,'request_id':secrets.token_hex(16),'items':[{'id':'FL-TEST-PDF','quantity':5}]});check(status==201 and result['estimated_total']==7500,'Edited product price not persisted')
            status,text,_,_=request('admin/catalog.php',{'action':'archive','csrf_token':security,'sku':'FL-TEST-PDF'});check(status==200,'Product archiving failed')
            status,text,_,_=request('product.php?sku=FL-TEST-PDF');check(status==404,'Archived product is public')
            stage={'csrf_token':security,'slug':'mushrooms','status':'development','summary':'A controlled cultivation project with fresh and dried mushroom supply concepts.'}
            status,text,_,_=request('admin/industries.php',stage);check(status==200 and 'Project stage and summary updated.' in text,'Project stage update failed')
            status,text,_,_=request('industry-mushrooms.php');check('Under development' in text and stage['summary'] in text,'Project stage is not reflected on the public page')
            site_values={'csrf_token':security,'headline':'Growing together through agriculture.','summary':'Eight connected industries for agricultural products, responsible manufacturing and global trade.','intro':'A Sri Lankan agricultural portfolio connecting local products and international business opportunities.','phone':'+94 71 234 5678','whatsapp':'94712345678','email':'qa@example.test','address':'Test contact address, Sri Lanka.','hours':'Monday to Friday, 9 AM to 5 PM'}
            status,text,_,_=request('admin/site.php',site_values);check(status==200 and 'Website content saved.' in text,'Website content update failed')
            status,text,_,_=request('index.php');check(site_values['headline'] in text and 'qa@example.test' in text and site_values['address'] in text,'Homepage/contact content was not updated')
            status,text,_,_=request('sitemap.xml');sitemap=ET.fromstring(text);locations=[node.text for node in sitemap.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
            check(status==200 and len(locations)==42 and any('product.php?sku=FL-EGG-30' in loc for loc in locations) and not any('FL-TEST-PDF' in loc for loc in locations),'Sitemap failed to include published pages/products only')
            status,text,_,_=request('robots.txt');check(status==200 and 'Disallow: /admin/' in text and 'Sitemap:' in text,'Robots configuration failed')
            status,text,_,_=request('admin/',{'action':'logout','csrf_token':security});check('Welcome back.' in text,'Logout failed')
            status,text,_,_=request('contact.php')
            current_form=next(form for form in Page(text).forms if form['attrs'].get('data-inquiry')=='contact')
            payload.update({field['name']:field.get('value','') for field in current_form['fields'] if field.get('type')=='hidden'})
            status,text,_,url=request('api/inquiries.php',{**payload,'request_id':secrets.token_hex(16)})
            check(status==200 and 'request-result.php' in url and 'Your request is saved' in text,'Native form submission failed')
            fixture('reset-rates')
            for index in range(13):status,result,headers=submit({**payload,'request_id':secrets.token_hex(16)})
            check(status==429 and headers.get('Retry-After')=='600','Submission rate limit failed')
            print(f'PASS: {passed} HTTP, form, security, persistence, catalog and admin checks across {len(pages)} pages.')
        finally:
            process.terminate();process.wait(timeout=10);log.close()

def re_error(text):
    return any(marker in text for marker in ('Fatal error:','Warning:','Parse error:','Stack trace:'))

if __name__=='__main__':main()
