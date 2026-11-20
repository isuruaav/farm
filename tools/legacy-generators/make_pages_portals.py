#!/usr/bin/env python3
"""
Generates products.html, export.html, investment.html, and partners.html for FOREST LANKA.
"""

from base_templates import COMMON_HEAD, get_header, COMMON_FOOTER

# ================= 1. PRODUCTS.HTML =================
products_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>Products & Commercial Store | FOREST LANKA E-Commerce & Inquiries</title>
  {COMMON_HEAD}
</head>
<body data-lang="en">
  {get_header('products')}

  <main id="main-content">
    <div class="bg-forest-dark text-white py-16 relative">
      <div class="max-w-7xl mx-auto px-4 relative z-10">
        <div class="text-xs text-gold uppercase tracking-wider font-semibold mb-2 flex items-center gap-2">
          <a href="index.html" class="hover:underline">Home</a>
          <i class="fas fa-chevron-right text-[10px]"></i>
          <span>Product Catalog</span>
        </div>
        <h1 class="text-3xl sm:text-5xl font-black font-heading text-white mb-2">
          <span class="lang-en">Product Catalog & Commercial Orders</span>
          <span class="lang-si">නිෂ්පාදන නාමාවලිය සහ ඇණවුම්</span>
        </h1>
        <p class="text-xs sm:text-base text-emerald-100 max-w-3xl leading-relaxed">
          <span class="lang-en">
            Explore our complete range of certified agricultural and industrial products. Order retail products directly online or request B2B wholesale quotations across our 8 core industries.
          </span>
          <span class="lang-si">
            ආයතනයේ සියලුම කර්මාන්ත අංශයන්හි නිෂ්පාදන මෙහි ඇතුළත් කර ඇත. සිල්ලර හා තොග මිල ගණන් ඉල්ලුම් කළ හැකිය.
          </span>
        </p>
      </div>
    </div>

    <!-- Product Filter & Search Bar -->
    <section class="py-8 bg-white border-b border-gray-200 sticky top-[73px] z-30 shadow-xs">
      <div class="max-w-7xl mx-auto px-4">
        <div class="flex flex-col md:flex-row gap-4 items-center justify-between">
          <!-- Category Tabs -->
          <div class="flex flex-wrap gap-1.5 overflow-x-auto w-full md:w-auto pb-2 md:pb-0 text-xs">
            <button onclick="filterCategory('all', this)" class="prod-cat-btn px-3 py-1.5 rounded-full font-bold bg-forest text-gold shadow-xs">All Products</button>
            <button onclick="filterCategory('poultry', this)" class="prod-cat-btn px-3 py-1.5 rounded-full font-semibold bg-gray-100 hover:bg-emerald-50 text-gray-700">1. Poultry & Eggs</button>
            <button onclick="filterCategory('feed', this)" class="prod-cat-btn px-3 py-1.5 rounded-full font-semibold bg-gray-100 hover:bg-emerald-50 text-gray-700">2. Animal Feed</button>
            <button onclick="filterCategory('trays', this)" class="prod-cat-btn px-3 py-1.5 rounded-full font-semibold bg-gray-100 hover:bg-emerald-50 text-gray-700">3. Egg Trays</button>
            <button onclick="filterCategory('mushrooms', this)" class="prod-cat-btn px-3 py-1.5 rounded-full font-semibold bg-gray-100 hover:bg-emerald-50 text-gray-700">4. Mushrooms</button>
            <button onclick="filterCategory('egg-powder', this)" class="prod-cat-btn px-3 py-1.5 rounded-full font-semibold bg-gray-100 hover:bg-emerald-50 text-gray-700">5. Egg Powders</button>
            <button onclick="filterCategory('fertilizer', this)" class="prod-cat-btn px-3 py-1.5 rounded-full font-semibold bg-gray-100 hover:bg-emerald-50 text-gray-700">6. Bio-Fertilizer</button>
            <button onclick="filterCategory('growing-media', this)" class="prod-cat-btn px-3 py-1.5 rounded-full font-semibold bg-gray-100 hover:bg-emerald-50 text-gray-700">7. Growing Media</button>
            <button onclick="filterCategory('water-tech', this)" class="prod-cat-btn px-3 py-1.5 rounded-full font-semibold bg-gray-100 hover:bg-emerald-50 text-gray-700">8. Korean Water Tech</button>
          </div>

          <!-- Live Search -->
          <div class="relative w-full md:w-64">
            <input type="text" id="product-search-input" onkeyup="searchProducts()" placeholder="Search products..." class="w-full text-xs pl-8 pr-3 py-2 border rounded-full focus:ring-1 focus:ring-emerald-700">
            <i class="fas fa-search absolute left-3 top-2.5 text-gray-400 text-xs"></i>
          </div>
        </div>
      </div>
    </section>

    <!-- Product Grid -->
    <section class="py-12 bg-warmwhite">
      <div class="max-w-7xl mx-auto px-4">
        <div id="product-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">

          <!-- 1. POULTRY SECTOR -->
          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="poultry">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=600&q=80" alt="Cleaned Graded Eggs 30-Tray" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-forest text-gold text-[10px] font-bold px-2 py-0.5 rounded">Sector 1 • Poultry</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">Farm Fresh Cleaned & Graded Eggs (30-Tray)</h3>
                <p class="text-xs text-gray-500 mb-2">Automated candling, cleaned, sanitized, weight-classified Grade A eggs.</p>
                <div class="text-[11px] text-gray-600 bg-warmwhite p-2 rounded mb-2">
                  <span>Variant: 30-Egg Tray</span> • <span>Grade A Medium/Large</span>
                </div>
                <div class="text-sm font-bold text-emerald-800">LKR 1,350.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-EGG-30', name: 'Cleaned Graded Eggs (30-Tray)', price: 1350, priceType: 'fixed', variant: '30-Pack Tray', industry: 'Poultry', image: 'https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=600&q=80'}})" class="btn-primary text-xs w-full py-2">
                <i class="fas fa-cart-plus"></i> Add to Cart
              </button>
            </div>
          </div>

          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="poultry">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1506976785307-8732e854ad03?auto=format&fit=crop&w=600&q=80" alt="Supermarket Retail 12-Pack" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-forest text-gold text-[10px] font-bold px-2 py-0.5 rounded">Sector 1 • Poultry</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">Supermarket Retail Egg Pack (12 Eggs)</h3>
                <p class="text-xs text-gray-500 mb-2">Sealed in biodegradable molded pulp carton with freshness barcode.</p>
                <div class="text-[11px] text-gray-600 bg-warmwhite p-2 rounded mb-2">
                  <span>Variant: 12-Egg Clamshell</span> • <span>Grade A Large</span>
                </div>
                <div class="text-sm font-bold text-emerald-800">LKR 560.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-EGG-12', name: 'Supermarket Egg Pack (12 Eggs)', price: 560, priceType: 'fixed', variant: '12-Egg Pack', industry: 'Poultry', image: 'https://images.unsplash.com/photo-1506976785307-8732e854ad03?auto=format&fit=crop&w=600&q=80'}})" class="btn-primary text-xs w-full py-2">
                <i class="fas fa-cart-plus"></i> Add to Cart
              </button>
            </div>
          </div>

          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="poultry">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1516467508483-a7212febe31a?auto=format&fit=crop&w=600&q=80" alt="Supermarket Retail 6-Pack" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-forest text-gold text-[10px] font-bold px-2 py-0.5 rounded">Sector 1 • Poultry</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">Compact Fresh Egg Pack (06 Eggs)</h3>
                <p class="text-xs text-gray-500 mb-2">Eco-friendly compact retail clamshell for convenience stores.</p>
                <div class="text-[11px] text-gray-600 bg-warmwhite p-2 rounded mb-2">
                  <span>Variant: 06-Egg Pack</span> • <span>Grade A Jumbo</span>
                </div>
                <div class="text-sm font-bold text-emerald-800">LKR 290.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-EGG-06', name: 'Compact Fresh Egg Pack (06 Eggs)', price: 290, priceType: 'fixed', variant: '06-Egg Pack', industry: 'Poultry', image: 'https://images.unsplash.com/photo-1516467508483-a7212febe31a?auto=format&fit=crop&w=600&q=80'}})" class="btn-primary text-xs w-full py-2">
                <i class="fas fa-cart-plus"></i> Add to Cart
              </button>
            </div>
          </div>

          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="poultry">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?auto=format&fit=crop&w=600&q=80" alt="Commercial Hotel Master Crate" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-forest text-gold text-[10px] font-bold px-2 py-0.5 rounded">Sector 1 • Poultry</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">Bakery & Hotel Wholesale (360 Eggs Crate)</h3>
                <p class="text-xs text-gray-500 mb-2">Bulk master shipping container of 12 trays for food production.</p>
                <div class="text-[11px] text-amber-800 bg-amber-50 p-2 rounded mb-2 font-semibold">
                  <span>B2B Commercial Master Pack</span>
                </div>
                <div class="text-sm font-bold text-forest">LKR 15,800.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-EGG-360', name: 'Bakery & Hotel Wholesale (360 Crate)', price: 15800, priceType: 'fixed', variant: '360 Eggs Crate', industry: 'Poultry', image: 'https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?auto=format&fit=crop&w=600&q=80'}})" class="btn-gold text-xs w-full py-2">
                <i class="fas fa-file-invoice"></i> Add Bulk Order
              </button>
            </div>
          </div>

          <!-- 2. ANIMAL FEED SECTOR -->
          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="feed">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1574943320219-553eb213f72d?auto=format&fit=crop&w=600&q=80" alt="High-Yield Layer Feed" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-emerald-700 text-white text-[10px] font-bold px-2 py-0.5 rounded">Sector 2 • Feed</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">High-Yield Layer Feed Pellets (50kg)</h3>
                <p class="text-xs text-gray-500 mb-2">Calibrated crude protein & bio-calcium for extended laying cycles.</p>
                <div class="text-[11px] text-gray-600 bg-warmwhite p-2 rounded mb-2">
                  <span>50kg Polypropylene Bag</span> • <span>Pellet: 3.0mm</span>
                </div>
                <div class="text-sm font-bold text-emerald-800">LKR 7,850.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-FEED-L50', name: 'High-Yield Layer Feed Pellets (50kg)', price: 7850, priceType: 'fixed', variant: '50kg Bag', industry: 'Animal Feed', image: 'https://images.unsplash.com/photo-1574943320219-553eb213f72d?auto=format&fit=crop&w=600&q=80'}})" class="btn-primary text-xs w-full py-2">
                <i class="fas fa-cart-plus"></i> Add to Cart
              </button>
            </div>
          </div>

          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="feed">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=600&q=80" alt="Chick Starter Feed" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-emerald-700 text-white text-[10px] font-bold px-2 py-0.5 rounded">Sector 2 • Feed</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">Chick Starter Crumbles (25kg)</h3>
                <p class="text-xs text-gray-500 mb-2">Micro-crumbled 20.5% protein feed enriched with gut prebiotics.</p>
                <div class="text-[11px] text-gray-600 bg-warmwhite p-2 rounded mb-2">
                  <span>25kg Moisture-Proof Bag</span> • <span>Age: 0-6 Weeks</span>
                </div>
                <div class="text-sm font-bold text-emerald-800">LKR 4,200.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-FEED-C25', name: 'Chick Starter Crumbles (25kg)', price: 4200, priceType: 'fixed', variant: '25kg Bag', industry: 'Animal Feed', image: 'https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=600&q=80'}})" class="btn-primary text-xs w-full py-2">
                <i class="fas fa-cart-plus"></i> Add to Cart
              </button>
            </div>
          </div>

          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="feed">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?auto=format&fit=crop&w=600&q=80" alt="Dairy Cattle Feed" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-emerald-700 text-white text-[10px] font-bold px-2 py-0.5 rounded">Sector 2 • Feed</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">High-Lactation Cattle Feed (50kg)</h3>
                <p class="text-xs text-gray-500 mb-2">Optimized bypass protein and digestible fiber for commercial dairy cows.</p>
                <div class="text-[11px] text-gray-600 bg-warmwhite p-2 rounded mb-2">
                  <span>50kg Bag</span> • <span>Pellet: 4.5mm</span>
                </div>
                <div class="text-sm font-bold text-emerald-800">LKR 6,950.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-FEED-CAT50', name: 'High-Lactation Cattle Feed (50kg)', price: 6950, priceType: 'fixed', variant: '50kg Bag', industry: 'Animal Feed', image: 'https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?auto=format&fit=crop&w=600&q=80'}})" class="btn-primary text-xs w-full py-2">
                <i class="fas fa-cart-plus"></i> Add to Cart
              </button>
            </div>
          </div>

          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="feed">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?auto=format&fit=crop&w=600&q=80" alt="Aquaculture Fish Feed" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-emerald-700 text-white text-[10px] font-bold px-2 py-0.5 rounded">Sector 2 • Feed</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">Floating Aquaculture Fish Pellets (25kg)</h3>
                <p class="text-xs text-gray-500 mb-2">High water stability (>90 mins) enriched with fish meal and omega oils.</p>
                <div class="text-[11px] text-gray-600 bg-warmwhite p-2 rounded mb-2">
                  <span>25kg Floating Pellets</span> • <span>Protein: 32%</span>
                </div>
                <div class="text-sm font-bold text-emerald-800">LKR 5,850.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-FEED-FISH25', name: 'Floating Fish Pellets (25kg)', price: 5850, priceType: 'fixed', variant: '25kg Bag', industry: 'Animal Feed', image: 'https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?auto=format&fit=crop&w=600&q=80'}})" class="btn-primary text-xs w-full py-2">
                <i class="fas fa-cart-plus"></i> Add to Cart
              </button>
            </div>
          </div>

          <!-- 3. RECYCLED PAPER EGG TRAYS -->
          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="trays">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1506976785307-8732e854ad03?auto=format&fit=crop&w=600&q=80" alt="Molded Pulp 30-Egg Trays" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-forest text-gold text-[10px] font-bold px-2 py-0.5 rounded">Sector 3 • Trays</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">Molded Pulp 30-Egg Trays (Bundle 100)</h3>
                <p class="text-xs text-gray-500 mb-2">100% recycled paper molded pulp, shock absorbing commercial trays.</p>
                <div class="text-[11px] text-gray-600 bg-warmwhite p-2 rounded mb-2">
                  <span>Bundle of 100 Trays</span> • <span>Biodegradable</span>
                </div>
                <div class="text-sm font-bold text-emerald-800">LKR 3,200.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-TRAY-B100', name: '30-Egg Trays (Bundle of 100)', price: 3200, priceType: 'fixed', variant: 'Bundle of 100', industry: 'Egg Trays', image: 'https://images.unsplash.com/photo-1506976785307-8732e854ad03?auto=format&fit=crop&w=600&q=80'}})" class="btn-primary text-xs w-full py-2">
                <i class="fas fa-cart-plus"></i> Add to Cart
              </button>
            </div>
          </div>

          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="trays">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=600&q=80" alt="Molded Pulp 12-Egg Clamshell" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-forest text-gold text-[10px] font-bold px-2 py-0.5 rounded">Sector 3 • Trays</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">Molded Pulp 12-Egg Cartons (Pack of 50)</h3>
                <p class="text-xs text-gray-500 mb-2">Consumer interlocking clamshell boxes designed for supermarket shelves.</p>
                <div class="text-[11px] text-gray-600 bg-warmwhite p-2 rounded mb-2">
                  <span>Pack of 50 Cartons</span> • <span>Interlocking Clip</span>
                </div>
                <div class="text-sm font-bold text-emerald-800">LKR 2,450.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-TRAY-C50', name: '12-Egg Cartons (Pack of 50)', price: 2450, priceType: 'fixed', variant: 'Pack of 50', industry: 'Egg Trays', image: 'https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=600&q=80'}})" class="btn-primary text-xs w-full py-2">
                <i class="fas fa-cart-plus"></i> Add to Cart
              </button>
            </div>
          </div>

          <!-- 4. MUSHROOM SECTOR -->
          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="mushrooms">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1509358271058-acd22cc93898?auto=format&fit=crop&w=600&q=80" alt="Shiitake Mushrooms Dried" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-emerald-800 text-gold text-[10px] font-bold px-2 py-0.5 rounded">Sector 4 • Mushrooms</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">Dried Premium Shiitake Mushrooms (1kg)</h3>
                <p class="text-xs text-gray-500 mb-2">Cultivated in IoT climate rooms, slow dehydrated for intense aroma.</p>
                <div class="text-[11px] text-gray-600 bg-warmwhite p-2 rounded mb-2">
                  <span>1kg Vacuum Bag</span> • <span>Export Quality Grade A</span>
                </div>
                <div class="text-sm font-bold text-emerald-800">LKR 6,800.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-MUSH-SH1', name: 'Dried Shiitake Mushrooms (1kg)', price: 6800, priceType: 'fixed', variant: '1kg Vacuum Bag', industry: 'Mushroom', image: 'https://images.unsplash.com/photo-1509358271058-acd22cc93898?auto=format&fit=crop&w=600&q=80'}})" class="btn-primary text-xs w-full py-2">
                <i class="fas fa-cart-plus"></i> Add to Cart
              </button>
            </div>
          </div>

          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="mushrooms">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1518736114815-20be4bf5645e?auto=format&fit=crop&w=600&q=80" alt="Fresh Oyster Mushrooms Punnet" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-emerald-800 text-gold text-[10px] font-bold px-2 py-0.5 rounded">Sector 4 • Mushrooms</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">Fresh Oyster Mushrooms Punnet (200g)</h3>
                <p class="text-xs text-gray-500 mb-2">Daily harvested crisp pearl oyster mushrooms in breathable punnet.</p>
                <div class="text-[11px] text-gray-600 bg-warmwhite p-2 rounded mb-2">
                  <span>200g Retail Punnet</span> • <span>Cold-Chain Delivered</span>
                </div>
                <div class="text-sm font-bold text-emerald-800">LKR 280.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-MUSH-OY200', name: 'Fresh Oyster Mushrooms (200g)', price: 280, priceType: 'fixed', variant: '200g Punnet', industry: 'Mushroom', image: 'https://images.unsplash.com/photo-1518736114815-20be4bf5645e?auto=format&fit=crop&w=600&q=80'}})" class="btn-primary text-xs w-full py-2">
                <i class="fas fa-cart-plus"></i> Add to Cart
              </button>
            </div>
          </div>

          <!-- 5. EGG POWDER & VALUE ADDED SECTOR -->
          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="egg-powder">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1516467508483-a7212febe31a?auto=format&fit=crop&w=600&q=80" alt="Spray Dried Whole Egg Powder" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-gold text-forest text-[10px] font-bold px-2 py-0.5 rounded">Sector 5 • Egg Powder</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">Spray-Dried Whole Egg Powder (20kg)</h3>
                <p class="text-xs text-gray-500 mb-2">Pasteurized, 24-month ambient shelf life for commercial food manufacturers.</p>
                <div class="text-[11px] text-amber-800 bg-amber-50 p-2 rounded mb-2 font-semibold">
                  <span>B2B Industrial Quotation</span> • <span>20kg Box</span>
                </div>
                <div class="text-sm font-bold text-amber-700">Commercial Quote</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-EP-WHOLE20', name: 'Spray-Dried Whole Egg Powder (20kg)', price: 0, priceType: 'quote', variant: '20kg Box', industry: 'Egg Powder', image: 'https://images.unsplash.com/photo-1516467508483-a7212febe31a?auto=format&fit=crop&w=600&q=80'}})" class="btn-gold text-xs w-full py-2">
                <i class="fas fa-file-invoice"></i> Request Quote
              </button>
            </div>
          </div>

          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="egg-powder">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=600&q=80" alt="High Whip Albumen Powder" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-gold text-forest text-[10px] font-bold px-2 py-0.5 rounded">Sector 5 • Egg Powder</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">High-Whipping Egg White Albumen Powder (1kg)</h3>
                <p class="text-xs text-gray-500 mb-2">Desugared, rapid whipping stability for high-end bakeries & meringues.</p>
                <div class="text-[11px] text-gray-600 bg-warmwhite p-2 rounded mb-2">
                  <span>1kg Moisture Foil Pouch</span> • <span>High-Gel</span>
                </div>
                <div class="text-sm font-bold text-emerald-800">LKR 3,850.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-EP-ALB1', name: 'High-Whip Albumen Powder (1kg)', price: 3850, priceType: 'fixed', variant: '1kg Pouch', industry: 'Egg Powder', image: 'https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=600&q=80'}})" class="btn-primary text-xs w-full py-2">
                <i class="fas fa-cart-plus"></i> Add to Cart
              </button>
            </div>
          </div>

          <!-- 6. ORGANIC FERTILIZER SECTOR -->
          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="fertilizer">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1615811361523-6bd03d7748e7?auto=format&fit=crop&w=600&q=80" alt="Pelleted Poultry Fertilizer" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-emerald-700 text-white text-[10px] font-bold px-2 py-0.5 rounded">Sector 6 • Fertilizer</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">Sterilized Pelleted Poultry Bio-Fertilizer (20kg)</h3>
                <p class="text-xs text-gray-500 mb-2">100% organic farm manure, pathogen-free, odorless 4mm slow-release pellets.</p>
                <div class="text-[11px] text-gray-600 bg-warmwhite p-2 rounded mb-2">
                  <span>20kg Heavy-Duty Sack</span> • <span>NPK 4:3:2.5</span>
                </div>
                <div class="text-sm font-bold text-emerald-800">LKR 1,850.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-FERT-20KG', name: 'Sterilized Poultry Fertilizer (20kg)', price: 1850, priceType: 'fixed', variant: '20kg Sack', industry: 'Organic Fertilizer', image: 'https://images.unsplash.com/photo-1615811361523-6bd03d7748e7?auto=format&fit=crop&w=600&q=80'}})" class="btn-primary text-xs w-full py-2">
                <i class="fas fa-cart-plus"></i> Add to Cart
              </button>
            </div>
          </div>

          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="fertilizer">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?auto=format&fit=crop&w=600&q=80" alt="Garden Compost" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-emerald-700 text-white text-[10px] font-bold px-2 py-0.5 rounded">Sector 6 • Fertilizer</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">Enriched Bio-Organic Garden Compost (10kg)</h3>
                <p class="text-xs text-gray-500 mb-2">Inoculated with beneficial soil microbes and humic acid for lush flowering.</p>
                <div class="text-[11px] text-gray-600 bg-warmwhite p-2 rounded mb-2">
                  <span>10kg Consumer Pack</span> • <span>Rich Organic Matter</span>
                </div>
                <div class="text-sm font-bold text-emerald-800">LKR 950.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-FERT-10KG', name: 'Enriched Garden Compost (10kg)', price: 950, priceType: 'fixed', variant: '10kg Pack', industry: 'Organic Fertilizer', image: 'https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?auto=format&fit=crop&w=600&q=80'}})" class="btn-primary text-xs w-full py-2">
                <i class="fas fa-cart-plus"></i> Add to Cart
              </button>
            </div>
          </div>

          <!-- 7. GROWING MEDIA SECTOR -->
          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="growing-media">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?auto=format&fit=crop&w=600&q=80" alt="Seed Starting Mix" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-emerald-900 text-gold text-[10px] font-bold px-2 py-0.5 rounded">Sector 7 • Media</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">Precision Seed Starting Propagation Mix (25L)</h3>
                <p class="text-xs text-gray-500 mb-2">Fine-milled, sterile seedling substrate ensuring >95% germination rates.</p>
                <div class="text-[11px] text-gray-600 bg-warmwhite p-2 rounded mb-2">
                  <span>25 Liters Bag</span> • <span>Low EC & Balanced Aeration</span>
                </div>
                <div class="text-sm font-bold text-emerald-800">LKR 1,450.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-GM-SEED25', name: 'Seed Starting Mix (25L)', price: 1450, priceType: 'fixed', variant: '25L Bag', industry: 'Growing Media', image: 'https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?auto=format&fit=crop&w=600&q=80'}})" class="btn-primary text-xs w-full py-2">
                <i class="fas fa-cart-plus"></i> Add to Cart
              </button>
            </div>
          </div>

          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="growing-media">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1615811361523-6bd03d7748e7?auto=format&fit=crop&w=600&q=80" alt="Potting Mix" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-emerald-900 text-gold text-[10px] font-bold px-2 py-0.5 rounded">Sector 7 • Media</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">Premium Potting Soil Mix (50L)</h3>
                <p class="text-xs text-gray-500 mb-2">Nutrient-buffered coco and perlite blend for potted ornamentals and vegetables.</p>
                <div class="text-[11px] text-gray-600 bg-warmwhite p-2 rounded mb-2">
                  <span>50 Liters Sack</span> • <span>pH 6.0 – 6.5</span>
                </div>
                <div class="text-sm font-bold text-emerald-800">LKR 2,600.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-GM-POT50', name: 'Premium Potting Soil Mix (50L)', price: 2600, priceType: 'fixed', variant: '50L Bag', industry: 'Growing Media', image: 'https://images.unsplash.com/photo-1615811361523-6bd03d7748e7?auto=format&fit=crop&w=600&q=80'}})" class="btn-primary text-xs w-full py-2">
                <i class="fas fa-cart-plus"></i> Add to Cart
              </button>
            </div>
          </div>

          <!-- 8. WATER TECH SECTOR -->
          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="water-tech">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=600&q=80" alt="Korean Smart RO Purifier" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-waterblue text-white text-[10px] font-bold px-2 py-0.5 rounded">Sector 8 • Water Tech</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">South Korean Smart IoT Alkaline RO Purifier</h3>
                <p class="text-xs text-gray-500 mb-2">Touch UI, real-time TDS display, UV-C tank disinfection, Korean membrane.</p>
                <div class="text-[11px] text-blue-900 bg-blue-50 p-2 rounded mb-2 font-semibold">
                  <span>Domestic Smart Countertop</span> • <span>75 GPD</span>
                </div>
                <div class="text-sm font-bold text-waterblue">LKR 89,500.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-WT-SMART-RO', name: 'Korean Smart IoT RO Purifier', price: 89500, priceType: 'fixed', variant: 'Smart Countertop Unit', industry: 'Water Tech', image: 'https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=600&q=80'}})" class="btn-primary text-xs w-full py-2 bg-waterblue hover:bg-waterblue-dark">
                <i class="fas fa-cart-plus"></i> Add to Cart
              </button>
            </div>
          </div>

          <div class="product-item bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition" data-category="water-tech">
            <div>
              <div class="relative h-48 overflow-hidden bg-gray-100">
                <img src="https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=600&q=80" alt="Commercial RO Water Station" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-waterblue text-white text-[10px] font-bold px-2 py-0.5 rounded">Sector 8 • Water Tech</span>
              </div>
              <div class="p-4">
                <h3 class="font-bold text-sm text-forest mb-1">Commercial Multi-Stage 400 GPD Water Station</h3>
                <p class="text-xs text-gray-500 mb-2">High capacity purified drinking water for offices, schools, and hospitals.</p>
                <div class="text-[11px] text-blue-900 bg-blue-50 p-2 rounded mb-2 font-semibold">
                  <span>Commercial 400 GPD</span> • <span>Heavy-Duty</span>
                </div>
                <div class="text-sm font-bold text-waterblue">LKR 145,000.00</div>
              </div>
            </div>
            <div class="p-4 pt-0">
              <button onclick="addToCart({{id: 'FL-WT-COMM-400', name: 'Commercial 400 GPD Water Station', price: 145000, priceType: 'fixed', variant: 'Commercial Station', industry: 'Water Tech', image: 'https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=600&q=80'}})" class="btn-primary text-xs w-full py-2 bg-waterblue hover:bg-waterblue-dark">
                <i class="fas fa-cart-plus"></i> Add to Cart
              </button>
            </div>
          </div>

        </div>
      </div>
    </section>
  </main>

  {COMMON_FOOTER}
</body>
</html>
"""

# ================= 2. EXPORT.HTML (PDF SECTION 06) =================
export_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>Global Trading & Export Management | FOREST LANKA</title>
  {COMMON_HEAD}
</head>
<body data-lang="en">
  {get_header('export')}

  <main id="main-content">
    <div class="bg-forest-dark text-white py-16 relative">
      <div class="max-w-7xl mx-auto px-4 relative z-10">
        <div class="text-xs text-gold uppercase tracking-wider font-semibold mb-2 flex items-center gap-2">
          <a href="index.html" class="hover:underline">Home</a>
          <i class="fas fa-chevron-right text-[10px]"></i>
          <span>Global Trade</span>
        </div>
        <h1 class="text-3xl sm:text-5xl font-black font-heading text-white mb-2">
          <span class="lang-en">Global Trading & Export Opportunities</span>
          <span class="lang-si">ජාත්‍යන්තර වෙළෙඳාම සහ අපනයන කළමනාකරණය</span>
        </h1>
        <p class="text-xs sm:text-base text-emerald-100 max-w-3xl leading-relaxed">
          <span class="lang-en">
            Connecting international food importers, wholesale distributors, and global trading houses with Sri Lanka's finest export-grade mushrooms, functional egg powders, biodegradable paper egg trays, and advanced water purification systems.
          </span>
          <span class="lang-si">
            FOREST LANKA ආයතනයේ නිෂ්පාදන ජාත්‍යන්තර වෙළෙඳපොළ වෙත හඳුන්වාදීමට සහ විදේශීය ගැනුම්කරුවන් සමඟ සම්බන්ධ වීමට Export Management පහසුකම් මෙහි සලසා ඇත.
          </span>
        </p>
      </div>
    </div>

    <!-- Export Standards & Logistics Grid -->
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-16 text-center">
          <div class="p-6 bg-warmwhite rounded-2xl border border-gray-200">
            <div class="w-12 h-12 rounded-full bg-emerald-100 text-emerald-800 flex items-center justify-center text-xl mx-auto mb-3">
              <i class="fas fa-ship"></i>
            </div>
            <h4 class="font-bold text-sm text-forest mb-1">Sea Freight Logistics</h4>
            <p class="text-xs text-gray-600">FOB Colombo Port & Hambantota Deep Sea Port for full container loads (FCL).</p>
          </div>

          <div class="p-6 bg-warmwhite rounded-2xl border border-gray-200">
            <div class="w-12 h-12 rounded-full bg-emerald-100 text-emerald-800 flex items-center justify-center text-xl mx-auto mb-3">
              <i class="fas fa-plane-departure"></i>
            </div>
            <h4 class="font-bold text-sm text-forest mb-1">Air Cargo Dispatch</h4>
            <p class="text-xs text-gray-600">Daily temperature-controlled air freight via Bandaranaike International Airport (CMB).</p>
          </div>

          <div class="p-6 bg-warmwhite rounded-2xl border border-gray-200">
            <div class="w-12 h-12 rounded-full bg-emerald-100 text-emerald-800 flex items-center justify-center text-xl mx-auto mb-3">
              <i class="fas fa-snowflake"></i>
            </div>
            <h4 class="font-bold text-sm text-forest mb-1">Cold-Chain Assurance</h4>
            <p class="text-xs text-gray-600">Continuous 4°C monitoring for fresh mushrooms and table eggs from packing to port.</p>
          </div>

          <div class="p-6 bg-warmwhite rounded-2xl border border-gray-200">
            <div class="w-12 h-12 rounded-full bg-emerald-100 text-emerald-800 flex items-center justify-center text-xl mx-auto mb-3">
              <i class="fas fa-file-contract"></i>
            </div>
            <h4 class="font-bold text-sm text-forest mb-1">Global Trade Documents</h4>
            <p class="text-xs text-gray-600">Phytosanitary Certificates, Certificate of Origin, Bill of Lading, and Quality Audits.</p>
          </div>
        </div>

        <!-- Export Catalog & Specs Table (PDF Section 6.1) -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
          <div class="lg:col-span-7 space-y-6">
            <span class="text-xs font-bold uppercase tracking-wider text-emerald-700">Export Portfolio</span>
            <h2 class="text-2xl font-bold text-forest font-heading">Export Product Catalog & Minimum Order Quantities (MOQ)</h2>
            <div class="overflow-x-auto bg-white rounded-xl border border-gray-200 shadow-sm">
              <table class="w-full text-left border-collapse text-xs">
                <thead>
                  <tr class="bg-forest text-white">
                    <th class="p-3">Export Product</th>
                    <th class="p-3">Packaging Spec</th>
                    <th class="p-3">MOQ</th>
                    <th class="p-3">Target Markets</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-gray-100">
                  <tr>
                    <td class="p-3 font-semibold text-forest">Dehydrated Gourmet Mushrooms</td>
                    <td class="p-3 text-gray-600">1kg Vacuum Bags / 10kg Master Carton</td>
                    <td class="p-3 font-mono font-bold text-emerald-800">250 kg</td>
                    <td class="p-3 text-gray-600">Middle East, Asia, EU</td>
                  </tr>
                  <tr>
                    <td class="p-3 font-semibold text-forest">Spray-Dried Whole Egg Powder</td>
                    <td class="p-3 text-gray-600">20kg Multi-wall Poly Liner Boxes</td>
                    <td class="p-3 font-mono font-bold text-emerald-800">1,000 kg (1 MT)</td>
                    <td class="p-3 text-gray-600">Food Manufacturers Global</td>
                  </tr>
                  <tr>
                    <td class="p-3 font-semibold text-forest">High-Whipping Egg Albumen Powder</td>
                    <td class="p-3 text-gray-600">20kg Boxes / 1kg Pouches</td>
                    <td class="p-3 font-mono font-bold text-emerald-800">500 kg</td>
                    <td class="p-3 text-gray-600">Bakeries & Confectionery</td>
                  </tr>
                  <tr>
                    <td class="p-3 font-semibold text-forest">Recycled Molded Pulp Egg Trays</td>
                    <td class="p-3 text-gray-600">Bundles of 100 / Pallets of 5,000</td>
                    <td class="p-3 font-mono font-bold text-emerald-800">1 × 40ft HQ Container</td>
                    <td class="p-3 text-gray-600">Regional Poultry Exporters</td>
                  </tr>
                  <tr>
                    <td class="p-3 font-semibold text-forest">Fresh Grade A Table Eggs</td>
                    <td class="p-3 text-gray-600">Molded Trays in Master Shipping Cartons</td>
                    <td class="p-3 font-mono font-bold text-emerald-800">1 × 20ft Reefer Container</td>
                    <td class="p-3 text-gray-600">Maldives, Middle East</td>
                  </tr>
                  <tr>
                    <td class="p-3 font-semibold text-forest">Korean Water Purifier Units</td>
                    <td class="p-3 text-gray-600">Export Protective Packaging</td>
                    <td class="p-3 font-mono font-bold text-emerald-800">50 Units</td>
                    <td class="p-3 text-gray-600">South Asia Regional</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- Export Policies -->
            <div class="bg-warmwhite p-5 rounded-2xl border border-gray-200 text-xs text-gray-700 space-y-2">
              <h4 class="font-bold text-forest text-sm uppercase tracking-wider mb-2">Export Commercial Policies</h4>
              <p>• <strong>Payment Terms:</strong> Confirmed Irrevocable Letter of Credit (L/C at sight) or T/T Wire Transfer.</p>
              <p>• <strong>Samples:</strong> Express international sample courier available for registered food importers upon verification.</p>
              <p>• <strong>Custom Labeling:</strong> OEM branding, buyer barcoding, and multilingual box printing available for long-term contract quotas.</p>
            </div>
          </div>

          <!-- Interactive Export Quotation & Sample Request Form (PDF Page 13) -->
          <div class="lg:col-span-5">
            <div class="bg-forest-dark text-white p-6 sm:p-8 rounded-3xl border-2 border-gold/40 shadow-2xl">
              <div class="flex items-center gap-3 mb-4 border-b border-emerald-800 pb-3">
                <i class="fas fa-globe-asia text-gold text-2xl"></i>
                <div>
                  <h3 class="font-bold text-base text-white font-heading">Export Quotation & Sample Request</h3>
                  <p class="text-xs text-emerald-200">Direct Portal for Foreign Buyers & Importers</p>
                </div>
              </div>

              <form id="export-inquiry-form" class="space-y-3.5">
                <div>
                  <label class="block text-xs font-semibold text-emerald-200 mb-1">Contact Person Name *</label>
                  <input type="text" required placeholder="Full Name" class="w-full text-xs p-2.5 rounded bg-white text-charcoal border focus:ring-1 focus:ring-gold">
                </div>

                <div>
                  <label class="block text-xs font-semibold text-emerald-200 mb-1">Company / Importer Name *</label>
                  <input type="text" required placeholder="Corporate entity name" class="w-full text-xs p-2.5 rounded bg-white text-charcoal border focus:ring-1 focus:ring-gold">
                </div>

                <div class="grid grid-cols-2 gap-2">
                  <div>
                    <label class="block text-xs font-semibold text-emerald-200 mb-1">Buyer Country *</label>
                    <input type="text" required placeholder="e.g. UAE, Qatar, Maldives" class="w-full text-xs p-2.5 rounded bg-white text-charcoal border focus:ring-1 focus:ring-gold">
                  </div>
                  <div>
                    <label class="block text-xs font-semibold text-emerald-200 mb-1">Port of Destination</label>
                    <input type="text" placeholder="e.g. Jebel Ali, Malé" class="w-full text-xs p-2.5 rounded bg-white text-charcoal border focus:ring-1 focus:ring-gold">
                  </div>
                </div>

                <div class="grid grid-cols-2 gap-2">
                  <div>
                    <label class="block text-xs font-semibold text-emerald-200 mb-1">Email Address *</label>
                    <input type="email" required placeholder="procurement@company.com" class="w-full text-xs p-2.5 rounded bg-white text-charcoal border focus:ring-1 focus:ring-gold">
                  </div>
                  <div>
                    <label class="block text-xs font-semibold text-emerald-200 mb-1">WhatsApp / Phone *</label>
                    <input type="tel" required placeholder="+Country code..." class="w-full text-xs p-2.5 rounded bg-white text-charcoal border focus:ring-1 focus:ring-gold">
                  </div>
                </div>

                <div>
                  <label class="block text-xs font-semibold text-emerald-200 mb-1">Target Product Line *</label>
                  <select required class="w-full text-xs p-2.5 rounded bg-white text-charcoal border focus:ring-1 focus:ring-gold">
                    <option value="">Select Target Export Product</option>
                    <option value="shiitake_oyster">Dehydrated Shiitake & Gourmet Mushrooms</option>
                    <option value="egg_powder">Spray-Dried Whole Egg Powder (Food Grade)</option>
                    <option value="albumen_powder">High-Whipping Egg White Albumen Powder</option>
                    <option value="egg_trays">Recycled Molded Pulp Egg Trays (Bulk Containers)</option>
                    <option value="fresh_table_eggs">Fresh Table Eggs (Cold Reefer Containers)</option>
                    <option value="water_purifiers">Korean Smart Water Purifiers</option>
                  </select>
                </div>

                <div>
                  <label class="block text-xs font-semibold text-emerald-200 mb-1">Estimated Target Volume & Incoterms</label>
                  <input type="text" placeholder="e.g. 5 Metric Tons, FOB Colombo or CIF Jebel Ali" class="w-full text-xs p-2.5 rounded bg-white text-charcoal border focus:ring-1 focus:ring-gold">
                </div>

                <div class="flex items-center gap-2 pt-1 text-xs text-emerald-200">
                  <input type="checkbox" id="request-sample-check" class="rounded text-emerald-600 focus:ring-gold">
                  <label for="request-sample-check">Request Product Lab Sample for Evaluation</label>
                </div>

                <div>
                  <label class="block text-xs font-semibold text-emerald-200 mb-1">Commercial Specifications / Requirements</label>
                  <textarea rows="2" placeholder="Custom packaging, certification requests, delivery schedules..." class="w-full text-xs p-2.5 rounded bg-white text-charcoal border focus:ring-1 focus:ring-gold"></textarea>
                </div>

                <div class="pt-2">
                  <button type="submit" class="btn-gold text-xs w-full py-3">
                    <i class="fas fa-paper-plane"></i> Submit Export Inquiry & Sample Request
                  </button>
                </div>
              </form>

              <div class="mt-4 pt-3 border-t border-emerald-800 text-center">
                <a href="https://wa.me/94719740798" target="_blank" class="text-xs text-gold font-bold hover:underline flex items-center justify-center gap-1.5">
                  <i class="fab fa-whatsapp text-green-400"></i> Direct International Trade Desk on WhatsApp
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

  {COMMON_FOOTER}
</body>
</html>
"""

# ================= 3. INVESTMENT.HTML (PDF SECTION 07) =================
investment_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>Investment & Strategic Partnerships | FOREST LANKA Capital Projects</title>
  {COMMON_HEAD}
</head>
<body data-lang="en">
  {get_header('investment')}

  <main id="main-content">
    <div class="bg-forest-dark text-white py-16 relative">
      <div class="max-w-7xl mx-auto px-4 relative z-10">
        <div class="text-xs text-gold uppercase tracking-wider font-semibold mb-2 flex items-center gap-2">
          <a href="index.html" class="hover:underline">Home</a>
          <i class="fas fa-chevron-right text-[10px]"></i>
          <span>Strategic Capital</span>
        </div>
        <h1 class="text-3xl sm:text-5xl font-black font-heading text-white mb-2">
          <span class="lang-en">Investment & Strategic Partnerships</span>
          <span class="lang-si">ආයෝජන සහ උපායමාර්ගික හවුල්කාරිත්වය</span>
        </h1>
        <p class="text-xs sm:text-base text-emerald-100 max-w-3xl leading-relaxed">
          <span class="lang-en">
            FOREST LANKA presents 8 high-yield industrial capital projects designed for visionary domestic and foreign investors. Partner in our scalable smart agro-industrial ecosystem with South Korean technology integration.
          </span>
          <span class="lang-si">
            FOREST LANKA ආයතනයේ සැලසුම්ගත කර්මාන්ත ව්‍යාපෘති සඳහා දේශීය හා විදේශීය ආයෝජකයන් සම්බන්ධ කරගැනීමේ අවස්ථා 08ක් මෙහි ඉදිරිපත් කෙරේ.
          </span>
        </p>
      </div>
    </div>

    <!-- The 8 Investment Opportunities (PDF Section 7) -->
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4">
        <div class="text-center max-w-3xl mx-auto mb-14">
          <span class="text-xs font-bold uppercase tracking-wider text-emerald-700">Project Portfolio</span>
          <h2 class="text-3xl font-black text-forest font-heading">The 8 Capital Investment Projects</h2>
          <p class="text-xs sm:text-sm text-gray-600 mt-2">
            Each project features clear ROI metrics, robust biosecurity governance, land tenure clarity, and high-efficiency market pipelines.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
          <!-- 1. Poultry Expansion -->
          <div class="bg-warmwhite p-5 rounded-2xl border border-gray-200 flex flex-col justify-between shadow-xs">
            <div>
              <div class="flex justify-between items-center mb-3">
                <span class="text-xs font-bold text-gold bg-forest px-2.5 py-0.5 rounded">Project 01</span>
                <span class="badge-status-operational">Operational & Scaling</span>
              </div>
              <h3 class="font-bold text-sm text-forest mb-2">Modern Smart Layer Poultry Complex</h3>
              <p class="text-xs text-gray-600 leading-relaxed mb-3">
                Scaling from foundational 125,000 layers systematically to 2.5 Million hens with computerized multi-tier automated cage systems.
              </p>
              <div class="text-[11px] font-semibold text-emerald-800 bg-white p-2.5 rounded border border-gray-100 space-y-1 mb-4">
                <div>• Initial Flock: 125,000 Hens</div>
                <div>• Target Capacity: 2.5 Million Layers</div>
                <div>• High Daily Cashflow Velocity</div>
              </div>
            </div>
            <a href="#invest-form-section" class="btn-primary text-xs w-full py-2">Express Interest</a>
          </div>

          <!-- 2. Animal Feed Mill -->
          <div class="bg-warmwhite p-5 rounded-2xl border border-gray-200 flex flex-col justify-between shadow-xs">
            <div>
              <div class="flex justify-between items-center mb-3">
                <span class="text-xs font-bold text-gold bg-forest px-2.5 py-0.5 rounded">Project 02</span>
                <span class="badge-status-development">Under Development</span>
              </div>
              <h3 class="font-bold text-sm text-forest mb-2">Industrial High-Capacity Feed Mill</h3>
              <p class="text-xs text-gray-600 leading-relaxed mb-3">
                Full 12-step automated steam pelletizing plant supplying internal poultry flocks and commercial livestock farmers islandwide.
              </p>
              <div class="text-[11px] font-semibold text-emerald-800 bg-white p-2.5 rounded border border-gray-100 space-y-1 mb-4">
                <div>• Complete 12-Step Automated Line</div>
                <div>• Guaranteed Internal Captive Demand</div>
                <div>• High Commercial Margin Feed Blends</div>
              </div>
            </div>
            <a href="#invest-form-section" class="btn-primary text-xs w-full py-2">Express Interest</a>
          </div>

          <!-- 3. Egg Tray Plant -->
          <div class="bg-warmwhite p-5 rounded-2xl border border-gray-200 flex flex-col justify-between shadow-xs">
            <div>
              <div class="flex justify-between items-center mb-3">
                <span class="text-xs font-bold text-gold bg-forest px-2.5 py-0.5 rounded">Project 03</span>
                <span class="badge-status-operational">Operational</span>
              </div>
              <h3 class="font-bold text-sm text-forest mb-2">Recycled Paper Egg Tray Manufacturing</h3>
              <p class="text-xs text-gray-600 leading-relaxed mb-3">
                High-speed rotary vacuum forming machines producing 100,000+ biodegradable molded pulp trays daily from post-consumer paper.
              </p>
              <div class="text-[11px] font-semibold text-emerald-800 bg-white p-2.5 rounded border border-gray-100 space-y-1 mb-4">
                <div>• 100% Recycled Raw Material Input</div>
                <div>• Low Production Cost Structure</div>
                <div>• Growing Demand from Plastic Bans</div>
              </div>
            </div>
            <a href="#invest-form-section" class="btn-primary text-xs w-full py-2">Express Interest</a>
          </div>

          <!-- 4. Mushroom Facility -->
          <div class="bg-warmwhite p-5 rounded-2xl border border-gray-200 flex flex-col justify-between shadow-xs">
            <div>
              <div class="flex justify-between items-center mb-3">
                <span class="text-xs font-bold text-gold bg-forest px-2.5 py-0.5 rounded">Project 04</span>
                <span class="badge-status-development">Under Development</span>
              </div>
              <h3 class="font-bold text-sm text-forest mb-2">5-10 Acre Smart Mushroom Facility</h3>
              <p class="text-xs text-gray-600 leading-relaxed mb-3">
                Climate-controlled cleanroom chambers for gourmet Shiitake, Oyster, and Button mushrooms geared for lucrative air-cargo exports.
              </p>
              <div class="text-[11px] font-semibold text-emerald-800 bg-white p-2.5 rounded border border-gray-100 space-y-1 mb-4">
                <div>• 5 to 10 Acres High-Density Land</div>
                <div>• Positive Cashflow within 90 Days</div>
                <div>• Export Foreign Exchange Yield</div>
              </div>
            </div>
            <a href="#invest-form-section" class="btn-primary text-xs w-full py-2">Express Interest</a>
          </div>

          <!-- 5. Egg Processing -->
          <div class="bg-warmwhite p-5 rounded-2xl border border-gray-200 flex flex-col justify-between shadow-xs">
            <div>
              <div class="flex justify-between items-center mb-3">
                <span class="text-xs font-bold text-gold bg-forest px-2.5 py-0.5 rounded">Project 05</span>
                <span class="badge-status-planned">Planned (Phase 3)</span>
              </div>
              <h3 class="font-bold text-sm text-forest mb-2">Egg Spray-Drying & Powder Plant</h3>
              <p class="text-xs text-gray-600 leading-relaxed mb-3">
                Sri Lanka's breakthrough industrial facility transforming fresh surplus eggs into pasteurized Whole Egg, Yolk, and Albumen powders.
              </p>
              <div class="text-[11px] font-semibold text-emerald-800 bg-white p-2.5 rounded border border-gray-100 space-y-1 mb-4">
                <div>• Massive Import Substitution Value</div>
                <div>• 24-Month Ambient Shelf Life</div>
                <div>• Captive Demand from Food Industry</div>
              </div>
            </div>
            <a href="#invest-form-section" class="btn-primary text-xs w-full py-2">Express Interest</a>
          </div>

          <!-- 6. Organic Fertilizer -->
          <div class="bg-warmwhite p-5 rounded-2xl border border-gray-200 flex flex-col justify-between shadow-xs">
            <div>
              <div class="flex justify-between items-center mb-3">
                <span class="text-xs font-bold text-gold bg-forest px-2.5 py-0.5 rounded">Project 06</span>
                <span class="badge-status-operational">Operational</span>
              </div>
              <h3 class="font-bold text-sm text-forest mb-2">Commercial Bio-Organic Fertilizer Plant</h3>
              <p class="text-xs text-gray-600 leading-relaxed mb-3">
                Zero-waste conversion of poultry manure into sterilized, pelleted organic fertilizer for national tea estates and commercial crops.
              </p>
              <div class="text-[11px] font-semibold text-emerald-800 bg-white p-2.5 rounded border border-gray-100 space-y-1 mb-4">
                <div>• Zero Raw Material Cost from Farm</div>
                <div>• Government Certified Standards</div>
                <div>• Strong National Plantation Demand</div>
              </div>
            </div>
            <a href="#invest-form-section" class="btn-primary text-xs w-full py-2">Express Interest</a>
          </div>

          <!-- 7. Growing Media -->
          <div class="bg-warmwhite p-5 rounded-2xl border border-gray-200 flex flex-col justify-between shadow-xs">
            <div>
              <div class="flex justify-between items-center mb-3">
                <span class="text-xs font-bold text-gold bg-forest px-2.5 py-0.5 rounded">Project 07</span>
                <span class="badge-status-operational">Operational</span>
              </div>
              <h3 class="font-bold text-sm text-forest mb-2">Growing Media & Horticultural Substrates</h3>
              <p class="text-xs text-gray-600 leading-relaxed mb-3">
                Washed low-EC cocopeat and perlite soilless media processing facility supporting export floriculture and greenhouse horticulture.
              </p>
              <div class="text-[11px] font-semibold text-emerald-800 bg-white p-2.5 rounded border border-gray-100 space-y-1 mb-4">
                <div>• Abundant Local Raw Coir Sourcing</div>
                <div>• Rapidly Expanding Urban Garden Market</div>
                <div>• High Margin Specialty Formulations</div>
              </div>
            </div>
            <a href="#invest-form-section" class="btn-primary text-xs w-full py-2">Express Interest</a>
          </div>

          <!-- 8. Korean Water Tech -->
          <div class="bg-warmwhite p-5 rounded-2xl border border-gray-200 flex flex-col justify-between shadow-xs">
            <div>
              <div class="flex justify-between items-center mb-3">
                <span class="text-xs font-bold text-white bg-waterblue px-2.5 py-0.5 rounded">Project 08</span>
                <span class="badge-status-development">S. Korean Joint Venture</span>
              </div>
              <h3 class="font-bold text-sm text-forest mb-2">Smart Water Filtration Assembly Plant</h3>
              <p class="text-xs text-gray-600 leading-relaxed mb-3">
                Establishing an authorized assembly and manufacturing plant for South Korean smart IoT water purifiers and industrial RO plants.
              </p>
              <div class="text-[11px] font-semibold text-waterblue bg-blue-50/60 p-2.5 rounded border border-blue-100 space-y-1 mb-4">
                <div>• South Korean Technology Transfer</div>
                <div>• Domestic Plant Assembly Rights</div>
                <div>• Regional South Asian Export Access</div>
              </div>
            </div>
            <a href="#invest-form-section" class="btn-primary text-xs w-full py-2 bg-waterblue hover:bg-waterblue-dark">Express Interest</a>
          </div>
        </div>

        <!-- Investment EOI Form (PDF Section 7 & Page 14) -->
        <div id="invest-form-section" class="bg-forest-dark text-white p-8 lg:p-12 rounded-3xl border-2 border-gold/40 shadow-2xl">
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
            <div class="lg:col-span-5 space-y-4">
              <span class="text-xs font-bold text-gold uppercase tracking-wider bg-gold/10 px-3 py-1 rounded-full border border-gold/30">
                Direct Expression of Interest (EOI)
              </span>
              <h2 class="text-3xl font-black text-white font-heading">
                Submit an Investor Inquire to Our Board of Directors
              </h2>
              <p class="text-xs sm:text-sm text-emerald-100/90 leading-relaxed">
                Whether you represent an institutional private equity fund, an agribusiness group, an angel investor syndicate, or an international joint venture partner, FOREST LANKA welcomes strategic engagement.
              </p>
              <div class="space-y-2 text-xs text-emerald-200 pt-2">
                <div class="flex items-center gap-2"><i class="fas fa-check-circle text-gold"></i> Comprehensive Data Room Access</div>
                <div class="flex items-center gap-2"><i class="fas fa-check-circle text-gold"></i> Detailed Feasibility Studies & Financial Projections</div>
                <div class="flex items-center gap-2"><i class="fas fa-check-circle text-gold"></i> Direct Briefing with Company Leadership</div>
              </div>
            </div>

            <div class="lg:col-span-7 bg-white text-charcoal p-6 sm:p-8 rounded-2xl shadow-xl">
              <form id="investment-eoi-form" class="space-y-3.5">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div>
                    <label class="block text-xs font-semibold text-gray-700 mb-1">Investor / Firm Name *</label>
                    <input type="text" required placeholder="Individual or Institution" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700">
                  </div>
                  <div>
                    <label class="block text-xs font-semibold text-gray-700 mb-1">Company / Entity Name</label>
                    <input type="text" placeholder="Corporate name" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700">
                  </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div>
                    <label class="block text-xs font-semibold text-gray-700 mb-1">Country of Residence / Domicile *</label>
                    <input type="text" required placeholder="e.g. Sri Lanka, UAE, Singapore" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700">
                  </div>
                  <div>
                    <label class="block text-xs font-semibold text-gray-700 mb-1">Contact Phone / WhatsApp *</label>
                    <input type="tel" required placeholder="+Country code..." class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700">
                  </div>
                </div>

                <div>
                  <label class="block text-xs font-semibold text-gray-700 mb-1">Corporate Email Address *</label>
                  <input type="email" required placeholder="investor@domain.com" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700">
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div>
                    <label class="block text-xs font-semibold text-gray-700 mb-1">Project of Primary Interest *</label>
                    <select required class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700">
                      <option value="">Select an Investment Project</option>
                      <option value="p1">01. Modern Smart Layer Poultry Farm (2.5M Scale)</option>
                      <option value="p2">02. Modern Animal Feed Manufacturing Mill</option>
                      <option value="p3">03. Recycled Paper Egg Tray Manufacturing</option>
                      <option value="p4">04. 5-10 Acre Smart Mushroom Cultivation & Export</option>
                      <option value="p5">05. Egg Processing & Powder Spray-Drying</option>
                      <option value="p6">06. Commercial Bio-Organic Fertilizer Plant</option>
                      <option value="p7">07. Growing Media & Substrates Facility</option>
                      <option value="p8">08. South Korean Water Filtration Assembly Plant</option>
                      <option value="all">Multiple / Conglomerate Portfolio</option>
                    </select>
                  </div>
                  <div>
                    <label class="block text-xs font-semibold text-gray-700 mb-1">Partnership / Investment Mode *</label>
                    <select required class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700">
                      <option value="joint_venture">Joint Venture (JV) Partnership</option>
                      <option value="equity">Equity Capital Investment</option>
                      <option value="tech_transfer">Technology Transfer & Licensing</option>
                      <option value="outgrower">Outgrower / Contract Agribusiness</option>
                      <option value="debt">Debt Financing / Expansion Loan</option>
                    </select>
                  </div>
                </div>

                <div>
                  <label class="block text-xs font-semibold text-gray-700 mb-1">Investment Scale / Capital Bracket</label>
                  <select class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700">
                    <option value="bracket_1">LKR 10 Million – 50 Million (USD ~35k – 170k)</option>
                    <option value="bracket_2">LKR 50 Million – 200 Million (USD ~170k – 680k)</option>
                    <option value="bracket_3">LKR 200 Million – 500 Million (USD ~680k – 1.7M)</option>
                    <option value="bracket_4">Over LKR 500 Million (USD > 1.7M)</option>
                  </select>
                </div>

                <div>
                  <label class="block text-xs font-semibold text-gray-700 mb-1">Message / Key Partnership Objectives</label>
                  <textarea rows="2" placeholder="Brief outline of your investment background, timeframe, and specific expectations..." class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700"></textarea>
                </div>

                <div class="pt-2">
                  <button type="submit" class="btn-primary text-xs w-full py-3">
                    <i class="fas fa-handshake"></i> Submit Investment Expression of Interest (EOI)
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

  {COMMON_FOOTER}
</body>
</html>
"""

# ================= 4. PARTNERS.HTML (PDF SECTION 08) =================
partners_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>Become Our Business Partner | FOREST LANKA Partnership Portal</title>
  {COMMON_HEAD}
</head>
<body data-lang="en">
  {get_header('partners')}

  <main id="main-content">
    <div class="bg-forest-dark text-white py-16 relative">
      <div class="max-w-7xl mx-auto px-4 relative z-10">
        <div class="text-xs text-gold uppercase tracking-wider font-semibold mb-2 flex items-center gap-2">
          <a href="index.html" class="hover:underline">Home</a>
          <i class="fas fa-chevron-right text-[10px]"></i>
          <span>Partner Network</span>
        </div>
        <h1 class="text-3xl sm:text-5xl font-black font-heading text-white mb-2">
          <span class="lang-en">Become Our Business Partner</span>
          <span class="lang-si">ව්‍යාපාරික හවුල්කරුවන් ලියාපදිංචි කිරීම</span>
        </h1>
        <p class="text-xs sm:text-base text-emerald-100 max-w-3xl leading-relaxed">
          <span class="lang-en">
            FOREST LANKA actively collaborates with wholesale dealers, supermarket retail chains, hotel suppliers, exporters, outgrowers, distribution fleets, and technological partners across Sri Lanka and globally.
          </span>
          <span class="lang-si">
            දේශීය හා ජාත්‍යන්තර ව්‍යාපාරික සබඳතා ගොඩනැඟීමට අපේක්ෂා කරන පාර්ශ්ව සඳහා Business Partner Registration System මෙහි ක්‍රියාත්මක වේ.
          </span>
        </p>
      </div>
    </div>

    <!-- The 10 Eligible Partner Categories (PDF Section 8 & Page 14) -->
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4">
        <div class="text-center max-w-3xl mx-auto mb-12">
          <span class="text-xs font-bold uppercase tracking-wider text-emerald-700">Collaboration Matrix</span>
          <h2 class="text-3xl font-black text-forest font-heading">10 Eligible Business Partner Categories</h2>
          <p class="text-xs sm:text-sm text-gray-600 mt-2">
            Select your category to access preferential corporate pricing, priority factory allocations, and direct marketing support.
          </p>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-4 mb-16 text-center text-xs">
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-warehouse text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">1. Wholesalers</div>
            <div class="text-[11px] text-gray-500">තොග වෙළෙන්දන්</div>
          </div>
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-store text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">2. Retailers</div>
            <div class="text-[11px] text-gray-500">සිල්ලර වෙළෙන්දන්</div>
          </div>
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-cart-shopping text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">3. Supermarkets</div>
            <div class="text-[11px] text-gray-500">සුපිරි වෙළෙඳසැල්</div>
          </div>
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-hotel text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">4. Hotels & Restaurants</div>
            <div class="text-[11px] text-gray-500">හෝටල් සහ ආපනශාලා</div>
          </div>
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-ship text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">5. Exporters</div>
            <div class="text-[11px] text-gray-500">අපනයනකරුවන්</div>
          </div>
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-plane-arrival text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">6. Importers</div>
            <div class="text-[11px] text-gray-500">ආනයනකරුවන්</div>
          </div>
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-user-tie text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">7. Sales Agents</div>
            <div class="text-[11px] text-gray-500">අලෙවි නියෝජිතයන්</div>
          </div>
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-truck-fast text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">8. Distributors</div>
            <div class="text-[11px] text-gray-500">බෙදාහැරීමේ සමාගම්</div>
          </div>
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-coins text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">9. Investors</div>
            <div class="text-[11px] text-gray-500">ආයෝජකයන්</div>
          </div>
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-microchip text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">10. Tech Partners</div>
            <div class="text-[11px] text-gray-500">තාක්ෂණික හවුල්කරුවන්</div>
          </div>
        </div>

        <!-- Official Registration Form (PDF Page 15) -->
        <div class="max-w-4xl mx-auto bg-warmwhite p-8 sm:p-10 rounded-3xl border border-gray-200 shadow-lg">
          <div class="text-center mb-8 border-b pb-4">
            <h3 class="text-2xl font-bold text-forest font-heading">Partner Registration Application</h3>
            <p class="text-xs text-gray-600 mt-1">Complete the verified fields below to initiate commercial agreement accreditation.</p>
          </div>

          <form id="partner-registration-form" class="space-y-4">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-semibold text-gray-700 mb-1">Representative Full Name / පුද්ගලයාගේ නම *</label>
                <input type="text" required placeholder="Authorized contact person" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700">
              </div>
              <div>
                <label class="block text-xs font-semibold text-gray-700 mb-1">Business Name / ව්‍යාපාරයේ නම *</label>
                <input type="text" required placeholder="Registered business entity" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700">
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-semibold text-gray-700 mb-1">Business Category / ව්‍යාපාරික කාණ්ඩය *</label>
                <select required class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700">
                  <option value="">Select Category</option>
                  <option value="wholesale">Wholesale Trader (තොග වෙළෙන්දන්)</option>
                  <option value="retail">Retailer / Supermarket (සිල්ලර / සුපිරි වෙළෙඳසැල්)</option>
                  <option value="hospitality">Hotel / Restaurant / Baker (හෝටල් / බේකරි)</option>
                  <option value="export_import">Exporter / Importer (අපනයන / ආනයන)</option>
                  <option value="sales_agent">Regional Sales Agent (අලෙවි නියෝජිත)</option>
                  <option value="distributor">Logistics & Distribution (බෙදාහැරීමේ සමාගම්)</option>
                  <option value="tech_partner">Technology Partner (තාක්ෂණික හවුල්කරු)</option>
                </select>
              </div>
              <div>
                <label class="block text-xs font-semibold text-gray-700 mb-1">Country & District / Region *</label>
                <input type="text" required placeholder="e.g. Sri Lanka, Kurunegala / Colombo" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700">
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-semibold text-gray-700 mb-1">Official Email Address *</label>
                <input type="email" required placeholder="partner@enterprise.com" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700">
              </div>
              <div>
                <label class="block text-xs font-semibold text-gray-700 mb-1">Phone Number & WhatsApp *</label>
                <input type="tel" required placeholder="+94 7X XXX XXXX" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700">
              </div>
            </div>

            <div>
              <label class="block text-xs font-semibold text-gray-700 mb-1">Business Physical Address / ලිපිනය *</label>
              <input type="text" required placeholder="Registered office or warehouse address" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700">
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-semibold text-gray-700 mb-1">Target Products of Interest *</label>
                <select required class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700">
                  <option value="eggs_poultry">Fresh Eggs & Poultry Supply</option>
                  <option value="feed">Animal Feed Formulations (Layer/Cattle/Fish)</option>
                  <option value="egg_trays">Recycled Paper Egg Trays</option>
                  <option value="mushrooms">Fresh & Dried Gourmet Mushrooms</option>
                  <option value="egg_powder">Industrial Egg Powders & Albumen</option>
                  <option value="bio_fertilizer">Pelleted Bio-Organic Fertilizer</option>
                  <option value="growing_media">Growing Media & Potting Substrates</option>
                  <option value="water_purification">Korean Smart Water Filters & Purifiers</option>
                  <option value="all_products">Multi-Product Distribution</option>
                </select>
              </div>
              <div>
                <label class="block text-xs font-semibold text-gray-700 mb-1">Partnership Type / හවුල්කාරිත්ව වර්ගය *</label>
                <select required class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700">
                  <option value="authorized_dealer">Authorized Territorial Dealer</option>
                  <option value="direct_client">Direct Corporate Bulk Buyer</option>
                  <option value="logistics_partner">Distribution & Fleet Partner</option>
                  <option value="outgrower">Outgrower Contract Supplier</option>
                  <option value="franchise">Commercial Agency</option>
                </select>
              </div>
            </div>

            <div>
              <label class="block text-xs font-semibold text-gray-700 mb-1">Special Information / Volume Expectations / සටහන්</label>
              <textarea rows="3" placeholder="Estimated monthly volume capacity, target territory coverage, existing client network..." class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700"></textarea>
            </div>

            <div class="p-3 bg-white rounded-lg border text-xs text-gray-600">
              <i class="fas fa-info-circle text-emerald-700 mr-1"></i>
              <strong>Legal Note (PDF Section 08):</strong> Initial applications are reviewed by our Business Management team. Formal commercial agreements, credit terms, and legal vetting are concluded individually.
            </div>

            <div class="pt-2">
              <button type="submit" class="btn-primary text-xs w-full py-3 text-sm">
                <i class="fas fa-check-circle"></i> Submit Official Partner Registration
              </button>
            </div>
          </form>
        </div>
      </div>
    </section>
  </main>

  {COMMON_FOOTER}
</body>
</html>
"""

with open("products.html", "w", encoding="utf-8") as f:
    f.write(products_html)
print("products.html created.")

with open("export.html", "w", encoding="utf-8") as f:
    f.write(export_html)
print("export.html created.")

with open("investment.html", "w", encoding="utf-8") as f:
    f.write(investment_html)
print("investment.html created.")

with open("partners.html", "w", encoding="utf-8") as f:
    f.write(partners_html)
print("partners.html created.")
