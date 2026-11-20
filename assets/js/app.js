'use strict';

const storage = {
  get(key, fallback) { try { return JSON.parse(localStorage.getItem(key)) ?? fallback; } catch { return fallback; } },
  set(key, value) { try { localStorage.setItem(key, JSON.stringify(value)); } catch {} }
};
const catalogProducts = JSON.parse(document.getElementById('product-catalog')?.textContent || '[]');
const productMap = new Map(catalogProducts.map(product => [product.id, product]));
const legacyIds = {'FL-FEED-50':'FL-FEED-L50','FL-TRAY-100':'FL-TRAY-B100','FL-POWDER-20':'FL-EP-WHOLE20'};
const exchangeRates = {
  LKR: { rate: 1, symbol: 'LKR ', locale: 'en-LK' },
  USD: { rate: 0.0032, symbol: '$ ', locale: 'en-US' },
  EUR: { rate: 0.0030, symbol: '€ ', locale: 'de-DE' },
  AED: { rate: 0.0118, symbol: 'AED ', locale: 'en-AE' }
};
let currentCurrency = storage.get('forest_lanka_currency', 'LKR');
function formatMoney(value, curr = currentCurrency) {
  if (curr === 'LKR') {
    return new Intl.NumberFormat('en-LK', {style:'currency',currency:'LKR'}).format(value);
  }
  const config = exchangeRates[curr] || exchangeRates.LKR;
  const converted = value * config.rate;
  if (curr === 'USD') return new Intl.NumberFormat('en-US', {style:'currency',currency:'USD'}).format(converted);
  if (curr === 'EUR') return new Intl.NumberFormat('de-DE', {style:'currency',currency:'EUR'}).format(converted);
  return `${config.symbol}${converted.toFixed(2)}`;
}
const money = value => formatMoney(value, currentCurrency);
const escapeHtml = value => String(value ?? '').replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
function normalizeCart(value) {
  if (!Array.isArray(value)) return [];
  const merged = new Map();
  for (const item of value.slice(0, 50)) {
    if (!item || typeof item !== 'object') continue;
    const product = productMap.get(legacyIds[item.id] || item.id), quantity = Number(item.quantity);
    if (!product || product.availability === 'unavailable' || !Number.isSafeInteger(quantity) || quantity < 1) continue;
    merged.set(product.id, {...product, quantity:Math.min(9999, quantity + (merged.get(product.id)?.quantity || 0))});
  }
  return [...merged.values()];
}
let cart = normalizeCart(storage.get('forest_lanka_cart', []));
let activeCategory = 'all', activeDialog = null, returnFocus = null, inertElements = [];

function showToast(message, icon = 'fa-check-circle') {
  const container = document.getElementById('toast-container'); if (!container) return;
  const toast = document.createElement('div'), symbol = document.createElement('i'), label = document.createElement('span');
  toast.className = 'toast'; symbol.className = 'fas ' + (/^fa-[a-z-]+$/.test(icon) ? icon : 'fa-check-circle');
  symbol.setAttribute('aria-hidden','true'); label.textContent = message;
  toast.append(symbol,label); container.append(toast); setTimeout(() => toast.remove(),6500);
}
function persistCart() { storage.set('forest_lanka_cart',cart); updateCartUI(); }
function addToCart(input) {
  const product = productMap.get(legacyIds[input?.id] || input?.id);
  if (!product || product.availability === 'unavailable') { showToast('This product is unavailable. Please browse the current catalog.','fa-circle-info'); return; }
  const existing = cart.find(item => item.id === product.id);
  if (existing?.quantity >= 9999) { showToast('Maximum quantity reached.','fa-circle-info'); return; }
  if (existing) existing.quantity=Math.max(existing.quantity+1,product.minimumOrder||1); else cart.push({...product,quantity:product.minimumOrder||1});
  persistCart(); showToast(`${product.name} added to your inquiry cart.`,'fa-bag-shopping');
}
function removeFromCart(index) { if (cart[index]) { cart.splice(index,1); persistCart(); } }
function updateCartQuantity(index,change) { if (!cart[index] || ![-1,1].includes(change)) return; cart[index].quantity = Math.min(9999,cart[index].quantity+change); if (cart[index].quantity<(cart[index].minimumOrder||1)) cart.splice(index,1); persistCart(); }
function clearCart() { cart=[]; persistCart(); }
function cartTotal() { return cart.reduce((total,item) => total+(item.priceType==='fixed'?item.price*item.quantity:0),0); }
function estimate() { return money(cartTotal())+(cart.some(item=>item.priceType!=='fixed')?' + quote items':''); }
function updateCartUI() {
  const count = cart.reduce((total,item)=>total+item.quantity,0);
  document.querySelectorAll('.cart-count-badge').forEach(badge=>{badge.textContent=count>99?'99+':count;badge.hidden=!count;});
  const list = document.getElementById('cart-items-list');
  if (list) list.innerHTML=cart.length?cart.map((item,index)=>`<div class="cart-row"><div class="cart-row-details"><h3>${escapeHtml(item.name)}</h3><p>${escapeHtml(item.variant)} · ${escapeHtml(item.industry)}</p><strong>${item.priceType==='fixed'?money(item.price):'Quotation required'}</strong></div><div class="cart-row-controls"><div class="quantity-control"><button type="button" onclick="updateCartQuantity(${index},-1)" aria-label="Decrease ${escapeHtml(item.name)} quantity">−</button><span aria-label="Quantity">${item.quantity}</span><button type="button" onclick="updateCartQuantity(${index},1)" aria-label="Increase ${escapeHtml(item.name)} quantity" ${item.quantity>=9999?'disabled':''}>+</button></div><button type="button" class="remove-item" onclick="removeFromCart(${index})" aria-label="Remove ${escapeHtml(item.name)}">Remove</button></div></div>`).join(''):'<div class="empty-state"><i class="fas fa-basket-shopping" aria-hidden="true"></i><h3>Your inquiry cart is empty</h3><p>Explore our products and add what you need.</p><a href="products.php" class="btn-primary">Explore products</a></div>';
  const subtotal=document.getElementById('cart-subtotal');if(subtotal)subtotal.textContent=estimate();
  const proceed=document.querySelector('#cart-drawer [onclick="openCheckoutModal()"]');if(proceed)proceed.disabled=!cart.length;
}
function showDialog(element) {
  if (!element) return;
  if(activeDialog)hideDialog(activeDialog,false);
  returnFocus=document.activeElement;activeDialog=element;element.inert=false;element.classList.add('active');
  element.setAttribute('aria-hidden','false');element.setAttribute('role','dialog');element.setAttribute('aria-modal','true');element.tabIndex=-1;
  let branch=element;
  while(branch.parentElement && branch.parentElement!==document.documentElement){
    for(const sibling of branch.parentElement.children)if(sibling!==branch && sibling.id!=='toast-container' && !sibling.inert && !['SCRIPT','STYLE'].includes(sibling.tagName)){sibling.inert=true;inertElements.push(sibling);}
    branch=branch.parentElement;
  }
  document.body.classList.add('dialog-open');(element.querySelector('button,a[href],input:not([type="hidden"]),select,textarea')||element).focus();
}
function hideDialog(element,restore=true) {
  if(!element||activeDialog!==element)return;
  element.classList.remove('active');element.setAttribute('aria-hidden','true');element.inert=true;
  inertElements.forEach(node=>node.inert=false);inertElements=[];activeDialog=null;document.body.classList.remove('dialog-open');
  if(restore&&returnFocus?.isConnected)returnFocus.focus();
}
function openCartDrawer(){showDialog(document.getElementById('cart-drawer'));const overlay=document.getElementById('cart-drawer-overlay');if(overlay){overlay.inert=false;overlay.classList.add('active');}}
function closeCartDrawer(){hideDialog(document.getElementById('cart-drawer'));document.getElementById('cart-drawer-overlay')?.classList.remove('active');}
function populateCheckoutSummary(){
  const summary=document.getElementById('checkout-items-summary');
  if(summary)summary.innerHTML=cart.map(item=>`<div class="summary-row"><span>${escapeHtml(item.name)} <small>× ${item.quantity}</small></span><strong>${item.priceType==='fixed'?money(item.price*item.quantity):'Quote'}</strong></div>`).join('');
  const total=document.getElementById('checkout-total-amount');if(total)total.textContent=estimate();
  const input=document.getElementById('checkout-items-input');if(input)input.value=JSON.stringify(cart.map(({id,quantity})=>({id,quantity})));
}
function openCheckoutModal(){
  if(!cart.length){showToast('Add products before requesting a quotation.','fa-circle-info');return;}
  closeCartDrawer();document.getElementById('checkout-form').hidden=false;document.getElementById('checkout-success').hidden=true;
  populateCheckoutSummary();showDialog(document.getElementById('checkout-modal'));
}
function closeCheckoutModal(){hideDialog(document.getElementById('checkout-modal'));}
function sendOrderViaWhatsApp(){
  const form=document.getElementById('checkout-form');if(!form||!form.reportValidity()||!cart.length)return;
  const values=new FormData(form);
  let message=`FOREST LANKA — Quotation request\nName: ${values.get('name')}\nPhone: ${values.get('phone')}\nCity: ${values.get('city')}\nAddress: ${values.get('address')}\n`;
  if(values.get('email'))message+=`Email: ${values.get('email')}\n`;
  message+='\n'+cart.map(item=>`${item.name} (${item.variant}) × ${item.quantity}`).join('\n');
  message+=`\nEstimated listed total: ${money(cartTotal())}\n${values.get('message')||''}\nPlease confirm final pricing and availability.`;
  const desk = document.querySelector('meta[name="whatsapp-number"]')?.content || '94719740798';
  window.open(`https://wa.me/${/^\d{7,15}$/.test(desk)?desk:'94719740798'}?text=${encodeURIComponent(message)}`,'_blank','noopener,noreferrer');
  showToast('WhatsApp draft opened. Send it in WhatsApp to deliver your request.','fa-comment');
}
function clearFormErrors(form){form.querySelectorAll('.field-error').forEach(node=>node.remove());form.querySelectorAll('[aria-invalid]').forEach(field=>{field.removeAttribute('aria-invalid');field.removeAttribute('aria-describedby');});}
function displayFormErrors(form,errors){
  for(const [name,message]of Object.entries(errors||{})){
    const field=form.elements.namedItem(name);if(!(field instanceof HTMLElement)||field.type==='hidden')continue;
    const error=document.createElement('span');error.className='field-error';error.id=`error-${form.dataset.inquiry}-${name}`;error.textContent=message;
    field.setAttribute('aria-invalid','true');field.setAttribute('aria-describedby',error.id);(field.type==='checkbox'?field.closest('label'):field).after(error);
  }
  form.querySelector('[aria-invalid]')?.focus();
}
function newRequestId(){return Array.from(crypto.getRandomValues(new Uint8Array(16)),byte=>byte.toString(16).padStart(2,'0')).join('');}
async function submitInquiry(event){
  event.preventDefault();const form=event.currentTarget;if(form.dataset.busy==='true'||!form.reportValidity())return;
  if(form.dataset.inquiry==='order')populateCheckoutSummary();clearFormErrors(form);
  const feedback=form.querySelector('.form-feedback'),submit=form.querySelector('[type="submit"]'),label=submit?.innerHTML;
  const submittedCart=cart.map(({id,quantity})=>({id,quantity}));
  form.dataset.busy='true';form.setAttribute('aria-busy','true');if(submit){submit.disabled=true;submit.textContent='Saving your request…';}feedback.hidden=true;
  try{
    const response=await fetch(form.action,{method:'POST',body:new FormData(form),headers:{Accept:'application/json'},credentials:'same-origin'});
    let result;try{result=await response.json();}catch{throw new Error('The server could not process your request. Please try again or contact us by phone.');}
    if(!response.ok||!result.ok){feedback.className='form-feedback form-error';feedback.textContent=result.message||'Your request could not be saved.';feedback.hidden=false;displayFormErrors(form,result.errors);if(!form.querySelector('[aria-invalid]'))feedback.focus();return;}
    form.reset();form.elements.request_id.value=newRequestId();feedback.className='form-feedback form-success';feedback.textContent=`${result.message} Reference: ${result.reference}`;feedback.hidden=false;feedback.focus();
    if(form.dataset.inquiry==='order'){
      cart=normalizeCart(storage.get('forest_lanka_cart',cart)).map(item=>({...item,quantity:item.quantity-(submittedCart.find(sent=>sent.id===item.id)?.quantity||0)})).filter(item=>item.quantity>0);persistCart();form.hidden=true;
      const success=document.getElementById('checkout-success');success.innerHTML=`<i class="fas fa-circle-check" aria-hidden="true"></i><h3>Thank you. Your request is saved.</h3><p>Our team will review your requirements and contact you.</p><p class="reference-number">${escapeHtml(result.reference)}</p><p>This is a quotation request. Delivery and payment arrangements require confirmation.</p><button type="button" class="btn-primary" onclick="closeCheckoutModal()">Continue browsing</button>`;success.hidden=false;success.tabIndex=-1;success.focus();
    }
  }catch(error){feedback.className='form-feedback form-error';feedback.textContent=error.message||'Connection lost. Your details are kept; try again.';feedback.hidden=false;feedback.focus();}
  finally{form.dataset.busy='false';form.removeAttribute('aria-busy');if(submit){submit.disabled=false;submit.innerHTML=label;}}
}
function filterCategory(category,button){
  activeCategory=category;
  document.querySelectorAll('.prod-cat-btn').forEach(item=>{const active=item===button;item.setAttribute('aria-pressed',String(active));item.classList.toggle('bg-forest',active);item.classList.toggle('text-gold',active);item.classList.toggle('bg-gray-100',!active);item.classList.toggle('text-gray-700',!active);});applyProductFilters();
}
function searchProducts(){applyProductFilters();}
function applyProductFilters(){
  const grid=document.getElementById('product-grid');if(!grid)return;
  const query=(document.getElementById('product-search-input')?.value||'').trim().toLocaleLowerCase(),sort=document.getElementById('product-sort')?.value||'featured',cards=[...grid.querySelectorAll('.product-item')];let count=0;
  cards.forEach(card=>{card.hidden=!((activeCategory==='all'||card.dataset.category===activeCategory)&&card.textContent.toLocaleLowerCase().includes(query));if(!card.hidden)count++;});
  cards.sort((a,b)=>{if(sort==='name')return a.dataset.name.localeCompare(b.dataset.name);if(sort.startsWith('price-')){if(a.dataset.quote!==b.dataset.quote)return a.dataset.quote==='true'?1:-1;return(Number(a.dataset.price)-Number(b.dataset.price))*(sort==='price-high'?-1:1);}return Number(a.dataset.position)-Number(b.dataset.position);}).forEach(card=>grid.append(card));
  document.getElementById('product-results').textContent=`Showing ${count} of ${cards.length} products`;document.getElementById('product-empty').hidden=count>0;
  const url=new URL(location.href);for(const[key,value]of Object.entries({q:query,category:activeCategory==='all'?'':activeCategory,sort:sort==='featured'?'':sort})){if(value)url.searchParams.set(key,value);else url.searchParams.delete(key);}history.replaceState(null,'',url);
}
function resetProductFilters(){document.getElementById('product-search-input').value='';document.getElementById('product-sort').value='featured';filterCategory('all',document.querySelector('.prod-cat-btn'));}
function filterGallery(category,button){document.querySelectorAll('.gallery-filter-btn').forEach(item=>{const active=item===button;item.setAttribute('aria-pressed',String(active));for(const name of ['bg-forest','text-gold'])item.classList.toggle(name,active);for(const name of ['bg-gray-100','text-gray-700'])item.classList.toggle(name,!active);});document.querySelectorAll('.gallery-item').forEach(item=>item.hidden=category!=='all'&&item.dataset.cat!==category);}
function openGalleryModal(src,caption){const image=document.getElementById('lightbox-img');const local=/^assets\/images\/[a-zA-Z0-9_./-]+$/.test(src)&&!src.includes('..');if(!image||(!local&&!/^https:\/\/images\.unsplash\.com\//.test(src)))return;image.src=src;image.alt=caption||'Industry photograph';document.getElementById('lightbox-caption').textContent=caption||'';const dialog=document.getElementById('gallery-lightbox-modal');dialog?.setAttribute('aria-label','Industry photo viewer');showDialog(dialog);}
function closeGalleryModal(){hideDialog(document.getElementById('gallery-lightbox-modal'));}

function setCurrency(curr) {
  if (!exchangeRates[curr]) return;
  currentCurrency = curr;
  storage.set('forest_lanka_currency', curr);
  document.querySelectorAll('.currency-btn').forEach(btn => {
    btn.classList.toggle('is-active', btn.dataset.currency === curr);
  });
  updateCartUI();
  document.querySelectorAll('.product-item').forEach(card => {
    const isQuote = card.dataset.quote === 'true';
    const priceEl = card.querySelector('.product-card-price');
    if (priceEl) priceEl.textContent = isQuote ? 'Request a quotation' : formatMoney(Number(card.dataset.price), curr);
  });
  const detailPrice = document.querySelector('.detail-price');
  if (detailPrice && detailPrice.dataset.price) {
    const isQuote = detailPrice.dataset.quote === 'true';
    detailPrice.firstChild.textContent = isQuote ? 'Request a quotation' : formatMoney(Number(detailPrice.dataset.price), curr);
  }
}

function openProductQuickView(id) {
  const product = productMap.get(legacyIds[id] || id);
  if (!product) return;
  const modal = document.getElementById('quickview-modal');
  if (!modal) return;
  const img = document.getElementById('quickview-img');
  if (img) {
    img.src = product.image || (product.category === 'water-tech' ? 'assets/images/industries/water-tech.jpg' : 'assets/images/industries/landscape.jpg');
    img.alt = product.title || product.name;
  }
  const title = document.getElementById('quickview-title'); if (title) title.textContent = product.title || product.name;
  const industry = document.getElementById('quickview-industry'); if (industry) industry.textContent = product.industry;
  const desc = document.getElementById('quickview-desc'); if (desc) desc.textContent = product.description;
  const variant = document.getElementById('quickview-variant'); if (variant) variant.textContent = `${product.variant}${product.minimumOrder > 1 ? ' · Minimum order ' + product.minimumOrder : ''}`;
  const price = document.getElementById('quickview-price'); if (price) price.textContent = product.priceType === 'quote' ? 'Request a quotation' : formatMoney(Number(product.price));
  const avail = document.getElementById('quickview-avail'); if (avail) avail.textContent = product.availability === 'unavailable' ? 'Temporarily unavailable' : 'Availability confirmed with quotation';
  const link = document.getElementById('quickview-link'); if (link) link.href = `product.php?sku=${encodeURIComponent(product.id)}`;
  const addBtn = document.getElementById('quickview-add-btn');
  if (addBtn) {
    addBtn.disabled = product.availability === 'unavailable';
    addBtn.onclick = () => { addToCart(product); closeProductQuickView(); };
  }
  showDialog(modal);
}
function closeProductQuickView() {
  hideDialog(document.getElementById('quickview-modal'));
}

function toggleAiDrawer() {
  const drawer = document.getElementById('ai-drawer');
  const overlay = document.getElementById('ai-drawer-overlay');
  if (!drawer) return;
  const isOpen = drawer.classList.contains('active');
  if (isOpen) {
    hideDialog(drawer);
    overlay?.classList.remove('active');
  } else {
    showDialog(drawer);
    overlay?.classList.add('active');
    document.getElementById('ai-input-field')?.focus();
  }
}

function askAiQuestion(query) {
  const input = document.getElementById('ai-input-field');
  if (input) {
    input.value = query;
    handleAiChatSubmit(new Event('submit'));
  }
}

const aiKnowledge = [
  {
    triggers: ['export', 'port', 'ship', 'transit', 'freight', 'container', 'incoterm'],
    answer: '<strong>Forest Lanka Global Trade Desk:</strong> We export via Port of Colombo (CMB) with fast transit lines: Jebel Ali Dubai (4 days), Malé Maldives (2 days), Singapore (5 days), Doha Qatar (5 days), and Rotterdam EU (18 days). Available container specs include 40ft HC Reefers (2-4°C) for Fresh Eggs, 20ft Food-Grade dry for Egg Powders, and 40ft HC for Molded Trays. We support FOB Colombo, CIF and CFR terms.'
  },
  {
    triggers: ['feed', 'mill', 'poultry feed', 'protein', 'pellet'],
    answer: '<strong>Precision Animal Feed Manufacturing:</strong> Our feed mill facility executes a certified 12-stage automated production process: Raw Material Sourcing &rarr; NIR Inspection &rarr; Pre-Cleaning &rarr; Grinding &rarr; Precision Micro-Dosing Formulation &rarr; High-Shear Mixing &rarr; Steam Pelletizing (84.8°C) &rarr; Counterflow Cooling &rarr; Quality Testing &rarr; Automated Packaging &rarr; Silo Warehousing &rarr; Global Distribution. Formulated for layers, broilers, cattle, and aquaculture.'
  },
  {
    triggers: ['water', 'korean', 'ro', 'filter', 'purif'],
    answer: '<strong>Smart Water Filtration & Technology:</strong> Partnered with advanced South Korean membrane manufacturers, we engineer multi-stage smart water filtration systems: Sediment + Pre-Carbon + Korean RO Membrane (11 ppm TDS permeate purity) + UV Sterilization (99.99% log-4 bacterial kill). Designed for commercial agriculture, food processing, and residential safe drinking.'
  },
  {
    triggers: ['circular', 'bio', 'loop', 'zero waste', 'fertilizer', 'solar'],
    answer: '<strong>100% Circular Bio-Loop Model:</strong> At our Polpithigama complex, layer manure and agricultural crop residues are directed into automated in-vessel aerobic composters, producing 4.8 tons/day of enriched organic fertilizer and seedling media. Powered by a 240kW rooftop solar microgrid, this eliminates landfill waste and offsets 3.4 tons of CO₂e daily.'
  },
  {
    triggers: ['polpithigama', 'location', 'reg', 'registration', 'address', 'company'],
    answer: '<strong>Forest Lanka Enterprise Profile:</strong> Headquartered in Polpithigama, North Western Province, Sri Lanka. Business Registration: 16/2633. Hotline: +94 70 601 0108 | WhatsApp Desk: +94 71 974 0798 | Email: inquiries@forestlanka.com. Our facilities span 8 synchronized sectors connecting agriculture, manufacturing, and global trade.'
  },
  {
    triggers: ['egg', 'powder', 'albumen', 'liquid', 'yolk'],
    answer: '<strong>Egg Processing & Value-Addition:</strong> We produce spray-dried whole egg powder, high-whipping albumen (egg white) powder, egg yolk powder, and pasteurized liquid eggs. Shelf-stable up to 24 months in multi-ply vacuum packaging, certified for industrial bakeries, confectioneries, pasta manufacturing, and institutional food service.'
  },
  {
    triggers: ['mushroom', 'oyster', 'shiitake', 'cleanroom'],
    answer: '<strong>Smart Mushroom Cultivation:</strong> Controlled atmosphere cultivation on a 5-10 acre bio-complex. We cultivate gourmet Oyster and Shiitake mushrooms in HEPA Stage 3 filtered cleanrooms with automated CO₂ (850 ppm) and ultrasonic humidity control, supplying fresh, dried, and vacuum-sealed export packs.'
  }
];

function handleAiChatSubmit(event) {
  if (event && event.preventDefault) event.preventDefault();
  const input = document.getElementById('ai-input-field');
  const chatBody = document.getElementById('ai-chat-body');
  if (!input || !chatBody) return;
  const query = input.value.trim();
  if (!query) return;

  const userMsg = document.createElement('div');
  userMsg.className = 'ai-msg ai-msg-user';
  userMsg.textContent = query;
  chatBody.appendChild(userMsg);
  input.value = '';

  const lower = query.toLowerCase();
  let matched = aiKnowledge.find(item => item.triggers.some(t => lower.includes(t)));
  if (!matched) {
    matched = {
      answer: '<strong>Forest Lanka 2027 Copilot:</strong> Thank you for your inquiry! Forest Lanka connects 8 integrated agro-industrial sectors in Polpithigama, Sri Lanka. You can browse our <a href="products.php" class="text-gold underline">Product Catalog</a>, request an <a href="export.php" class="text-gold underline">Export Quotation</a>, or connect directly with our trade team on <a href="https://wa.me/94719740798" target="_blank" class="text-gold underline">WhatsApp (+94 71 974 0798)</a>.'
    };
  }

  setTimeout(() => {
    const botMsg = document.createElement('div');
    botMsg.className = 'ai-msg ai-msg-bot';
    botMsg.innerHTML = matched.answer;
    chatBody.appendChild(botMsg);
    chatBody.scrollTop = chatBody.scrollHeight;
  }, 350);
  chatBody.scrollTop = chatBody.scrollHeight;
}

function updateExportCalc() {
  const destSelect = document.getElementById('calc-destination');
  const cargoSelect = document.getElementById('calc-cargo');
  if (!destSelect || !cargoSelect) return;
  const destOption = destSelect.selectedOptions?.[0];
  const cargoOption = cargoSelect.selectedOptions?.[0];

  const transitStat = document.getElementById('calc-stat-transit');
  const packStat = document.getElementById('calc-stat-pack');
  const tempStat = document.getElementById('calc-stat-temp');

  if (transitStat && destOption) transitStat.textContent = `${destOption.dataset.days} Transit Days (${destOption.dataset.freight})`;
  if (packStat && cargoOption) packStat.textContent = `${cargoOption.dataset.container} · ${cargoOption.dataset.cap}`;
  if (tempStat && cargoOption) tempStat.textContent = cargoOption.dataset.temp;
}

function applyCalcToForm() {
  const destSelect = document.getElementById('calc-destination');
  const cargoSelect = document.getElementById('calc-cargo');
  const volSelect = document.getElementById('calc-volume');
  const incotermSelect = document.getElementById('calc-incoterm');
  if (!destSelect || !cargoSelect) return;

  const destOption = destSelect.selectedOptions?.[0];
  const cargoOption = cargoSelect.selectedOptions?.[0];
  const volText = volSelect?.selectedOptions?.[0]?.text || '';
  const incotermVal = incotermSelect?.value || 'FOB Colombo';

  const countryField = document.getElementById('export-country');
  const portField = document.getElementById('export-port');
  const indSelect = document.getElementById('export-industry');
  const qtyField = document.getElementById('export-quantity');

  if (countryField && destOption) countryField.value = destOption.dataset.country;
  if (portField && destOption) portField.value = destOption.dataset.port;
  if (indSelect && cargoOption && [...indSelect.options].some(o => o.value === cargoOption.dataset.code)) {
    indSelect.value = cargoOption.dataset.code;
  }
  if (qtyField) qtyField.value = `${volText}, ${incotermVal}`;

  const form = document.getElementById('export-inquiry-form');
  if (form) {
    form.scrollIntoView({ behavior: 'smooth' });
    document.getElementById('export-name')?.focus();
    showToast('Route estimate applied to quotation form!', 'fa-check');
  }
}

function initTelemetryTicker() {
  if (typeof window === 'undefined' || typeof setInterval === 'undefined') return;
  const eggEl = document.querySelector('[data-telemetry="poultry-eggs"]');
  const throughputEl = document.querySelector('[data-telemetry="feed-throughput"]');
  const waterVolEl = document.querySelector('[data-telemetry="water-vol"]');
  const solarEl = document.querySelector('[data-telemetry="solar-kw"]');
  const tempEl = document.querySelector('[data-telemetry="poultry-temp"]');

  if (!eggEl && !throughputEl && !waterVolEl && !solarEl) return;

  setInterval(() => {
    const pick = Math.floor(Math.random() * 5);
    if (pick === 0 && eggEl) {
      let current = parseInt(eggEl.textContent.replace(/,/g, ''), 10) || 19420;
      eggEl.textContent = (current + 1).toLocaleString();
    } else if (pick === 1 && throughputEl) {
      let val = (12.4 + (Math.random() * 0.4)).toFixed(1);
      throughputEl.textContent = val;
    } else if (pick === 2 && waterVolEl) {
      let current = parseInt(waterVolEl.textContent.replace(/,/g, ''), 10) || 146800;
      waterVolEl.textContent = (current + 10).toLocaleString();
    } else if (pick === 3 && solarEl) {
      let val = 240 + Math.floor(Math.random() * 10);
      solarEl.textContent = val;
    } else if (pick === 4 && tempEl) {
      let val = (24.0 + (Math.random() * 0.4)).toFixed(1);
      tempEl.textContent = val;
    }
  }, 3500);
}

document.addEventListener('DOMContentLoaded',()=>{
  updateCartUI();
  setCurrency(currentCurrency);
  initTelemetryTicker();
  updateExportCalc();
  document.querySelectorAll('[data-product]').forEach(button=>button.addEventListener('click',()=>{try{addToCart(JSON.parse(button.dataset.product));}catch{showToast('Please refresh the product catalog.','fa-circle-info');}}));
  document.querySelectorAll('form[data-inquiry]').forEach(form=>form.addEventListener('submit',submitInquiry));
  const closeDropdowns=()=>document.querySelectorAll('.nav-dropdown > button').forEach(button=>{button.setAttribute('aria-expanded','false');document.getElementById(button.getAttribute('aria-controls')).hidden=true;});
  document.querySelectorAll('.nav-dropdown > button').forEach(button=>button.addEventListener('click',()=>{const open=button.getAttribute('aria-expanded')!=='true';closeDropdowns();button.setAttribute('aria-expanded',String(open));document.getElementById(button.getAttribute('aria-controls')).hidden=!open;}));
  document.addEventListener('click',event=>{if(!event.target.closest('.nav-dropdown'))closeDropdowns();});
  const menuButton=document.getElementById('mobile-menu-btn'),menu=document.getElementById('mobile-nav-menu');
  menuButton?.addEventListener('click',()=>{menu.hidden=!menu.hidden;menuButton.setAttribute('aria-expanded',String(!menu.hidden));menuButton.setAttribute('aria-label',menu.hidden?'Open navigation':'Close navigation');});
  const header=document.querySelector('.site-header');if(header&&'ResizeObserver'in window)new ResizeObserver(entries=>document.documentElement.style.setProperty('--header-height',entries[0].contentRect.height+'px')).observe(header);
  if(document.getElementById('product-grid')){
    document.querySelectorAll('.product-item').forEach((item,index)=>item.dataset.position=index);
    const categories=[...document.querySelectorAll('.prod-cat-btn')];categories.forEach(button=>{button.dataset.category=button.getAttribute('onclick')?.match(/filterCategory\('([^']+)'/)?.[1]||'all';button.setAttribute('aria-pressed','false');});
    const params=new URLSearchParams(location.search),selected=categories.find(button=>button.dataset.category===params.get('category'))||categories[0],sort=document.getElementById('product-sort');
    document.getElementById('product-search-input').value=params.get('q')||'';if([...sort.options].some(option=>option.value===params.get('sort')))sort.value=params.get('sort');sort.addEventListener('change',applyProductFilters);filterCategory(selected.dataset.category,selected);
  }
  document.querySelectorAll('.gallery-filter-btn').forEach((button,index)=>button.setAttribute('aria-pressed',String(index===0)));
  document.querySelectorAll('.gallery-item[onclick]').forEach(item=>{item.tabIndex=0;item.setAttribute('role','button');item.setAttribute('aria-label','Enlarge '+(item.querySelector('img')?.alt||'industry photo'));item.addEventListener('keydown',event=>{if(event.key==='Enter'||event.key===' '){event.preventDefault();item.click();}});});
  const lightbox=document.getElementById('gallery-lightbox-modal');if(lightbox){lightbox.inert=true;lightbox.setAttribute('aria-hidden','true');}
  document.querySelectorAll('img').forEach(image=>{const fallback=()=>{if(!image.dataset.fallback){image.dataset.fallback='true';image.src='assets/images/logo.jpg';image.classList.add('image-fallback');}};image.addEventListener('error',fallback);if(image.getAttribute('src')&&image.complete&&image.naturalWidth===0)fallback();});
  document.getElementById('checkout-modal')?.addEventListener('click',event=>{if(event.target.id==='checkout-modal')closeCheckoutModal();});
  window.addEventListener('scroll',()=>{const button=document.querySelector('.back-to-top');if(button)button.hidden=window.scrollY<650;},{passive:true});
});
window.addEventListener('storage',event=>{if(event.key==='forest_lanka_cart'){cart=normalizeCart(storage.get('forest_lanka_cart',[]));updateCartUI();}});
document.addEventListener('keydown',event=>{
  if(event.key==='Escape'){
    if(activeDialog?.id==='cart-drawer')closeCartDrawer();else if(activeDialog)hideDialog(activeDialog);
    document.querySelectorAll('.nav-dropdown > button[aria-expanded="true"]').forEach(button=>{button.setAttribute('aria-expanded','false');document.getElementById(button.getAttribute('aria-controls')).hidden=true;button.focus();});
    const menu=document.getElementById('mobile-nav-menu');if(menu&&!menu.hidden){menu.hidden=true;const button=document.getElementById('mobile-menu-btn');button.setAttribute('aria-expanded','false');button.focus();}
  }
  if(event.key==='Tab'&&activeDialog){
    const fields=[...activeDialog.querySelectorAll('button:not(:disabled),a[href],input:not([type="hidden"]):not(:disabled),select:not(:disabled),textarea:not(:disabled),[tabindex="0"]')].filter(element=>element.getClientRects().length&&!element.closest('[inert]')),first=fields[0],last=fields[fields.length-1];
    if(!first){event.preventDefault();activeDialog.focus();}else if(event.shiftKey&&(document.activeElement===first||document.activeElement===activeDialog)){event.preventDefault();last.focus();}else if(!event.shiftKey&&(document.activeElement===last||!activeDialog.contains(document.activeElement))){event.preventDefault();first.focus();}
  }
});
