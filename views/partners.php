<main id="main-content">
    <div class="bg-forest-dark text-white py-16 relative page-intro page-intro--visual">
      <div class="page-intro-layout max-w-7xl mx-auto px-4 relative z-10"><div class="page-intro-copy">
        <div class="text-xs text-gold uppercase tracking-wider font-semibold mb-2 flex items-center gap-2">
          <a href="index.php" class="hover:underline">Home</a>
          <i class="fas fa-chevron-right text-2xs"></i>
          <span>Partner Network</span>
        </div>
        <h1>
          <span>Become Our Business Partner</span>
          
        </h1>
        <p class="text-base sm:text-base text-emerald-100 max-w-3xl leading-relaxed">
          <span>
            FOREST LANKA actively collaborates with wholesale dealers, supermarket retail chains, hotel suppliers, exporters, outgrowers, distribution fleets, and technological partners across Sri Lanka and globally.
          </span>
          
        </p>
      </div><?php require APP_ROOT . "/includes/page-intro-visual.php"; ?></div>
    </div>

    
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4">
        <div class="text-center max-w-3xl mx-auto mb-12">
          <span class="text-xs font-bold uppercase tracking-wider text-emerald-700">Collaboration Matrix</span>
          <h2 class="text-3xl font-black text-forest font-heading">10 Eligible Business Partner Categories</h2>
          <p class="text-base sm:text-sm text-gray-600 mt-2">
            Select your category to access preferential corporate pricing, priority factory allocations, and direct marketing support.
          </p>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-4 mb-16 text-center text-xs">
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-warehouse text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">1. Wholesalers</div>
          </div>
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-store text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">2. Retailers</div>
          </div>
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-cart-shopping text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">3. Supermarkets</div>
          </div>
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-hotel text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">4. Hotels & Restaurants</div>
          </div>
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-ship text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">5. Exporters</div>
          </div>
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-plane-arrival text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">6. Importers</div>
          </div>
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-user-tie text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">7. Sales Agents</div>
          </div>
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-truck-fast text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">8. Distributors</div>
          </div>
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-coins text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">9. Investors</div>
          </div>
          <div class="p-4 bg-warmwhite rounded-xl border border-gray-200 hover:border-emerald-700 transition">
            <i class="fas fa-microchip text-2xl text-emerald-800 mb-2"></i>
            <div class="font-bold text-forest">10. Tech Partners</div>
          </div>
        </div>

        
        <div class="max-w-4xl mx-auto bg-warmwhite p-8 sm:p-10 rounded-3xl border border-gray-200 shadow-lg">
          <div class="text-center mb-8 border-b pb-4">
            <h3 class="text-2xl font-bold text-forest font-heading">Partner Registration Application</h3>
            <p class="text-base text-gray-600 mt-1">Complete the verified fields below to initiate commercial agreement accreditation.</p>
          </div>

          <form id="partner-registration-form" class="space-y-4" method="post" action="api/inquiries.php" data-inquiry="partner">
<?php form_security("partner"); ?>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label for="partner-name" class="block text-xs font-semibold text-gray-700 mb-1">Representative Full Name *</label>
                <input type="text" required placeholder="Authorized contact person" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="name" id="partner-name" maxlength="180" autocomplete="name">
              </div>
              <div>
                <label for="partner-company" class="block text-xs font-semibold text-gray-700 mb-1">Business Name *</label>
                <input type="text" required placeholder="Registered business entity" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="company" id="partner-company" maxlength="180" autocomplete="organization">
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label for="partner-partner_type" class="block text-xs font-semibold text-gray-700 mb-1">Business Category *</label>
                <select required class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="partner_type" id="partner-partner_type">
                  <option value="">Select Category</option>
                  <option value="wholesale">Wholesale Trader</option>
                  <option value="retail">Retailer / Supermarket</option>
                  <option value="hospitality">Hotel / Restaurant / Baker</option>
                  <option value="export_import">Exporter / Importer</option>
                  <option value="sales_agent">Regional Sales Agent</option>
                  <option value="distributor">Logistics & Distribution</option>
                  <option value="tech_partner">Technology Partner</option>
                </select>
              </div>
              <div>
                <label for="partner-country" class="block text-xs font-semibold text-gray-700 mb-1">Country & District / Region *</label>
                <input type="text" required placeholder="e.g. Sri Lanka, Kurunegala / Colombo" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="country" id="partner-country" maxlength="180" autocomplete="country-name">
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label for="partner-email" class="block text-xs font-semibold text-gray-700 mb-1">Official Email Address *</label>
                <input type="email" required placeholder="partner@enterprise.com" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="email" id="partner-email" maxlength="254" autocomplete="email">
              </div>
              <div>
                <label for="partner-phone" class="block text-xs font-semibold text-gray-700 mb-1">Phone Number & WhatsApp *</label>
                <input type="tel" required placeholder="+94 7X XXX XXXX" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="phone" id="partner-phone" maxlength="32" autocomplete="tel">
              </div>
            </div>

            <div>
              <label for="partner-address" class="block text-xs font-semibold text-gray-700 mb-1">Business Physical Address *</label>
              <input type="text" required placeholder="Registered office or warehouse address" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="address" id="partner-address" maxlength="300">
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label for="partner-industry" class="block text-xs font-semibold text-gray-700 mb-1">Target Products of Interest *</label>
                <select required class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="industry" id="partner-industry">
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
                <label for="partner-experience" class="block text-xs font-semibold text-gray-700 mb-1">Partnership Type *</label>
                <select required class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="experience" id="partner-experience">
                  <option value="authorized_dealer">Authorized Territorial Dealer</option>
                  <option value="direct_client">Direct Corporate Bulk Buyer</option>
                  <option value="logistics_partner">Distribution & Fleet Partner</option>
                  <option value="outgrower">Outgrower Contract Supplier</option>
                  <option value="franchise">Commercial Agency</option>
                </select>
              </div>
            </div>

            <div>
              <label for="partner-message" class="block text-xs font-semibold text-gray-700 mb-1">Special Information / Volume Expectations</label>
              <textarea rows="3" placeholder="Estimated monthly volume capacity, target territory coverage, existing client network..." class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="message" id="partner-message" maxlength="5000"></textarea>
            </div>

            <div class="p-3 bg-white rounded-lg border text-xs text-gray-600">
              <i class="fas fa-info-circle text-emerald-700 mr-1"></i>
              <strong>Legal Note:</strong> Initial applications are reviewed by our Business Management team. Formal commercial agreements, credit terms, and legal vetting are concluded individually.
            </div>

            <div class="pt-2">
              <button type="submit" class="btn-primary text-xs w-full py-3 text-sm">
                <i class="fas fa-check-circle"></i> Submit Official Partner Registration
              </button>
            </div>
          <div class="form-privacy"><label><input type="checkbox" name="consent" value="1" required> <span>I agree to be contacted about this request. See our <a href="privacy-policy.php">Privacy Policy</a>.</span></label></div><p class="form-feedback" role="status" aria-live="polite" tabindex="-1" hidden></p>
</form>
        </div>
      </div>
    </section>
  </main>