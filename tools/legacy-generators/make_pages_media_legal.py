#!/usr/bin/env python3
"""
Generates gallery.html, news.html, contact.html, faq.html, privacy-policy.html,
terms.html, and delivery-returns.html for FOREST LANKA.
"""

from base_templates import COMMON_HEAD, get_header, COMMON_FOOTER

# ================= 1. GALLERY.HTML =================
gallery_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>Photo Gallery & Facility Tour | FOREST LANKA</title>
  {COMMON_HEAD}
</head>
<body data-lang="en">
  {get_header('gallery')}

  <main id="main-content">
    <div class="bg-forest-dark text-white py-16 relative">
      <div class="max-w-7xl mx-auto px-4 relative z-10">
        <div class="text-xs text-gold uppercase tracking-wider font-semibold mb-2 flex items-center gap-2">
          <a href="index.html" class="hover:underline">Home</a>
          <i class="fas fa-chevron-right text-[10px]"></i>
          <span>Media & Infrastructure</span>
        </div>
        <h1 class="text-3xl sm:text-5xl font-black font-heading text-white mb-2">
          <span class="lang-en">Photo Gallery & Facility Tour</span>
          <span class="lang-si">ඡායාරූප සහ පහසුකම් එකතුව</span>
        </h1>
        <p class="text-xs sm:text-base text-emerald-100 max-w-3xl leading-relaxed">
          <span class="lang-en">
            Visual inspection of our modern agricultural complexes, automated feed mills, eco egg tray molding units, IoT mushroom chambers, and Korean water purification technology.
          </span>
          <span class="lang-si">
            FOREST LANKA ආයතනයේ කර්මාන්තශාලා, නිෂ්පාදන ක්‍රියාවලි සහ තාක්ෂණික පහසුකම් පිළිබඳ ඡායාරූප මෙහි දැක්වේ.
          </span>
        </p>
      </div>
    </div>

    <!-- Gallery Categories -->
    <section class="py-6 bg-white border-b border-gray-200 sticky top-[73px] z-30 shadow-xs">
      <div class="max-w-7xl mx-auto px-4">
        <div class="flex flex-wrap gap-2 text-xs">
          <button onclick="filterGallery('all', this)" class="gallery-filter-btn px-3.5 py-1.5 rounded-full font-bold bg-forest text-gold">All Facilities</button>
          <button onclick="filterGallery('poultry', this)" class="gallery-filter-btn px-3.5 py-1.5 rounded-full font-semibold bg-gray-100 text-gray-700 hover:bg-emerald-50">1. Poultry Farm</button>
          <button onclick="filterGallery('feed', this)" class="gallery-filter-btn px-3.5 py-1.5 rounded-full font-semibold bg-gray-100 text-gray-700 hover:bg-emerald-50">2. Animal Feed Mill</button>
          <button onclick="filterGallery('trays', this)" class="gallery-filter-btn px-3.5 py-1.5 rounded-full font-semibold bg-gray-100 text-gray-700 hover:bg-emerald-50">3. Recycled Trays</button>
          <button onclick="filterGallery('mushrooms', this)" class="gallery-filter-btn px-3.5 py-1.5 rounded-full font-semibold bg-gray-100 text-gray-700 hover:bg-emerald-50">4. Mushroom IoT</button>
          <button onclick="filterGallery('powder', this)" class="gallery-filter-btn px-3.5 py-1.5 rounded-full font-semibold bg-gray-100 text-gray-700 hover:bg-emerald-50">5. Egg Processing</button>
          <button onclick="filterGallery('fertilizer', this)" class="gallery-filter-btn px-3.5 py-1.5 rounded-full font-semibold bg-gray-100 text-gray-700 hover:bg-emerald-50">6. Bio-Fertilizer</button>
          <button onclick="filterGallery('media', this)" class="gallery-filter-btn px-3.5 py-1.5 rounded-full font-semibold bg-gray-100 text-gray-700 hover:bg-emerald-50">7. Growing Media</button>
          <button onclick="filterGallery('water', this)" class="gallery-filter-btn px-3.5 py-1.5 rounded-full font-semibold bg-gray-100 text-gray-700 hover:bg-emerald-50">8. Korean Water Tech</button>
        </div>
      </div>
    </section>

    <!-- Gallery Grid -->
    <section class="py-12 bg-warmwhite">
      <div class="max-w-7xl mx-auto px-4">
        <div id="gallery-container" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">

          <!-- 1. Poultry -->
          <div class="gallery-item group relative overflow-hidden rounded-2xl bg-white border border-gray-200 shadow-sm cursor-pointer" data-cat="poultry" onclick="openGalleryModal('https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?auto=format&fit=crop&w=1200&q=80', 'Modern Climate-Controlled Layer Housing (125K Hens Phase 1)')">
            <div class="h-64 overflow-hidden">
              <img src="https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?auto=format&fit=crop&w=600&q=80" alt="Poultry Layer Housing" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            </div>
            <div class="p-4">
              <span class="text-[10px] font-bold text-gold bg-forest px-2 py-0.5 rounded">01. Poultry</span>
              <h4 class="font-bold text-sm text-forest mt-1.5">Automated Multi-Tier Layer Hen Housing</h4>
              <p class="text-xs text-gray-500 mt-1">Computerized ventilation, automatic feed lines, and fresh water nipples.</p>
            </div>
          </div>

          <!-- 2. Egg Grading -->
          <div class="gallery-item group relative overflow-hidden rounded-2xl bg-white border border-gray-200 shadow-sm cursor-pointer" data-cat="poultry" onclick="openGalleryModal('https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=1200&q=80', 'Automated Optical Candling & Electronic Weight Grading')">
            <div class="h-64 overflow-hidden">
              <img src="https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=600&q=80" alt="Egg Grading Facility" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            </div>
            <div class="p-4">
              <span class="text-[10px] font-bold text-gold bg-forest px-2 py-0.5 rounded">01. Poultry</span>
              <h4 class="font-bold text-sm text-forest mt-1.5">Gentle Belt Egg Collection & Candling Center</h4>
              <p class="text-xs text-gray-500 mt-1">Conveyor belt transport directly from nest boxes into hygienic sorting.</p>
            </div>
          </div>

          <!-- 3. Feed Mill -->
          <div class="gallery-item group relative overflow-hidden rounded-2xl bg-white border border-gray-200 shadow-sm cursor-pointer" data-cat="feed" onclick="openGalleryModal('https://images.unsplash.com/photo-1574943320219-553eb213f72d?auto=format&fit=crop&w=1200&q=80', 'Industrial Steam Conditioner & Ring-Die Pelletizing Mill')">
            <div class="h-64 overflow-hidden">
              <img src="https://images.unsplash.com/photo-1574943320219-553eb213f72d?auto=format&fit=crop&w=600&q=80" alt="Feed Mill Facility" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            </div>
            <div class="p-4">
              <span class="text-[10px] font-bold text-gold bg-forest px-2 py-0.5 rounded">02. Feed Mill</span>
              <h4 class="font-bold text-sm text-forest mt-1.5">Automated Steam Pelletizing & Conditioning</h4>
              <p class="text-xs text-gray-500 mt-1">12-step industrial manufacturing facility ensuring precise nutrition.</p>
            </div>
          </div>

          <!-- 4. Egg Trays -->
          <div class="gallery-item group relative overflow-hidden rounded-2xl bg-white border border-gray-200 shadow-sm cursor-pointer" data-cat="trays" onclick="openGalleryModal('https://images.unsplash.com/photo-1506976785307-8732e854ad03?auto=format&fit=crop&w=1200&q=80', 'Rotary Vacuum Molded Pulp Egg Tray Production')">
            <div class="h-64 overflow-hidden">
              <img src="https://images.unsplash.com/photo-1506976785307-8732e854ad03?auto=format&fit=crop&w=600&q=80" alt="Pulp Egg Tray Molding" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            </div>
            <div class="p-4">
              <span class="text-[10px] font-bold text-gold bg-forest px-2 py-0.5 rounded">03. Egg Trays</span>
              <h4 class="font-bold text-sm text-forest mt-1.5">Rotary Vacuum Forming & Tunnel Drying</h4>
              <p class="text-xs text-gray-500 mt-1">Converting recycled paper pulp into shock-proof biodegradable egg trays.</p>
            </div>
          </div>

          <!-- 5. Mushroom Chambers -->
          <div class="gallery-item group relative overflow-hidden rounded-2xl bg-white border border-gray-200 shadow-sm cursor-pointer" data-cat="mushrooms" onclick="openGalleryModal('https://images.unsplash.com/photo-1509358271058-acd22cc93898?auto=format&fit=crop&w=1200&q=80', 'IoT Ultrasonic Fogging & Cleanroom Mushroom Chambers')">
            <div class="h-64 overflow-hidden">
              <img src="https://images.unsplash.com/photo-1509358271058-acd22cc93898?auto=format&fit=crop&w=600&q=80" alt="Mushroom Cultivation" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            </div>
            <div class="p-4">
              <span class="text-[10px] font-bold text-gold bg-forest px-2 py-0.5 rounded">04. Mushrooms</span>
              <h4 class="font-bold text-sm text-forest mt-1.5">5-10 Acre High-Tech Indoor Cleanrooms</h4>
              <p class="text-xs text-gray-500 mt-1">Automated micro-climate sensors regulating Oyster and Shiitake pinning.</p>
            </div>
          </div>

          <!-- 6. Egg Powders -->
          <div class="gallery-item group relative overflow-hidden rounded-2xl bg-white border border-gray-200 shadow-sm cursor-pointer" data-cat="powder" onclick="openGalleryModal('https://images.unsplash.com/photo-1516467508483-a7212febe31a?auto=format&fit=crop&w=1200&q=80', 'Spray Drying Atomization Tower for Egg Powders')">
            <div class="h-64 overflow-hidden">
              <img src="https://images.unsplash.com/photo-1516467508483-a7212febe31a?auto=format&fit=crop&w=600&q=80" alt="Spray Drying Egg Powder" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            </div>
            <div class="p-4">
              <span class="text-[10px] font-bold text-gold bg-forest px-2 py-0.5 rounded">05. Egg Processing</span>
              <h4 class="font-bold text-sm text-forest mt-1.5">Pasteurized Spray-Drying Tower & Lab</h4>
              <p class="text-xs text-gray-500 mt-1">Aseptic dehydration creating whole egg powder and whipping albumen.</p>
            </div>
          </div>

          <!-- 7. Bio Fertilizer -->
          <div class="gallery-item group relative overflow-hidden rounded-2xl bg-white border border-gray-200 shadow-sm cursor-pointer" data-cat="fertilizer" onclick="openGalleryModal('https://images.unsplash.com/photo-1615811361523-6bd03d7748e7?auto=format&fit=crop&w=1200&q=80', 'Aerobic Composting & Thermal Sterilization Windrows')">
            <div class="h-64 overflow-hidden">
              <img src="https://images.unsplash.com/photo-1615811361523-6bd03d7748e7?auto=format&fit=crop&w=600&q=80" alt="Bio Fertilizer Plant" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            </div>
            <div class="p-4">
              <span class="text-[10px] font-bold text-gold bg-forest px-2 py-0.5 rounded">06. Bio-Fertilizer</span>
              <h4 class="font-bold text-sm text-forest mt-1.5">Poultry Manure Composting & Extrusion Plant</h4>
              <p class="text-xs text-gray-600 mt-1">Thermal sterilization producing pathogen-free 4mm organic fertilizer pellets.</p>
            </div>
          </div>

          <!-- 8. Growing Media -->
          <div class="gallery-item group relative overflow-hidden rounded-2xl bg-white border border-gray-200 shadow-sm cursor-pointer" data-cat="media" onclick="openGalleryModal('https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?auto=format&fit=crop&w=1200&q=80', 'Triple-Washing & Buffering Cocopeat Processing')">
            <div class="h-64 overflow-hidden">
              <img src="https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?auto=format&fit=crop&w=600&q=80" alt="Growing Media Substrate" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            </div>
            <div class="p-4">
              <span class="text-[10px] font-bold text-gold bg-forest px-2 py-0.5 rounded">07. Growing Media</span>
              <h4 class="font-bold text-sm text-forest mt-1.5">Low-EC Substrate Buffering & Mixing</h4>
              <p class="text-xs text-gray-500 mt-1">High-porosity seed starting and greenhouse hydroponic potting blends.</p>
            </div>
          </div>

          <!-- 9. Water Technology -->
          <div class="gallery-item group relative overflow-hidden rounded-2xl bg-white border border-gray-200 shadow-sm cursor-pointer" data-cat="water" onclick="openGalleryModal('https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1200&q=80', 'South Korean Membrane Technology Assembly Facility')">
            <div class="h-64 overflow-hidden">
              <img src="https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=600&q=80" alt="Water Purification Lab" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            </div>
            <div class="p-4">
              <span class="text-[10px] font-bold text-white bg-waterblue px-2 py-0.5 rounded">08. Water Tech</span>
              <h4 class="font-bold text-sm text-forest mt-1.5">South Korean Smart IoT Purifier Assembly</h4>
              <p class="text-xs text-gray-500 mt-1">Precision testing of 0.0001-micron RO membranes and IoT telemetry.</p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- Lightbox Modal -->
    <div id="gallery-lightbox-modal" class="modal-backdrop flex items-center justify-center p-4" onclick="closeGalleryModal()">
      <div class="bg-forest-dark p-4 rounded-2xl max-w-4xl w-full text-white relative shadow-2xl" onclick="event.stopPropagation()">
        <button onclick="closeGalleryModal()" class="absolute top-3 right-4 text-gray-300 hover:text-white text-2xl" aria-label="Close lightbox">
          <i class="fas fa-times"></i>
        </button>
        <div class="rounded-xl overflow-hidden mb-3 max-h-[75vh] flex items-center justify-center bg-black">
          <img id="lightbox-img" src="" alt="Enlarged view" class="max-h-[70vh] w-auto object-contain">
        </div>
        <p id="lightbox-caption" class="text-xs sm:text-sm text-emerald-200 font-semibold"></p>
      </div>
    </div>
  </main>

  {COMMON_FOOTER}
</body>
</html>
"""

# ================= 2. NEWS.HTML =================
news_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>News & Announcements | FOREST LANKA Corporate Updates</title>
  {COMMON_HEAD}
</head>
<body data-lang="en">
  {get_header('news')}

  <main id="main-content">
    <div class="bg-forest-dark text-white py-16 relative">
      <div class="max-w-7xl mx-auto px-4 relative z-10">
        <div class="text-xs text-gold uppercase tracking-wider font-semibold mb-2 flex items-center gap-2">
          <a href="index.html" class="hover:underline">Home</a>
          <i class="fas fa-chevron-right text-[10px]"></i>
          <span>Press & Media</span>
        </div>
        <h1 class="text-3xl sm:text-5xl font-black font-heading text-white mb-2">
          <span class="lang-en">News & Corporate Updates</span>
          <span class="lang-si">වතමන් පුවත් සහ නිවේදන</span>
        </h1>
        <p class="text-xs sm:text-base text-emerald-100 max-w-3xl leading-relaxed">
          <span class="lang-en">
            Stay informed with the latest updates on our agricultural facilities, expansion phases, international trade negotiations, and South Korean technological developments.
          </span>
          <span class="lang-si">
            FOREST LANKA ආයතනයේ නවතම ව්‍යාපෘති තත්ත්වයන්, ගිවිසුම් සහ පුවත් මෙහි ප්‍රදර්ශනය කෙරේ.
          </span>
        </p>
      </div>
    </div>

    <!-- News Grid -->
    <section class="py-16 bg-warmwhite">
      <div class="max-w-7xl mx-auto px-4">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">

          <!-- Article 1 -->
          <article class="bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition">
            <div>
              <img src="https://images.unsplash.com/photo-1548550023-2bdb3c5beed7?auto=format&fit=crop&w=700&q=80" alt="Layer Farm Groundbreaking" class="w-full h-52 object-cover">
              <div class="p-6">
                <div class="flex items-center gap-2 text-[11px] text-gray-500 mb-2">
                  <i class="fas fa-calendar-alt text-emerald-700"></i>
                  <span>November 18, 2026</span>
                  <span>•</span>
                  <span class="text-emerald-800 font-semibold">Agro-Industry</span>
                </div>
                <h3 class="text-lg font-bold text-forest font-heading mb-2">
                  Phase 1 Modern Smart Layer Poultry Farm Breaks Ground at Polpithigama
                </h3>
                <p class="text-xs text-gray-600 leading-relaxed mb-4">
                  FOREST LANKA has officially commenced civil construction of the Phase 1 automated layer poultry complex in Polpithigama, Kurunegala. Designed for 125,000 layers in its initial phase, the site features computerized climate regulation, automatic feeding lines, and soft-belt egg collection systems targeting a daily yield of over 110,000 Grade A fresh eggs.
                </p>
              </div>
            </div>
            <div class="px-6 pb-6">
              <span class="text-xs font-bold text-emerald-800 flex items-center gap-1">Status: Operational Construction Active</span>
            </div>
          </article>

          <!-- Article 2 -->
          <article class="bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition">
            <div>
              <img src="https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=700&q=80" alt="Korean Water Tech Partnership" class="w-full h-52 object-cover">
              <div class="p-6">
                <div class="flex items-center gap-2 text-[11px] text-gray-500 mb-2">
                  <i class="fas fa-calendar-alt text-waterblue"></i>
                  <span>November 10, 2026</span>
                  <span>•</span>
                  <span class="text-waterblue font-semibold">Bilateral Tech</span>
                </div>
                <h3 class="text-lg font-bold text-forest font-heading mb-2">
                  Strategic Agreement Finalized with South Korean Water Purifier Innovators
                </h3>
                <p class="text-xs text-gray-600 leading-relaxed mb-4">
                  In a major breakthrough for industrial and residential water safety, FOREST LANKA has finalized a bilateral technology transfer memorandum with South Korean water purification specialists. The partnership authorizes local assembly of smart IoT domestic purifiers, commercial multi-stage RO units, and industrial agricultural treatment plants across Sri Lanka.
                </p>
              </div>
            </div>
            <div class="px-6 pb-6">
              <span class="text-xs font-bold text-waterblue flex items-center gap-1">Status: Licensing & Assembly Stage</span>
            </div>
          </article>

          <!-- Article 3 -->
          <article class="bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition">
            <div>
              <img src="https://images.unsplash.com/photo-1509358271058-acd22cc93898?auto=format&fit=crop&w=700&q=80" alt="Mushroom Export Blueprint" class="w-full h-52 object-cover">
              <div class="p-6">
                <div class="flex items-center gap-2 text-[11px] text-gray-500 mb-2">
                  <i class="fas fa-calendar-alt text-emerald-700"></i>
                  <span>October 28, 2026</span>
                  <span>•</span>
                  <span class="text-emerald-800 font-semibold">Global Export</span>
                </div>
                <h3 class="text-lg font-bold text-forest font-heading mb-2">
                  5–10 Acre High-Density Indoor Mushroom Complex Configured for Middle East
                </h3>
                <p class="text-xs text-gray-600 leading-relaxed mb-4">
                  Engineering blueprints for the 5 to 10-acre smart indoor mushroom facility have been completed. Equipped with positive-pressure HEPA cleanrooms and ultrasonic humidity misting, the plant will produce premium Shiitake, Oyster, and Button mushrooms for immediate air cargo delivery to Dubai, Doha, and regional hospitality markets.
                </p>
              </div>
            </div>
            <div class="px-6 pb-6">
              <span class="text-xs font-bold text-emerald-800 flex items-center gap-1">Status: Detailed Planning Complete</span>
            </div>
          </article>

          <!-- Article 4 -->
          <article class="bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition">
            <div>
              <img src="https://images.unsplash.com/photo-1506976785307-8732e854ad03?auto=format&fit=crop&w=700&q=80" alt="Eco Egg Tray Line" class="w-full h-52 object-cover">
              <div class="p-6">
                <div class="flex items-center gap-2 text-[11px] text-gray-500 mb-2">
                  <i class="fas fa-calendar-alt text-emerald-700"></i>
                  <span>October 15, 2026</span>
                  <span>•</span>
                  <span class="text-emerald-800 font-semibold">Sustainability</span>
                </div>
                <h3 class="text-lg font-bold text-forest font-heading mb-2">
                  Zero-Waste Initiative: 100% Recycled Molded Pulp Egg Tray Line Commences Operations
                </h3>
                <p class="text-xs text-gray-600 leading-relaxed mb-4">
                  The eco-friendly molded fiber tray manufacturing line is running at peak capacity. Utilizing post-consumer newspaper and cardboard, the plant produces 100,000+ biodegradable 30-egg and retail cartons every day, eliminating plastic packaging and providing sustainable shock protection for local poultry farms.
                </p>
              </div>
            </div>
            <div class="px-6 pb-6">
              <span class="text-xs font-bold text-emerald-800 flex items-center gap-1">Status: Operational & Distributing</span>
            </div>
          </article>

          <!-- Article 5 -->
          <article class="bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition">
            <div>
              <img src="https://images.unsplash.com/photo-1615811361523-6bd03d7748e7?auto=format&fit=crop&w=700&q=80" alt="Bio-Fertilizer Launch" class="w-full h-52 object-cover">
              <div class="p-6">
                <div class="flex items-center gap-2 text-[11px] text-gray-500 mb-2">
                  <i class="fas fa-calendar-alt text-emerald-700"></i>
                  <span>October 02, 2026</span>
                  <span>•</span>
                  <span class="text-emerald-800 font-semibold">Circular Economy</span>
                </div>
                <h3 class="text-lg font-bold text-forest font-heading mb-2">
                  Bio-Organic Fertilizer Conversion Plant Supplies First 500 Tons to Regional Estates
                </h3>
                <p class="text-xs text-gray-600 leading-relaxed mb-4">
                  Demonstrating complete circular agriculture, Forest Lanka's bio-fertilizer facility has successfully transformed organic poultry manure into certified odorless 4mm pellets. The initial batch of 500 tons has been dispatched to coconut and vegetable growers with verified soil microbial rejuvenation results.
                </p>
              </div>
            </div>
            <div class="px-6 pb-6">
              <span class="text-xs font-bold text-emerald-800 flex items-center gap-1">Status: Regular Commercial Output</span>
            </div>
          </article>

          <!-- Article 6 -->
          <article class="bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm flex flex-col justify-between hover:shadow-md transition">
            <div>
              <img src="https://images.unsplash.com/photo-1516467508483-a7212febe31a?auto=format&fit=crop&w=700&q=80" alt="Digital Portal Rollout" class="w-full h-52 object-cover">
              <div class="p-6">
                <div class="flex items-center gap-2 text-[11px] text-gray-500 mb-2">
                  <i class="fas fa-calendar-alt text-gold"></i>
                  <span>September 20, 2026</span>
                  <span>•</span>
                  <span class="text-emerald-800 font-semibold">Digital Platform</span>
                </div>
                <h3 class="text-lg font-bold text-forest font-heading mb-2">
                  FOREST LANKA Complete Dynamic Trade Portal & E-Commerce Platform Rolled Out
                </h3>
                <p class="text-xs text-gray-600 leading-relaxed mb-4">
                  Developed in collaboration with ISD Tech Hub (Pvt) Ltd under proposal ISD/FL/2026/108, the state-of-the-art web platform unites digital product catalogs, live inquiry carts, B2B quotation workflows, export portals, and bilingual accessibility for seamless customer engagement worldwide.
                </p>
              </div>
            </div>
            <div class="px-6 pb-6">
              <span class="text-xs font-bold text-emerald-800 flex items-center gap-1">Status: Live Platform Active</span>
            </div>
          </article>

        </div>
      </div>
    </section>
  </main>

  {COMMON_FOOTER}
</body>
</html>
"""

# ================= 3. CONTACT.HTML (PDF SECTION 19) =================
contact_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>Contact Us & Official Inquiries | FOREST LANKA Headquarters</title>
  {COMMON_HEAD}
</head>
<body data-lang="en">
  {get_header('contact')}

  <main id="main-content">
    <div class="bg-forest-dark text-white py-16 relative">
      <div class="max-w-7xl mx-auto px-4 relative z-10">
        <div class="text-xs text-gold uppercase tracking-wider font-semibold mb-2 flex items-center gap-2">
          <a href="index.html" class="hover:underline">Home</a>
          <i class="fas fa-chevron-right text-[10px]"></i>
          <span>Official Inquiries</span>
        </div>
        <h1 class="text-3xl sm:text-5xl font-black font-heading text-white mb-2">
          <span class="lang-en">Contact Us & Inquiry Desk</span>
          <span class="lang-si">සම්බන්ධතා සහ විමසීම් කළමනාකරණය</span>
        </h1>
        <p class="text-xs sm:text-base text-emerald-100 max-w-3xl leading-relaxed">
          <span class="lang-en">
            Reach out to our executive headquarters, industrial production managers, and trade desks in Polpithigama, Kurunegala. We respond to all inquiries within 24 business hours.
          </span>
          <span class="lang-si">
            FOREST LANKA ආයතනය සමඟ සම්බන්ධ වීමට සහ සියලු ව්‍යාපාරික විමසීම් සඳහා පහත තොරතුරු හා පෝරමය භාවිත කරන්න.
          </span>
        </p>
      </div>
    </div>

    <!-- Official Contact Details & Dynamic Form (PDF Section 19) -->
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">

          <!-- Left Info Cards -->
          <div class="lg:col-span-5 space-y-6">
            <div class="bg-warmwhite p-6 sm:p-8 rounded-3xl border border-gray-200 shadow-sm">
              <span class="text-xs font-bold uppercase tracking-wider text-emerald-700 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-200">
                Official Registered Office
              </span>
              <h2 class="text-2xl font-bold text-forest font-heading mt-3 mb-4">FOREST LANKA Headquarters</h2>

              <div class="space-y-4 text-xs text-gray-700">
                <div class="flex items-start gap-3">
                  <div class="w-9 h-9 rounded-full bg-emerald-100 text-emerald-800 flex items-center justify-center shrink-0 text-base mt-0.5">
                    <i class="fas fa-certificate text-gold"></i>
                  </div>
                  <div>
                    <strong>Registration Number (ලි.ප. අංකය):</strong>
                    <div class="text-sm font-bold text-forest mt-0.5 font-mono">16/2633</div>
                  </div>
                </div>

                <div class="flex items-start gap-3">
                  <div class="w-9 h-9 rounded-full bg-emerald-100 text-emerald-800 flex items-center justify-center shrink-0 text-base mt-0.5">
                    <i class="fas fa-map-location-dot"></i>
                  </div>
                  <div>
                    <strong>Registered Address (ලිපිනය):</strong>
                    <div class="text-xs text-gray-600 mt-0.5 leading-relaxed">
                      434, Thalpathwewa, Polpithigama,<br>
                      Kurunegala District, North Western Province, Sri Lanka.
                    </div>
                    <div class="text-[11px] font-bold text-emerald-800 mt-1">Postal Code: 60620</div>
                  </div>
                </div>

                <div class="flex items-start gap-3">
                  <div class="w-9 h-9 rounded-full bg-emerald-100 text-emerald-800 flex items-center justify-center shrink-0 text-base mt-0.5">
                    <i class="fas fa-phone-volume"></i>
                  </div>
                  <div>
                    <strong>Direct Office Telephone:</strong>
                    <div class="text-sm font-bold text-forest mt-0.5 font-mono">
                      <a href="tel:+94706010108" class="hover:text-emerald-700">+94 70 601 0108</a>
                    </div>
                  </div>
                </div>

                <div class="flex items-start gap-3">
                  <div class="w-9 h-9 rounded-full bg-green-100 text-green-700 flex items-center justify-center shrink-0 text-base mt-0.5">
                    <i class="fab fa-whatsapp"></i>
                  </div>
                  <div>
                    <strong>WhatsApp Direct Operations Desk:</strong>
                    <div class="text-sm font-bold text-green-800 mt-0.5 font-mono">
                      <a href="https://wa.me/94719740798" target="_blank" class="hover:underline">+94 71 974 0798</a>
                    </div>
                  </div>
                </div>

                <div class="flex items-start gap-3">
                  <div class="w-9 h-9 rounded-full bg-emerald-100 text-emerald-800 flex items-center justify-center shrink-0 text-base mt-0.5">
                    <i class="fas fa-envelope-open-text"></i>
                  </div>
                  <div>
                    <strong>Official Corporate Email:</strong>
                    <div class="text-xs font-bold text-forest mt-0.5 font-mono">
                      <a href="mailto:thilankaherath7@gmail.com" class="hover:text-emerald-700">thilankaherath7@gmail.com</a>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Quick Action Box -->
              <div class="mt-6 pt-5 border-t border-gray-200">
                <a href="https://wa.me/94719740798?text=Hello%20Forest%20Lanka,%20I%20am%20contacting%20you%20regarding%20business%20inquiries." target="_blank" class="btn-gold text-xs w-full py-2.5 flex items-center justify-center gap-2">
                  <i class="fab fa-whatsapp text-green-700 text-base"></i>
                  <span>Message Us Directly on WhatsApp</span>
                </a>
              </div>
            </div>

            <!-- Map Placeholder / Embed -->
            <div class="bg-warmwhite p-4 rounded-3xl border border-gray-200 overflow-hidden shadow-sm">
              <h3 class="text-xs font-bold text-forest uppercase tracking-wider mb-2">Location Map (Polpithigama, Kurunegala)</h3>
              <div class="w-full h-48 bg-emerald-950 rounded-2xl flex flex-col items-center justify-center text-emerald-200 text-center p-4 relative overflow-hidden">
                <i class="fas fa-map-marked-alt text-4xl text-gold mb-2"></i>
                <div class="font-bold text-xs text-white">FOREST LANKA Agro-Industrial Base</div>
                <div class="text-[11px] text-emerald-300">434, Thalpathwewa, Polpithigama, Sri Lanka</div>
                <a href="https://maps.google.com/?q=Polpithigama,Kurunegala,Sri+Lanka" target="_blank" class="mt-3 text-[11px] bg-gold text-forest font-bold px-3 py-1 rounded-full hover:bg-white transition">
                  <i class="fas fa-external-link-alt mr-1"></i> Open in Google Maps
                </a>
              </div>
            </div>
          </div>

          <!-- Right Dynamic Inquiry Form (PDF Section 19 & Page 24) -->
          <div class="lg:col-span-7">
            <div class="bg-forest-dark text-white p-8 sm:p-10 rounded-3xl border-2 border-gold/40 shadow-2xl">
              <div class="border-b border-emerald-800 pb-4 mb-6">
                <h3 class="text-2xl font-black font-heading text-white">Dynamic Inquiry Form (විමසීම් පෝරමය)</h3>
                <p class="text-xs text-emerald-200 mt-1">Please specify your requirements below. All submissions are logged directly into our central commercial registry.</p>
              </div>

              <form class="dynamic-inquiry-form space-y-4">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label class="block text-xs font-semibold text-emerald-200 mb-1">Your Full Name / නම *</label>
                    <input type="text" required placeholder="Mr. / Ms. Full Name" class="w-full text-xs p-3 rounded-lg bg-white text-charcoal border focus:ring-1 focus:ring-gold">
                  </div>
                  <div>
                    <label class="block text-xs font-semibold text-emerald-200 mb-1">Company / Farm / ආයතනය</label>
                    <input type="text" placeholder="Company or farm name" class="w-full text-xs p-3 rounded-lg bg-white text-charcoal border focus:ring-1 focus:ring-gold">
                  </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label class="block text-xs font-semibold text-emerald-200 mb-1">Country / රට *</label>
                    <input type="text" required placeholder="Sri Lanka / Other Country" class="w-full text-xs p-3 rounded-lg bg-white text-charcoal border focus:ring-1 focus:ring-gold">
                  </div>
                  <div>
                    <label class="block text-xs font-semibold text-emerald-200 mb-1">Email Address / ඊමේල් *</label>
                    <input type="email" required placeholder="name@domain.com" class="w-full text-xs p-3 rounded-lg bg-white text-charcoal border focus:ring-1 focus:ring-gold">
                  </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label class="block text-xs font-semibold text-emerald-200 mb-1">Telephone Number / දුරකථන අංකය *</label>
                    <input type="tel" required placeholder="+94 7X XXX XXXX" class="w-full text-xs p-3 rounded-lg bg-white text-charcoal border focus:ring-1 focus:ring-gold">
                  </div>
                  <div>
                    <label class="block text-xs font-semibold text-emerald-200 mb-1">Inquiry Type / විමසීම් වර්ගය *</label>
                    <select required class="w-full text-xs p-3 rounded-lg bg-white text-charcoal border focus:ring-1 focus:ring-gold">
                      <option value="">Select Inquiry Classification</option>
                      <option value="retail_order">Retail Product Order</option>
                      <option value="wholesale_quote">Wholesale Commercial Quotation</option>
                      <option value="hotel_supermarket">Supermarket / Hotel Supply Contract</option>
                      <option value="export_inquiry">Global Export / Foreign Trade Inquiry</option>
                      <option value="investment_eoi">Investment & Capital Partnership</option>
                      <option value="partner_registration">Business Partner Registration</option>
                      <option value="other">General Corporate Inquiry</option>
                    </select>
                  </div>
                </div>

                <div>
                  <label class="block text-xs font-semibold text-emerald-200 mb-1">Interested Product or Industry / අදාළ අංශය *</label>
                  <select required class="w-full text-xs p-3 rounded-lg bg-white text-charcoal border focus:ring-1 focus:ring-gold">
                    <option value="">Select Core Industry</option>
                    <option value="ind_poultry">01. Modern Smart Layer Poultry Farm (Fresh Eggs)</option>
                    <option value="ind_feed">02. Animal Feed Manufacturing (Layer, Cattle, Fish Feed)</option>
                    <option value="ind_trays">03. Recycled Paper Egg Tray Manufacturing</option>
                    <option value="ind_mushrooms">04. Smart Mushroom Farming & Export (Shiitake, Oyster)</option>
                    <option value="ind_powder">05. Egg Processing & Powders (Whole Egg, Albumen)</option>
                    <option value="ind_fertilizer">06. Organic Fertilizer Manufacturing (Pelleted Bio-Fertilizer)</option>
                    <option value="ind_media">07. Growing Media & Planting Substrates</option>
                    <option value="ind_water">08. Korean Smart Water Purifiers & Industrial RO</option>
                  </select>
                </div>

                <div>
                  <label class="block text-xs font-semibold text-emerald-200 mb-1">Message / Requirements / පණිවිඩය *</label>
                  <textarea rows="4" required placeholder="Please provide specific details such as target quantities, delivery timeframe, destination or custom requirements..." class="w-full text-xs p-3 rounded-lg bg-white text-charcoal border focus:ring-1 focus:ring-gold"></textarea>
                </div>

                <div class="pt-2">
                  <button type="submit" class="btn-gold text-xs w-full py-3.5 text-sm">
                    <i class="fas fa-paper-plane mr-1"></i> Send Official Inquiry
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

# ================= 4. FAQ.HTML =================
faq_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>Frequently Asked Questions | FOREST LANKA Knowledge Base</title>
  {COMMON_HEAD}
</head>
<body data-lang="en">
  {get_header('faq')}

  <main id="main-content">
    <div class="bg-forest-dark text-white py-16 relative">
      <div class="max-w-7xl mx-auto px-4 relative z-10">
        <div class="text-xs text-gold uppercase tracking-wider font-semibold mb-2 flex items-center gap-2">
          <a href="index.html" class="hover:underline">Home</a>
          <i class="fas fa-chevron-right text-[10px]"></i>
          <span>Support & FAQs</span>
        </div>
        <h1 class="text-3xl sm:text-5xl font-black font-heading text-white mb-2">
          <span class="lang-en">Frequently Asked Questions (FAQ)</span>
          <span class="lang-si">නිතර අසන ප්‍රශ්න සහ පිළිතුරු</span>
        </h1>
        <p class="text-xs sm:text-base text-emerald-100 max-w-3xl leading-relaxed">
          <span class="lang-en">
            Clear, transparent answers to commercial ordering, wholesale supply, international export logistics, fertilizer application, and technology partnership queries.
          </span>
          <span class="lang-si">
            FOREST LANKA ආයතනයේ සේවාවන්, නිෂ්පාදන සහ ගිවිසුම් පිළිබඳ නිතර අසන ගැටලු සඳහා පිළිතුරු.
          </span>
        </p>
      </div>
    </div>

    <!-- FAQ Accordion List -->
    <section class="py-16 bg-warmwhite">
      <div class="max-w-4xl mx-auto px-4 space-y-4">

        <div class="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm">
          <h3 class="text-base font-bold text-forest mb-2 flex items-center gap-2">
            <i class="fas fa-question-circle text-gold"></i>
            How do I purchase fresh table eggs in wholesale volumes for supermarkets or hotels?
          </h3>
          <p class="text-xs text-gray-700 leading-relaxed">
            You can add products directly to our Inquiry Cart on the website and submit a wholesale request, or visit our <a href="partners.html" class="text-emerald-800 font-bold hover:underline">Business Partner Registration page</a>. We provide scheduled weekly or daily cold-chain deliveries in 30-egg trays and 360-egg master crates with customized barcoding for supermarket distribution.
          </p>
        </div>

        <div class="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm">
          <h3 class="text-base font-bold text-forest mb-2 flex items-center gap-2">
            <i class="fas fa-question-circle text-gold"></i>
            What is the delivery radius and turnaround time for poultry feed and bio-fertilizer?
          </h3>
          <p class="text-xs text-gray-700 leading-relaxed">
            We deliver islandwide across Sri Lanka. For standard commercial feed bags (25kg and 50kg) and bio-fertilizer, deliveries in the North Western, Western, and Central provinces are executed within 24 to 48 hours. Estate orders exceeding 5 tons are scheduled via our dedicated logistics fleet directly to your estate warehouse.
          </p>
        </div>

        <div class="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm">
          <h3 class="text-base font-bold text-forest mb-2 flex items-center gap-2">
            <i class="fas fa-question-circle text-gold"></i>
            Are the recycled paper egg trays safe for food contact and moisture resistant?
          </h3>
          <p class="text-xs text-gray-700 leading-relaxed">
            Yes. Our egg trays are manufactured using an 8-step hydraulic hydrapulping process utilizing clean post-consumer paper cured in high-temperature hot-air tunnels. The resulting molded fiber is chemically inert, non-toxic, highly breathable, shock-absorbing, and naturally biodegradable within 90 days in compost.
          </p>
        </div>

        <div class="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm">
          <h3 class="text-base font-bold text-forest mb-2 flex items-center gap-2">
            <i class="fas fa-question-circle text-gold"></i>
            Can foreign importers request product samples for dehydrated mushrooms and egg powders?
          </h3>
          <p class="text-xs text-gray-700 leading-relaxed">
            Yes. Through our <a href="export.html" class="text-emerald-800 font-bold hover:underline">Global Export Portal</a>, international food companies and distributors can check "Request Product Lab Sample". Upon corporate verification, our export desk dispatches samples via express air courier along with laboratory certificates of analysis (COA).
          </p>
        </div>

        <div class="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm">
          <h3 class="text-base font-bold text-forest mb-2 flex items-center gap-2">
            <i class="fas fa-question-circle text-gold"></i>
            What are the advantages of Whole Egg Powder over fresh eggs for bakeries?
          </h3>
          <p class="text-xs text-gray-700 leading-relaxed">
            Whole Egg Powder has a 24-month ambient shelf life without refrigeration, eliminates shell breakage losses, guarantees microbiological freedom from Salmonella, saves massive cold-storage space, and simplifies baking batch measurement (1kg powder + 3kg water reconstitutes into 4kg fresh egg liquid).
          </p>
        </div>

        <div class="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm">
          <h3 class="text-base font-bold text-forest mb-2 flex items-center gap-2">
            <i class="fas fa-question-circle text-gold"></i>
            How does the South Korean Smart Water Purifier dealership opportunity work?
          </h3>
          <p class="text-xs text-gray-700 leading-relaxed">
            As authorized technology partners, we offer exclusive district dealership rights across Sri Lanka for sales, installation, and replacement cartridges. Dealers receive comprehensive technical training, stock credits, marketing collateral, and full replacement warranty support.
          </p>
        </div>

        <div class="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm">
          <h3 class="text-base font-bold text-forest mb-2 flex items-center gap-2">
            <i class="fas fa-question-circle text-gold"></i>
            What payment methods are supported for online and wholesale purchases?
          </h3>
          <p class="text-xs text-gray-700 leading-relaxed">
            We support PayHere card payments (Visa, MasterCard), Direct Bank Transfer, Cash on Delivery (for retail and regional egg deliveries), and formal B2B invoicing with commercial credit terms for accredited corporate partners. International orders are handled via Irrevocable Letters of Credit (L/C) or T/T Wire Transfer.
          </p>
        </div>

      </div>
    </section>
  </main>

  {COMMON_FOOTER}
</body>
</html>
"""

# ================= 5. PRIVACY-POLICY.HTML (PDF SECTION 17) =================
privacy_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>Privacy Policy & Data Protection | FOREST LANKA</title>
  {COMMON_HEAD}
</head>
<body data-lang="en">
  {get_header('privacy')}

  <main id="main-content">
    <div class="bg-forest-dark text-white py-16 relative">
      <div class="max-w-7xl mx-auto px-4 relative z-10">
        <h1 class="text-3xl sm:text-5xl font-black font-heading text-white mb-2">Privacy & Data Protection Policy</h1>
        <p class="text-xs sm:text-base text-emerald-100 max-w-3xl leading-relaxed">
          In strict compliance with Section 17 of our operational standards, FOREST LANKA ensures rigorous cyber security and data protection for all customers, outgrowers, and commercial partners.
        </p>
      </div>
    </div>

    <section class="py-16 bg-white">
      <div class="max-w-4xl mx-auto px-4 text-xs sm:text-sm text-gray-700 leading-relaxed space-y-6">
        <div>
          <h2 class="text-xl font-bold text-forest font-heading mb-2">1. Scope & Commitment</h2>
          <p>FOREST LANKA (Reg: 16/2633) is dedicated to maintaining the highest ethical and technical standards when handling commercial, personal, and transactional data. This policy outlines how information gathered through our web platform is gathered, used, and protected.</p>
        </div>

        <div>
          <h2 class="text-xl font-bold text-forest font-heading mb-2">2. Cyber Security Architecture (Section 17)</h2>
          <p>Our platform incorporates multi-tiered security defenses as stipulated in Section 17 of our foundational specification:</p>
          <ul class="list-disc pl-5 mt-2 space-y-1">
            <li>End-to-end HTTPS 256-bit SSL encryption across all browsing and transactional endpoints.</li>
            <li>Role-Based Access Control (RBAC) ensuring only authorized administrative personnel can access partner profiles.</li>
            <li>Server-side input validation and SQL injection framework protections.</li>
            <li>Automated CSRF protection and secure session management.</li>
            <li>Zero storage of sensitive payment card details; all financial authorizations are handled via PCI-DSS compliant payment gateways.</li>
          </ul>
        </div>

        <div>
          <h2 class="text-xl font-bold text-forest font-heading mb-2">3. Information Collected</h2>
          <p>We only collect data necessary to fulfill commercial transactions and verify partnership accreditations, including contact names, company registrations, phone numbers, delivery addresses, and product volume specifications.</p>
        </div>

        <div>
          <h2 class="text-xl font-bold text-forest font-heading mb-2">4. Contact Governance</h2>
          <p>For data inquiries or deletion requests, contact our Data Protection Officer at: <strong>thilankaherath7@gmail.com</strong> or write to FOREST LANKA, 434, Thalpathwewa, Polpithigama, Kurunegala, Sri Lanka.</p>
        </div>
      </div>
    </section>
  </main>

  {COMMON_FOOTER}
</body>
</html>
"""

# ================= 6. TERMS.HTML (PDF SECTION 29) =================
terms_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>Terms & Conditions | FOREST LANKA</title>
  {COMMON_HEAD}
</head>
<body data-lang="en">
  {get_header('terms')}

  <main id="main-content">
    <div class="bg-forest-dark text-white py-16 relative">
      <div class="max-w-7xl mx-auto px-4 relative z-10">
        <h1 class="text-3xl sm:text-5xl font-black font-heading text-white mb-2">Terms and Conditions</h1>
        <p class="text-xs sm:text-base text-emerald-100 max-w-3xl leading-relaxed">
          Standard commercial and contractual terms governing web transactions, quotation requests, and partnership engagements (PDF Section 29).
        </p>
      </div>
    </div>

    <section class="py-16 bg-white">
      <div class="max-w-4xl mx-auto px-4 text-xs sm:text-sm text-gray-700 leading-relaxed space-y-6">
        <div>
          <h2 class="text-xl font-bold text-forest font-heading mb-2">1. General Overview (පොදු ගිවිසුම් කොන්දේසි)</h2>
          <p>These terms govern all transactions, inquiries, and commercial partnerships initiated through the FOREST LANKA digital portal. By placing an order or registering as a partner, you agree to these binding provisions.</p>
        </div>

        <div>
          <h2 class="text-xl font-bold text-forest font-heading mb-2">2. Quotation Requests & Price Validity</h2>
          <p>Quotation estimates provided for bulk agricultural produce (fresh eggs, animal feeds, egg trays, and gourmet mushrooms) remain valid for 14 calendar days from issuance due to fluctuating raw material and freight indices. Official contract execution requires mutual written confirmation.</p>
        </div>

        <div>
          <h2 class="text-xl font-bold text-forest font-heading mb-2">3. Product Specifications & Tolerances</h2>
          <p>All agricultural products conform to declared national standards (SLS) and industry grading conventions. Weight grading tolerances for fresh eggs and moisture tolerances for pelleted animal feeds conform to agreed certified laboratory parameters.</p>
        </div>

        <div>
          <h2 class="text-xl font-bold text-forest font-heading mb-2">4. Warranties & Technical Support (Section 27)</h2>
          <p>Industrial machinery and South Korean water purification units carry a standard 30-day bug-fix and commissioning warranty from formal delivery, followed by optional extended annual maintenance agreements (AMC).</p>
        </div>

        <div>
          <h2 class="text-xl font-bold text-forest font-heading mb-2">5. Governing Law & Jurisdiction</h2>
          <p>All contracts and commercial disputes are subject to the exclusive jurisdiction of the Courts of Sri Lanka.</p>
        </div>
      </div>
    </section>
  </main>

  {COMMON_FOOTER}
</body>
</html>
"""

# ================= 7. DELIVERY-RETURNS.HTML (PDF SECTION 10.2 & 27) =================
delivery_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>Delivery & Returns Policy | FOREST LANKA</title>
  {COMMON_HEAD}
</head>
<body data-lang="en">
  {get_header('delivery')}

  <main id="main-content">
    <div class="bg-forest-dark text-white py-16 relative">
      <div class="max-w-7xl mx-auto px-4 relative z-10">
        <h1 class="text-3xl sm:text-5xl font-black font-heading text-white mb-2">Delivery & Return Policy</h1>
        <p class="text-xs sm:text-base text-emerald-100 max-w-3xl leading-relaxed">
          Logistics protocols, shipping schedules, temperature control, and return inspection guidelines across all 8 commercial industries.
        </p>
      </div>
    </div>

    <section class="py-16 bg-white">
      <div class="max-w-4xl mx-auto px-4 text-xs sm:text-sm text-gray-700 leading-relaxed space-y-6">
        <div>
          <h2 class="text-xl font-bold text-forest font-heading mb-2">1. Delivery Schedules & Logistics Fleet</h2>
          <p>FOREST LANKA maintains a dedicated distribution fleet and partners with certified freight providers. Domestic deliveries are categorized into:</p>
          <ul class="list-disc pl-5 mt-2 space-y-1">
            <li><strong>Perishable Goods (Fresh Eggs & Mushrooms):</strong> Transported via climate-controlled vans within 24 to 48 hours of harvest.</li>
            <li><strong>Dry Bulk Goods (Animal Feeds & Egg Trays):</strong> Scheduled dispatch within 2 to 4 business days of order confirmation.</li>
            <li><strong>Machinery & Water Systems:</strong> Pre-scheduled delivery with dedicated installation technician teams.</li>
          </ul>
        </div>

        <div>
          <h2 class="text-xl font-bold text-forest font-heading mb-2">2. Delivery Charges (Section 10.2)</h2>
          <p>Local retail delivery rates are calculated dynamically based on distance and order weight. Wholesale deliveries exceeding minimum contract volumes receive subsidized or complimentary delivery to regional hub centers.</p>
        </div>

        <div>
          <h2 class="text-xl font-bold text-forest font-heading mb-2">3. Inspection upon Delivery</h2>
          <p>Customers and receiving logistics personnel must inspect packages upon arrival. Any breakage, moisture ingress, or shortage in egg crates or feed bags must be endorsed on the delivery dispatch note immediately.</p>
        </div>

        <div>
          <h2 class="text-xl font-bold text-forest font-heading mb-2">4. Claims & Replacements (Section 27)</h2>
          <p>In the event of verified transit damage or quality deviations, FOREST LANKA provides free replacement stock on the subsequent delivery run or applies an immediate credit note to the client account.</p>
        </div>
      </div>
    </section>
  </main>

  {COMMON_FOOTER}
</body>
</html>
"""

with open("gallery.html", "w", encoding="utf-8") as f:
    f.write(gallery_html)
print("gallery.html created.")

with open("news.html", "w", encoding="utf-8") as f:
    f.write(news_html)
print("news.html created.")

with open("contact.html", "w", encoding="utf-8") as f:
    f.write(contact_html)
print("contact.html created.")

with open("faq.html", "w", encoding="utf-8") as f:
    f.write(faq_html)
print("faq.html created.")

with open("privacy-policy.html", "w", encoding="utf-8") as f:
    f.write(privacy_html)
print("privacy-policy.html created.")

with open("terms.html", "w", encoding="utf-8") as f:
    f.write(terms_html)
print("terms.html created.")

with open("delivery-returns.html", "w", encoding="utf-8") as f:
    f.write(delivery_html)
print("delivery-returns.html created.")

