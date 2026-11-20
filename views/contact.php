<main id="main-content">
    <div class="bg-forest-dark text-white py-16 relative page-intro page-intro--visual">
      <div class="page-intro-layout max-w-7xl mx-auto px-4 relative z-10"><div class="page-intro-copy">
        <div class="text-xs text-gold uppercase tracking-wider font-semibold mb-2 flex items-center gap-2">
          <a href="index.php" class="hover:underline">Home</a>
          <i class="fas fa-chevron-right text-2xs"></i>
          <span>Official Inquiries</span>
        </div>
        <h1>
          <span>Contact Us & Inquiry Desk</span>
          
        </h1>
        <p class="text-base sm:text-base text-emerald-100 max-w-3xl leading-relaxed">
          <span>
            Share your product, project or partnership requirements with the FOREST LANKA team. Keep the reference number shown after submitting your inquiry so we can help you follow up.
          </span>
          
        </p>
      </div><?php require APP_ROOT . "/includes/page-intro-visual.php"; ?></div>
    </div>

    
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">

          
          <div class="lg:col-span-5 space-y-6">
            <div class="bg-warmwhite p-6 sm:p-8 rounded-3xl border border-gray-200 shadow-xs">
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
                    <strong>Registration Number:</strong>
                    <div class="text-sm font-bold text-forest mt-0.5 font-mono">16/2633</div>
                  </div>
                </div>

                <div class="flex items-start gap-3">
                  <div class="w-9 h-9 rounded-full bg-emerald-100 text-emerald-800 flex items-center justify-center shrink-0 text-base mt-0.5">
                    <i class="fas fa-map-location-dot"></i>
                  </div>
                  <div>
                    <strong>Registered Address:</strong>
                    <div class="text-xs text-gray-600 mt-0.5 leading-relaxed">
                      <?= e($site['address']) ?>
                    </div>
                    <div class="text-2xs font-bold text-emerald-800 mt-1">Postal Code: 60620</div>
                  </div>
                </div>

                <div class="flex items-start gap-3">
                  <div class="w-9 h-9 rounded-full bg-emerald-100 text-emerald-800 flex items-center justify-center shrink-0 text-base mt-0.5">
                    <i class="fas fa-phone-volume"></i>
                  </div>
                  <div>
                    <strong>Direct Office Telephone:</strong>
                    <div class="text-sm font-bold text-forest mt-0.5 font-mono">
                      <a href="tel:<?= e(preg_replace('/[^+0-9]/','',$site['phone'])) ?>" class="hover:text-emerald-700"><?= e($site['phone']) ?></a>
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
                      <a href="https://wa.me/<?= e($site['whatsapp']) ?>" target="_blank" rel="noopener noreferrer" class="hover:underline">WhatsApp operations desk</a>
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
                      <a href="mailto:<?= e($site['email']) ?>" class="hover:text-emerald-700"><?= e($site['email']) ?></a>
                    </div>
                  </div>
                </div>
              </div>

              
              <div class="mt-6 pt-5 border-t border-gray-200">
                <a href="https://wa.me/<?= e($site['whatsapp']) ?>?text=Hello%20Forest%20Lanka,%20I%20am%20contacting%20you%20regarding%20business%20inquiries." target="_blank" rel="noopener noreferrer" class="btn-gold text-xs w-full py-2.5 flex items-center justify-center gap-2">
                  <i class="fab fa-whatsapp text-green-700 text-base"></i>
                  <span>Message Us Directly on WhatsApp</span>
                </a>
              </div>
            </div>

            
            <div class="bg-warmwhite p-4 rounded-3xl border border-gray-200 overflow-hidden shadow-xs">
              <h3 class="text-xs font-bold text-forest uppercase tracking-wider mb-2">Location Map (Polpithigama, Kurunegala)</h3>
              <div class="w-full h-48 bg-emerald-950 rounded-2xl flex flex-col items-center justify-center text-emerald-200 text-center p-4 relative overflow-hidden">
                <i class="fas fa-map-marked-alt text-4xl text-gold mb-2"></i>
                <div class="font-bold text-xs text-white">FOREST LANKA Agro-Industrial Base</div>
                <div class="text-2xs text-emerald-300"><?= e($site['address']) ?></div>
                <a href="https://maps.google.com/?q=<?= rawurlencode($site['address']) ?>" target="_blank" rel="noopener noreferrer" class="mt-3 text-2xs bg-gold text-forest font-bold px-3 py-1 rounded-full hover:bg-white transition">
                  <i class="fas fa-external-link-alt mr-1"></i> Open in Google Maps
                </a>
              </div>
            </div>
          </div>

          
          <div class="lg:col-span-7">
            <div class="bg-forest-dark text-white p-8 sm:p-10 rounded-3xl border-2 border-gold/40 shadow-2xl">
              <div class="border-b border-emerald-800 pb-4 mb-6">
                <h3 class="text-2xl font-black font-heading text-white">Send an Inquiry</h3>
                <p class="text-base text-emerald-200 mt-1">Please specify your requirements below. Your request is saved securely for our team to review. Keep the reference number shown after submission.</p>
              </div>

              <form class="dynamic-inquiry-form space-y-4" method="post" action="api/inquiries.php" data-inquiry="contact">
<?php form_security("contact"); ?>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label for="contact-name" class="block text-xs font-semibold text-emerald-200 mb-1">Your Full Name *</label>
                    <input type="text" required placeholder="Mr. / Ms. Full Name" class="w-full text-xs p-3 rounded-lg bg-white text-charcoal border focus:ring-1 focus:ring-gold" name="name" id="contact-name" maxlength="180" autocomplete="name">
                  </div>
                  <div>
                    <label for="contact-company" class="block text-xs font-semibold text-emerald-200 mb-1">Company / Farm</label>
                    <input type="text" placeholder="Company or farm name" class="w-full text-xs p-3 rounded-lg bg-white text-charcoal border focus:ring-1 focus:ring-gold" name="company" id="contact-company" maxlength="180" autocomplete="organization">
                  </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label for="contact-country" class="block text-xs font-semibold text-emerald-200 mb-1">Country *</label>
                    <input type="text" required placeholder="Sri Lanka / Other Country" class="w-full text-xs p-3 rounded-lg bg-white text-charcoal border focus:ring-1 focus:ring-gold" name="country" id="contact-country" maxlength="180" autocomplete="country-name">
                  </div>
                  <div>
                    <label for="contact-email" class="block text-xs font-semibold text-emerald-200 mb-1">Email Address *</label>
                    <input type="email" required placeholder="name@domain.com" class="w-full text-xs p-3 rounded-lg bg-white text-charcoal border focus:ring-1 focus:ring-gold" name="email" id="contact-email" maxlength="254" autocomplete="email">
                  </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label for="contact-phone" class="block text-xs font-semibold text-emerald-200 mb-1">Telephone Number *</label>
                    <input type="tel" required placeholder="+94 7X XXX XXXX" class="w-full text-xs p-3 rounded-lg bg-white text-charcoal border focus:ring-1 focus:ring-gold" name="phone" id="contact-phone" maxlength="32" autocomplete="tel">
                  </div>
                  <div>
                    <label for="contact-inquiry_type" class="block text-xs font-semibold text-emerald-200 mb-1">Inquiry Type *</label>
                    <select required class="w-full text-xs p-3 rounded-lg bg-white text-charcoal border focus:ring-1 focus:ring-gold" name="inquiry_type" id="contact-inquiry_type">
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
                  <label for="contact-industry" class="block text-xs font-semibold text-emerald-200 mb-1">Interested Product or Industry *</label>
                  <select required class="w-full text-xs p-3 rounded-lg bg-white text-charcoal border focus:ring-1 focus:ring-gold" name="industry" id="contact-industry">
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
                  <label for="contact-message" class="block text-xs font-semibold text-emerald-200 mb-1">Message / Requirements *</label>
                  <textarea rows="4" required placeholder="Please provide specific details such as target quantities, delivery timeframe, destination or custom requirements..." class="w-full text-xs p-3 rounded-lg bg-white text-charcoal border focus:ring-1 focus:ring-gold" name="message" id="contact-message" maxlength="5000"></textarea>
                </div>

                <div class="pt-2">
                  <button type="submit" class="btn-gold text-xs w-full py-3.5 text-sm">
                    <i class="fas fa-paper-plane mr-1"></i> Send Official Inquiry
                  </button>
                </div>
              <div class="form-privacy"><label><input type="checkbox" name="consent" value="1" required> <span>I agree to be contacted about this request. See our <a href="privacy-policy.php">Privacy Policy</a>.</span></label></div><p class="form-feedback" role="status" aria-live="polite" tabindex="-1" hidden></p>
</form>
            </div>
          </div>

        </div>
      </div>
    </section>
  </main>
