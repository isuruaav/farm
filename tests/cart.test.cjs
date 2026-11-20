const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const products = JSON.parse(fs.readFileSync('data/products.json','utf8'));
const source = fs.readFileSync('assets/js/app.js','utf8');
function context(stored = '[]', blocked = false) {
  const elements = new Map([['product-catalog',{textContent:JSON.stringify(products)}]]);
  const document = {getElementById:id=>elements.get(id)||null,querySelectorAll:()=>[],querySelector:()=>null,addEventListener:()=>{}};
  const localStorage = {getItem:()=>{if(blocked)throw Error('blocked');return stored;},setItem:(key,value)=>{stored=value;}};
  const sandbox = vm.createContext({document,localStorage,Intl,console,setTimeout:()=>{},window:{addEventListener:()=>{}},URL,location:{href:'http://localhost/products.php'},history:{replaceState:()=>{}}});
  vm.runInContext(source,sandbox); return {sandbox,elements,document,run:code=>vm.runInContext(code,sandbox)};
}
let app=context('{broken');assert.equal(app.run('cart.length'),0);
app=context('[]',true);app.run("addToCart({id:'FL-EGG-30',price:1,name:'<script>bad</script>'})");assert.equal(app.run('cartTotal()'),1350);assert.equal(app.run('cart[0].name'),products[0].name);
app.run("addToCart({id:'FL-FEED-50'})");assert.equal(app.run('cart[1].id'),'FL-FEED-L50');
app.run('updateCartQuantity(0,-1)');assert.equal(app.run('cart.length'),1);
app.run('removeFromCart(999); updateCartQuantity(-1,1); clearCart()');assert.equal(app.run('cart.length'),0);
app=context('[{"id":"FL-EGG-30","quantity":999999},{"id":"bad","quantity":1},{"id":"FL-EGG-12","quantity":null}]');assert.equal(app.run('cart.length'),1);assert.equal(app.run('cart[0].quantity'),9999);
app.run("addToCart({id:'FL-EGG-30'})");assert.equal(app.run('cart[0].quantity'),9999);
assert.equal(app.run("escapeHtml('<img onerror=evil>')"),'&lt;img onerror=evil&gt;');
app=context();app.run("productMap.set('FL-EGG-30',{...productMap.get('FL-EGG-30'),minimumOrder:12});addToCart({id:'FL-EGG-30'})");assert.equal(app.run('cart[0].quantity'),12);
app.run('updateCartQuantity(0,-1)');assert.equal(app.run('cart.length'),0);
app.run("productMap.set('FL-EGG-30',{...productMap.get('FL-EGG-30'),availability:'unavailable'});addToCart({id:'FL-EGG-30'})");assert.equal(app.run('cart.length'),0);
const cards=[{dataset:{category:'poultry',name:'Eggs',price:'1350',quote:'false',position:'0'},textContent:'Fresh eggs',hidden:false},{dataset:{category:'feed',name:'Feed',price:'4500',quote:'false',position:'1'},textContent:'Layer feed',hidden:false}];
app.elements.set('product-grid',{querySelectorAll:()=>cards,append:()=>{}});app.elements.set('product-search-input',{value:'feed'});app.elements.set('product-sort',{value:'featured'});app.elements.set('product-results',{textContent:''});app.elements.set('product-empty',{hidden:true});
app.run("activeCategory='poultry'; applyProductFilters()");assert.equal(cards.filter(card=>!card.hidden).length,0);assert.equal(app.elements.get('product-empty').hidden,false);
app.run("activeCategory='feed'; applyProductFilters()");assert.equal(cards.filter(card=>!card.hidden).length,1);assert.equal(app.elements.get('product-results').textContent,'Showing 1 of 2 products');
console.log('PASS: Cart recovery, canonical pricing, legacy IDs, quantity bounds, HTML escaping, blocked storage and combined product filtering.');
