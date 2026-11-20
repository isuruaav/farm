"""One-time migration of the original static pages. Original sources are archived."""
from pathlib import Path
from html.parser import HTMLParser
import html
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]

class CardParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cards = []
        self.card = None
        self.depth = 0
        self.heading = False
        self.description = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'div' and 'product-item' in a.get('class', '').split():
            self.card = {'category': a['data-category'], 'title': '', 'description': ''}
            self.depth = 1
        elif self.card is not None:
            if tag == 'div': self.depth += 1
            if tag == 'h3': self.heading = True
            if tag == 'p' and not self.card['description']: self.description = True
            if tag == 'img': self.card['image'] = a['src']
            action = a.get('onclick', '')
            if action.startswith('addToCart('):
                obj = action[len('addToCart('):-1]
                for key, value in re.findall(r"(\w+):\s*('(?:[^'\\]|\\.)*'|[0-9.]+)", obj):
                    self.card[key] = value[1:-1].replace("\\'", "'") if value.startswith("'") else float(value)

    def handle_endtag(self, tag):
        if self.card is None: return
        if tag == 'h3': self.heading = False
        if tag == 'p': self.description = False
        if tag == 'div':
            self.depth -= 1
            if self.depth == 0:
                self.cards.append(self.card)
                self.card = None

    def handle_data(self, data):
        if self.card is not None:
            if self.heading: self.card['title'] += data.strip()
            if self.description: self.card['description'] += data.strip()

def name_fields(form, kind):
    names = {
        'contact': ['name','company','country','email','phone','inquiry_type','industry','message'],
        'export': ['name','company','country','port','email','phone','industry','quantity','sample','message'],
        'investment': ['name','company','country','phone','email','industry','investment_range','partnership_type','message'],
        'partner': ['name','company','partner_type','country','email','phone','address','industry','experience','message'],
    }[kind]
    fields = iter(names)
    def field(m):
        name = next(fields)
        tag = m[0]
        if ' name=' not in tag: tag = tag[:-1] + f' name="{name}">'
        if ' id=' not in tag: tag = tag[:-1] + f' id="{kind}-{name}">'
        if tag.startswith('<input'):
            limit = 254 if name == 'email' else 300 if name == 'address' else 180
            tag = tag[:-1] + f' maxlength="{limit}">'
        if tag.startswith('<textarea'): tag = tag[:-1] + ' maxlength="5000">'
        if name in ('name','email','phone','country','company'):
            autocomplete = {'name':'name','email':'email','phone':'tel','country':'country-name','company':'organization'}[name]
            tag = tag[:-1] + f' autocomplete="{autocomplete}">'
        return tag
    form = re.sub(r'<(?:input|select|textarea)\b[^>]*>', field, form)
    # Every visible control gets an explicit label association, including checkboxes.
    form = re.sub(r'(<label\b)([^>]*>)(.*?)(</label>\s*<(?:input|select|textarea)\b[^>]*id="([^"]+)"[^>]*>)',
                  lambda m: m[1]+' for="'+m[5]+'"'+m[2]+m[3]+m[4], form, flags=re.S)
    form = re.sub(r'<form\b([^>]*)>', lambda m: '<form'+m[1]+f' method="post" action="api/inquiries.php" data-inquiry="{kind}">\n'
        + '<?php form_security("'+kind+'"); ?>', form, count=1)
    consent = '<div class="form-privacy"><label><input type="checkbox" name="consent" value="1" required> <span>I agree to be contacted about this request. See our <a href="privacy-policy.php">Privacy Policy</a>.</span></label></div><p class="form-feedback" role="status" aria-live="polite" tabindex="-1" hidden></p>'
    form = form.replace('</form>', consent+'\n</form>')
    return form

def main():
    pages = sorted(ROOT.glob('*.html'))
    if not pages: raise SystemExit('No legacy HTML pages found; migration already completed.')
    (ROOT/'storage/backups').mkdir(parents=True, exist_ok=True)
    backup = ROOT/'storage/backups/original-static-site.zip'
    if backup.exists(): raise SystemExit('Backup already exists; refusing to overwrite original sources.')
    with zipfile.ZipFile(backup, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in pages + list((ROOT/'assets').rglob('*')) + list(ROOT.glob('*.py')):
            if p.is_file(): z.write(p, p.relative_to(ROOT))
    (ROOT/'views').mkdir(exist_ok=True)
    (ROOT/'data').mkdir(exist_ok=True)
    products = CardParser()
    products.feed((ROOT/'products.html').read_text(encoding='utf-8'))
    assert len(products.cards) == 20
    (ROOT/'data/products.json').write_text(json.dumps(products.cards, ensure_ascii=False, indent=2), encoding='utf-8')
    metadata = {}
    schemas = {}
    for p in pages:
        source = p.read_text(encoding='utf-8')
        title = html.unescape(re.search(r'<title>(.*?)</title>',source,re.S)[1]).strip()
        main = re.search(r'<main\b.*?</main>',source,re.S)[0]
        main = re.sub(r'([\w-]+)\.html',r'\1.php',main)
        main = main.replace('WCAG 2.2 AAA Target','Keyboard Accessible').replace('\ufffd','é')
        # Runtime inputs have names, bounds, consent, and a real endpoint.
        kind = {'contact':'contact','export':'export','investment':'investment','partners':'partner'}.get(p.stem)
        if kind:
            main = re.sub(r'<form\b.*?</form>',lambda m:name_fields(m[0],kind),main,flags=re.S)
            class FormSchema(HTMLParser):
                def __init__(self): super().__init__(); self.fields={}; self.select=None; self.option=None; self.option_text=''
                def handle_starttag(self,tag,attrs):
                    a=dict(attrs)
                    if tag in ('input','textarea','select') and a.get('name') not in (None,'consent'):
                        self.fields[a['name']]={'required':'required' in a,'type':a.get('type','text'),'max':int(a.get('maxlength','180'))}
                        if tag=='select': self.select=a['name']; self.fields[self.select]['options']=[]
                    if tag=='option': self.option=a.get('value'); self.option_text=''
                def handle_data(self,data):
                    if self.select: self.option_text+=data
                def handle_endtag(self,tag):
                    if tag=='option' and self.select:
                        value=self.option if self.option is not None else self.option_text.strip()
                        self.fields[self.select]['options'].append(value)
                    if tag=='select': self.select=None
            schema=FormSchema();schema.feed(main);schemas[kind]=schema.fields
        main = re.sub(r'<img\b(?![^>]*loading=)', '<img loading="lazy" decoding="async"', main)
        main = re.sub(r'target="_blank"(?!\s+rel=)', 'target="_blank" rel="noopener noreferrer"',main)
        main = re.sub(r'<i class="([^\"]*fa-arrow[^\"]*)"></i>', '', main)
        if p.stem == 'products':
            start = main.index('<div id="product-grid"')
            end = main.index('<!--',main.index('<!-- 8.',start)) if '<!-- 8.' in main[start:] else -1
            # Replace the complete grid using balanced div depth, leaving the surrounding sections.
            class GridEnd(HTMLParser):
                def __init__(self): super().__init__(); self.depth=0; self.started=False; self.end=None
                def handle_starttag(self,tag,attrs):
                    if tag=='div': self.depth+=1; self.started=True
                def handle_endtag(self,tag):
                    if tag=='div':
                        self.depth-=1
                        if self.started and self.depth==0 and self.end is None:
                            line,col=self.getpos(); self.end=sum(len(x) for x in self.rawdata.splitlines(keepends=True)[:line-1])+col+6
            parser=GridEnd();parser.feed(main[start:]);assert parser.end
            main=main[:start]+'''<div class="catalog-toolbar"><p id="product-results" role="status" aria-live="polite"></p><label for="product-sort">Sort by <select id="product-sort"><option value="featured">Featured</option><option value="name">Name: A–Z</option><option value="price-low">Price: low to high</option><option value="price-high">Price: high to low</option></select></label></div>
<div id="product-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
<?php foreach (catalog() as $product): require APP_ROOT . '/includes/product-card.php'; endforeach; ?>
</div><div id="product-empty" class="empty-state" hidden><h3>No matching products</h3><p>Try another search or choose a different category.</p><button type="button" class="btn-primary" onclick="resetProductFilters()">Reset filters</button></div>
<p class="catalog-note">Catalog images are illustrative. Listed prices are estimates; availability, delivery charges and final pricing are confirmed by our team.</p>'''+main[start+parser.end:]
            main=main.replace('onkeyup="searchProducts()"','oninput="searchProducts()" aria-label="Search products"')
            main=main.replace('sticky top-[73px]','catalog-filters sticky')
        if p.stem=='gallery':
            main=main.replace('<!-- Gallery', '<!-- Gallery',1)
            main=main.replace('<main id="main-content">','<main id="main-content"><p class="media-notice">Illustrative industry photography. Contact us to arrange a facility visit or request verified project photographs.</p>',1)
        main=main.replace('Dynamic Inquiry Form (විමසීම් පෝරමය)','Send an Inquiry / විමසීමක් යවන්න')
        main=main.replace('All submissions are logged directly into our central commercial registry.','Your request is saved securely for our team to review. Keep the reference number shown after submission.')
        main=re.sub(r'<!--.*?-->', '', main, flags=re.S)
        (ROOT/'views'/f'{p.stem}.php').write_text(main,encoding='utf-8')
        (ROOT/f'{p.stem}.php').write_text("<?php\ndeclare(strict_types=1);\n$page = '"+p.stem+"';\nrequire __DIR__ . '/includes/render.php';\n",encoding='utf-8')
        metadata[p.stem]={'title':title,'description':title.split('|')[0].strip()+' — FOREST LANKA agriculture, industry and trade in Sri Lanka.'}
    (ROOT/'data/pages.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2),encoding='utf-8')
    (ROOT/'data/forms.json').write_text(json.dumps(schemas,ensure_ascii=False,indent=2),encoding='utf-8')
    for p in pages: p.unlink()
    print(f'Migrated {len(pages)} pages and {len(products.cards)} products. Backup: {backup}')

if __name__=='__main__': main()
