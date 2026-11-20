<footer class="corporate-footer">
  <div class="site-container footer-grid">
    <div class="footer-brand">
      <a href="index.php" class="brand"><img src="assets/images/logo.jpg" alt="" width="56" height="56" loading="lazy"><span><strong>FOREST LANKA</strong><small>ROOTED IN SRI LANKA. GROWING GLOBALLY.</small></span></a>
      <p><span>Connecting agriculture, responsible industry and global trade through eight integrated sectors.</span></p>
      <p><?= e($site['address']) ?><br><span class="footer-registration">Business Registration: 16/2633</span></p>
    </div>
    <div><h2>Our Industries</h2><ul><?php foreach ($industries as $slug=>$label): ?><li><a href="industry-<?= e($slug) ?>.php"><?= e($label) ?></a></li><?php endforeach; ?></ul></div>
    <div><h2>Explore</h2><ul><?php foreach (['products'=>'Product Catalog','export'=>'Global Trading & Export','investment'=>'Investment Opportunities','partners'=>'Business Partnerships','gallery'=>'Industry Gallery','news'=>'News & Updates','faq'=>'Help & FAQs'] as $slug=>$label): ?><li><a href="<?= e($slug) ?>.php"><?= e($label) ?></a></li><?php endforeach; ?></ul></div>
    <div><h2>Let's Talk</h2><ul><li><a href="tel:<?= e(preg_replace('/[^+0-9]/','',$site['phone'])) ?>"><?= e($site['phone']) ?></a></li><li><a href="https://wa.me/<?= e($site['whatsapp']) ?>" target="_blank" rel="noopener noreferrer">Connect on WhatsApp</a></li><li><a href="mailto:<?= e($site['email']) ?>"><?= e($site['email']) ?></a></li><li><?= e($site['hours']) ?></li></ul><a href="contact.php" class="footer-contact">Send an inquiry</a></div>
  </div>
  <div class="site-container footer-bottom"><p>© <?= date('Y') ?> FOREST LANKA. All rights reserved.</p><nav aria-label="Legal"><a href="privacy-policy.php">Privacy</a><a href="terms.php">Terms</a><a href="delivery-returns.php">Delivery & Returns</a><a href="admin/">Staff Login</a></nav></div>
</footer>
<div class="floating-actions" aria-label="Quick actions"><button type="button" class="float-btn float-btn-ai" onclick="toggleAiDrawer()" aria-label="Open Forest Lanka 2027 AI Agri-Copilot" title="Forest Lanka AI Copilot"><i class="fas fa-robot" aria-hidden="true"></i><span class="ai-btn-pulse"></span></button><a href="https://wa.me/<?= e($site['whatsapp']) ?>" target="_blank" rel="noopener noreferrer" class="float-btn float-btn-whatsapp" aria-label="Open WhatsApp chat"><i class="fab fa-whatsapp" aria-hidden="true"></i></a><button type="button" class="float-btn back-to-top" aria-label="Back to top" onclick="window.scrollTo({top:0,behavior:'smooth'})" hidden><i class="fas fa-chevron-up" aria-hidden="true"></i></button></div>
<div id="ai-drawer-overlay" class="ai-drawer-overlay" onclick="toggleAiDrawer()"></div>
<aside id="ai-drawer" class="ai-drawer" role="dialog" aria-modal="true" aria-labelledby="ai-drawer-heading" inert>
  <div class="ai-drawer-header">
    <div class="ai-drawer-title">
      <div class="metric-icon metric-icon--emerald"><i class="fas fa-robot" aria-hidden="true"></i></div>
      <div>
        <h2 id="ai-drawer-heading">Forest Lanka AI Copilot</h2>
        <span class="ai-drawer-status"><span class="pulse-beacon" aria-hidden="true"></span> 2027 Knowledge Core · Online</span>
      </div>
    </div>
    <button type="button" onclick="toggleAiDrawer()" aria-label="Close AI Copilot" class="icon-button"><i class="fas fa-xmark" aria-hidden="true"></i></button>
  </div>
  <div id="ai-chat-body" class="ai-chat-body">
    <div class="ai-msg ai-msg-bot">
      <p><strong>Ayubowan! Welcome to Forest Lanka.</strong></p>
      <p>I am your 2027 Next-Gen Agri-Industrial Assistant. Ask me anything about our 8 integrated sectors, Polpithigama facilities, export packaging, or trade logistics.</p>
      <div class="ai-quick-chips">
        <button type="button" class="ai-chip" onclick="askAiQuestion('What are your export shipping terms and ports?')">Export Logistics &amp; Ports</button>
        <button type="button" class="ai-chip" onclick="askAiQuestion('Tell me about the 12-Stage Feed Mill')">12-Stage Feed Mill</button>
        <button type="button" class="ai-chip" onclick="askAiQuestion('How does the Circular Bio-Loop work?')">Circular Bio-Loop</button>
        <button type="button" class="ai-chip" onclick="askAiQuestion('What is the Korean Water Purification project?')">Korean Water Tech</button>
        <button type="button" class="ai-chip" onclick="askAiQuestion('Where is the facility and what is Reg 16/2633?')">Polpithigama Facility</button>
      </div>
    </div>
  </div>
  <form id="ai-chat-form" class="ai-input-bar" onsubmit="handleAiChatSubmit(event)">
    <input type="text" id="ai-input-field" class="ai-input-field" placeholder="Ask about products, exports, bio-loop..." autocomplete="off" maxlength="300" required>
    <button type="submit" class="ai-send-btn" aria-label="Send query"><i class="fas fa-arrow-up" aria-hidden="true"></i></button>
  </form>
</aside>
<div id="quickview-modal" class="modal-backdrop flex items-center justify-center p-4" role="dialog" aria-modal="true" aria-labelledby="quickview-title" tabindex="-1" inert>
  <div class="quickview-modal relative">
    <button type="button" onclick="closeProductQuickView()" class="checkout-close icon-button" aria-label="Close product view"><i class="fas fa-xmark" aria-hidden="true"></i></button>
    <div class="quickview-grid">
      <div class="quickview-img" id="quickview-img-box">
        <img id="quickview-img" src="" alt="Product view" loading="lazy">
      </div>
      <div class="quickview-details">
        <div>
          <span class="audience-pill" id="quickview-industry">Industry</span>
          <h2 id="quickview-title">Product Name</h2>
          <p id="quickview-desc">Description</p>
          <div class="product-pack" id="quickview-variant">Variant</div>
          <div class="product-card-price" id="quickview-price">Price</div>
          <span class="product-availability" id="quickview-avail">Availability</span>
        </div>
        <div class="panel-actions">
          <button type="button" id="quickview-add-btn" class="btn-primary flex-1"><i class="fas fa-plus" aria-hidden="true"></i> Add to inquiry</button>
          <a href="#" id="quickview-link" class="text-link">Full page</a>
        </div>
      </div>
    </div>
  </div>
</div>
<div id="cart-drawer-overlay" class="cart-drawer-overlay" onclick="closeCartDrawer()"></div>
<aside id="cart-drawer" class="cart-drawer" role="dialog" aria-modal="true" aria-labelledby="cart-title" tabindex="-1" inert>
  <div class="drawer-heading"><h2 id="cart-title">Your inquiry cart</h2><button type="button" onclick="closeCartDrawer()" aria-label="Close cart" class="icon-button"><i class="fas fa-xmark" aria-hidden="true"></i></button></div>
  <div id="cart-items-list" class="flex-1 overflow-y-auto p-4 space-y-3"></div>
  <div class="drawer-footer"><div class="cart-estimate"><span>Estimated total</span><strong id="cart-subtotal">LKR 0.00</strong></div><p>Submit your requirements for confirmation of pricing, stock and delivery. No payment is collected here.</p><div class="drawer-buttons"><button type="button" onclick="clearCart()" class="btn-secondary">Clear cart</button><button type="button" onclick="openCheckoutModal()" class="btn-primary">Request quotation</button></div></div>
</aside>
<div id="checkout-modal" class="modal-backdrop flex items-center justify-center p-4" role="dialog" aria-modal="true" aria-labelledby="checkout-title" tabindex="-1" inert>
  <div class="modal-content-box p-6 relative">
    <button type="button" onclick="closeCheckoutModal()" class="checkout-close icon-button" aria-label="Close quotation form"><i class="fas fa-xmark" aria-hidden="true"></i></button>
    <h2 id="checkout-title">Request a quotation</h2><p class="checkout-intro">Our team will review your requirements and contact you. Prices are estimates until confirmed.</p>
    <div class="checkout-summary"><div id="checkout-items-summary"></div><div class="cart-estimate"><span>Estimated total</span><strong id="checkout-total-amount"></strong></div></div>
    <form id="checkout-form" method="post" action="api/inquiries.php" data-inquiry="order" class="checkout-form">
      <?php form_security('order'); ?>
      <input type="hidden" name="items" id="checkout-items-input" value="[]">
      <div class="form-two-columns"><div><label for="cust-name">Full name *</label><input name="name" id="cust-name" required maxlength="180" autocomplete="name"></div><div><label for="cust-phone">Phone *</label><input type="tel" name="phone" id="cust-phone" required maxlength="32" autocomplete="tel"></div></div>
      <div class="form-two-columns"><div><label for="cust-email">Email</label><input type="email" name="email" id="cust-email" maxlength="254" autocomplete="email"></div><div><label for="cust-city">City *</label><input name="city" id="cust-city" required maxlength="180" autocomplete="address-level2"></div></div>
      <div><label for="cust-address">Delivery address *</label><input name="address" id="cust-address" required maxlength="300" autocomplete="street-address"></div>
      <div><label for="payment-method">Preferred arrangement</label><select name="payment_method" id="payment-method"><option value="b2b_quotation">Quotation first</option><option value="cash_on_delivery">Cash on delivery, subject to availability</option><option value="bank_transfer">Bank transfer after confirmation</option></select></div>
      <div><label for="cust-notes">Additional requirements</label><textarea name="message" id="cust-notes" rows="3" maxlength="5000"></textarea></div>
      <div class="form-privacy"><label><input type="checkbox" name="consent" value="1" required><span>I agree to be contacted about this request. <a href="privacy-policy.php">Privacy Policy</a></span></label></div>
      <p class="form-feedback" role="status" aria-live="polite" tabindex="-1" hidden></p>
      <div class="drawer-buttons"><button type="button" onclick="sendOrderViaWhatsApp()" class="btn-secondary"><i class="fab fa-whatsapp" aria-hidden="true"></i> Open WhatsApp draft</button><button type="submit" class="btn-primary">Submit request</button></div>
    </form>
    <div id="checkout-success" class="success-panel" role="status" hidden></div>
  </div>
</div>
<div id="toast-container" class="toast-container" role="status" aria-live="polite" aria-atomic="false"></div>
</body>
</html>
