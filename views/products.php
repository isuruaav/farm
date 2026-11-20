<main id="main-content">
    <div class="bg-forest-dark text-white py-16 relative page-intro page-intro--visual">
      <div class="page-intro-layout max-w-7xl mx-auto px-4 relative z-10"><div class="page-intro-copy">
        <div class="text-xs text-gold uppercase tracking-wider font-semibold mb-2 flex items-center gap-2">
          <a href="index.php" class="hover:underline">Home</a>
          <i class="fas fa-chevron-right text-2xs"></i>
          <span>Product Catalog</span>
        </div>
        <h1>
          <span>Product Catalog & Commercial Orders</span>
          
        </h1>
        <p class="text-base sm:text-base text-emerald-100 max-w-3xl leading-relaxed">
          <span>
            Explore products across our eight industry sectors. View pack formats and indicative prices, then request a quotation for confirmed specifications, availability and delivery.
          </span>
          
        </p>
      </div><?php require APP_ROOT . "/includes/page-intro-visual.php"; ?></div>
    </div>

    
    <section class="py-8 bg-white border-b border-gray-200 catalog-filters md:sticky z-30 shadow-xs">
      <div class="max-w-7xl mx-auto px-4">
        <div class="flex flex-col md:flex-row gap-4 items-center justify-between">
          
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

          
          <div class="relative w-full md:w-64">
            <input type="text" id="product-search-input" oninput="searchProducts()" aria-label="Search products" placeholder="Search products..." class="w-full text-xs pl-8 pr-3 py-2 border rounded-full focus:ring-1 focus:ring-emerald-700">
            <i class="fas fa-search absolute left-3 top-2.5 text-gray-400 text-xs"></i>
          </div>
        </div>
      </div>
    </section>

    
    <section class="py-12 bg-warmwhite">
      <div class="max-w-7xl mx-auto px-4">
        <div class="catalog-toolbar"><p id="product-results" role="status" aria-live="polite"></p><label for="product-sort">Sort by <select id="product-sort"><option value="featured">Featured</option><option value="name">Name: A–Z</option><option value="price-low">Price: low to high</option><option value="price-high">Price: high to low</option></select></label></div>
<div id="product-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
<?php foreach (catalog() as $product): require APP_ROOT . '/includes/product-card.php'; endforeach; ?>
</div><div id="product-empty" class="empty-state" hidden><h3>No matching products</h3><p>Try another search or choose a different category.</p><button type="button" class="btn-primary" onclick="resetProductFilters()">Reset filters</button></div>
<p class="catalog-note">Catalog images are illustrative. Listed prices are estimates; availability, delivery charges and final pricing are confirmed by our team.</p>
      </div>
    </section>
  </main>
