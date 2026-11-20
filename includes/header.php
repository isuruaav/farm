<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="<?= e($meta['description']) ?>">
  <meta name="theme-color" content="#123f32">
  <?php if ($page==='404'): ?><meta name="robots" content="noindex,nofollow"><?php endif; ?>
  <meta name="csrf-token" content="<?= e(csrf_token()) ?>">
  <meta property="og:title" content="<?= e($meta['title']) ?>">
  <meta property="og:description" content="<?= e($meta['description']) ?>">
  <meta property="og:type" content="website">
  <meta property="og:image" content="<?= e(site_url('assets/images/logo.jpg')) ?>">
  <meta property="og:locale" content="en_LK">
  <meta name="whatsapp-number" content="<?= e($site['whatsapp']) ?>">
  <link rel="canonical" href="<?= e(site_url($canonicalPath ?? ($page==='index'?'':$page.'.php'))) ?>">
  <title><?= e($meta['title']) ?></title>
  <link rel="icon" type="image/jpeg" href="assets/images/logo.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Poppins:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/vendor/fontawesome/css/all.min.css">
  <link rel="stylesheet" href="assets/css/utilities.css?v=4.3.5-imagery">
  <script type="application/json" id="product-catalog"><?= json_encode(catalog(), JSON_UNESCAPED_UNICODE | JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT) ?></script>
  <script src="assets/js/app.js?v=4" defer></script>
  <script src="assets/js/scroll-reveal.js?v=2" defer></script>
  <script src="assets/js/experience.js?v=1" defer></script>
  <script type="application/ld+json"><?= json_encode(['@context'=>'https://schema.org','@type'=>'Organization','name'=>'FOREST LANKA','url'=>site_url(),'logo'=>site_url('assets/images/logo.jpg'),'telephone'=>$site['phone'],'email'=>$site['email'],'address'=>$site['address']],JSON_UNESCAPED_SLASHES|JSON_HEX_TAG|JSON_HEX_AMP|JSON_HEX_APOS|JSON_HEX_QUOT) ?></script>
</head>
<body data-page="<?= e($page) ?>">
<a href="#main-content" class="skip-to-content">Skip to main content</a>
<div class="utility-bar">
  <div class="site-container utility-content">
    <div class="flex items-center gap-3">
      <span class="utility-location"><i class="fas fa-location-dot" aria-hidden="true"></i> Polpithigama, Sri Lanka <span class="registration">Reg. 16/2633</span></span>
      <span class="telemetry-status-pill hidden sm:inline-flex"><span class="pulse-beacon" aria-hidden="true"></span> 2027 Bio-Loop: Optimal</span>
    </div>
    <div class="utility-links">
      <div class="currency-selector" aria-label="Currency selector">
        <span class="currency-label"><i class="fas fa-coins" aria-hidden="true"></i></span>
        <button type="button" class="currency-btn is-active" data-currency="LKR" onclick="setCurrency('LKR')">LKR</button>
        <button type="button" class="currency-btn" data-currency="USD" onclick="setCurrency('USD')">USD</button>
        <button type="button" class="currency-btn" data-currency="EUR" onclick="setCurrency('EUR')">EUR</button>
        <button type="button" class="currency-btn" data-currency="AED" onclick="setCurrency('AED')">AED</button>
      </div>
      <a href="tel:<?= e(preg_replace('/[^+0-9]/','',$site['phone'])) ?>"><i class="fas fa-phone" aria-hidden="true"></i> <?= e($site['phone']) ?></a>
      <a class="utility-email" href="mailto:<?= e($site['email']) ?>"><?= e($site['email']) ?></a>
    </div>
  </div>
</div>
<header class="site-header">
  <div class="site-container header-content">
    <a href="index.php" class="brand" aria-label="Forest Lanka home">
      <img src="assets/images/logo.jpg" alt="" width="56" height="56">
      <span><strong>FOREST LANKA</strong><small>AGRICULTURE · INDUSTRY · GLOBAL TRADE</small></span>
    </a>
    <nav class="desktop-nav" aria-label="Main navigation">
      <a href="index.php" class="nav-link <?= $page==='index'?'active':'' ?>" <?= $page==='index'?'aria-current="page"':'' ?>><span>Home</span></a>
      <a href="about.php" class="nav-link <?= $page==='about'?'active':'' ?>" <?= $page==='about'?'aria-current="page"':'' ?>><span>About</span></a>
      <div class="nav-dropdown">
        <button type="button" class="nav-link <?= str_starts_with($page,'industr')?'active':'' ?>" aria-expanded="false" aria-controls="industry-menu"><span>Industries</span> <i class="fas fa-chevron-down" aria-hidden="true"></i></button>
        <div id="industry-menu" class="nav-panel" hidden>
          <a href="industries.php">Explore all 8 industries</a>
          <?php foreach ($industries as $slug => $label): ?><a href="industry-<?= e($slug) ?>.php" <?= $page==='industry-'.$slug?'aria-current="page"':'' ?>><?= e($label) ?></a><?php endforeach; ?>
        </div>
      </div>
      <a href="products.php" class="nav-link <?= $page==='products'?'active':'' ?>" <?= $page==='products'?'aria-current="page"':'' ?>><span>Products</span></a>
      <div class="nav-dropdown">
        <button type="button" class="nav-link" aria-expanded="false" aria-controls="connect-menu"><span>Connect</span> <i class="fas fa-chevron-down" aria-hidden="true"></i></button>
        <div id="connect-menu" class="nav-panel" hidden>
          <?php foreach (['export'=>'Global Trading & Export','investment'=>'Investment Opportunities','partners'=>'Become a Partner','gallery'=>'Photo Gallery','news'=>'News & Updates','faq'=>'Frequently Asked Questions'] as $slug=>$label): ?><a href="<?= e($slug) ?>.php" <?= $page===$slug?'aria-current="page"':'' ?>><?= e($label) ?></a><?php endforeach; ?>
        </div>
      </div>
      <a href="contact.php" class="nav-link <?= $page==='contact'?'active':'' ?>" <?= $page==='contact'?'aria-current="page"':'' ?>><span>Contact Us</span></a>
    </nav>
    <div class="header-actions">
      <a href="contact.php" class="header-contact"><span>Get in touch</span></a>
      <button type="button" onclick="openCartDrawer()" class="cart-trigger" aria-label="Open inquiry cart"><i class="fas fa-bag-shopping" aria-hidden="true"></i><span class="cart-count-badge" aria-label="Items in cart">0</span></button>
      <button type="button" id="mobile-menu-btn" class="menu-trigger" aria-label="Open navigation" aria-expanded="false" aria-controls="mobile-nav-menu"><i class="fas fa-bars" aria-hidden="true"></i></button>
    </div>
  </div>
  <nav id="mobile-nav-menu" class="mobile-navigation" aria-label="Mobile navigation" hidden>
    <?php foreach (['index'=>'Home','about'=>'About','industries'=>'Our 8 Industries','products'=>'Products','export'=>'Global Export','investment'=>'Investment','partners'=>'Become a Partner','gallery'=>'Gallery','news'=>'News','faq'=>'FAQs','contact'=>'Contact'] as $slug=>$label): ?><a href="<?= e($slug) ?>.php" <?= $page===$slug?'aria-current="page"':'' ?>><?= e($label) ?></a><?php endforeach; ?>
  </nav>
</header>
<noscript><p class="media-notice">JavaScript enables the cart and filters. You can still browse all pages and submit an inquiry through the <a href="contact.php">contact form</a>.</p></noscript>
