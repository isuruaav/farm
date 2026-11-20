#!/usr/bin/env python3
"""
Generates industries.html and the 8 dedicated industry pages for FOREST LANKA.
"""

from base_templates import COMMON_HEAD, get_header, COMMON_FOOTER

# ================= 1. INDUSTRIES.HTML (INDEX) =================
industries_index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>8 Core Industries | FOREST LANKA Dynamic Agro-Industrial Ecosystem</title>
  {COMMON_HEAD}
</head>
<body data-lang="en">
  {get_header('industries')}

  <main id="main-content">
    <div class="bg-forest-dark text-white py-16 relative">
      <div class="max-w-7xl mx-auto px-4 relative z-10">
        <div class="text-xs text-gold uppercase tracking-wider font-semibold mb-2 flex items-center gap-2">
          <a href="index.html" class="hover:underline">Home</a>
          <i class="fas fa-chevron-right text-[10px]"></i>
          <span>Industrial Portfolio</span>
        </div>
        <h1 class="text-3xl sm:text-5xl font-black font-heading text-white mb-3">
          <span class="lang-en">Our 8 Core Business Industries</span>
          <span class="lang-si">ප්‍රධාන ව්‍යාපාරික අංශ 08</span>
        </h1>
        <p class="text-xs sm:text-base text-emerald-100/90 max-w-3xl leading-relaxed">
          <span class="lang-en">
            FOREST LANKA drives 8 interdependent industrial operations spanning high-tech poultry farming, industrial feed milling, circular recycled pulp packaging, IoT climate-controlled mushroom cultivation, functional egg powder processing, bio-fertilizers, specialized horticultural media, and South Korean water purification engineering.
          </span>
          <span class="lang-si">
            ආයතනයේ ප්‍රධාන ව්‍යාපාරික අංශ 08 සඳහා වෙන් වෙන් වූ නිෂ්පාදන, ක්‍රියාවලි සහ වෙළෙඳ පහසුකම් මෙහි ඉදිරිපත් කර ඇත.
          </span>
        </p>
      </div>
    </div>

    <!-- Industries Grid -->
    <section class="py-16 bg-warmwhite">
      <div class="max-w-7xl mx-auto px-4">
        <div class="space-y-12">

          <!-- 01. Poultry Farm -->
          <div class="bg-white rounded-3xl border border-gray-200 shadow-sm overflow-hidden grid grid-cols-1 lg:grid-cols-12 gap-0 hover:shadow-md transition">
            <div class="lg:col-span-5 h-64 lg:h-auto relative">
              <img src="https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?auto=format&fit=crop&w=800&q=80" alt="Poultry Farm" class="w-full h-full object-cover">
              <div class="absolute top-4 left-4 bg-forest text-gold font-bold px-3 py-1 rounded-full text-xs shadow">
                Sector 01 • Poultry
              </div>
            </div>
            <div class="lg:col-span-7 p-6 sm:p-8 flex flex-col justify-between">
              <div>
                <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                  <h2 class="text-2xl font-bold text-forest font-heading">Modern Smart Layer Poultry Farm</h2>
                  <span class="badge-status-operational"><i class="fas fa-check-circle"></i> Operational (Phase 1)</span>
                </div>
                <div class="text-xs font-semibold text-emerald-800 mb-2 font-heading">
                  නවීන බිත්තර නිෂ්පාදන කර්මාන්තය • Modern Smart Layer Poultry Farm
                </div>
                <p class="text-xs sm:text-sm text-gray-600 leading-relaxed mb-4">
                  Initial capacity of 125,000 layer hens expanding in planned phases to 2.5 Million hens. Equipped with multi-tier computerized climate housing, automatic belt egg collection, digital egg grading, and packaging.
                </p>
                <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs text-gray-700 bg-warmwhite p-3 rounded-xl border border-gray-200 mb-6">
                  <div><strong>Packs:</strong> 6, 12, 15, 30-egg packs</div>
                  <div><strong>Capacity:</strong> 125K to 2.5M Layers</div>
                  <div><strong>Market:</strong> Retail & B2B Wholesale</div>
                  <div><strong>Clients:</strong> Supermarkets, Hotels, Bakeries</div>
                  <div><strong>Location:</strong> Polpithigama Farm Base</div>
                  <div><strong>Traceability:</strong> Cleaned & Graded</div>
                </div>
              </div>
              <div class="flex flex-wrap gap-3">
                <a href="industry-poultry.html" class="btn-primary text-xs py-2.5 px-5">Explore Sector Details <i class="fas fa-arrow-right ml-1"></i></a>
                <a href="products.html?cat=poultry" class="btn-secondary text-xs py-2.5 px-4"><i class="fas fa-shopping-cart"></i> View Poultry Products</a>
              </div>
            </div>
          </div>

          <!-- 02. Animal Feed -->
          <div class="bg-white rounded-3xl border border-gray-200 shadow-sm overflow-hidden grid grid-cols-1 lg:grid-cols-12 gap-0 hover:shadow-md transition">
            <div class="lg:col-span-5 h-64 lg:h-auto relative">
              <img src="https://images.unsplash.com/photo-1574943320219-553eb213f72d?auto=format&fit=crop&w=800&q=80" alt="Animal Feed Mill" class="w-full h-full object-cover">
              <div class="absolute top-4 left-4 bg-forest text-gold font-bold px-3 py-1 rounded-full text-xs shadow">
                Sector 02 • Animal Feed
              </div>
            </div>
            <div class="lg:col-span-7 p-6 sm:p-8 flex flex-col justify-between">
              <div>
                <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                  <h2 class="text-2xl font-bold text-forest font-heading">Modern Animal Feed Manufacturing</h2>
                  <span class="badge-status-development"><i class="fas fa-cog fa-spin"></i> In Development</span>
                </div>
                <div class="text-xs font-semibold text-emerald-800 mb-2 font-heading">
                  සත්ත්ව ආහාර නිෂ්පාදන කර්මාන්තය • Modern Animal Feed Manufacturing
                </div>
                <p class="text-xs sm:text-sm text-gray-600 leading-relaxed mb-4">
                  Full 12-step automated industrial feed production process ensuring scientific crude protein, amino acid, and mineral ratios for commercial layer hens, broilers, cattle, goats, and aquaculture fish.
                </p>
                <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs text-gray-700 bg-warmwhite p-3 rounded-xl border border-gray-200 mb-6">
                  <div><strong>Products:</strong> Starter, Grower, Layer, Broiler</div>
                  <div><strong>Livestock:</strong> Cattle, Goat, Sheep, Fish</div>
                  <div><strong>Packaging:</strong> 25kg, 50kg, Bulk bags</div>
                  <div><strong>Process:</strong> 12-Step Industrial Pipeline</div>
                  <div><strong>Contracts:</strong> Outgrower & Farm Supply</div>
                  <div><strong>Quality:</strong> Lab Tested & Calibrated</div>
                </div>
              </div>
              <div class="flex flex-wrap gap-3">
                <a href="industry-feed.html" class="btn-primary text-xs py-2.5 px-5">Explore 12-Step Process <i class="fas fa-arrow-right ml-1"></i></a>
                <a href="products.html?cat=feed" class="btn-secondary text-xs py-2.5 px-4"><i class="fas fa-shopping-cart"></i> View Feed Products</a>
              </div>
            </div>
          </div>

          <!-- 03. Recycled Paper Egg Trays -->
          <div class="bg-white rounded-3xl border border-gray-200 shadow-sm overflow-hidden grid grid-cols-1 lg:grid-cols-12 gap-0 hover:shadow-md transition">
            <div class="lg:col-span-5 h-64 lg:h-auto relative">
              <img src="https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=800&q=80" alt="Recycled Paper Egg Trays" class="w-full h-full object-cover">
              <div class="absolute top-4 left-4 bg-forest text-gold font-bold px-3 py-1 rounded-full text-xs shadow">
                Sector 03 • Egg Trays
              </div>
            </div>
            <div class="lg:col-span-7 p-6 sm:p-8 flex flex-col justify-between">
              <div>
                <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                  <h2 class="text-2xl font-bold text-forest font-heading">Recycled Paper Egg Tray Manufacturing</h2>
                  <span class="badge-status-operational"><i class="fas fa-check-circle"></i> Operational</span>
                </div>
                <div class="text-xs font-semibold text-emerald-800 mb-2 font-heading">
                  කඩදාසි බිත්තර ට්‍රේ නිෂ්පාදන කර්මාන්තය • Recycled Paper Egg Tray Manufacturing
                </div>
                <p class="text-xs sm:text-sm text-gray-600 leading-relaxed mb-4">
                  100% biodegradable and recyclable molded fiber trays utilizing post-consumer paper. 8-step hydraulic pulp molding, dewatering, and hot-air kiln drying process with high shock absorption.
                </p>
                <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs text-gray-700 bg-warmwhite p-3 rounded-xl border border-gray-200 mb-6">
                  <div><strong>Tray Sizes:</strong> 6, 12, 15, 30 Eggs</div>
                  <div><strong>Eco Standard:</strong> 100% Biodegradable Pulp</div>
                  <div><strong>Process:</strong> 8-Step Molding & Drying</div>
                  <div><strong>Target:</strong> Farms, Supermarkets, Exporters</div>
                  <div><strong>Moisture:</strong> Kiln Dried (<8% moisture)</div>
                  <div><strong>Custom Orders:</strong> Logo Embossing Available</div>
                </div>
              </div>
              <div class="flex flex-wrap gap-3">
                <a href="industry-egg-trays.html" class="btn-primary text-xs py-2.5 px-5">Explore 8-Step Process <i class="fas fa-arrow-right ml-1"></i></a>
                <a href="products.html?cat=trays" class="btn-secondary text-xs py-2.5 px-4"><i class="fas fa-shopping-cart"></i> Order Egg Trays</a>
              </div>
            </div>
          </div>

          <!-- 04. Smart Mushroom Farming -->
          <div class="bg-white rounded-3xl border border-gray-200 shadow-sm overflow-hidden grid grid-cols-1 lg:grid-cols-12 gap-0 hover:shadow-md transition">
            <div class="lg:col-span-5 h-64 lg:h-auto relative">
              <img src="https://images.unsplash.com/photo-1509358271058-acd22cc93898?auto=format&fit=crop&w=800&q=80" alt="Smart Mushroom Farm" class="w-full h-full object-cover">
              <div class="absolute top-4 left-4 bg-forest text-gold font-bold px-3 py-1 rounded-full text-xs shadow">
                Sector 04 • Mushrooms
              </div>
            </div>
            <div class="lg:col-span-7 p-6 sm:p-8 flex flex-col justify-between">
              <div>
                <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                  <h2 class="text-2xl font-bold text-forest font-heading">Smart Mushroom Farming & Global Export</h2>
                  <span class="badge-status-development"><i class="fas fa-cog fa-spin"></i> In Development (5-10 Acres)</span>
                </div>
                <div class="text-xs font-semibold text-emerald-800 mb-2 font-heading">
                  නවීන ස්මාර්ට් බිම්මල් නිෂ්පාදන කර්මාන්තය • Smart Mushroom Farming & Global Export
                </div>
                <p class="text-xs sm:text-sm text-gray-600 leading-relaxed mb-4">
                  High-technology indoor cleanroom cultivation planned across 5–10 acres. Cultivating premium Oyster, Shiitake, and Button mushrooms for local fresh distribution and international export agreements.
                </p>
                <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs text-gray-700 bg-warmwhite p-3 rounded-xl border border-gray-200 mb-6">
                  <div><strong>Area:</strong> 5 – 10 Acres High-Tech</div>
                  <div><strong>Varieties:</strong> Oyster, Shiitake, Button</div>
                  <div><strong>Formats:</strong> Fresh, Dehydrated, Powders</div>
                  <div><strong>Technology:</strong> IoT Sensors & Cleanrooms</div>
                  <div><strong>Export:</strong> Cold Chain & Air Cargo</div>
                  <div><strong>Certifications:</strong> Target HACCP/ISO</div>
                </div>
              </div>
              <div class="flex flex-wrap gap-3">
                <a href="industry-mushrooms.html" class="btn-primary text-xs py-2.5 px-5">Explore Mushroom Facility <i class="fas fa-arrow-right ml-1"></i></a>
                <a href="export.html" class="btn-gold text-xs py-2.5 px-4"><i class="fas fa-ship"></i> Export Quotations</a>
              </div>
            </div>
          </div>

          <!-- 05. Egg Processing & Powders -->
          <div class="bg-white rounded-3xl border border-gray-200 shadow-sm overflow-hidden grid grid-cols-1 lg:grid-cols-12 gap-0 hover:shadow-md transition">
            <div class="lg:col-span-5 h-64 lg:h-auto relative">
              <img src="https://images.unsplash.com/photo-1516467508483-a7212febe31a?auto=format&fit=crop&w=800&q=80" alt="Egg Powder Processing" class="w-full h-full object-cover">
              <div class="absolute top-4 left-4 bg-forest text-gold font-bold px-3 py-1 rounded-full text-xs shadow">
                Sector 05 • Egg Processing
              </div>
            </div>
            <div class="lg:col-span-7 p-6 sm:p-8 flex flex-col justify-between">
              <div>
                <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                  <h2 class="text-2xl font-bold text-forest font-heading">Egg Processing & Value-Added Products</h2>
                  <span class="badge-status-planned"><i class="fas fa-clock"></i> Planned (Phase 3)</span>
                </div>
                <div class="text-xs font-semibold text-emerald-800 mb-2 font-heading">
                  බිත්තර ආශ්‍රිත අගය එකතු කළ නිෂ්පාදන • Egg Processing & Value-Added Products
                </div>
                <p class="text-xs sm:text-sm text-gray-600 leading-relaxed mb-4">
                  Advanced breaking, separation, pasteurization, and spray-drying plant producing Whole Egg Powder, Egg Yolk Powder, High-Whipping Albumen, and pasteurized liquid egg blends for industrial bakeries and food manufacturing.
                </p>
                <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs text-gray-700 bg-warmwhite p-3 rounded-xl border border-gray-200 mb-6">
                  <div><strong>Powders:</strong> Whole Egg, Yolk, Albumen</div>
                  <div><strong>Liquids:</strong> Pasteurized Whole & White</div>
                  <div><strong>Shelf Life:</strong> 24 Months Ambient</div>
                  <div><strong>Target:</strong> Bakeries, Confectionery, Biscuits</div>
                  <div><strong>Packaging:</strong> 20kg Boxes & 1kg Pouches</div>
                  <div><strong>Standard:</strong> Pure Microbiological Safety</div>
                </div>
              </div>
              <div class="flex flex-wrap gap-3">
                <a href="industry-egg-processing.html" class="btn-primary text-xs py-2.5 px-5">Explore Processing Technology <i class="fas fa-arrow-right ml-1"></i></a>
                <a href="products.html?cat=processing" class="btn-secondary text-xs py-2.5 px-4"><i class="fas fa-file-invoice"></i> B2B Inquiries</a>
              </div>
            </div>
          </div>

          <!-- 06. Organic Bio-Fertilizer -->
          <div class="bg-white rounded-3xl border border-gray-200 shadow-sm overflow-hidden grid grid-cols-1 lg:grid-cols-12 gap-0 hover:shadow-md transition">
            <div class="lg:col-span-5 h-64 lg:h-auto relative">
              <img src="https://images.unsplash.com/photo-1615811361523-6bd03d7748e7?auto=format&fit=crop&w=800&q=80" alt="Organic Fertilizer" class="w-full h-full object-cover">
              <div class="absolute top-4 left-4 bg-forest text-gold font-bold px-3 py-1 rounded-full text-xs shadow">
                Sector 06 • Bio-Fertilizer
              </div>
            </div>
            <div class="lg:col-span-7 p-6 sm:p-8 flex flex-col justify-between">
              <div>
                <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                  <h2 class="text-2xl font-bold text-forest font-heading">Organic Fertilizer Manufacturing</h2>
                  <span class="badge-status-operational"><i class="fas fa-check-circle"></i> Operational</span>
                </div>
                <div class="text-xs font-semibold text-emerald-800 mb-2 font-heading">
                  කාබනික පොහොර නිෂ්පාදන කර්මාන්තය • Organic Fertilizer Manufacturing
                </div>
                <p class="text-xs sm:text-sm text-gray-600 leading-relaxed mb-4">
                  Transforming poultry droppings, crop residues, and agricultural biomass into odorless, pathogen-free granular and pelleted bio-fertilizer rich in nitrogen, phosphorus, potassium, and soil-regenerating microbes.
                </p>
                <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs text-gray-700 bg-warmwhite p-3 rounded-xl border border-gray-200 mb-6">
                  <div><strong>Forms:</strong> Granular, Pelleted & Compost</div>
                  <div><strong>Raw Material:</strong> Farm Poultry Manure</div>
                  <div><strong>Packaging:</strong> 5kg, 10kg, 20kg & Bulk</div>
                  <div><strong>Applications:</strong> Paddy, Tea, Coconut, Veg</div>
                  <div><strong>Pathogen-Free:</strong> Thermal Composting</div>
                  <div><strong>Distribution:</strong> Agrarian Centers & Dealers</div>
                </div>
              </div>
              <div class="flex flex-wrap gap-3">
                <a href="industry-fertilizer.html" class="btn-primary text-xs py-2.5 px-5">Explore Fertilizer Line <i class="fas fa-arrow-right ml-1"></i></a>
                <a href="products.html?cat=fertilizer" class="btn-secondary text-xs py-2.5 px-4"><i class="fas fa-shopping-cart"></i> Buy Fertilizer</a>
              </div>
            </div>
          </div>

          <!-- 07. Growing Media & Solutions -->
          <div class="bg-white rounded-3xl border border-gray-200 shadow-sm overflow-hidden grid grid-cols-1 lg:grid-cols-12 gap-0 hover:shadow-md transition">
            <div class="lg:col-span-5 h-64 lg:h-auto relative">
              <img src="https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?auto=format&fit=crop&w=800&q=80" alt="Growing Media" class="w-full h-full object-cover">
              <div class="absolute top-4 left-4 bg-forest text-gold font-bold px-3 py-1 rounded-full text-xs shadow">
                Sector 07 • Growing Media
              </div>
            </div>
            <div class="lg:col-span-7 p-6 sm:p-8 flex flex-col justify-between">
              <div>
                <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                  <h2 class="text-2xl font-bold text-forest font-heading">Growing Media & Planting Solutions</h2>
                  <span class="badge-status-operational"><i class="fas fa-check-circle"></i> Operational</span>
                </div>
                <div class="text-xs font-semibold text-emerald-800 mb-2 font-heading">
                  වගා මාධ්‍ය සහ පැළ සිටුවීමේ මාධ්‍ය • Growing Media & Planting Solutions
                </div>
                <p class="text-xs sm:text-sm text-gray-600 leading-relaxed mb-4">
                  Engineered soilless substrates, sterile seed starting media, and buffered potting soils formulated for commercial plant nurseries, floriculture exporters, greenhouse growers, and urban home gardening.
                </p>
                <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs text-gray-700 bg-warmwhite p-3 rounded-xl border border-gray-200 mb-6">
                  <div><strong>Lines:</strong> Seed Starting Mix, Potting Mix</div>
                  <div><strong>Specialty:</strong> Greenhouse Hydroponic Media</div>
                  <div><strong>Aeration:</strong> Balanced Porosity & Water Retention</div>
                  <div><strong>Clients:</strong> Plant Nurseries, Greenhouses</div>
                  <div><strong>Enriched:</strong> Bio-inoculants & Minerals</div>
                  <div><strong>Packaging:</strong> 5L, 10L, 25L & 50L Sacks</div>
                </div>
              </div>
              <div class="flex flex-wrap gap-3">
                <a href="industry-growing-media.html" class="btn-primary text-xs py-2.5 px-5">Explore Media Solutions <i class="fas fa-arrow-right ml-1"></i></a>
                <a href="products.html?cat=media" class="btn-secondary text-xs py-2.5 px-4"><i class="fas fa-shopping-cart"></i> View Products</a>
              </div>
            </div>
          </div>

          <!-- 08. Smart Water Filtration -->
          <div class="bg-white rounded-3xl border border-gray-200 shadow-sm overflow-hidden grid grid-cols-1 lg:grid-cols-12 gap-0 hover:shadow-md transition">
            <div class="lg:col-span-5 h-64 lg:h-auto relative">
              <img src="https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=800&q=80" alt="Water Purification Technology" class="w-full h-full object-cover">
              <div class="absolute top-4 left-4 bg-waterblue text-white font-bold px-3 py-1 rounded-full text-xs shadow">
                Sector 08 • Water Technology
              </div>
            </div>
            <div class="lg:col-span-7 p-6 sm:p-8 flex flex-col justify-between">
              <div>
                <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                  <h2 class="text-2xl font-bold text-forest font-heading">Smart Water Filtration & Purification Solutions</h2>
                  <span class="badge-status-development"><i class="fas fa-cog fa-spin"></i> S. Korean Tech Collaboration</span>
                </div>
                <div class="text-xs font-semibold text-waterblue mb-2 font-heading">
                  ස්මාර්ට් ජල පෙරහන් සහ ජල පිරිපහදු තාක්ෂණය • South Korean Smart Water Solutions
                </div>
                <p class="text-xs sm:text-sm text-gray-600 leading-relaxed mb-4">
                  Bilateral technology partnership introducing South Korea's premier smart IoT water purifiers, commercial multi-stage RO drinking systems, and industrial water filtration plants to Sri Lanka and regional export markets.
                </p>
                <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs text-gray-700 bg-blue-50/50 p-3 rounded-xl border border-blue-100 mb-6">
                  <div><strong>Tech Source:</strong> South Korea Tech Transfer</div>
                  <div><strong>Systems:</strong> Domestic, Commercial, Industrial</div>
                  <div><strong>Smart IoT:</strong> Filter Life Telemetry & UV</div>
                  <div><strong>Consumables:</strong> RO Membranes, Cartridges</div>
                  <div><strong>Opportunities:</strong> Islandwide Dealerships</div>
                  <div><strong>Industrial:</strong> Poultry, Dairy & Factory Water</div>
                </div>
              </div>
              <div class="flex flex-wrap gap-3">
                <a href="industry-water-tech.html" class="btn-primary text-xs py-2.5 px-5 bg-waterblue hover:bg-waterblue-dark">Explore Korean Water Tech <i class="fas fa-arrow-right ml-1"></i></a>
                <a href="partners.html" class="btn-gold text-xs py-2.5 px-4"><i class="fas fa-handshake"></i> Become a Regional Dealer</a>
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

with open("industries.html", "w", encoding="utf-8") as f:
    f.write(industries_index_html)
print("industries.html created.")

# Helper function to generate single industry template
def generate_industry_page(filename, active_id, title_en, title_si, sector_num, status_badge, hero_class, overview_text, products_list, process_steps, pack_types, opportunities_list, specs_table, related_products):
    procs_html = ""
    if process_steps:
        steps_items = "".join([f"""
          <div class="flex items-start gap-4 p-4 bg-white rounded-xl border border-gray-200 shadow-sm">
            <div class="process-step-badge">{idx+1}</div>
            <div>
              <h4 class="font-bold text-sm text-forest">{step['title']}</h4>
              <p class="text-xs text-gray-600 mt-1">{step['desc']}</p>
            </div>
          </div>
        """ for idx, step in enumerate(process_steps)])
        procs_html = f"""
        <section class="py-16 bg-warmwhite border-y border-gray-200">
          <div class="max-w-7xl mx-auto px-4">
            <div class="text-center max-w-2xl mx-auto mb-10">
              <span class="text-xs font-bold uppercase tracking-wider text-emerald-700">Engineering & Precision</span>
              <h3 class="text-2xl sm:text-3xl font-black text-forest font-heading">Industrial Manufacturing Process</h3>
              <p class="text-xs text-gray-600 mt-1">Strict quality control implemented at every phase from raw intake to final dispatch.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {steps_items}
            </div>
          </div>
        </section>
        """

    prods_html = "".join([f"""
      <li class="flex items-center gap-2 text-xs text-gray-700 bg-white p-2.5 rounded-lg border border-gray-100 shadow-2xs">
        <i class="fas fa-check-circle text-emerald-600 text-sm"></i>
        <span>{p}</span>
      </li>
    """ for p in products_list])

    opps_html = "".join([f"""
      <li class="flex items-start gap-2 text-xs text-gray-700">
        <i class="fas fa-handshake text-gold mt-0.5"></i>
        <span>{o}</span>
      </li>
    """ for o in opportunities_list])

    specs_rows = "".join([f"""
      <tr class="border-b border-gray-100">
        <td class="py-2.5 px-3 font-semibold text-forest text-xs bg-gray-50/50 w-1/3">{k}</td>
        <td class="py-2.5 px-3 text-xs text-gray-700">{v}</td>
      </tr>
    """ for k, v in specs_table.items()])

    rel_cards = "".join([f"""
      <div class="bg-white rounded-xl border border-gray-200 p-4 shadow-sm flex flex-col justify-between">
        <div>
          <div class="h-36 rounded-lg overflow-hidden mb-3 bg-gray-100">
            <img src="{p['image']}" alt="{p['name']}" class="w-full h-full object-cover">
          </div>
          <h4 class="font-bold text-xs text-forest mb-1">{p['name']}</h4>
          <p class="text-[11px] text-gray-500 mb-2">{p['variant']}</p>
          <div class="font-semibold text-xs text-emerald-800 mb-3">{p['priceText']}</div>
        </div>
        <button onclick="addToCart({{'id': '{p['id']}', 'name': '{p['name']}', 'price': {p['price']}, 'priceType': '{p['priceType']}', 'variant': '{p['variant']}', 'industry': '{title_en}', 'image': '{p['image']}'}})" class="btn-primary text-xs w-full py-2">
          <i class="fas fa-cart-plus"></i> {('Add to Cart' if p['priceType']=='fixed' else 'Request Quote')}
        </button>
      </div>
    """ for p in related_products])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>{title_en} | FOREST LANKA</title>
  {COMMON_HEAD}
</head>
<body data-lang="en">
  {get_header('industries')}

  <main id="main-content">
    <!-- Hero Banner -->
    <div class="{hero_class} text-white py-16 relative">
      <div class="max-w-7xl mx-auto px-4 relative z-10">
        <div class="text-xs text-gold uppercase tracking-wider font-semibold mb-2 flex items-center gap-2">
          <a href="index.html" class="hover:underline">Home</a>
          <i class="fas fa-chevron-right text-[10px]"></i>
          <a href="industries.html" class="hover:underline">Industries</a>
          <i class="fas fa-chevron-right text-[10px]"></i>
          <span>{title_en}</span>
        </div>
        <div class="inline-block mb-3">{status_badge}</div>
        <h1 class="text-3xl sm:text-5xl font-black font-heading text-white mb-2">
          <span class="lang-en">{title_en}</span>
          <span class="lang-si">{title_si}</span>
        </h1>
        <p class="text-xs sm:text-base text-emerald-100 max-w-3xl leading-relaxed">
          {overview_text}
        </p>
      </div>
    </div>

    <!-- Overview & Products -->
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
          <!-- Left Specs & Products -->
          <div class="lg:col-span-7 space-y-8">
            <div>
              <span class="text-xs font-bold uppercase tracking-wider text-emerald-700">Commercial Output</span>
              <h2 class="text-2xl font-bold text-forest font-heading mb-4">Manufactured Products & Variations</h2>
              <ul class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                {prods_html}
              </ul>
            </div>

            <div>
              <h3 class="text-lg font-bold text-forest font-heading mb-3">Packaging & Availability</h3>
              <div class="bg-warmwhite p-4 rounded-xl border border-gray-200">
                <p class="text-xs text-gray-700 leading-relaxed mb-3">
                  All items are packaged according to strict commercial hygiene and food safety standards to prevent contamination and damage during transit.
                </p>
                <div class="flex flex-wrap gap-2 text-xs">
                  {"".join([f'<span class="bg-white border px-3 py-1 rounded-full font-semibold text-emerald-900">{pk}</span>' for pk in pack_types])}
                </div>
              </div>
            </div>

            <div>
              <h3 class="text-lg font-bold text-forest font-heading mb-3">Technical Specifications</h3>
              <div class="overflow-x-auto bg-white rounded-xl border border-gray-200">
                <table class="w-full text-left border-collapse">
                  <tbody>
                    {specs_rows}
                  </tbody>
                </table>
              </div>
            </div>
          </div>

          <!-- Right Opportunities & Direct Inquiries -->
          <div class="lg:col-span-5 space-y-6">
            <div class="bg-warmwhite p-6 rounded-2xl border border-emerald-900/10 shadow-sm">
              <h3 class="text-lg font-bold text-forest font-heading mb-3 flex items-center gap-2">
                <i class="fas fa-handshake text-gold"></i> Commercial Opportunities
              </h3>
              <p class="text-xs text-gray-600 mb-4">
                We welcome bulk purchase inquiries, outgrower contracts, regional distribution agreements, and international trade inquiries.
              </p>
              <ul class="space-y-2.5 mb-6">
                {opps_html}
              </ul>
              <div class="space-y-2">
                <a href="partners.html" class="btn-primary text-xs w-full py-2.5">
                  <i class="fas fa-file-signature"></i> Register as a Business Partner
                </a>
                <a href="https://wa.me/94719740798" target="_blank" class="btn-gold text-xs w-full py-2.5">
                  <i class="fab fa-whatsapp text-green-700"></i> Direct Operations Inquiry via WhatsApp
                </a>
              </div>
            </div>

            <!-- Quick Inquiry Card -->
            <div class="bg-forest-dark text-white p-6 rounded-2xl border-2 border-gold/40 shadow-md">
              <h4 class="text-sm font-bold text-gold uppercase tracking-wider mb-2">Request Sector Quotation</h4>
              <p class="text-xs text-emerald-200 mb-4">Submit your requirements directly to our industrial dispatch manager.</p>
              
              <form class="dynamic-inquiry-form space-y-3">
                <input type="hidden" name="industry" value="{title_en}">
                <div>
                  <input type="text" required placeholder="Your Name or Enterprise *" class="w-full text-xs p-2.5 rounded bg-white text-charcoal border focus:ring-1 focus:ring-gold">
                </div>
                <div>
                  <input type="tel" required placeholder="Phone / WhatsApp Number *" class="w-full text-xs p-2.5 rounded bg-white text-charcoal border focus:ring-1 focus:ring-gold">
                </div>
                <div>
                  <textarea rows="2" placeholder="Required quantities, delivery destination, or specs..." class="w-full text-xs p-2.5 rounded bg-white text-charcoal border focus:ring-1 focus:ring-gold"></textarea>
                </div>
                <button type="submit" class="btn-gold text-xs w-full py-2.5">
                  <i class="fas fa-paper-plane"></i> Submit Quotation Request
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Manufacturing Process (if applicable) -->
    {procs_html}

    <!-- Related Products Store Strip -->
    <section class="py-16 bg-white border-t border-gray-200">
      <div class="max-w-7xl mx-auto px-4">
        <div class="flex justify-between items-center mb-8">
          <div>
            <span class="text-xs font-bold uppercase tracking-wider text-emerald-700">Commercial Catalog</span>
            <h3 class="text-2xl font-bold text-forest font-heading">Order Related Products</h3>
          </div>
          <a href="products.html" class="text-xs font-bold text-emerald-800 hover:text-emerald-950 flex items-center gap-1">
            <span>All Catalog Lines</span> <i class="fas fa-arrow-right"></i>
          </a>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {rel_cards}
        </div>
      </div>
    </section>
  </main>

  {COMMON_FOOTER}
</body>
</html>
"""

# ----------------- PAGE 1: POULTRY -----------------
poultry_html = generate_industry_page(
    filename="industry-poultry.html",
    active_id="poultry",
    title_en="Modern Smart Layer Poultry Farm",
    title_si="නවීන බිත්තර නිෂ්පාදන කර්මාන්තය",
    sector_num="01",
    status_badge='<span class="badge-status-operational"><i class="fas fa-check-circle"></i> Operational (Phase 1: 125,000 Hens)</span>',
    hero_class="industry-hero-poultry",
    overview_text="FOREST LANKA's flagship agricultural enterprise launching with 125,000 layer hens and scaling step-by-step to 2.5 Million hens. Featuring computerized climate-controlled houses, automatic feed lines, automated gentle belt collection, and electronic weight grading.",
    products_list=[
        "Fresh Farm Chicken Table Eggs (නැවුම් කුකුළු බිත්තර)",
        "Cleaned, Candled & Graded Eggs (පිරිසිදු කර වර්ගීකරණය කළ බිත්තර)",
        "Size-Sorted Eggs: Grade A Large, Medium, Extra-Large (ප්‍රමාණය අනුව වෙන් කළ බිත්තර)",
        "Supermarket Sealed Retail Packs (සුපිරි වෙළෙඳසැල් සඳහා බිත්තර)",
        "Bulk Eggs for Hotels, Resorts & Catering (හෝටල් සහ ආපනශාලා සඳහා තොග බිත්තර)",
        "Commercial Eggs for Bakeries & Biscuit Manufacturers (බේකරි හා ආහාර නිෂ්පාදන කර්මාන්ත සඳහා බිත්තර)"
    ],
    process_steps=[
        {"title": "Automated Layer Housing", "desc": "Computer-regulated ambient temperature, humidity, and fresh airflow ensure stress-free laying hens."},
        {"title": "Nutritional Feed Delivery", "desc": "Scheduled automated feed delivery formulated directly by Forest Lanka Feed Mill for peak egg quality."},
        {"title": "Gentle Belt Collection", "desc": "Automated soft belts transport eggs continuously from nesting boxes directly to the grading center without human contact."},
        {"title": "Sanitization & Inspection", "desc": "Soft surface cleaning and optical candling to verify interior shell integrity and zero hairline fractures."},
        {"title": "Electronic Weight Grading", "desc": "High-speed precision scales sort eggs into calibrated sizes: Small, Medium, Large, Extra Large, Jumbo."},
        {"title": "Molded Pulp Packaging", "desc": "Eggs are seated directly into 100% recycled paper egg trays and sealed packs for shock-proof delivery."}
    ],
    pack_types=["06-Egg Packs", "12-Egg Packs", "15-Egg Packs", "30-Egg Commercial Trays", "Master Transport Crates (360 Eggs)"],
    opportunities_list=[
        "Retail egg orders with islandwide scheduled cold-chain delivery.",
        "Bulk wholesale egg orders for major distributors and egg dealers.",
        "Contract supply agreements for supermarket chains with barcode printing.",
        "Institutional daily/weekly bulk quotas for star-class hotels and bakeries.",
        "Regional dealer and wholesale distributor franchise registration.",
        "Future export agreements for fresh table eggs to Maldives and regional hubs."
    ],
    specs_table={
        "Initial Flock Size": "125,000 Commercial Laying Hens (Phase 1)",
        "Long-term Expansion": "Scaled systematically up to 2,500,000 Layers (Phase 4)",
        "Egg Grades": "Grade A Large (58-65g), Medium (50-57g), Extra Large (>65g)",
        "Housing System": "Fully enclosed climate-controlled multi-tier automated cage systems",
        "Biosecurity": "Disinfection mist tunnels, restricted zone biosafety, regular avian PCR testing",
        "Egg Handling": "Automated collection, optical candling, grading, zero touch packaging"
    },
    related_products=[
        {
            "id": "FL-EGG-30",
            "name": "Cleaned & Graded Fresh Eggs (30-Tray)",
            "variant": "30 Eggs / Recycled Pulp Tray",
            "price": 1350,
            "priceType": "fixed",
            "priceText": "LKR 1,350.00 / Tray",
            "image": "https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=500&q=80"
        },
        {
            "id": "FL-EGG-12",
            "name": "Supermarket Sealed Retail Pack (12 Eggs)",
            "variant": "12 Eggs / Biodegradable Pack",
            "price": 560,
            "priceType": "fixed",
            "priceText": "LKR 560.00 / Pack",
            "image": "https://images.unsplash.com/photo-1506976785307-8732e854ad03?auto=format&fit=crop&w=500&q=80"
        },
        {
            "id": "FL-EGG-HOTEL",
            "name": "Hotel & Bakery Bulk Supply (360 Eggs Master Crate)",
            "variant": "12 Trays × 30 Eggs (360 Units)",
            "price": 15800,
            "priceType": "fixed",
            "priceText": "LKR 15,800.00 / Master Crate",
            "image": "https://images.unsplash.com/photo-1516467508483-a7212febe31a?auto=format&fit=crop&w=500&q=80"
        }
    ]
)

with open("industry-poultry.html", "w", encoding="utf-8") as f:
    f.write(poultry_html)
print("industry-poultry.html created.")

# ----------------- PAGE 2: ANIMAL FEED -----------------
feed_html = generate_industry_page(
    filename="industry-feed.html",
    active_id="feed",
    title_en="Modern Animal Feed Manufacturing",
    title_si="සත්ත්ව ආහාර නිෂ්පාදන කර්මාන්තය",
    sector_num="02",
    status_badge='<span class="badge-status-development"><i class="fas fa-cog fa-spin"></i> In Development (Industrial Feed Mill)</span>',
    hero_class="industry-hero-feed",
    overview_text="Engineered to meet national livestock nutrition demands through an automated 12-step industrial manufacturing facility. Producing scientifically balanced feed for poultry, dairy cattle, goats, sheep, and aquaculture fish.",
    products_list=[
        "Chick Starter Feed (පැටවුන් ආරම්භක ආහාර)",
        "Grower Feed (වැඩෙන සතුන්ගේ ආහාර)",
        "High-Yield Layer Feed Pellets (බිත්තර කිකිළියන්ගේ ආහාර)",
        "Broiler Finisher & Starter Feed (මස් කුකුළු ආහාර)",
        "High-Milk Dairy Cattle Feed (ගව ආහාර)",
        "Goat and Sheep High-Fiber Feed (එළු සහ බැටළු ආහාර)",
        "Aquaculture Fish Pellets (මාළු ආහාර)",
        "Specialty Custom Farm Formulations (වෙනත් සත්ත්ව ආහාර)"
    ],
    process_steps=[
        {"title": "1. Raw Material Sourcing (අමුද්‍රව්‍ය මිලදී ගැනීම)", "desc": "Procuring certified high-grade maize, soybean meal, rice bran, vitamins, and minerals."},
        {"title": "2. Quality Inspection (අමුද්‍රව්‍ය පරීක්ෂාව)", "desc": "Laboratory testing for moisture, protein %, aflatoxin levels, and physical purity."},
        {"title": "3. Cleaning & De-stoning (පිරිසිදු කිරීම)", "desc": "Magnetic separators and air screeners remove metal tramp, dust, and stones."},
        {"title": "4. Grinding & Hammer Milling (ඇඹරීම)", "desc": "High-capacity hammer mills pulverize grain into uniform particle micrometers."},
        {"title": "5. Nutritional Formulation (පෝෂණ සංයුතිය සකස් කිරීම)", "desc": "Automated micro-dosing of essential amino acids, calcium, phosphate, and enzymes."},
        {"title": "6. Homogeneous Blending (මිශ්‍ර කිරීම)", "desc": "Twin-shaft paddle mixers achieve optimal homogeneity (Coefficient of Variation < 5%)."},
        {"title": "7. Steam Pelletizing (Pelletizing)", "desc": "High-pressure thermal conditioner gelatinizes starches followed by ring-die extrusion."},
        {"title": "8. Counterflow Cooling (සිසිල් කිරීම)", "desc": "Air-flow cooling locks in pellet durability and cools to within 3°C of ambient temperature."},
        {"title": "9. Quality & Crumbling (තත්ත්ව පරීක්ෂාව)", "desc": "Pellet Durability Index (PDI) measurement and crumbling for starter chick sizes."},
        {"title": "10. Automated Packaging (ඇසුරුම් කිරීම)", "desc": "Computerized weighing and thermal stitching into 25kg, 50kg, and jumbo bulk sacks."},
        {"title": "11. Climate Warehousing (ගබඩා කිරීම)", "desc": "Ventilated, palletized storage with strict FIFO (First In First Out) rotation."},
        {"title": "12. Fleet Distribution (බෙදාහැරීම)", "desc": "Direct factory fleet dispatch to outgrower farms, dealer networks, and estates."}
    ],
    pack_types=["25kg Woven Polypropylene Bags", "50kg Heavy-Duty Feed Sacks", "Bulk 1-Ton Jumbo Bags", "Bulk Silo Tanker Deliveries"],
    opportunities_list=[
        "Long-term farm supply agreements with fixed scheduled delivery cycles.",
        "Exclusive territorial dealer and feed distributor franchises across Sri Lanka.",
        "Bulk wholesale quotation requests for commercial poultry and dairy farms.",
        "Custom nutritional batch formulation for large commercial agribusinesses."
    ],
    specs_table={
        "Manufacturing Pipeline": "12-Step Continuous Automated Industrial Processing Plant",
        "Pellet Dimensions": "2.0mm (Chicks), 3.0mm (Layers), 4.5mm (Cattle & Fish)",
        "Pellet Durability (PDI)": "> 96.5% Durability Index for zero transit crumbling",
        "Packaging Options": "25kg, 50kg Multi-wall Polypropylene Bags with Inner Liner",
        "Nutrient Guarantee": "Crude Protein: 17.5% - 21.0%, Calcium: 3.8% - 4.2%, Phosphorus: 0.45%",
        "Aflatoxin Control": "Tested < 10 ppb (Parts Per Billion) maximum tolerance"
    },
    related_products=[
        {
            "id": "FL-FEED-LAYER50",
            "name": "High-Yield Layer Feed Pellets (50kg)",
            "variant": "50kg Woven Bag",
            "price": 7850,
            "priceType": "fixed",
            "priceText": "LKR 7,850.00 / 50kg Bag",
            "image": "https://images.unsplash.com/photo-1574943320219-553eb213f72d?auto=format&fit=crop&w=500&q=80"
        },
        {
            "id": "FL-FEED-CHICK25",
            "name": "Chick Starter Crumbles (25kg)",
            "variant": "25kg Bag",
            "price": 4200,
            "priceType": "fixed",
            "priceText": "LKR 4,200.00 / 25kg Bag",
            "image": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=500&q=80"
        },
        {
            "id": "FL-FEED-CATTLE50",
            "name": "Dairy Cattle High-Lactation Feed (50kg)",
            "variant": "50kg Bag",
            "price": 6950,
            "priceType": "fixed",
            "priceText": "LKR 6,950.00 / 50kg Bag",
            "image": "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?auto=format&fit=crop&w=500&q=80"
        }
    ]
)

with open("industry-feed.html", "w", encoding="utf-8") as f:
    f.write(feed_html)
print("industry-feed.html created.")

# ----------------- PAGE 3: RECYCLED PAPER EGG TRAYS -----------------
egg_trays_html = generate_industry_page(
    filename="industry-egg-trays.html",
    active_id="egg-trays",
    title_en="Recycled Paper Egg Tray Manufacturing",
    title_si="කඩදාසි බිත්තර ට්‍රේ නිෂ්පාදන කර්මාන්තය",
    sector_num="03",
    status_badge='<span class="badge-status-operational"><i class="fas fa-check-circle"></i> Operational (Eco-Packaging Plant)</span>',
    hero_class="industry-hero-egg-trays",
    overview_text="Eliminating single-use plastics from poultry packaging through 100% biodegradable molded pulp engineering. Operating an 8-step hydraulic hydrapulping, vacuum forming, and continuous hot-air drying plant.",
    products_list=[
        "06-Egg Molded Pulp Clamshell Trays (බිත්තර 06 සඳහා ට්‍රේ)",
        "12-Egg Retail Molded Pulp Cartons (බිත්තර 12 සඳහා ට්‍රේ)",
        "15-Egg Supermarket Trays (බිත්තර 15 සඳහා ට්‍රේ)",
        "30-Egg Standard Commercial Trays (බිත්තර 30 සඳහා ට්‍රේ)",
        "Master Shipping Protective Trays (තොග ප්‍රවාහනය සඳහා ට්‍රේ)",
        "Custom Molded Pulp Industrial Packaging (විශේෂ ඇණවුම් අනුව ඇසුරුම්)"
    ],
    process_steps=[
        {"title": "1. Waste Paper Collection (භාවිත කළ කඩදාසි එකතු කිරීම)", "desc": "Collecting clean post-consumer newspaper, cardboard cartons, and office paper."},
        {"title": "2. Sorting & Grading (කඩදාසි වෙන් කිරීම)", "desc": "Eliminating plastics, adhesives, and tape to retain high-tensile cellulosic fibers."},
        {"title": "3. Hydrapulping & Refining (පල්ප් සකස් කිරීම)", "desc": "High-shear hydrapulpers blend paper with water to produce smooth homogeneous pulp slurry."},
        {"title": "4. Vacuum Molding (අච්චු කිරීම)", "desc": "Rotary vacuum forming molds shape the slurry into precision egg cup geometries."},
        {"title": "5. Water Extraction (ජලය ඉවත් කිරීම)", "desc": "High-pressure hydraulic suction removes over 70% of moisture instantly."},
        {"title": "6. Tunnel Drying (වියළීම)", "desc": "Automated multi-layer hot-air drying tunnel cures trays to optimal rigidity."},
        {"title": "7. Quality & Shock Testing (තත්ත්ව පරීක්ෂාව)", "desc": "Compressive strength, drop resistance, and nesting alignment inspection."},
        {"title": "8. Stacking & Logistics (ගබඩා කිරීම සහ බෙදාහැරීම)", "desc": "Automated counting, bundling in sets of 100, and dispatch to farms."}
    ],
    pack_types=["Bundles of 100 Trays", "Master Pallets of 5,000 Trays", "Custom Logo Printed Cartons"],
    opportunities_list=[
        "Contract tray supply for third-party poultry farms across Sri Lanka.",
        "Direct bulk packaging supply for national supermarket chains and exporters.",
        "Eco-friendly packaging replacement contracts for commercial egg distributors.",
        "Custom-molded industrial pulp trays designed to custom product blueprints."
    ],
    specs_table={
        "Raw Material": "100% Recycled Newspaper, Kraft Cardboard & Clean Office Paper",
        "Biodegradability": "100% Natural Biodegradable & Compostable within 90 days",
        "Stacking Strength": "Resistant to > 150 kg static vertical load per stack of 6 trays",
        "Moisture Content": "< 8.0% residual moisture post-drying",
        "Production Capacity": "100,000+ Trays per day continuous output",
        "Cup Geometries": "Engineered shock-absorbing cushions for Small to Jumbo eggs"
    },
    related_products=[
        {
            "id": "FL-TRAY-30B100",
            "name": "30-Egg Molded Pulp Trays (Bundle of 100)",
            "variant": "Bundle of 100 Trays",
            "price": 3200,
            "priceType": "fixed",
            "priceText": "LKR 3,200.00 / 100 Trays",
            "image": "https://images.unsplash.com/photo-1506976785307-8732e854ad03?auto=format&fit=crop&w=500&q=80"
        },
        {
            "id": "FL-TRAY-12B50",
            "name": "12-Egg Clamshell Cartons (Bundle of 50)",
            "variant": "Bundle of 50 Cartons",
            "price": 2450,
            "priceType": "fixed",
            "priceText": "LKR 2,450.00 / 50 Cartons",
            "image": "https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=500&q=80"
        },
        {
            "id": "FL-TRAY-PALLET",
            "name": "Industrial Bulk Pallet (5,000 Trays)",
            "variant": "Pallet of 5,000 Trays",
            "price": 145000,
            "priceType": "fixed",
            "priceText": "LKR 145,000.00 / Pallet",
            "image": "https://images.unsplash.com/photo-1516467508483-a7212febe31a?auto=format&fit=crop&w=500&q=80"
        }
    ]
)

with open("industry-egg-trays.html", "w", encoding="utf-8") as f:
    f.write(egg_trays_html)
print("industry-egg-trays.html created.")

# ----------------- PAGE 4: MUSHROOMS -----------------
mushrooms_html = generate_industry_page(
    filename="industry-mushrooms.html",
    active_id="mushrooms",
    title_en="Smart Mushroom Farming & Global Export",
    title_si="නවීන ස්මාර්ට් බිම්මල් නිෂ්පාදන කර්මාන්තය",
    sector_num="04",
    status_badge='<span class="badge-status-development"><i class="fas fa-cog fa-spin"></i> In Development (5-10 Acres Smart Facility)</span>',
    hero_class="industry-hero-mushrooms",
    overview_text="High-tech indoor climate-controlled mushroom cultivation spanning 5–10 acres targeting domestic gourmet markets and lucrative international exports across the Middle East and Asia. Featuring IoT sensor telemetry, automated PID temperature regulation, cleanroom positive pressure, and blast-freezing cold storage.",
    products_list=[
        "Fresh Oyster Mushrooms (නැවුම් ඔයිස්ටර් බිම්මල්)",
        "Premium Shiitake Mushrooms (ෂිටාකේ බිම්මල්)",
        "White & Brown Button Mushrooms (බටන් බිම්මල්)",
        "Dehydrated / Sun & Hot-Air Dried Gourmet Mushrooms (වියළි බිම්මල්)",
        "Vacuum-Sealed Retail Mushroom Packs (ඇසුරුම් කළ බිම්මල්)",
        "Dehydrated Mushroom Powders & Slices for Food Processing (ආහාර නිෂ්පාදන සඳහා අමුද්‍රව්‍ය)",
        "Value-Added Pickled & Seasoned Mushrooms (අගය එකතු කළ බිම්මල් නිෂ්පාදන)"
    ],
    process_steps=[
        {"title": "1. Substrate Formulation & Bagging", "desc": "Sawdust, rice bran, and calcium carbonate blended and filled into heat-resistant polypropylene bags."},
        {"title": "2. High-Pressure Autoclave Sterilization", "desc": "Substrate bags autoclaved at 121°C for 4 hours to eliminate competing spores and microbes."},
        {"title": "3. Cleanroom Inoculation (Laminar Flow)", "desc": "HEPA-filtered sterile hoods ensure pure mycelium spawn inoculation without contamination."},
        {"title": "4. Dark Incubation Period", "desc": "Spawns colonize substrate in controlled 24°C darkness until complete mycelial run."},
        {"title": "5. IoT-Controlled Fruiting Chambers", "desc": "Automated misting, temperature drops, light exposure, and CO2 ventilation trigger pinning."},
        {"title": "6. Harvesting & Sorting", "desc": "Hand-picked at peak cap development, inspected, stem-trimmed, and size classified."},
        {"title": "7. Dehydration & Value Addition", "desc": "Precision hot-air dryers dehydrate selected batches to < 10% moisture for export shelf-life."},
        {"title": "8. Cold-Chain Packaging & Export", "desc": "Vacuum-sealed or modified atmosphere packaged (MAP) and stored in 4°C cold rooms."}
    ],
    pack_types=["200g & 500g Fresh Retail Punnet Packs", "1kg Vacuum Packs", "5kg Dehydrated Export Cartons", "Bulk Mushroom Powder Drums"],
    opportunities_list=[
        "Fresh daily supply contracts for star-class hotels, catering, and supermarket chains.",
        "International bulk export agreements under CIF/FOB terms to Dubai, Qatar, Singapore, and Europe.",
        "Sample request program for foreign food importers and distributors.",
        "Long-term outgrower incubation programs for local mushroom growers."
    ],
    specs_table={
        "Project Land Extent": "5 to 10 Acres High-Density Indoor Cleanroom Facility",
        "Target Varieties": "Oyster (Pleurotus ostreatus), Shiitake (Lentinula edodes), Button (Agaricus bisporus)",
        "Climate Tech": "Micro-PID automated temperature (16°C - 24°C) & ultrasonic fogging (85% - 95% RH)",
        "Sterilization": "Industrial steam autoclaves operating at 121°C & 15 psi",
        "Air Filtration": "Positive-pressure cleanrooms with HEPA Class 10,000 air handling",
        "Export Standards": "Targeting Global G.A.P, HACCP, and ISO 22000 export certifications"
    },
    related_products=[
        {
            "id": "FL-MUSH-SHIITAKE",
            "name": "Dehydrated Premium Shiitake Mushrooms (1kg)",
            "variant": "1kg Vacuum Sealed Export Grade",
            "price": 6800,
            "priceType": "fixed",
            "priceText": "LKR 6,800.00 / 1kg Pack",
            "image": "https://images.unsplash.com/photo-1509358271058-acd22cc93898?auto=format&fit=crop&w=500&q=80"
        },
        {
            "id": "FL-MUSH-OYSTER",
            "name": "Fresh Oyster Mushrooms Punnet (200g)",
            "variant": "200g Retail Punnet",
            "price": 280,
            "priceType": "fixed",
            "priceText": "LKR 280.00 / Punnet",
            "image": "https://images.unsplash.com/photo-1518736114815-20be4bf5645e?auto=format&fit=crop&w=500&q=80"
        },
        {
            "id": "FL-MUSH-EXP-BULK",
            "name": "Global Export Gourmet Mushroom Container (FOB/CIF)",
            "variant": "Minimum Order Quantity: 500kg",
            "price": 0,
            "priceType": "quote",
            "priceText": "Export Quotation Required",
            "image": "https://images.unsplash.com/photo-1506976785307-8732e854ad03?auto=format&fit=crop&w=500&q=80"
        }
    ]
)

with open("industry-mushrooms.html", "w", encoding="utf-8") as f:
    f.write(mushrooms_html)
print("industry-mushrooms.html created.")

# ----------------- PAGE 5: EGG PROCESSING -----------------
egg_processing_html = generate_industry_page(
    filename="industry-egg-processing.html",
    active_id="egg-processing",
    title_en="Egg Processing & Value-Added Products",
    title_si="බිත්තර ආශ්‍රිත අගය එකතු කළ නිෂ්පාදන",
    sector_num="05",
    status_badge='<span class="badge-status-planned"><i class="fas fa-clock"></i> Planned (Phase 3: Value-Addition)</span>',
    hero_class="industry-hero-egg-processing",
    overview_text="Transitioning commercial poultry into industrial biotechnology. Establishing Sri Lanka's high-efficiency egg breaking, component separation, pasteurization, and spray-drying plant to produce functional egg powders and pasteurized liquid eggs.",
    products_list=[
        "Whole Egg Powder (සම්පූර්ණ බිත්තර පිටි)",
        "Egg Yolk Powder (බිත්තර කහ මදය පිටි)",
        "Egg White Powder / High-Whipping Albumen (බිත්තර සුදු මදය පිටි)",
        "Liquid Pasteurized Whole Egg (ද්‍රව බිත්තර නිෂ්පාදන)",
        "Liquid Pasteurized Egg White & Yolk",
        "Functional Bakery & Confectionery Customized Powder Mixes"
    ],
    process_steps=[
        {"title": "1. Egg Washing & Candling", "desc": "Automated brushing and UV sanitizing of shells followed by acoustic crack detection."},
        {"title": "2. High-Speed Egg Breaking & Separation", "desc": "Robotic breakers separate yolks and whites or blend into homogeneous liquid."},
        {"title": "3. Homogenization & Pasteurization", "desc": "Plate heat exchangers pasteurize liquid egg to eliminate Salmonella while protecting protein functionality."},
        {"title": "4. Enzymatic Sugar Removal (Desugaring)", "desc": "Controlled fermentation removes glucose from egg whites to prevent Maillard browning during drying."},
        {"title": "5. Spray-Drying Atomization", "desc": "High-pressure centrifugal nozzles atomize liquid into heated drying towers creating fine powder."},
        {"title": "6. Aseptic Nitrogen Packaging", "desc": "Hermetically sealed into multilayer bags with nitrogen flushing for 24-month ambient shelf life."}
    ],
    pack_types=["1kg Stand-Up Pouches", "5kg Catering Buckets", "20kg Industrial Corrugated Boxes", "Bulk Bag Totes"],
    opportunities_list=[
        "Annual bulk ingredient contracts for national biscuit and bakery chains.",
        "Supplying mayonnaise, sauce, and pasta food processing conglomerates.",
        "Export agreements for food-grade egg powders to Southeast Asia and Middle East.",
        "Institutional hotel & airline catering contracts for safe pasteurized liquid eggs."
    ],
    specs_table={
        "Whole Egg Powder Ratio": "1 kg powder + 3 kg water = 4 kg fresh whole egg (approx. 80 fresh eggs)",
        "Egg White (Albumen) Whipping": "High-gel, high-whipping whip height > 165mm for bakery meringues",
        "Moisture Content": "< 4.0% maximum moisture content",
        "Solubility Index": "> 92% instant rehydration in ambient water",
        "Microbiology Standard": "Salmonella negative in 25g, Total Plate Count < 10,000 cfu/g",
        "Shelf Life": "24 Months at ambient temperature without refrigeration"
    },
    related_products=[
        {
            "id": "FL-EP-WHOLE20",
            "name": "Industrial Whole Egg Powder (20kg Box)",
            "variant": "20kg Multi-wall Poly Liner Box",
            "price": 0,
            "priceType": "quote",
            "priceText": "B2B Quotation Required",
            "image": "https://images.unsplash.com/photo-1516467508483-a7212febe31a?auto=format&fit=crop&w=500&q=80"
        },
        {
            "id": "FL-EP-ALBUMEN1",
            "name": "High-Whip Egg White Albumen Powder (1kg)",
            "variant": "1kg Foil Zipper Pouch",
            "price": 3850,
            "priceType": "fixed",
            "priceText": "LKR 3,850.00 / 1kg Pouch",
            "image": "https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=500&q=80"
        },
        {
            "id": "FL-EP-YOLK20",
            "name": "Pasteurized Egg Yolk Powder (20kg Box)",
            "variant": "20kg Box",
            "price": 0,
            "priceType": "quote",
            "priceText": "B2B Quotation Required",
            "image": "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?auto=format&fit=crop&w=500&q=80"
        }
    ]
)

with open("industry-egg-processing.html", "w", encoding="utf-8") as f:
    f.write(egg_processing_html)
print("industry-egg-processing.html created.")

# ----------------- PAGE 6: ORGANIC FERTILIZER -----------------
fertilizer_html = generate_industry_page(
    filename="industry-fertilizer.html",
    active_id="fertilizer",
    title_en="Organic Fertilizer Manufacturing",
    title_si="කාබනික පොහොර නිෂ්පාදන කර්මාන්තය",
    sector_num="06",
    status_badge='<span class="badge-status-operational"><i class="fas fa-check-circle"></i> Operational (Zero-Waste Bio-Plant)</span>',
    hero_class="industry-hero-fertilizer",
    overview_text="Championing the circular bio-economy. Converting 100% of organic poultry manure, farm crop residues, and biomass into certified pathogen-free, odorless granular and pelleted bio-organic fertilizer.",
    products_list=[
        "Granular Bio-Organic Compost (කාබනික පොහොර)",
        "Sterilized Pelleted Poultry Manure (සැකසූ කුකුළු පොහොර)",
        "Enriched Bio-Fertilizer Blends with Minerals (කාබනික පොහොර මිශ්‍රණ)",
        "Soil Conditioner & Humic Acid Enriched Compost",
        "Slow-Release Plantation Grade Organic Pellets"
    ],
    process_steps=[
        {"title": "1. Pure Poultry Manure Collection", "desc": "Automated scraper systems collect fresh layer manure from poultry housing daily."},
        {"title": "2. High-Temperature Aerobic Fermentation", "desc": "Windrow composting reaches 65°C - 70°C for 21 days, destroying all weed seeds and pathogens."},
        {"title": "3. Beneficial Microbe Inoculation", "desc": "Enriching compost with Trichoderma, Bacillus subtilis, and mycorrhizal fungi."},
        {"title": "4. Crushing & Fine Screening", "desc": "Trommel screens separate coarse matter to ensure fine particle consistency."},
        {"title": "5. Rotary Extrusion Pelletizing", "desc": "Compressing organic matter into durable, easy-to-spread 4mm fertilizer pellets."},
        {"title": "6. Packaging & Sealing", "desc": "Sealed into moisture-resistant 5kg, 10kg, 20kg retail bags and 1-ton bulk bags."}
    ],
    pack_types=["05 kg Handy Consumer Pack", "10 kg Garden Bags", "20 kg Commercial Farm Sacks", "Bulk 500kg / 1000kg Jumbo Bags"],
    opportunities_list=[
        "Direct wholesale supply for commercial tea, rubber, coconut, and cinnamon plantations.",
        "Retail distribution through plant nurseries, home gardening stores, and hardware shops.",
        "Supply contracts for commercial organic vegetable, fruit, and paddy growers.",
        "Bulk wholesale quotation requests for estate management companies."
    ],
    specs_table={
        "Organic Matter Content": "> 45.0% Organic Carbon on dry matter basis",
        "Macro Nutrients (NPK)": "Total N: 3.5% - 4.5%, P2O5: 2.8% - 3.5%, K2O: 2.2% - 3.0%",
        "C:N Ratio": "Balanced 12:1 to 15:1 for rapid soil microbial uptake",
        "Moisture Content": "< 20.0% moisture content",
        "Pathogen Safety": "E. coli and Salmonella completely non-detectable",
        "Odor Profile": "Earthy, fully stabilized, 100% non-offensive odor"
    },
    related_products=[
        {
            "id": "FL-FERT-20KG",
            "name": "Sterilized Pelleted Poultry Bio-Fertilizer (20kg)",
            "variant": "20kg Heavy-Duty Sack",
            "price": 1850,
            "priceType": "fixed",
            "priceText": "LKR 1,850.00 / 20kg Bag",
            "image": "https://images.unsplash.com/photo-1615811361523-6bd03d7748e7?auto=format&fit=crop&w=500&q=80"
        },
        {
            "id": "FL-FERT-10KG",
            "name": "Enriched Organic Garden Compost (10kg)",
            "variant": "10kg Bag",
            "price": 950,
            "priceType": "fixed",
            "priceText": "LKR 950.00 / 10kg Bag",
            "image": "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?auto=format&fit=crop&w=500&q=80"
        },
        {
            "id": "FL-FERT-TON",
            "name": "Estate Bulk Jumbo Sack (1,000kg)",
            "variant": "1-Ton Jumbo Bag",
            "price": 82000,
            "priceType": "fixed",
            "priceText": "LKR 82,000.00 / 1-Ton",
            "image": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=500&q=80"
        }
    ]
)

with open("industry-fertilizer.html", "w", encoding="utf-8") as f:
    f.write(fertilizer_html)
print("industry-fertilizer.html created.")

# ----------------- PAGE 7: GROWING MEDIA -----------------
growing_media_html = generate_industry_page(
    filename="industry-growing-media.html",
    active_id="growing-media",
    title_en="Growing Media & Planting Solutions",
    title_si="වගා මාධ්‍ය සහ පැළ සිටුවීමේ මාධ්‍ය",
    sector_num="07",
    status_badge='<span class="badge-status-operational"><i class="fas fa-check-circle"></i> Operational (Horticultural Media)</span>',
    hero_class="industry-hero-growing-media",
    overview_text="High-performance horticultural substrates, fine-particle seed propagation blends, and soilless greenhouse growing media engineered for rapid root development, maximum aeration, and balanced moisture retention.",
    products_list=[
        "Seed Starting Mix (පැළ සිටුවීමේ මාධ්‍ය)",
        "Premium Enriched Potting Mix (පෝච්චි වගා මිශ්‍රණ)",
        "Commercial Nursery Propagation Media (නර්සරි සඳහා වගා මාධ්‍ය)",
        "Greenhouse Hydroponic Soilless Substrates (හරිතාගාර වගා මාධ්‍ය)",
        "Washed & Low-EC Cocopeat / Perlite Blends",
        "Custom Specialized Growing Media Formulations (විශේෂ වගා මාධ්‍ය මිශ්‍රණ)"
    ],
    process_steps=[
        {"title": "1. Raw Substrate Washing & Buffering", "desc": "Cocopeat fibers triple-washed and calcium buffered to achieve low electrical conductivity (EC < 0.5 mS/cm)."},
        {"title": "2. Thermal Pasteurization", "desc": "Steam treating substrate to eradicate weed seeds, fungal spores, and insect larvae."},
        {"title": "3. Component Ratio Blending", "desc": "Scientific blending of washed coco fiber, perlite, vermiculite, and organic bio-compost."},
        {"title": "4. pH & Micronutrient Adjustment", "desc": "Stabilizing pH between 5.8 – 6.5 and adding slow-release starter trace minerals."},
        {"title": "5. Moisture Balancing", "desc": "Controlled moisture content maintained for instant seedling ready workability."},
        {"title": "6. Bagging & Sealing", "desc": "Automated bagging into breathable UV-resistant packaging."}
    ],
    pack_types=["10 Liter Handy Bags", "25 Liter Medium Bags", "50 Liter Commercial Grower Bags", "Bulk Palletized Sacks"],
    opportunities_list=[
        "Commercial nursery supply contracts for fruit, vegetable, and timber sapling growers.",
        "Greenhouse horticultural substrate orders for hydroponic bell pepper, tomato, and strawberry farms.",
        "Direct retail orders for home gardeners, urban farming enthusiasts, and landscapers.",
        "Bulk wholesale quotation requests for floriculture export enterprises."
    ],
    specs_table={
        "Electrical Conductivity (EC)": "< 0.5 mS/cm (Washed & Safe for sensitive roots)",
        "pH Range": "Optimally buffered at 5.8 – 6.5",
        "Water Holding Capacity": "Retains up to 6.5× its dry weight in moisture",
        "Air-Filled Porosity": "22% - 28% for aggressive root zone aeration",
        "Weed & Nematode Status": "100% Sterile & Guaranteed Zero Weed Contamination",
        "Organic Matter": "> 85% high-grade organic substrate matrix"
    },
    related_products=[
        {
            "id": "FL-GM-SEED25",
            "name": "Precision Seed Starting Mix (25 Liters)",
            "variant": "25L Grower Bag",
            "price": 1450,
            "priceType": "fixed",
            "priceText": "LKR 1,450.00 / 25L Bag",
            "image": "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?auto=format&fit=crop&w=500&q=80"
        },
        {
            "id": "FL-GM-POT50",
            "name": "Premium Enriched Potting Soil Mix (50 Liters)",
            "variant": "50L Commercial Bag",
            "price": 2600,
            "priceType": "fixed",
            "priceText": "LKR 2,600.00 / 50L Bag",
            "image": "https://images.unsplash.com/photo-1615811361523-6bd03d7748e7?auto=format&fit=crop&w=500&q=80"
        },
        {
            "id": "FL-GM-COCO50",
            "name": "Low-EC Buffered Coco/Perlite Substrate (50L)",
            "variant": "50L Greenhouse Hydroponic",
            "price": 2850,
            "priceType": "fixed",
            "priceText": "LKR 2,850.00 / 50L Bag",
            "image": "https://images.unsplash.com/photo-1574943320219-553eb213f72d?auto=format&fit=crop&w=500&q=80"
        }
    ]
)

with open("industry-growing-media.html", "w", encoding="utf-8") as f:
    f.write(growing_media_html)
print("industry-growing-media.html created.")

# ----------------- PAGE 8: WATER TECH -----------------
water_tech_html = generate_industry_page(
    filename="industry-water-tech.html",
    active_id="water-tech",
    title_en="Smart Water Filtration & Purification Solutions",
    title_si="ස්මාර්ට් ජල පෙරහන් සහ ජල පිරිපහදු තාක්ෂණය",
    sector_num="08",
    status_badge='<span class="badge-status-development"><i class="fas fa-cog fa-spin"></i> S. Korean Tech Collaboration</span>',
    hero_class="industry-hero-water-tech",
    overview_text="Strategic bilateral technology collaboration with South Korea introducing world-leading smart IoT drinking water purifiers, commercial multi-stage RO purification plants, and high-capacity industrial filtration systems to Sri Lanka and South Asian regional markets.",
    products_list=[
        "Smart IoT Water Purifiers with App Telemetry (ස්මාර්ට් ජල පෙරහන්)",
        "Domestic Multi-Stage RO & Alkaline Filters (ගෘහස්ථ ජල පෙරහන්)",
        "Commercial RO Water Purification Systems (වාණිජ ජල පිරිපහදු පද්ධති)",
        "Heavy-Duty Industrial Water Filtration Systems (කාර්මික පෙරහන් පද්ධති)",
        "Drinking Water Purification Equipment & Dispensers (පානීය ජල පිරිපහදු උපකරණ)",
        "Replacement Cartridges & RO Membranes (Water Filter Replacement Cartridges)",
        "Water Purification Accessories & Spare Parts (Water Purification Accessories)"
    ],
    process_steps=[
        {"title": "1. Multi-Stage Sediment Pre-filtration", "desc": "5-micron and 1-micron spun polypropylene filters trap rust, silt, sand, and particulate debris."},
        {"title": "2. Activated Carbon Block Adsorption", "desc": "High-iodine coconut shell activated carbon adsorbs chlorine, trihalomethanes, and chemical odors."},
        {"title": "3. South Korean RO Membrane Separation", "desc": "0.0001-micron Korean polyamide thin-film composite (TFC) membrane rejects 99.8% of heavy metals, salts, and microbes."},
        {"title": "4. Mineralizing & Alkaline Rebalancing", "desc": "Bio-ceramic post-cartridge restores vital potassium, magnesium, calcium, and balances pH to 7.8 - 8.2."},
        {"title": "5. Smart IoT Telemetry & UV Sterilization", "desc": "Built-in Korean microcontrollers monitor TDS, temperature, and filter lifecycle with UV-C tank disinfection."},
        {"title": "6. Automated Backwash & Self-Cleaning", "desc": "Auto-flush valves prolong membrane operational lifespan and guarantee sanitary reliability."}
    ],
    pack_types=["Residential Countertop Purifiers", "Commercial Undersink RO Stations", "Wall-Mount UV Dispensers", "Containerized 5,000L/hr Industrial Plants"],
    opportunities_list=[
        "South Korean technology transfer & domestic manufacturing facility establishment.",
        "Islandwide regional sales, installation, and filter replacement dealership opportunities.",
        "Commercial water purification installations for schools, hospitals, hotels, and corporate offices.",
        "Industrial water supply treatment for poultry hatcheries, mushroom chambers, and food plants."
    ],
    specs_table={
        "Technology Origin": "South Korea Smart Membrane Engineering Collaboration",
        "Filtration Precision": "0.0001 Microns (Reverses Osmosis) + UV-C Microbial Kill",
        "Smart Features": "Real-time TDS Display, Auto Leak Shut-off, Wi-Fi / App Filter Life Alerts",
        "Daily Capacity": "Domestic: 75 – 100 GPD; Commercial: 400 – 1,000 GPD; Industrial: 10,000+ LPD",
        "TDS Reduction": "> 98.5% total dissolved solids reduction",
        "Warranty": "Comprehensive warranty with continuous South Korean certified spare parts"
    },
    related_products=[
        {
            "id": "FL-WT-KOREAN-SMART",
            "name": "Korean Smart IoT 6-Stage Alkaline RO Purifier",
            "variant": "Countertop Smart Touch System",
            "price": 89500,
            "priceType": "fixed",
            "priceText": "LKR 89,500.00 / Unit",
            "image": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=500&q=80"
        },
        {
            "id": "FL-WT-COMMERCIAL",
            "name": "Commercial Multi-Stage 400 GPD Office Water Station",
            "variant": "Heavy-Duty Dual Membrane System",
            "price": 145000,
            "priceType": "fixed",
            "priceText": "LKR 145,000.00 / Unit",
            "image": "https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=500&q=80"
        },
        {
            "id": "FL-WT-CARTRIDGE-SET",
            "name": "Korean Authentic Replacement Cartridge Set (4-Pack)",
            "variant": "Sediment + Pre-Carbon + RO + Post-Carbon",
            "price": 14500,
            "priceType": "fixed",
            "priceText": "LKR 14,500.00 / Set",
            "image": "https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?auto=format&fit=crop&w=500&q=80"
        }
    ]
)

with open("industry-water-tech.html", "w", encoding="utf-8") as f:
    f.write(water_tech_html)
print("industry-water-tech.html created.")

