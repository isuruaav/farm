#!/usr/bin/env python3
"""
Generates index.html and about.html for FOREST LANKA
"""

from base_templates import COMMON_HEAD, get_header, COMMON_FOOTER

# ================= INDEX.HTML =================
index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>FOREST LANKA | Growing Agriculture. Building Industries. Connecting Global Markets.</title>
  {COMMON_HEAD}
</head>
<body data-lang="en">
  {get_header('home')}

  <main id="main-content">
    <!-- Hero Section -->
    <section class="relative bg-forest-dark text-white overflow-hidden py-20 lg:py-32">
      <!-- Background Graphic Overlay -->
      <div class="absolute inset-0 opacity-20 bg-[radial-gradient(#EBC975_1px,transparent_1px)] [background-size:24px_24px]"></div>
      <div class="absolute -top-40 -right-40 w-96 h-96 bg-emerald-600/20 rounded-full blur-3xl"></div>
      <div class="absolute -bottom-40 -left-40 w-96 h-96 bg-gold/10 rounded-full blur-3xl"></div>

      <div class="max-w-7xl mx-auto px-4 relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          <div class="lg:col-span-7 space-y-6">
            <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-emerald-800/80 border border-gold/40 text-gold text-xs font-semibold">
              <i class="fas fa-seedling text-sm"></i>
              <span class="lang-en">Official Agro-Industrial Venture • Reg: 16/2633</span>
              <span class="lang-si">රාජ්‍ය ලියාපදිංචි අංකය: 16/2633</span>
            </div>

            <h1 class="text-3xl sm:text-5xl lg:text-6xl font-black text-white leading-tight font-heading">
              <span class="text-gold">FOREST LANKA</span><br>
              <span class="lang-en text-2xl sm:text-4xl lg:text-5xl font-extrabold text-emerald-100 block mt-2">
                Growing Agriculture.<br>Building Industries.<br>Connecting Global Markets.
              </span>
              <span class="lang-si text-2xl sm:text-3xl lg:text-4xl font-bold text-emerald-100 block mt-2">
                කෘෂිකර්මාන්තය නංවමු.<br>කර්මාන්ත ගොඩනඟමු.<br>ගෝලීය වෙළෙඳපොළ ජයගනිමු.
              </span>
            </h1>

            <p class="text-sm sm:text-base text-emerald-100/90 leading-relaxed max-w-2xl">
              <span class="lang-en">
                Sri Lanka's premier integrated dynamic business platform encompassing 8 foundational industrial sectors: Smart Layer Poultry Farming, High-yield Animal Feed, 100% Recycled Paper Egg Trays, Smart Indoor Mushroom Cultivation, Industrial Egg Processing, Bio-Organic Fertilizers, Specialized Growing Media, and South Korean Smart Water Purification Technology.
              </span>
              <span class="lang-si">
                FOREST LANKA ආයතනයේ කෘෂිකාර්මික, කාර්මික නිෂ්පාදන, ආහාර නිෂ්පාදන, අපනයන, ජාත්‍යන්තර වෙළෙඳාම සහ ආයෝජන අවස්ථා දේශීය හා විදේශීය පාර්ශ්වයන් වෙත හඳුන්වාදෙන නවීන තාක්ෂණයෙන් සන්නද්ධ ප්‍රමුඛතම ව්‍යවසාය.
              </span>
            </p>

            <div class="flex flex-wrap gap-4 pt-2">
              <a href="industries.html" class="btn-gold text-sm px-6 py-3.5">
                <i class="fas fa-industry"></i>
                <span class="lang-en">Explore 8 Core Industries</span>
                <span class="lang-si">ප්‍රධාන කර්මාන්ත 08</span>
              </a>
              <a href="products.html" class="btn-primary text-sm px-6 py-3.5 border border-emerald-400/30">
                <i class="fas fa-boxes-stacked"></i>
                <span class="lang-en">Product Catalog & Store</span>
                <span class="lang-si">නිෂ්පාදන නාමාවලිය</span>
              </a>
              <a href="investment.html" class="btn-outline-white text-sm px-5 py-3.5">
                <i class="fas fa-chart-line text-gold"></i>
                <span class="lang-en">Investment & Export</span>
                <span class="lang-si">ආයෝජන හා අපනයන</span>
              </a>
            </div>

            <!-- Key Trust Badges -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-6 border-t border-emerald-800/80 text-xs text-emerald-200">
              <div class="flex items-center gap-2">
                <i class="fas fa-shield-halved text-gold text-base"></i>
                <span>Registered 16/2633</span>
              </div>
              <div class="flex items-center gap-2">
                <i class="fas fa-recycle text-emerald-400 text-base"></i>
                <span>Zero-Waste Circular</span>
              </div>
              <div class="flex items-center gap-2">
                <i class="fas fa-microchip text-blue-300 text-base"></i>
                <span>Korean Tech Partner</span>
              </div>
              <div class="flex items-center gap-2">
                <i class="fas fa-universal-access text-gold text-base"></i>
                <span>WCAG 2.2 AAA Target</span>
              </div>
            </div>
          </div>

          <!-- Hero Image & Interactive Card -->
          <div class="lg:col-span-5 flex justify-center">
            <div class="relative w-full max-w-md">
              <div class="bg-gradient-to-br from-emerald-800/60 to-forest-dark border-2 border-gold/40 rounded-3xl p-6 shadow-2xl backdrop-blur-md relative overflow-hidden">
                <div class="flex justify-between items-center mb-4">
                  <span class="badge-status-operational"><i class="fas fa-circle text-[8px] animate-pulse"></i> Active Agro-Industrial Hub</span>
                  <span class="text-xs text-gold font-mono">EST. 2026</span>
                </div>

                <div class="bg-white rounded-2xl p-6 text-center shadow-inner mb-5">
                  <img src="assets/images/logo.jpg" alt="FOREST LANKA Logo" class="max-h-56 mx-auto object-contain transition-transform hover:scale-105 duration-300">
                </div>

                <div class="space-y-3 text-xs">
                  <div class="flex justify-between items-center py-1.5 border-b border-emerald-700/50">
                    <span class="text-emerald-200">Initial Layer Capacity:</span>
                    <span class="font-bold text-white">125,000 Hens (Phase 1)</span>
                  </div>
                  <div class="flex justify-between items-center py-1.5 border-b border-emerald-700/50">
                    <span class="text-emerald-200">Expansion Target:</span>
                    <span class="font-bold text-gold">2,500,000 Hens</span>
                  </div>
                  <div class="flex justify-between items-center py-1.5 border-b border-emerald-700/50">
                    <span class="text-emerald-200">Mushroom Facility:</span>
                    <span class="font-bold text-white">5 – 10 Acres IoT Chambers</span>
                  </div>
                  <div class="flex justify-between items-center py-1.5">
                    <span class="text-emerald-200">Global Logistics:</span>
                    <span class="font-bold text-emerald-300">Direct Export & Port Clearances</span>
                  </div>
                </div>

                <div class="mt-5">
                  <a href="https://wa.me/94719740798" target="_blank" class="w-full btn-gold text-xs py-2.5 flex items-center justify-center gap-2">
                    <i class="fab fa-whatsapp text-green-700 text-sm"></i>
                    <span>Contact Operations on WhatsApp</span>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Scale Metrics Section -->
    <section class="bg-emerald-950 text-white py-10 border-b border-emerald-800">
      <div class="max-w-7xl mx-auto px-4">
        <div class="grid grid-cols-2 md:grid-cols-5 gap-6 text-center">
          <div class="p-4 border-r border-emerald-800/60 last:border-0">
            <div class="text-3xl sm:text-4xl font-extrabold text-gold font-heading mb-1">125K+</div>
            <div class="text-xs text-emerald-200 uppercase tracking-wider font-semibold">Phase 1 Hens</div>
            <div class="text-[11px] text-emerald-400 mt-0.5">Scaling to 2.5M layers</div>
          </div>
          <div class="p-4 border-r border-emerald-800/60 last:border-0">
            <div class="text-3xl sm:text-4xl font-extrabold text-white font-heading mb-1">08</div>
            <div class="text-xs text-emerald-200 uppercase tracking-wider font-semibold">Core Industries</div>
            <div class="text-[11px] text-emerald-400 mt-0.5">Synergistic ecosystem</div>
          </div>
          <div class="p-4 border-r border-emerald-800/60 last:border-0">
            <div class="text-3xl sm:text-4xl font-extrabold text-gold font-heading mb-1">5-10</div>
            <div class="text-xs text-emerald-200 uppercase tracking-wider font-semibold">Acres Smart Farm</div>
            <div class="text-[11px] text-emerald-400 mt-0.5">Mushroom export base</div>
          </div>
          <div class="p-4 border-r border-emerald-800/60 last:border-0">
            <div class="text-3xl sm:text-4xl font-extrabold text-white font-heading mb-1">100%</div>
            <div class="text-xs text-emerald-200 uppercase tracking-wider font-semibold">Recycled Trays</div>
            <div class="text-[11px] text-emerald-400 mt-0.5">Molded pulp technology</div>
          </div>
          <div class="col-span-2 md:col-span-1 p-4">
            <div class="text-3xl sm:text-4xl font-extrabold text-blue-300 font-heading mb-1">S. KOREA</div>
            <div class="text-xs text-emerald-200 uppercase tracking-wider font-semibold">Tech Collaboration</div>
            <div class="text-[11px] text-emerald-400 mt-0.5">Smart water purification</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 8 Core Industries Showcase (PDF Section 05) -->
    <section class="py-20 bg-warmwhite">
      <div class="max-w-7xl mx-auto px-4">
        <div class="text-center max-w-3xl mx-auto mb-16">
          <div class="inline-block px-3 py-1 bg-emerald-100 text-emerald-800 rounded-full text-xs font-bold uppercase tracking-wider mb-2">
            Dynamic Business Ecosystem
          </div>
          <h2 class="text-3xl sm:text-4xl font-black text-forest font-heading">
            <span class="lang-en">The 8 Core Business Industries</span>
            <span class="lang-si">ප්‍රධාන ව්‍යාපාරික අංශ 08</span>
          </h2>
          <p class="text-sm text-gray-600 mt-3">
            <span class="lang-en">
              FOREST LANKA unites modern agricultural cultivation, industrial feed processing, eco-friendly manufacturing, and high-tech purification into a high-capacity closed-loop value chain.
            </span>
            <span class="lang-si">
              FOREST LANKA ආයතනයේ ප්‍රධාන ව්‍යාපාරික අංශ 08 එකම මධ්‍යගත පද්ධතියක් යටතේ ක්‍රියාත්මක වේ.
            </span>
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <!-- 1. Layer Poultry Farm -->
          <div class="glass-card flex flex-col justify-between overflow-hidden">
            <div class="h-44 relative overflow-hidden">
              <img src="https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?auto=format&fit=crop&w=700&q=80" alt="Modern Smart Layer Poultry Farm" class="w-full h-full object-cover transition-transform duration-500 hover:scale-110">
              <div class="absolute top-3 right-3">
                <span class="badge-status-operational"><i class="fas fa-check text-[10px]"></i> Operational</span>
              </div>
              <div class="absolute bottom-2 left-3 bg-forest/80 backdrop-blur-sm text-gold px-2.5 py-0.5 rounded text-xs font-bold">
                01. Poultry
              </div>
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <h3 class="text-base font-bold text-forest mb-2">Modern Smart Layer Poultry Farm</h3>
                <p class="text-xs text-gray-600 leading-relaxed mb-3">
                  Automated layer farm launching with 125,000 hens with multi-tier climate systems, automated sorting, and fresh retail & bulk egg distribution.
                </p>
                <div class="text-[11px] text-emerald-800 font-semibold space-y-1 mb-4 bg-emerald-50/80 p-2.5 rounded">
                  <div>• 6, 12, 15 & 30-Egg Packs</div>
                  <div>• Direct Hotel, Bakery & Wholesale Supply</div>
                </div>
              </div>
              <a href="industry-poultry.html" class="btn-primary text-xs w-full justify-between">
                <span>View Poultry Sector</span>
                <i class="fas fa-arrow-right"></i>
              </a>
            </div>
          </div>

          <!-- 2. Animal Feed Manufacturing -->
          <div class="glass-card flex flex-col justify-between overflow-hidden">
            <div class="h-44 relative overflow-hidden">
              <img src="https://images.unsplash.com/photo-1574943320219-553eb213f72d?auto=format&fit=crop&w=700&q=80" alt="Modern Animal Feed Manufacturing" class="w-full h-full object-cover transition-transform duration-500 hover:scale-110">
              <div class="absolute top-3 right-3">
                <span class="badge-status-development"><i class="fas fa-cog fa-spin text-[10px]"></i> In Progress</span>
              </div>
              <div class="absolute bottom-2 left-3 bg-forest/80 backdrop-blur-sm text-gold px-2.5 py-0.5 rounded text-xs font-bold">
                02. Animal Feed
              </div>
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <h3 class="text-base font-bold text-forest mb-2">Modern Animal Feed Manufacturing</h3>
                <p class="text-xs text-gray-600 leading-relaxed mb-3">
                  Comprehensive 12-step industrial manufacturing line delivering Chick Starter, Grower, Layer, Broiler, Cattle, Goat and Fish feed.
                </p>
                <div class="text-[11px] text-emerald-800 font-semibold space-y-1 mb-4 bg-emerald-50/80 p-2.5 rounded">
                  <div>• 12-Step Automated Process</div>
                  <div>• 25kg, 50kg Bags & Bulk Farm Contracts</div>
                </div>
              </div>
              <a href="industry-feed.html" class="btn-primary text-xs w-full justify-between">
                <span>View Feed Mill Sector</span>
                <i class="fas fa-arrow-right"></i>
              </a>
            </div>
          </div>

          <!-- 3. Recycled Paper Egg Trays -->
          <div class="glass-card flex flex-col justify-between overflow-hidden">
            <div class="h-44 relative overflow-hidden">
              <img src="https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=700&q=80" alt="Recycled Paper Egg Tray Manufacturing" class="w-full h-full object-cover transition-transform duration-500 hover:scale-110">
              <div class="absolute top-3 right-3">
                <span class="badge-status-operational"><i class="fas fa-check text-[10px]"></i> Operational</span>
              </div>
              <div class="absolute bottom-2 left-3 bg-forest/80 backdrop-blur-sm text-gold px-2.5 py-0.5 rounded text-xs font-bold">
                03. Egg Trays
              </div>
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <h3 class="text-base font-bold text-forest mb-2">Recycled Paper Egg Tray Manufacturing</h3>
                <p class="text-xs text-gray-600 leading-relaxed mb-3">
                  Eco-friendly biodegradable molded pulp packaging from recycled paper with an 8-step continuous vacuum molding system.
                </p>
                <div class="text-[11px] text-emerald-800 font-semibold space-y-1 mb-4 bg-emerald-50/80 p-2.5 rounded">
                  <div>• 6, 12, 15, 30-Egg Trays</div>
                  <div>• Shock-proof Commercial Export Trays</div>
                </div>
              </div>
              <a href="industry-egg-trays.html" class="btn-primary text-xs w-full justify-between">
                <span>View Egg Tray Sector</span>
                <i class="fas fa-arrow-right"></i>
              </a>
            </div>
          </div>

          <!-- 4. Smart Mushroom Farming -->
          <div class="glass-card flex flex-col justify-between overflow-hidden">
            <div class="h-44 relative overflow-hidden">
              <img src="https://images.unsplash.com/photo-1509358271058-acd22cc93898?auto=format&fit=crop&w=700&q=80" alt="Smart Mushroom Farming & Global Export" class="w-full h-full object-cover transition-transform duration-500 hover:scale-110">
              <div class="absolute top-3 right-3">
                <span class="badge-status-development"><i class="fas fa-cog fa-spin text-[10px]"></i> Expanding</span>
              </div>
              <div class="absolute bottom-2 left-3 bg-forest/80 backdrop-blur-sm text-gold px-2.5 py-0.5 rounded text-xs font-bold">
                04. Mushrooms
              </div>
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <h3 class="text-base font-bold text-forest mb-2">Smart Mushroom Farming & Global Export</h3>
                <p class="text-xs text-gray-600 leading-relaxed mb-3">
                  5–10 acres of IoT climate-controlled chambers producing Oyster, Shiitake, and Button mushrooms in fresh, dried, and powdered forms.
                </p>
                <div class="text-[11px] text-emerald-800 font-semibold space-y-1 mb-4 bg-emerald-50/80 p-2.5 rounded">
                  <div>• Automated PID Temperature & Humidity</div>
                  <div>• International Export Agreements & MOQ</div>
                </div>
              </div>
              <a href="industry-mushrooms.html" class="btn-primary text-xs w-full justify-between">
                <span>View Mushroom Sector</span>
                <i class="fas fa-arrow-right"></i>
              </a>
            </div>
          </div>

          <!-- 5. Egg Processing & Value Added -->
          <div class="glass-card flex flex-col justify-between overflow-hidden">
            <div class="h-44 relative overflow-hidden">
              <img src="https://images.unsplash.com/photo-1516467508483-a7212febe31a?auto=format&fit=crop&w=700&q=80" alt="Egg Processing & Value-Added Products" class="w-full h-full object-cover transition-transform duration-500 hover:scale-110">
              <div class="absolute top-3 right-3">
                <span class="badge-status-planned"><i class="fas fa-clock text-[10px]"></i> Planned</span>
              </div>
              <div class="absolute bottom-2 left-3 bg-forest/80 backdrop-blur-sm text-gold px-2.5 py-0.5 rounded text-xs font-bold">
                05. Egg Processing
              </div>
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <h3 class="text-base font-bold text-forest mb-2">Egg Processing & Value-Added Products</h3>
                <p class="text-xs text-gray-600 leading-relaxed mb-3">
                  Advanced processing facility transforming farm eggs into pasteurized liquid eggs, Whole Egg Powder, Egg Yolk Powder, and High-Whipping Albumen.
                </p>
                <div class="text-[11px] text-emerald-800 font-semibold space-y-1 mb-4 bg-emerald-50/80 p-2.5 rounded">
                  <div>• Long Shelf-Life Industrial Ingredients</div>
                  <div>• Bulk Supply for Bakeries & Biscuit Makers</div>
                </div>
              </div>
              <a href="industry-egg-processing.html" class="btn-primary text-xs w-full justify-between">
                <span>View Egg Powder Sector</span>
                <i class="fas fa-arrow-right"></i>
              </a>
            </div>
          </div>

          <!-- 6. Organic Fertilizer Manufacturing -->
          <div class="glass-card flex flex-col justify-between overflow-hidden">
            <div class="h-44 relative overflow-hidden">
              <img src="https://images.unsplash.com/photo-1615811361523-6bd03d7748e7?auto=format&fit=crop&w=700&q=80" alt="Organic Fertilizer Manufacturing" class="w-full h-full object-cover transition-transform duration-500 hover:scale-110">
              <div class="absolute top-3 right-3">
                <span class="badge-status-operational"><i class="fas fa-check text-[10px]"></i> Operational</span>
              </div>
              <div class="absolute bottom-2 left-3 bg-forest/80 backdrop-blur-sm text-gold px-2.5 py-0.5 rounded text-xs font-bold">
                06. Bio-Fertilizer
              </div>
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <h3 class="text-base font-bold text-forest mb-2">Organic Fertilizer Manufacturing</h3>
                <p class="text-xs text-gray-600 leading-relaxed mb-3">
                  Converting organic poultry manure and agricultural residues into sterilized, high-grade pelleted and granular bio-fertilizer.
                </p>
                <div class="text-[11px] text-emerald-800 font-semibold space-y-1 mb-4 bg-emerald-50/80 p-2.5 rounded">
                  <div>• 5kg, 10kg, 20kg & Bulk Sacks</div>
                  <div>• Enriched Formulations for Plantations</div>
                </div>
              </div>
              <a href="industry-fertilizer.html" class="btn-primary text-xs w-full justify-between">
                <span>View Fertilizer Sector</span>
                <i class="fas fa-arrow-right"></i>
              </a>
            </div>
          </div>

          <!-- 7. Growing Media & Planting Solutions -->
          <div class="glass-card flex flex-col justify-between overflow-hidden">
            <div class="h-44 relative overflow-hidden">
              <img src="https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?auto=format&fit=crop&w=700&q=80" alt="Growing Media & Planting Solutions" class="w-full h-full object-cover transition-transform duration-500 hover:scale-110">
              <div class="absolute top-3 right-3">
                <span class="badge-status-operational"><i class="fas fa-check text-[10px]"></i> Operational</span>
              </div>
              <div class="absolute bottom-2 left-3 bg-forest/80 backdrop-blur-sm text-gold px-2.5 py-0.5 rounded text-xs font-bold">
                07. Growing Media
              </div>
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <h3 class="text-base font-bold text-forest mb-2">Growing Media & Planting Solutions</h3>
                <p class="text-xs text-gray-600 leading-relaxed mb-3">
                  High-porosity Seed Starting Mix, Premium Potting Mix, and Soilless Substrates specifically formulated for nurseries and commercial greenhouses.
                </p>
                <div class="text-[11px] text-emerald-800 font-semibold space-y-1 mb-4 bg-emerald-50/80 p-2.5 rounded">
                  <div>• Seedling & Potting Mix</div>
                  <div>• Commercial Greenhouse Substrates</div>
                </div>
              </div>
              <a href="industry-growing-media.html" class="btn-primary text-xs w-full justify-between">
                <span>View Media Sector</span>
                <i class="fas fa-arrow-right"></i>
              </a>
            </div>
          </div>

          <!-- 8. Smart Water Filtration -->
          <div class="glass-card flex flex-col justify-between overflow-hidden">
            <div class="h-44 relative overflow-hidden">
              <img src="https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=700&q=80" alt="Smart Water Filtration & Purification Solutions" class="w-full h-full object-cover transition-transform duration-500 hover:scale-110">
              <div class="absolute top-3 right-3">
                <span class="badge-status-development"><i class="fas fa-cog fa-spin text-[10px]"></i> S. Korean Tech</span>
              </div>
              <div class="absolute bottom-2 left-3 bg-waterblue text-white px-2.5 py-0.5 rounded text-xs font-bold">
                08. Water Tech
              </div>
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <div>
                <h3 class="text-base font-bold text-forest mb-2">Smart Water Filtration & Purification</h3>
                <p class="text-xs text-gray-600 leading-relaxed mb-3">
                  South Korean technology collaboration providing smart IoT domestic purifiers, commercial RO systems, and industrial water plants.
                </p>
                <div class="text-[11px] text-waterblue font-semibold space-y-1 mb-4 bg-blue-50/80 p-2.5 rounded">
                  <div>• Smart Purifiers & Cartridges</div>
                  <div>• Islandwide Dealership & Export</div>
                </div>
              </div>
              <a href="industry-water-tech.html" class="btn-primary text-xs w-full justify-between">
                <span>View Water Tech Sector</span>
                <i class="fas fa-arrow-right"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Circular Economy Synergy Section -->
    <section class="py-16 bg-white border-y border-gray-200">
      <div class="max-w-7xl mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
          <div class="lg:col-span-5 space-y-4">
            <span class="text-xs font-bold uppercase tracking-wider text-emerald-700 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-200">
              Zero-Waste Closed Loop Ecosystem
            </span>
            <h2 class="text-3xl font-black text-forest font-heading">
              How Our Industries Connect in a Sustainable Bio-Economy
            </h2>
            <p class="text-xs sm:text-sm text-gray-600 leading-relaxed">
              FOREST LANKA is engineered to operate without waste. Every raw material, by-product, and output is continuously recirculated across our 8 industrial pillars, creating unmatched cost efficiency, environmental sustainability, and premium product value.
            </p>
            <div class="space-y-3 pt-2">
              <div class="flex items-start gap-3">
                <div class="w-8 h-8 rounded-full bg-emerald-100 text-emerald-800 flex items-center justify-center font-bold text-sm shrink-0 mt-0.5">1</div>
                <div class="text-xs">
                  <strong class="text-forest">Feed Mill supplies Poultry & Livestock:</strong> High-protein nutrition ensures peak layer health and maximum egg laying yield.
                </div>
              </div>
              <div class="flex items-start gap-3">
                <div class="w-8 h-8 rounded-full bg-emerald-100 text-emerald-800 flex items-center justify-center font-bold text-sm shrink-0 mt-0.5">2</div>
                <div class="text-xs">
                  <strong class="text-forest">Poultry Manure becomes Bio-Fertilizer:</strong> 100% of layer droppings are collected and converted into odorless, sterilized bio-organic fertilizer.
                </div>
              </div>
              <div class="flex items-start gap-3">
                <div class="w-8 h-8 rounded-full bg-emerald-100 text-emerald-800 flex items-center justify-center font-bold text-sm shrink-0 mt-0.5">3</div>
                <div class="text-xs">
                  <strong class="text-forest">Recycled Paper Trays Protect Eggs:</strong> Waste paper is hydrapulped into biodegradable trays, eliminating plastic and packing millions of eggs.
                </div>
              </div>
              <div class="flex items-start gap-3">
                <div class="w-8 h-8 rounded-full bg-waterblue text-white flex items-center justify-center font-bold text-sm shrink-0 mt-0.5">4</div>
                <div class="text-xs">
                  <strong class="text-waterblue">Korean Water Tech fuels Agriculture:</strong> Purified smart water feeds our mushroom climate rooms, poultry lines, and local communities.
                </div>
              </div>
            </div>
          </div>

          <div class="lg:col-span-7">
            <div class="bg-forest-dark text-white p-8 rounded-3xl border-2 border-gold/40 relative shadow-2xl">
              <div class="text-center mb-6">
                <h3 class="text-lg font-bold text-gold uppercase tracking-wider">The Forest Lanka Interconnected Value Engine</h3>
                <p class="text-xs text-emerald-200">Self-sustaining supply chain from farm gate to global port</p>
              </div>

              <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center text-xs">
                <div class="bg-emerald-900/60 p-3 rounded-xl border border-emerald-700">
                  <i class="fas fa-wheat-awn text-2xl text-gold mb-1"></i>
                  <div class="font-bold">Feed Mill</div>
                  <div class="text-[10px] text-emerald-300">Formulated Diet</div>
                </div>
                <div class="bg-emerald-900/60 p-3 rounded-xl border border-emerald-700">
                  <i class="fas fa-egg text-2xl text-gold mb-1"></i>
                  <div class="font-bold">Layer Farm</div>
                  <div class="text-[10px] text-emerald-300">125K to 2.5M Layers</div>
                </div>
                <div class="bg-emerald-900/60 p-3 rounded-xl border border-emerald-700">
                  <i class="fas fa-box-open text-2xl text-gold mb-1"></i>
                  <div class="font-bold">Pulp Trays</div>
                  <div class="text-[10px] text-emerald-300">100% Recycled Pack</div>
                </div>
                <div class="bg-emerald-900/60 p-3 rounded-xl border border-emerald-700">
                  <i class="fas fa-mortar-pestle text-2xl text-gold mb-1"></i>
                  <div class="font-bold">Egg Powders</div>
                  <div class="text-[10px] text-emerald-300">Industrial Ingredients</div>
                </div>
                <div class="bg-emerald-900/60 p-3 rounded-xl border border-emerald-700">
                  <i class="fas fa-leaf text-2xl text-emerald-400 mb-1"></i>
                  <div class="font-bold">Mushroom IoT</div>
                  <div class="text-[10px] text-emerald-300">5-10 Acre Export</div>
                </div>
                <div class="bg-emerald-900/60 p-3 rounded-xl border border-emerald-700">
                  <i class="fas fa-seedling text-2xl text-emerald-400 mb-1"></i>
                  <div class="font-bold">Bio-Fertilizer</div>
                  <div class="text-[10px] text-emerald-300">Organic Enrichment</div>
                </div>
                <div class="bg-emerald-900/60 p-3 rounded-xl border border-emerald-700">
                  <i class="fas fa-plant-wilt text-2xl text-emerald-400 mb-1"></i>
                  <div class="font-bold">Growing Media</div>
                  <div class="text-[10px] text-emerald-300">Nursery Substrates</div>
                </div>
                <div class="bg-waterblue/80 p-3 rounded-xl border border-cyan-400">
                  <i class="fas fa-droplet text-2xl text-cyan-300 mb-1"></i>
                  <div class="font-bold">Korean Water</div>
                  <div class="text-[10px] text-cyan-200">Smart Purification</div>
                </div>
              </div>

              <div class="mt-6 text-center">
                <a href="about.html" class="inline-flex items-center gap-2 text-xs font-bold text-gold hover:underline">
                  <span>Learn more about our Vision, Mission & Board</span>
                  <i class="fas fa-arrow-right"></i>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Products Preview with Instant Add-to-Cart -->
    <section class="py-20 bg-warmwhite">
      <div class="max-w-7xl mx-auto px-4">
        <div class="flex flex-col md:flex-row justify-between items-start md:items-end mb-12 gap-4">
          <div>
            <div class="text-xs font-bold uppercase tracking-wider text-emerald-700 mb-1">Commercial & Retail Store</div>
            <h2 class="text-3xl font-black text-forest font-heading">Featured Products & Commercial Lines</h2>
            <p class="text-xs sm:text-sm text-gray-600 mt-1">Available for direct purchase, wholesale bulk contracts, and export inquiries.</p>
          </div>
          <a href="products.html" class="btn-primary text-xs py-2.5 px-4 shrink-0">
            <span>View All Products (30+ Lines)</span>
            <i class="fas fa-arrow-right"></i>
          </a>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <!-- Product 1: Farm Fresh Graded Eggs -->
          <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-4 flex flex-col justify-between hover:shadow-md transition">
            <div>
              <div class="relative h-44 rounded-lg overflow-hidden mb-3 bg-warmwhite">
                <img src="https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=500&q=80" alt="Farm Fresh Cleaned & Graded Eggs" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-forest text-gold text-[10px] font-bold px-2 py-0.5 rounded">Poultry</span>
              </div>
              <h4 class="font-bold text-sm text-forest mb-1">Farm Fresh Cleaned & Graded Eggs</h4>
              <p class="text-xs text-gray-500 mb-2">Automated candling, cleaned, sanitized, weight-classified Grade A eggs.</p>
              <div class="text-xs font-semibold text-emerald-800 mb-3">
                <span>Pack: 30-Egg Commercial Tray</span> • <span class="text-forest font-bold">LKR 1,350.00</span>
              </div>
            </div>
            <button onclick="addToCart({{id: 'FL-EGG-30', name: 'Cleaned Graded Eggs (30-Tray)', price: 1350, priceType: 'fixed', variant: '30-Pack Tray', industry: 'Poultry', image: 'https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=500&q=80'}})" class="btn-primary text-xs w-full py-2">
              <i class="fas fa-cart-plus"></i> Add to Cart
            </button>
          </div>

          <!-- Product 2: High Yield Layer Feed 50kg -->
          <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-4 flex flex-col justify-between hover:shadow-md transition">
            <div>
              <div class="relative h-44 rounded-lg overflow-hidden mb-3 bg-warmwhite">
                <img src="https://images.unsplash.com/photo-1574943320219-553eb213f72d?auto=format&fit=crop&w=500&q=80" alt="Premium Layer Feed Mash & Pellets" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-emerald-700 text-white text-[10px] font-bold px-2 py-0.5 rounded">Animal Feed</span>
              </div>
              <h4 class="font-bold text-sm text-forest mb-1">High-Yield Layer Feed Pellets (50kg)</h4>
              <p class="text-xs text-gray-500 mb-2">Scientific calcium & crude protein balanced formula for maximum laying cycle duration.</p>
              <div class="text-xs font-semibold text-emerald-800 mb-3">
                <span>Pack: 50kg Woven Bag</span> • <span class="text-forest font-bold">LKR 7,850.00</span>
              </div>
            </div>
            <button onclick="addToCart({{id: 'FL-FEED-50', name: 'High-Yield Layer Feed (50kg)', price: 7850, priceType: 'fixed', variant: '50kg Bag', industry: 'Animal Feed', image: 'https://images.unsplash.com/photo-1574943320219-553eb213f72d?auto=format&fit=crop&w=500&q=80'}})" class="btn-primary text-xs w-full py-2">
              <i class="fas fa-cart-plus"></i> Add to Cart
            </button>
          </div>

          <!-- Product 3: Recycled Paper 30-Egg Trays -->
          <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-4 flex flex-col justify-between hover:shadow-md transition">
            <div>
              <div class="relative h-44 rounded-lg overflow-hidden mb-3 bg-warmwhite">
                <img src="https://images.unsplash.com/photo-1506976785307-8732e854ad03?auto=format&fit=crop&w=500&q=80" alt="Recycled Paper Molded 30-Egg Trays" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-forest text-gold text-[10px] font-bold px-2 py-0.5 rounded">Egg Trays</span>
              </div>
              <h4 class="font-bold text-sm text-forest mb-1">Molded Pulp 30-Egg Trays (Bundle of 100)</h4>
              <p class="text-xs text-gray-500 mb-2">100% biodegradable, vibration absorbing, high tensile recycled fiber trays.</p>
              <div class="text-xs font-semibold text-emerald-800 mb-3">
                <span>Pack: Bundle of 100 Trays</span> • <span class="text-forest font-bold">LKR 3,200.00</span>
              </div>
            </div>
            <button onclick="addToCart({{id: 'FL-TRAY-100', name: 'Recycled Egg Trays (Bundle 100)', price: 3200, priceType: 'fixed', variant: 'Bundle of 100', industry: 'Egg Trays', image: 'https://images.unsplash.com/photo-1506976785307-8732e854ad03?auto=format&fit=crop&w=500&q=80'}})" class="btn-primary text-xs w-full py-2">
              <i class="fas fa-cart-plus"></i> Add to Cart
            </button>
          </div>

          <!-- Product 4: Whole Egg Powder (Commercial B2B) -->
          <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-4 flex flex-col justify-between hover:shadow-md transition">
            <div>
              <div class="relative h-44 rounded-lg overflow-hidden mb-3 bg-warmwhite">
                <img src="https://images.unsplash.com/photo-1516467508483-a7212febe31a?auto=format&fit=crop&w=500&q=80" alt="Spray Dried Whole Egg Powder" class="w-full h-full object-cover">
                <span class="absolute top-2 left-2 bg-gold text-forest text-[10px] font-bold px-2 py-0.5 rounded">Egg Powder</span>
              </div>
              <h4 class="font-bold text-sm text-forest mb-1">Spray-Dried Whole Egg Powder (20kg)</h4>
              <p class="text-xs text-gray-500 mb-2">Pasteurized, 24-month shelf life. Replaces 1,600 fresh eggs per 20kg box for industrial food processors.</p>
              <div class="text-xs font-semibold text-amber-700 mb-3">
                <span>B2B Quotation Required</span>
              </div>
            </div>
            <button onclick="addToCart({{id: 'FL-POWDER-20', name: 'Spray-Dried Whole Egg Powder (20kg)', price: 0, priceType: 'quote', variant: '20kg Box', industry: 'Egg Processing', image: 'https://images.unsplash.com/photo-1516467508483-a7212febe31a?auto=format&fit=crop&w=500&q=80'}})" class="btn-gold text-xs w-full py-2">
              <i class="fas fa-file-invoice"></i> Request B2B Quote
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Global Export & Investment Highlight Banner -->
    <section class="py-16 bg-gradient-to-r from-forest via-emerald-900 to-forest text-white">
      <div class="max-w-7xl mx-auto px-4">
        <div class="bg-forest-dark/70 rounded-3xl p-8 lg:p-12 border-2 border-gold/40 shadow-2xl">
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
            <div class="lg:col-span-8 space-y-4">
              <span class="text-xs font-bold text-gold uppercase tracking-wider bg-gold/10 px-3 py-1 rounded-full border border-gold/30">
                International Trade & Strategic Capital
              </span>
              <h2 class="text-2xl sm:text-4xl font-extrabold text-white font-heading">
                Connecting Sri Lanka's Agro-Industrial Prowess with Global Markets
              </h2>
              <p class="text-xs sm:text-sm text-emerald-100/90 leading-relaxed">
                Whether you are a foreign buyer seeking premium vacuum-packed Shiitake mushrooms and spray-dried egg powder, an institutional distributor seeking egg trays, or an international investor exploring our 8 high-ROI ventures with Korean technology integration — FOREST LANKA is your certified partner.
              </p>
              <div class="flex flex-wrap gap-3 pt-2">
                <a href="export.html" class="btn-gold text-xs py-3 px-6">
                  <i class="fas fa-ship"></i> International Export Portal
                </a>
                <a href="investment.html" class="btn-primary text-xs py-3 px-6">
                  <i class="fas fa-handshake"></i> Explore 8 Investment Projects
                </a>
                <a href="partners.html" class="btn-outline-white text-xs py-3 px-5">
                  <i class="fas fa-user-plus text-gold"></i> Become Our Partner
                </a>
              </div>
            </div>

            <div class="lg:col-span-4 bg-white/5 border border-white/10 rounded-2xl p-5 text-xs text-emerald-100 space-y-3">
              <h4 class="font-bold text-gold text-sm uppercase tracking-wider border-b border-white/10 pb-2">Export Standards</h4>
              <div class="flex items-center gap-2"><i class="fas fa-check-circle text-gold"></i> HACCP & ISO Target Architecture</div>
              <div class="flex items-center gap-2"><i class="fas fa-check-circle text-gold"></i> Temperature Controlled Cold-Chain</div>
              <div class="flex items-center gap-2"><i class="fas fa-check-circle text-gold"></i> FOB / CIF Shipping via Colombo Port</div>
              <div class="flex items-center gap-2"><i class="fas fa-check-circle text-gold"></i> South Korea Tech Transfer Assurance</div>
              <div class="pt-2">
                <a href="mailto:thilankaherath7@gmail.com" class="text-gold font-bold hover:underline flex items-center gap-1.5">
                  <i class="fas fa-envelope"></i> export@forestlanka.lk / Contact Director
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Latest News & Milestones -->
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4">
        <div class="flex justify-between items-end mb-10">
          <div>
            <span class="text-xs font-bold uppercase tracking-wider text-emerald-700">Media & Announcements</span>
            <h2 class="text-2xl sm:text-3xl font-black text-forest font-heading">Latest Corporate Milestones</h2>
          </div>
          <a href="news.html" class="text-xs font-bold text-emerald-800 hover:text-emerald-950 flex items-center gap-1">
            <span>All Updates</span> <i class="fas fa-arrow-right"></i>
          </a>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <article class="bg-warmwhite rounded-xl border border-gray-200 overflow-hidden shadow-sm hover:shadow-md transition">
            <img src="https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?auto=format&fit=crop&w=600&q=80" alt="Layer Farm Launch" class="w-full h-44 object-cover">
            <div class="p-5">
              <span class="text-[11px] font-semibold text-gray-500">November 2026 • Kurunegala</span>
              <h3 class="font-bold text-sm text-forest mt-1 mb-2 hover:text-emerald-700">
                <a href="news.html">Phase 1 Modern Smart Layer Poultry Farm Breaks Ground</a>
              </h3>
              <p class="text-xs text-gray-600 line-clamp-2">
                Initial housing for 125,000 layers initiated in Polpithigama with automated feed dispensing and computerized egg collection lines.
              </p>
            </div>
          </article>

          <article class="bg-warmwhite rounded-xl border border-gray-200 overflow-hidden shadow-sm hover:shadow-md transition">
            <img src="https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=600&q=80" alt="Korean Water Filtration Agreement" class="w-full h-44 object-cover">
            <div class="p-5">
              <span class="text-[11px] font-semibold text-gray-500">November 2026 • Technology</span>
              <h3 class="font-bold text-sm text-forest mt-1 mb-2 hover:text-emerald-700">
                <a href="news.html">Strategic Agreement Signed with South Korean Water Purifier Innovators</a>
              </h3>
              <p class="text-xs text-gray-600 line-clamp-2">
                Bilateral technology transfer brings smart domestic, commercial, and agricultural water purification plants to Sri Lanka.
              </p>
            </div>
          </article>

          <article class="bg-warmwhite rounded-xl border border-gray-200 overflow-hidden shadow-sm hover:shadow-md transition">
            <img src="https://images.unsplash.com/photo-1509358271058-acd22cc93898?auto=format&fit=crop&w=600&q=80" alt="Mushroom Export Strategy" class="w-full h-44 object-cover">
            <div class="p-5">
              <span class="text-[11px] font-semibold text-gray-500">October 2026 • Global Export</span>
              <h3 class="font-bold text-sm text-forest mt-1 mb-2 hover:text-emerald-700">
                <a href="news.html">5–10 Acre Smart Mushroom Facility Configured for Asian & Middle East Markets</a>
              </h3>
              <p class="text-xs text-gray-600 line-clamp-2">
                Climate-controlled cleanroom chambers optimized for fresh Shiitake, Oyster, and dried gourmet mushroom exports.
              </p>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- Interactive Direct Inquiry CTA -->
    <section class="py-16 bg-warmwhite border-t border-gray-200">
      <div class="max-w-4xl mx-auto px-4 text-center">
        <div class="w-16 h-16 rounded-full bg-emerald-100 text-emerald-800 flex items-center justify-center mx-auto mb-4 text-2xl shadow-inner">
          <i class="fas fa-headset"></i>
        </div>
        <h2 class="text-2xl sm:text-3xl font-black text-forest font-heading mb-2">Speak Directly with Forest Lanka Headquarters</h2>
        <p class="text-xs sm:text-sm text-gray-600 mb-6 max-w-xl mx-auto">
          Need custom egg deliveries, feed distributions, wholesale egg trays, export containers, or investment briefings? Our commercial desks are active.
        </p>
        <div class="flex flex-wrap justify-center gap-4">
          <a href="contact.html" class="btn-primary text-xs py-3 px-6">
            <i class="fas fa-envelope-open-text"></i> Open Inquiry Desk
          </a>
          <a href="https://wa.me/94719740798" target="_blank" class="btn-gold text-xs py-3 px-6">
            <i class="fab fa-whatsapp text-green-700 text-base"></i> WhatsApp Desk (+94 71 974 0798)
          </a>
          <a href="tel:+94706010108" class="btn-secondary text-xs py-3 px-6">
            <i class="fas fa-phone-alt"></i> Call +94 70 601 0108
          </a>
        </div>
      </div>
    </section>
  </main>

  {COMMON_FOOTER}
</body>
</html>
"""

# ================= ABOUT.HTML =================
about_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>About Us | FOREST LANKA Corporate Profile & Strategic Vision</title>
  {COMMON_HEAD}
</head>
<body data-lang="en">
  {get_header('about')}

  <main id="main-content">
    <!-- Breadcrumb & Hero -->
    <div class="bg-forest-dark text-white py-16 relative overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 relative z-10">
        <div class="text-xs text-gold uppercase tracking-wider font-semibold mb-2 flex items-center gap-2">
          <a href="index.html" class="hover:underline">Home</a>
          <i class="fas fa-chevron-right text-[10px]"></i>
          <span>Corporate Overview</span>
        </div>
        <h1 class="text-3xl sm:text-5xl font-black font-heading text-white mb-4">
          <span class="lang-en">About FOREST LANKA</span>
          <span class="lang-si">FOREST LANKA ආයතනය පිළිබඳව</span>
        </h1>
        <p class="text-sm sm:text-base text-emerald-100/90 max-w-3xl leading-relaxed">
          <span class="lang-en">
            Pioneering a sustainable, technology-driven agro-industrial revolution in Sri Lanka through 8 integrated business pillars, South Korean technology partnerships, and ethical zero-waste circular production.
          </span>
          <span class="lang-si">
            වෘත්තීය මට්ටමේ කෘෂිකාර්මික හා කාර්මික නිෂ්පාදන පද්ධතියක් මඟින් දේශීය ආර්ථිකය ශක්තිමත් කරමින් ගෝලීය වෙළෙඳපොළට උසස් තත්ත්වයේ නිෂ්පාදන සැපයීම අපගේ පරමාර්ථයයි.
          </span>
        </p>
      </div>
    </div>

    <!-- Corporate Introduction -->
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          <div class="lg:col-span-7 space-y-5">
            <div class="inline-block px-3 py-1 bg-emerald-100 text-emerald-800 rounded-full text-xs font-bold uppercase tracking-wider">
              Incorporated Enterprise • Reg: 16/2633
            </div>
            <h2 class="text-3xl font-black text-forest font-heading">
              Building Self-Reliance Through Smart Agriculture & Modern Manufacturing
            </h2>
            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed">
              FOREST LANKA was founded with an uncompromising mission: to bridge traditional Sri Lankan agricultural excellence with modern high-yield technology, sustainable circular processing, and international export capabilities.
            </p>
            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed">
              Located at <strong>434, Thalpathwewa, Polpithigama in the Kurunegala district</strong>, our operations are purposefully clustered to allow complete closed-loop manufacturing. From our high-capacity layer poultry houses to our automated animal feed mill, molded pulp recycled paper egg tray plants, climate-controlled indoor mushroom chambers, and our South Korean water purification partnership, every process reinforces the other.
            </p>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-3">
              <div class="border-l-4 border-emerald-600 pl-4 py-1 bg-emerald-50/50 rounded-r-lg">
                <h4 class="font-bold text-sm text-forest">Zero Environmental Waste</h4>
                <p class="text-xs text-gray-600 mt-1">100% of organic animal residues are scientifically processed into bio-organic fertilizer and specialized seedling media.</p>
              </div>
              <div class="border-l-4 border-gold pl-4 py-1 bg-amber-50/50 rounded-r-lg">
                <h4 class="font-bold text-forest text-sm">International Tech Standards</h4>
                <p class="text-xs text-gray-600 mt-1">Incorporating South Korean membrane engineering and automated European environmental telemetry systems.</p>
              </div>
            </div>
          </div>

          <div class="lg:col-span-5">
            <div class="bg-forest-dark p-6 rounded-3xl text-white shadow-2xl border-2 border-gold/40 relative">
              <div class="bg-white p-6 rounded-2xl text-center mb-6">
                <img src="assets/images/logo.jpg" alt="FOREST LANKA Logo" class="max-h-52 mx-auto object-contain">
              </div>

              <div class="space-y-3 text-xs">
                <div class="flex justify-between border-b border-emerald-800 pb-2">
                  <span class="text-emerald-200">Legal Entity:</span>
                  <span class="font-bold text-white">FOREST LANKA</span>
                </div>
                <div class="flex justify-between border-b border-emerald-800 pb-2">
                  <span class="text-emerald-200">Registration Number:</span>
                  <span class="font-bold text-gold">16/2633</span>
                </div>
                <div class="flex justify-between border-b border-emerald-800 pb-2">
                  <span class="text-emerald-200">Headquarters:</span>
                  <span class="font-bold text-white">Polpithigama, Kurunegala</span>
                </div>
                <div class="flex justify-between border-b border-emerald-800 pb-2">
                  <span class="text-emerald-200">Postal Code:</span>
                  <span class="font-bold text-white">60620</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-emerald-200">Core Industries:</span>
                  <span class="font-bold text-emerald-300">8 Strategic Sectors</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Vision, Mission & Core Values -->
    <section class="py-16 bg-warmwhite border-t border-gray-200">
      <div class="max-w-7xl mx-auto px-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
          <!-- Vision -->
          <div class="bg-white p-8 rounded-2xl border border-gray-200 shadow-sm relative overflow-hidden">
            <div class="absolute -right-6 -bottom-6 text-emerald-100 text-8xl font-black select-none pointer-events-none">
              <i class="fas fa-eye"></i>
            </div>
            <div class="w-12 h-12 rounded-xl bg-forest text-gold flex items-center justify-center text-xl mb-4">
              <i class="fas fa-eye"></i>
            </div>
            <h3 class="text-2xl font-bold text-forest mb-3">Our Vision / දැක්ම</h3>
            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed">
              <span class="lang-en">
                To establish FOREST LANKA as Sri Lanka's benchmark smart agro-industrial enterprise, driving national food sovereignty, high-value agricultural manufacturing, and premier export recognition across Asia, the Middle East, and worldwide markets.
              </span>
              <span class="lang-si">
                ශ්‍රී ලංකාවේ ප්‍රමුඛතම තාක්ෂණික කෘෂි-කාර්මික ව්‍යවසාය බවට පත්වෙමින්, උසස් තාක්ෂණය හා පරිසර හිතකාමී ක්‍රමවේද හරහා දේශීය අවශ්‍යතා සපුරා ගෝලීය වෙළෙඳපොළ ජයගැනීම.
              </span>
            </p>
          </div>

          <!-- Mission -->
          <div class="bg-white p-8 rounded-2xl border border-gray-200 shadow-sm relative overflow-hidden">
            <div class="absolute -right-6 -bottom-6 text-emerald-100 text-8xl font-black select-none pointer-events-none">
              <i class="fas fa-bullseye"></i>
            </div>
            <div class="w-12 h-12 rounded-xl bg-emerald-700 text-white flex items-center justify-center text-xl mb-4">
              <i class="fas fa-bullseye"></i>
            </div>
            <h3 class="text-2xl font-bold text-forest mb-3">Our Mission / මෙහෙවර</h3>
            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed">
              <span class="lang-en">
                To harness modern engineering, automated climate systems, and zero-waste circular bio-processing across 8 core sectors, producing superior eggs, livestock feed, biodegradable trays, mushrooms, organic fertilizers, and purified water that uplift our farmers, partners, and consumers.
              </span>
              <span class="lang-si">
                නවීන තාක්ෂණය, තත්ත්ව සහතික, පාරිසරික තිරසාරභාවය සහ ගෝලීය ප්‍රමිතීන් පෙරදැරි කරගනිමින් පාරිභෝගිකයන්ට සහ හවුල්කරුවන්ට අසමසම වටිනාකමක් ලබාදීම.
              </span>
            </p>
          </div>
        </div>

        <!-- 4 Core Strategic Pillars -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <div class="bg-white p-6 rounded-xl border border-gray-200 text-center">
            <div class="w-12 h-12 rounded-full bg-emerald-50 text-emerald-700 flex items-center justify-center text-xl mx-auto mb-3">
              <i class="fas fa-microchip"></i>
            </div>
            <h4 class="font-bold text-sm text-forest mb-2">Smart Technology</h4>
            <p class="text-xs text-gray-600">IoT sensors, computerized ventilation, automated sorting, and South Korean membrane filtration.</p>
          </div>

          <div class="bg-white p-6 rounded-xl border border-gray-200 text-center">
            <div class="w-12 h-12 rounded-full bg-emerald-50 text-emerald-700 flex items-center justify-center text-xl mx-auto mb-3">
              <i class="fas fa-recycle"></i>
            </div>
            <h4 class="font-bold text-sm text-forest mb-2">Circular Sustainability</h4>
            <p class="text-xs text-gray-600">Zero-waste poultry byproduct conversion into bio-fertilizer and 100% recycled paper packaging.</p>
          </div>

          <div class="bg-white p-6 rounded-xl border border-gray-200 text-center">
            <div class="w-12 h-12 rounded-full bg-emerald-50 text-emerald-700 flex items-center justify-center text-xl mx-auto mb-3">
              <i class="fas fa-globe"></i>
            </div>
            <h4 class="font-bold text-sm text-forest mb-2">Global Export Quality</h4>
            <p class="text-xs text-gray-600">ISO and HACCP targeted processing designed for Middle East, Asian, and European distribution.</p>
          </div>

          <div class="bg-white p-6 rounded-xl border border-gray-200 text-center">
            <div class="w-12 h-12 rounded-full bg-emerald-50 text-emerald-700 flex items-center justify-center text-xl mx-auto mb-3">
              <i class="fas fa-handshake"></i>
            </div>
            <h4 class="font-bold text-sm text-forest mb-2">Equitable Partnerships</h4>
            <p class="text-xs text-gray-600">Transparent long-term contracts for wholesalers, retailers, outgrowers, and international investors.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Phased Milestone Roadmap (PDF Section 21 & 24) -->
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4">
        <div class="text-center max-w-2xl mx-auto mb-12">
          <span class="text-xs font-bold uppercase tracking-wider text-emerald-700">Strategic Horizon</span>
          <h2 class="text-3xl font-black text-forest font-heading">Our 4-Phase Scale & Expansion Roadmap</h2>
          <p class="text-xs sm:text-sm text-gray-600 mt-2">Designed to safely scale from foundational capacity to a multi-million-layer national leader.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 relative">
          <!-- Phase 1 -->
          <div class="bg-warmwhite p-6 rounded-2xl border-2 border-emerald-600 relative">
            <div class="badge-status-operational mb-3">Phase 01: Core Launch</div>
            <h4 class="text-base font-bold text-forest mb-2">125,000 Layer Poultry Facility</h4>
            <p class="text-xs text-gray-600 leading-relaxed mb-4">
              Commencing layer hen facility at Polpithigama, launching recycled paper egg tray manufacturing unit, initial bio-fertilizer processing, and digital ordering platform.
            </p>
            <div class="text-[11px] font-bold text-emerald-800 bg-white p-2.5 rounded border border-emerald-200">
              Capacity: 125,000 Hens • Initial 8 Modules
            </div>
          </div>

          <!-- Phase 2 -->
          <div class="bg-warmwhite p-6 rounded-2xl border border-gray-300 relative">
            <div class="badge-status-development mb-3">Phase 02: Expansion</div>
            <h4 class="text-base font-bold text-forest mb-2">5-10 Acre Smart Mushroom Facility</h4>
            <p class="text-xs text-gray-600 leading-relaxed mb-4">
              Scaling layer flock to 500,000 hens, commissioning the 5-10 acre indoor climate-controlled mushroom chambers, and initiating South Korean water purifier assembly line.
            </p>
            <div class="text-[11px] font-bold text-gray-700 bg-white p-2.5 rounded border border-gray-200">
              500K Layers • S. Korean Tech Plant
            </div>
          </div>

          <!-- Phase 3 -->
          <div class="bg-warmwhite p-6 rounded-2xl border border-gray-300 relative">
            <div class="badge-status-planned mb-3">Phase 03: Value-Addition</div>
            <h4 class="text-base font-bold text-forest mb-2">Commercial Egg Powder Mill</h4>
            <p class="text-xs text-gray-600 leading-relaxed mb-4">
              Installation of spray-drying facilities for whole egg powder, yolk powder, and high-whipping albumen. Rollout of islandwide water purification dealership network.
            </p>
            <div class="text-[11px] font-bold text-gray-700 bg-white p-2.5 rounded border border-gray-200">
              Pasteurized Powder • 1M+ Layers
            </div>
          </div>

          <!-- Phase 4 -->
          <div class="bg-warmwhite p-6 rounded-2xl border border-gray-300 relative">
            <div class="badge-status-planned mb-3">Phase 04: Global Giant</div>
            <h4 class="text-base font-bold text-forest mb-2">2,500,000 Layers & Global Ports</h4>
            <p class="text-xs text-gray-600 leading-relaxed mb-4">
              Full realization of the 2.5 million hen multi-facility complex, high-volume automated export logistics, and regional South Asian distribution agreements.
            </p>
            <div class="text-[11px] font-bold text-gold-dark bg-white p-2.5 rounded border border-gold">
              2.5 Million Hens • Regional Export Powerhouse
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Leadership, Governance & Accessibility Commitment (PDF Section 14) -->
    <section class="py-16 bg-warmwhite border-t border-gray-200">
      <div class="max-w-7xl mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          <div class="lg:col-span-6 space-y-4">
            <span class="text-xs font-bold uppercase tracking-wider text-emerald-700">Universal Access & Inclusion</span>
            <h2 class="text-3xl font-black text-forest font-heading">
              WCAG 2.2 Level AAA Accessibility Architecture
            </h2>
            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed">
              In accordance with Section 14 and Section 21 of our foundational technical specification, the FOREST LANKA digital portal is architected to target <strong>WCAG 2.2 Level AAA Accessibility standards</strong>.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs text-gray-700 pt-2">
              <div class="flex items-center gap-2">
                <i class="fas fa-check-circle text-emerald-600"></i>
                <span>7:1 Normal Text Contrast Ratio</span>
              </div>
              <div class="flex items-center gap-2">
                <i class="fas fa-check-circle text-emerald-600"></i>
                <span>Full Keyboard Tab Navigation</span>
              </div>
              <div class="flex items-center gap-2">
                <i class="fas fa-check-circle text-emerald-600"></i>
                <span>Screen Reader & ARIA Attributes</span>
              </div>
              <div class="flex items-center gap-2">
                <i class="fas fa-check-circle text-emerald-600"></i>
                <span>Bilingual Sinhala / English Support</span>
              </div>
            </div>
            <p class="text-xs text-gray-500 italic mt-2">
              We believe agricultural modernization must empower every citizen, worker, and customer, including users with visual, auditory, motor, or cognitive disabilities.
            </p>
          </div>

          <div class="lg:col-span-6 bg-white p-8 rounded-2xl border border-gray-200 shadow-sm">
            <h3 class="text-lg font-bold text-forest mb-4 border-b pb-2">Registered Corporate Information</h3>
            <div class="space-y-3 text-xs text-gray-700">
              <p><strong>Corporate Name:</strong> FOREST LANKA</p>
              <p><strong>Enterprise Tagline:</strong> Growing Agriculture. Building Industries. Connecting Global Markets.</p>
              <p><strong>Business Registration:</strong> 16/2633</p>
              <p><strong>Registered Address:</strong> 434, Thalpathwewa, Polpithigama, Kurunegala, Sri Lanka</p>
              <p><strong>Postal Code:</strong> 60620</p>
              <p><strong>Official Direct Lines:</strong> +94 70 601 0108 / WhatsApp +94 71 974 0798</p>
              <p><strong>Email Address:</strong> thilankaherath7@gmail.com</p>
            </div>
            <div class="mt-6 flex gap-3">
              <a href="contact.html" class="btn-primary text-xs py-2 px-4">Contact Governance</a>
              <a href="investment.html" class="btn-gold text-xs py-2 px-4">Investor Inquiries</a>
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

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)
print("index.html created.")

with open("about.html", "w", encoding="utf-8") as f:
    f.write(about_html)
print("about.html created.")

