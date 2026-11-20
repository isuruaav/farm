#!/usr/bin/env python3
"""
Generator script to build the complete, multi-page static website for FOREST LANKA
based directly on the ISD Tech Hub proposal specification and company logo.
"""

import os

COMMON_HEAD = """
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="FOREST LANKA - Growing Agriculture. Building Industries. Connecting Global Markets. Premier Sri Lankan Agro-Industrial & Export Enterprise.">
  <meta name="keywords" content="Forest Lanka, Sri Lanka Poultry, Smart Layer Farm, Animal Feed, Recycled Egg Trays, Mushroom Export, Egg Powder, Organic Fertilizer, Growing Media, Water Filtration, Korean Technology">
  <meta name="author" content="ISD Tech Hub / FOREST LANKA">
  <link rel="icon" type="image/jpeg" href="assets/images/logo.jpg">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans+Sinhala:wght@400;500;600;700&family=Poppins:wght@500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Font Awesome 6 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  
  <!-- Tailwind CSS Play CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            forest: {
              DEFAULT: '#123F32',
              dark: '#0c2b22',
              light: '#1b5947'
            },
            emerald: {
              DEFAULT: '#1D6248',
              dark: '#144633',
              light: '#288562'
            },
            gold: {
              DEFAULT: '#EBC975',
              dark: '#c9a54a',
              light: '#f5de9f'
            },
            warmwhite: '#F4F8F2',
            charcoal: '#1B2C26',
            waterblue: {
              DEFAULT: '#14516A',
              dark: '#0e394b',
              light: '#217b9f'
            }
          },
          fontFamily: {
            sans: ['Inter', 'Noto Sans Sinhala', 'Segoe UI', 'Roboto', 'sans-serif'],
            heading: ['Poppins', 'Noto Sans Sinhala', 'sans-serif']
          }
        }
      }
    }
  </script>
  
  <!-- Custom Stylesheet -->
  <link rel="stylesheet" href="assets/css/styles.css">
"""

def get_header(active_page="home"):
    def nav_class(page_name):
        return "nav-link active font-bold text-gold" if active_page == page_name else "nav-link"

    return f"""
  <!-- Accessibility Skip Link -->
  <a href="#main-content" class="skip-to-content">Skip to Main Content / ප්‍රධාන අන්තර්ගතයට යන්න</a>

  <!-- Top Announcement & Contact Bar -->
  <div class="top-bar py-2 px-4">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center text-xs gap-2">
      <div class="flex flex-wrap items-center gap-4 text-emerald-100">
        <span class="flex items-center gap-1.5"><i class="fas fa-certificate text-gold"></i> Reg No: <strong>16/2633</strong></span>
        <span class="flex items-center gap-1.5"><i class="fas fa-map-marker-alt text-gold"></i> Polpithigama, Kurunegala, Sri Lanka</span>
        <span class="hidden sm:inline-flex items-center gap-1.5"><i class="fas fa-phone-alt text-gold"></i> +94 70 601 0108</span>
      </div>
      <div class="flex items-center gap-4">
        <a href="https://wa.me/94719740798" target="_blank" class="hover:text-gold flex items-center gap-1 text-emerald-100">
          <i class="fab fa-whatsapp text-green-400"></i> WhatsApp: +94 71 974 0798
        </a>
        <a href="mailto:thilankaherath7@gmail.com" class="hidden sm:inline-flex hover:text-gold items-center gap-1 text-emerald-100">
          <i class="fas fa-envelope text-gold"></i> thilankaherath7@gmail.com
        </a>
        <!-- Bilingual Switcher -->
        <div class="flex items-center bg-emerald-900 bg-opacity-60 rounded-full p-0.5 border border-emerald-700">
          <button onclick="setLanguage('en')" data-lang-choice="en" class="lang-btn px-2.5 py-0.5 text-xs rounded-full transition" title="English">EN</button>
          <button onclick="setLanguage('si')" data-lang-choice="si" class="lang-btn px-2.5 py-0.5 text-xs rounded-full transition" title="සිංහල">සිං</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Main Navigation Header -->
  <header class="site-header">
    <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
      <!-- Brand Logo -->
      <a href="index.html" class="flex items-center gap-3 group text-decoration-none">
        <img src="assets/images/logo.jpg" alt="FOREST LANKA Logo" class="h-14 sm:h-16 w-auto rounded-lg shadow-sm border border-emerald-700/50 object-contain bg-white p-1 group-hover:scale-105 transition">
        <div>
          <div class="text-xl sm:text-2xl font-black tracking-wide text-white font-heading">FOREST LANKA</div>
          <div class="text-xs text-gold font-medium tracking-tight hidden sm:block">
            <span class="lang-en">Growing Agriculture. Building Industries. Connecting Global Markets.</span>
            <span class="lang-si">කෘෂිකර්මාන්තය නංවමු. කර්මාන්ත ගොඩනඟමු.</span>
          </div>
        </div>
      </a>

      <!-- Desktop Navigation Menu -->
      <nav class="hidden lg:flex items-center space-x-1" aria-label="Main Navigation">
        <a href="index.html" class="{nav_class('home')}">
          <span class="lang-en">Home</span><span class="lang-si">මුල් පිටුව</span>
        </a>
        <a href="about.html" class="{nav_class('about')}">
          <span class="lang-en">About Us</span><span class="lang-si">අප ගැන</span>
        </a>
        
        <!-- Industries Dropdown -->
        <div class="relative group">
          <a href="industries.html" class="{nav_class('industries')}">
            <span class="lang-en">8 Industries</span><span class="lang-si">කර්මාන්ත 08</span>
            <i class="fas fa-chevron-down text-xs ml-1 opacity-70 group-hover:rotate-180 transition"></i>
          </a>
          <div class="absolute left-0 mt-1 w-72 bg-white rounded-xl shadow-2xl border border-emerald-900/10 py-2 hidden group-hover:block transition z-50 text-charcoal">
            <a href="industry-poultry.html" class="block px-4 py-2.5 text-xs font-semibold hover:bg-emerald-50 hover:text-emerald-800 border-b border-gray-100 flex items-center gap-2">
              <i class="fas fa-egg text-emerald-700 w-4"></i> 1. Smart Layer Poultry Farm
            </a>
            <a href="industry-feed.html" class="block px-4 py-2.5 text-xs font-semibold hover:bg-emerald-50 hover:text-emerald-800 border-b border-gray-100 flex items-center gap-2">
              <i class="fas fa-wheat-awn text-emerald-700 w-4"></i> 2. Animal Feed Manufacturing
            </a>
            <a href="industry-egg-trays.html" class="block px-4 py-2.5 text-xs font-semibold hover:bg-emerald-50 hover:text-emerald-800 border-b border-gray-100 flex items-center gap-2">
              <i class="fas fa-box-open text-emerald-700 w-4"></i> 3. Recycled Paper Egg Trays
            </a>
            <a href="industry-mushrooms.html" class="block px-4 py-2.5 text-xs font-semibold hover:bg-emerald-50 hover:text-emerald-800 border-b border-gray-100 flex items-center gap-2">
              <i class="fas fa-leaf text-emerald-700 w-4"></i> 4. Smart Mushroom & Global Export
            </a>
            <a href="industry-egg-processing.html" class="block px-4 py-2.5 text-xs font-semibold hover:bg-emerald-50 hover:text-emerald-800 border-b border-gray-100 flex items-center gap-2">
              <i class="fas fa-mortar-pestle text-emerald-700 w-4"></i> 5. Egg Processing & Powders
            </a>
            <a href="industry-fertilizer.html" class="block px-4 py-2.5 text-xs font-semibold hover:bg-emerald-50 hover:text-emerald-800 border-b border-gray-100 flex items-center gap-2">
              <i class="fas fa-seedling text-emerald-700 w-4"></i> 6. Organic Bio-Fertilizer
            </a>
            <a href="industry-growing-media.html" class="block px-4 py-2.5 text-xs font-semibold hover:bg-emerald-50 hover:text-emerald-800 border-b border-gray-100 flex items-center gap-2">
              <i class="fas fa-plant-wilt text-emerald-700 w-4"></i> 7. Growing Media & Substrates
            </a>
            <a href="industry-water-tech.html" class="block px-4 py-2.5 text-xs font-semibold hover:bg-emerald-50 hover:text-emerald-800 flex items-center gap-2">
              <i class="fas fa-droplet text-waterblue w-4"></i> 8. Korean Smart Water Solutions
            </a>
          </div>
        </div>

        <a href="products.html" class="{nav_class('products')}">
          <span class="lang-en">Products</span><span class="lang-si">නිෂ්පාදන</span>
        </a>
        <a href="export.html" class="{nav_class('export')}">
          <span class="lang-en">Global Export</span><span class="lang-si">අපනයන</span>
        </a>
        <a href="investment.html" class="{nav_class('investment')}">
          <span class="lang-en">Investments</span><span class="lang-si">ආයෝජන</span>
        </a>
        <a href="partners.html" class="{nav_class('partners')}">
          <span class="lang-en">Partners</span><span class="lang-si">හවුල්කරුවන්</span>
        </a>
        <a href="gallery.html" class="{nav_class('gallery')}">
          <span class="lang-en">Gallery</span><span class="lang-si">ඡායාරූප</span>
        </a>
        <a href="news.html" class="{nav_class('news')}">
          <span class="lang-en">News</span><span class="lang-si">පුවත්</span>
        </a>
        <a href="contact.html" class="{nav_class('contact')}">
          <span class="lang-en">Contact</span><span class="lang-si">සම්බන්ධ වන්න</span>
        </a>
      </nav>

      <!-- Cart Button & Quick Action -->
      <div class="flex items-center gap-3">
        <button onclick="openCartDrawer()" class="relative p-2.5 text-gold hover:text-white bg-emerald-900/60 hover:bg-emerald-800 rounded-lg transition" aria-label="Open Inquiry Cart">
          <i class="fas fa-shopping-cart text-lg"></i>
          <span class="cart-count-badge">0</span>
        </button>

        <a href="partners.html" class="hidden sm:inline-flex btn-gold text-xs py-2 px-3.5 shadow">
          <i class="fas fa-handshake"></i>
          <span class="lang-en">Partner With Us</span><span class="lang-si">හවුල්කරුවෙකු වන්න</span>
        </a>

        <!-- Mobile Menu Hamburger Button -->
        <button id="mobile-menu-btn" class="lg:hidden p-2 text-white hover:text-gold focus:outline-none" aria-label="Toggle Mobile Menu" aria-expanded="false">
          <i class="fas fa-bars text-xl"></i>
        </button>
      </div>
    </div>

    <!-- Mobile Navigation Drawer -->
    <div id="mobile-nav-menu" class="hidden lg:hidden bg-forest-dark border-t border-emerald-800 px-4 py-4 space-y-2">
      <a href="index.html" class="block py-2 text-sm text-white hover:text-gold border-b border-emerald-900/50">Home / මුල් පිටුව</a>
      <a href="about.html" class="block py-2 text-sm text-white hover:text-gold border-b border-emerald-900/50">About Us / අප ගැන</a>
      <a href="industries.html" class="block py-2 text-sm text-gold font-bold border-b border-emerald-900/50">Core 08 Industries / ප්‍රධාන කර්මාන්ත 08</a>
      <div class="pl-4 py-1 space-y-1.5 text-xs text-emerald-200">
        <a href="industry-poultry.html" class="block hover:text-white">• 1. Smart Layer Poultry Farm</a>
        <a href="industry-feed.html" class="block hover:text-white">• 2. Animal Feed Manufacturing</a>
        <a href="industry-egg-trays.html" class="block hover:text-white">• 3. Recycled Paper Egg Trays</a>
        <a href="industry-mushrooms.html" class="block hover:text-white">• 4. Smart Mushroom & Global Export</a>
        <a href="industry-egg-processing.html" class="block hover:text-white">• 5. Egg Processing & Powders</a>
        <a href="industry-fertilizer.html" class="block hover:text-white">• 6. Organic Bio-Fertilizer</a>
        <a href="industry-growing-media.html" class="block hover:text-white">• 7. Growing Media & Solutions</a>
        <a href="industry-water-tech.html" class="block hover:text-white">• 8. Korean Water Filtration</a>
      </div>
      <a href="products.html" class="block py-2 text-sm text-white hover:text-gold border-b border-emerald-900/50">Product Catalog & Store / නිෂ්පාදන</a>
      <a href="export.html" class="block py-2 text-sm text-white hover:text-gold border-b border-emerald-900/50">Global Trading & Export / අපනයන</a>
      <a href="investment.html" class="block py-2 text-sm text-white hover:text-gold border-b border-emerald-900/50">Investment Opportunities / ආයෝජන</a>
      <a href="partners.html" class="block py-2 text-sm text-white hover:text-gold border-b border-emerald-900/50">Become Our Partner / හවුල්කරුවන්</a>
      <a href="gallery.html" class="block py-2 text-sm text-white hover:text-gold border-b border-emerald-900/50">Photo Gallery / ඡායාරූප</a>
      <a href="news.html" class="block py-2 text-sm text-white hover:text-gold border-b border-emerald-900/50">News & Updates / පුවත්</a>
      <a href="contact.html" class="block py-2 text-sm text-white hover:text-gold">Contact Us / සම්බන්ධ වන්න</a>
    </div>
  </header>
"""

COMMON_FOOTER = """
  <!-- Floating Action Buttons -->
  <div class="floating-actions" aria-label="Quick Actions">
    <a href="https://wa.me/94719740798?text=Hello%20Forest%20Lanka,%20I%20would%20like%20to%20inquire%20about%20your%20products%20and%20industrial%20opportunities." target="_blank" class="float-btn float-btn-whatsapp" title="Chat on WhatsApp" aria-label="Contact Forest Lanka on WhatsApp">
      <i class="fab fa-whatsapp text-3xl"></i>
    </a>
    <button onclick="openCartDrawer()" class="float-btn float-btn-cart" title="View Inquiry Cart" aria-label="View Inquiry Cart">
      <i class="fas fa-shopping-basket text-2xl"></i>
      <span class="cart-count-badge">0</span>
    </button>
  </div>

  <!-- Shopping Cart & Quotation Drawer -->
  <div id="cart-drawer-overlay" class="cart-drawer-overlay" onclick="closeCartDrawer()"></div>
  <aside id="cart-drawer" class="cart-drawer" aria-label="Inquiry Cart Drawer">
    <div class="p-4 bg-forest text-white flex justify-between items-center border-b border-emerald-800">
      <div class="flex items-center gap-2">
        <i class="fas fa-shopping-bag text-gold"></i>
        <h3 class="font-bold text-base text-white m-0">Inquiry & Order Cart</h3>
      </div>
      <button onclick="closeCartDrawer()" class="text-gray-300 hover:text-white text-lg p-1" aria-label="Close Cart"><i class="fas fa-times"></i></button>
    </div>
    
    <div id="cart-items-list" class="flex-1 overflow-y-auto p-4 space-y-3">
      <!-- Populated via main.js -->
    </div>

    <div class="p-4 border-t border-gray-200 bg-white">
      <div class="flex justify-between items-center mb-3">
        <span class="text-xs text-gray-500 font-medium uppercase tracking-wider">Estimated Total</span>
        <span id="cart-subtotal" class="font-bold text-forest text-base">LKR 0.00</span>
      </div>
      <p class="text-xs text-gray-500 mb-4 leading-tight">Wholesale & Export orders are processed as quotation requests. Standard retail orders support direct payment.</p>
      
      <div class="grid grid-cols-2 gap-2">
        <button onclick="clearCart()" class="btn-secondary text-xs py-2 px-3 w-full">Clear Cart</button>
        <button onclick="openCheckoutModal()" class="btn-primary text-xs py-2 px-3 w-full">Proceed / ඉල්ලුම් කරන්න</button>
      </div>
    </div>
  </aside>

  <!-- Checkout / Order / Quotation Modal -->
  <div id="checkout-modal" class="modal-backdrop flex items-center justify-center p-4">
    <div class="modal-content-box p-6 relative">
      <button onclick="closeCheckoutModal()" class="absolute top-4 right-4 text-gray-400 hover:text-gray-700 text-lg" aria-label="Close modal">
        <i class="fas fa-times"></i>
      </button>

      <div id="checkout-modal-content">
        <div class="flex items-center gap-3 border-b border-gray-200 pb-3 mb-4">
          <div class="w-10 h-10 rounded-full bg-emerald-100 text-emerald-800 flex items-center justify-center text-lg">
            <i class="fas fa-clipboard-check"></i>
          </div>
          <div>
            <h3 class="text-lg font-bold text-forest m-0">Finalize Order & Quotation</h3>
            <p class="text-xs text-gray-500">FOREST LANKA Secure E-Commerce & Inquiries</p>
          </div>
        </div>

        <!-- Summary -->
        <div class="bg-warmwhite p-3.5 rounded-lg border border-gray-200 mb-4">
          <h4 class="text-xs font-bold text-forest uppercase tracking-wider mb-2">Cart Review</h4>
          <div id="checkout-items-summary" class="max-h-36 overflow-y-auto mb-2 space-y-1"></div>
          <div class="flex justify-between text-xs font-bold text-emerald-900 pt-2 border-t border-gray-200">
            <span>Total Value:</span>
            <span id="checkout-total-amount">LKR 0.00</span>
          </div>
        </div>

        <form onsubmit="handleCheckoutSubmit(event)" class="space-y-3">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div>
              <label class="block text-xs font-semibold text-gray-700 mb-1">Your Full Name / ආයතනය හෝ නම *</label>
              <input type="text" id="cust-name" required placeholder="Mr. / Ms. / Company" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-600">
            </div>
            <div>
              <label class="block text-xs font-semibold text-gray-700 mb-1">Phone Number / දුරකථන අංකය *</label>
              <input type="tel" id="cust-phone" required placeholder="+94 7X XXX XXXX" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-600">
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div>
              <label class="block text-xs font-semibold text-gray-700 mb-1">Email Address / ඊමේල්</label>
              <input type="email" id="cust-email" placeholder="name@company.com" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-600">
            </div>
            <div>
              <label class="block text-xs font-semibold text-gray-700 mb-1">City / Town / නගරය *</label>
              <input type="text" id="cust-city" required placeholder="e.g. Kurunegala, Colombo" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-600">
            </div>
          </div>

          <div>
            <label class="block text-xs font-semibold text-gray-700 mb-1">Delivery / Billing Address / ලිපිනය *</label>
            <input type="text" id="cust-address" required placeholder="Street address or warehouse location" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-600">
          </div>

          <div>
            <label class="block text-xs font-semibold text-gray-700 mb-1">Preferred Method / ගෙවීම් ක්‍රමය *</label>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
              <label class="border p-2 rounded-lg flex items-center gap-1.5 cursor-pointer hover:bg-emerald-50">
                <input type="radio" name="payment_method" value="cash_on_delivery" checked> COD
              </label>
              <label class="border p-2 rounded-lg flex items-center gap-1.5 cursor-pointer hover:bg-emerald-50">
                <input type="radio" name="payment_method" value="bank_transfer"> Bank Transfer
              </label>
              <label class="border p-2 rounded-lg flex items-center gap-1.5 cursor-pointer hover:bg-emerald-50">
                <input type="radio" name="payment_method" value="payhere_card"> Card / PayHere
              </label>
              <label class="border p-2 rounded-lg flex items-center gap-1.5 cursor-pointer hover:bg-emerald-50">
                <input type="radio" name="payment_method" value="b2b_quotation"> B2B Quotation
              </label>
            </div>
          </div>

          <div>
            <label class="block text-xs font-semibold text-gray-700 mb-1">Special Instructions / අමතර සටහන්</label>
            <textarea id="cust-notes" rows="2" placeholder="Packaging requirements, delivery schedule, target quantity, or custom requests" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-600"></textarea>
          </div>

          <div class="pt-2 flex flex-col sm:flex-row gap-2">
            <button type="button" onclick="sendOrderViaWhatsApp()" class="btn-gold flex-1 text-xs py-2.5">
              <i class="fab fa-whatsapp text-base"></i> Send Instant Order via WhatsApp
            </button>
            <button type="submit" class="btn-primary flex-1 text-xs py-2.5">
              <i class="fas fa-paper-plane text-base"></i> Submit System Order / Request
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>

  <!-- Corporate Footer -->
  <footer class="bg-forest-dark text-emerald-100 pt-16 pb-8 border-t-4 border-gold">
    <div class="max-w-7xl mx-auto px-4">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-8 mb-12">
        <!-- Brand Info -->
        <div class="lg:col-span-2">
          <div class="flex items-center gap-3 mb-4">
            <img src="assets/images/logo.jpg" alt="FOREST LANKA" class="h-16 w-auto bg-white p-1 rounded-lg border border-gold/40">
            <div>
              <span class="text-2xl font-black text-white font-heading tracking-wide">FOREST LANKA</span>
              <p class="text-xs text-gold font-medium mt-0.5">Growing Agriculture. Building Industries. Connecting Global Markets.</p>
            </div>
          </div>
          <p class="text-xs text-emerald-200/90 leading-relaxed mb-4">
            <span class="lang-en">FOREST LANKA is an ambitious agro-industrial conglomerate dedicated to modern egg production, balanced animal feeds, eco-friendly molded pulp egg trays, smart climate-controlled mushroom cultivation, functional egg powders, bio-organic fertilizers, specialized growing media, and advanced South Korean water purification technology.</span>
            <span class="lang-si">FOREST LANKA ආයතනය නවීන කෘෂිකාර්මික, කාර්මික නිෂ්පාදන, ආහාර නිෂ්පාදන, අපනයන සහ ජාත්‍යන්තර වෙළෙඳාම වෙනුවෙන් තාක්ෂණයෙන් සන්නද්ධ සම්පූර්ණ ගතික ව්‍යවසායකි.</span>
          </p>
          <div class="bg-forest/80 p-3 rounded-lg border border-emerald-800 text-xs space-y-1">
            <p><strong>Registration No:</strong> 16/2633</p>
            <p><strong>Registered Address:</strong> 434, Thalpathwewa, Polpithigama, Kurunegala, Sri Lanka (Postal: 60620)</p>
          </div>
        </div>

        <!-- 8 Core Industries Links -->
        <div>
          <h4 class="text-sm font-bold text-gold uppercase tracking-wider mb-3">Our 8 Industries</h4>
          <ul class="text-xs space-y-2 text-emerald-200">
            <li><a href="industry-poultry.html" class="hover:text-gold flex items-center gap-1.5"><i class="fas fa-chevron-right text-[10px] text-gold"></i> Smart Layer Poultry Farm</a></li>
            <li><a href="industry-feed.html" class="hover:text-gold flex items-center gap-1.5"><i class="fas fa-chevron-right text-[10px] text-gold"></i> Animal Feed Manufacturing</a></li>
            <li><a href="industry-egg-trays.html" class="hover:text-gold flex items-center gap-1.5"><i class="fas fa-chevron-right text-[10px] text-gold"></i> Recycled Paper Egg Trays</a></li>
            <li><a href="industry-mushrooms.html" class="hover:text-gold flex items-center gap-1.5"><i class="fas fa-chevron-right text-[10px] text-gold"></i> Smart Mushroom Farming</a></li>
            <li><a href="industry-egg-processing.html" class="hover:text-gold flex items-center gap-1.5"><i class="fas fa-chevron-right text-[10px] text-gold"></i> Egg Powder Processing</a></li>
            <li><a href="industry-fertilizer.html" class="hover:text-gold flex items-center gap-1.5"><i class="fas fa-chevron-right text-[10px] text-gold"></i> Organic Bio-Fertilizer</a></li>
            <li><a href="industry-growing-media.html" class="hover:text-gold flex items-center gap-1.5"><i class="fas fa-chevron-right text-[10px] text-gold"></i> Growing Media & Substrates</a></li>
            <li><a href="industry-water-tech.html" class="hover:text-gold flex items-center gap-1.5"><i class="fas fa-chevron-right text-[10px] text-gold"></i> Korean Water Filtration</a></li>
          </ul>
        </div>

        <!-- Strategic Portals -->
        <div>
          <h4 class="text-sm font-bold text-gold uppercase tracking-wider mb-3">Portals & Trade</h4>
          <ul class="text-xs space-y-2 text-emerald-200">
            <li><a href="products.html" class="hover:text-gold flex items-center gap-1.5"><i class="fas fa-chevron-right text-[10px] text-gold"></i> Product Catalog & Store</a></li>
            <li><a href="export.html" class="hover:text-gold flex items-center gap-1.5"><i class="fas fa-chevron-right text-[10px] text-gold"></i> Global Trading & Export</a></li>
            <li><a href="investment.html" class="hover:text-gold flex items-center gap-1.5"><i class="fas fa-chevron-right text-[10px] text-gold"></i> 8 Investment Opportunities</a></li>
            <li><a href="partners.html" class="hover:text-gold flex items-center gap-1.5"><i class="fas fa-chevron-right text-[10px] text-gold"></i> Become Our Business Partner</a></li>
            <li><a href="gallery.html" class="hover:text-gold flex items-center gap-1.5"><i class="fas fa-chevron-right text-[10px] text-gold"></i> Facilities Photo Gallery</a></li>
            <li><a href="news.html" class="hover:text-gold flex items-center gap-1.5"><i class="fas fa-chevron-right text-[10px] text-gold"></i> Press & Corporate News</a></li>
            <li><a href="faq.html" class="hover:text-gold flex items-center gap-1.5"><i class="fas fa-chevron-right text-[10px] text-gold"></i> Frequently Asked Questions</a></li>
          </ul>
        </div>

        <!-- Official Contact -->
        <div>
          <h4 class="text-sm font-bold text-gold uppercase tracking-wider mb-3">Official Inquiries</h4>
          <div class="text-xs text-emerald-200 space-y-2.5">
            <p class="flex items-start gap-2">
              <i class="fas fa-phone-alt text-gold mt-1"></i>
              <span><strong>Telephone:</strong><br>+94 70 601 0108</span>
            </p>
            <p class="flex items-start gap-2">
              <i class="fab fa-whatsapp text-green-400 mt-1"></i>
              <span><strong>WhatsApp Desk:</strong><br>+94 71 974 0798</span>
            </p>
            <p class="flex items-start gap-2">
              <i class="fas fa-envelope text-gold mt-1"></i>
              <span><strong>Official Email:</strong><br>thilankaherath7@gmail.com</span>
            </p>
            <p class="flex items-start gap-2">
              <i class="fas fa-clock text-gold mt-1"></i>
              <span><strong>Working Hours:</strong><br>Mon - Sat: 8:00 AM - 5:30 PM</span>
            </p>
            
            <div class="pt-2 flex items-center gap-3">
              <a href="#" class="w-8 h-8 rounded-full bg-emerald-900 flex items-center justify-center hover:bg-gold hover:text-forest transition" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
              <a href="#" class="w-8 h-8 rounded-full bg-emerald-900 flex items-center justify-center hover:bg-gold hover:text-forest transition" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
              <a href="#" class="w-8 h-8 rounded-full bg-emerald-900 flex items-center justify-center hover:bg-gold hover:text-forest transition" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
              <a href="https://wa.me/94719740798" target="_blank" class="w-8 h-8 rounded-full bg-emerald-900 flex items-center justify-center hover:bg-green-500 hover:text-white transition" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>
            </div>
          </div>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="pt-8 border-t border-emerald-900/60 flex flex-col md:flex-row justify-between items-center text-xs text-emerald-300 gap-4">
        <p>© 2026 <strong>FOREST LANKA</strong>. All Rights Reserved. Reg: 16/2633. Designed with WCAG 2.2 AAA Accessibility Standards.</p>
        <div class="flex flex-wrap items-center gap-4">
          <a href="privacy-policy.html" class="hover:text-gold">Privacy Policy</a>
          <span class="text-emerald-800">•</span>
          <a href="terms.html" class="hover:text-gold">Terms & Conditions</a>
          <span class="text-emerald-800">•</span>
          <a href="delivery-returns.html" class="hover:text-gold">Delivery & Returns</a>
          <span class="text-emerald-800">•</span>
          <a href="contact.html" class="hover:text-gold">Site Map & Support</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="assets/js/main.js"></script>
"""

print("Base templates defined successfully.")

