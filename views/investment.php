<main id="main-content"><div class="page-intro page-intro--visual"><div class="page-intro-layout site-container"><div class="page-intro-copy"><p class="brand-eyebrow">INVESTMENT &amp; STRATEGIC PARTNERSHIPS</p><h1>Build with purpose.<br>Grow with a shared vision.</h1><p>Explore eight project concepts spanning agriculture, food, packaging and water technology. Share your interests and begin a discussion with our team.</p></div><?php require APP_ROOT . "/includes/page-intro-visual.php"; ?></div></div>
<section class="section-space"><div class="site-container"><div class="journal-intro"><p>The portfolio presents planned opportunities and project targets. Capacity figures are planning ambitions, not confirmed operating capacity or investment returns. Project details, funding requirements and agreements are discussed individually.</p></div><div class="investment-grid">
<?php foreach ($sectors as $sector): ?><article class="investment-card"><img class="section-context-photo investment-project-photo" src="<?= e(str_replace(".webp", "-768.webp", $sector["image"])) ?>" alt="Illustrative <?= e(strtolower($sector["shortName"])) ?> project theme" width="768" height="512" loading="lazy" decoding="async"><div class="investment-card-top"><i class="fas <?= e($sector['icon']) ?>" aria-hidden="true"></i><?= project_status($sector['status']) ?></div><h2><?= e($sector['name']) ?></h2><p><?= e($sector['description']) ?></p><div class="investment-target"><?= e($sector['target']) ?></div><div class="investment-actions"><a class="btn-primary" href="#invest-form-section" data-investment-project="<?= e($sector['investmentValue']) ?>">Express interest</a><a class="text-link" href="industry-<?= e($sector['slug']) ?>.php">Project overview</a></div></article><?php endforeach; ?></div>
<div id="invest-form-section" class="inquiry-surface p-8 lg:p-12 rounded-3xl border border-emerald-100 shadow-sm">
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
            <div class="lg:col-span-5 space-y-4">
              <span class="text-xs font-bold text-emerald-700 uppercase tracking-wider bg-gold/10 px-3 py-1 rounded-full border border-gold/30">
                Direct Expression of Interest (EOI)
              </span>
              <h2 class="text-3xl font-black text-forest font-heading">
                Discuss an investment or partnership idea
              </h2>
              <p class="text-base sm:text-sm text-gray-600 leading-relaxed">
                Whether you represent an institutional private equity fund, an agribusiness group, an angel investor syndicate, or an international joint venture partner, FOREST LANKA welcomes strategic engagement.
              </p>
              <div class="space-y-2 text-xs text-emerald-800 pt-2">
                <div class="flex items-center gap-2"><i class="fas fa-check-circle text-emerald-700"></i> Discuss project information</div>
                <div class="flex items-center gap-2"><i class="fas fa-check-circle text-emerald-700"></i> Share partnership requirements</div>
                <div class="flex items-center gap-2"><i class="fas fa-check-circle text-emerald-700"></i> Arrange a follow-up conversation</div>
              </div>
            </div>

            <div class="lg:col-span-7 bg-white text-charcoal p-6 sm:p-8 rounded-2xl shadow-xl">
              <form id="investment-eoi-form" class="space-y-3.5" method="post" action="api/inquiries.php" data-inquiry="investment">
<?php form_security("investment"); ?>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div>
                    <label for="investment-name" class="block text-xs font-semibold text-gray-700 mb-1">Investor / Firm Name *</label>
                    <input type="text" required placeholder="Individual or Institution" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="name" id="investment-name" maxlength="180" autocomplete="name">
                  </div>
                  <div>
                    <label for="investment-company" class="block text-xs font-semibold text-gray-700 mb-1">Company / Entity Name</label>
                    <input type="text" placeholder="Corporate name" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="company" id="investment-company" maxlength="180" autocomplete="organization">
                  </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div>
                    <label for="investment-country" class="block text-xs font-semibold text-gray-700 mb-1">Country of Residence / Domicile *</label>
                    <input type="text" required placeholder="e.g. Sri Lanka, UAE, Singapore" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="country" id="investment-country" maxlength="180" autocomplete="country-name">
                  </div>
                  <div>
                    <label for="investment-phone" class="block text-xs font-semibold text-gray-700 mb-1">Contact Phone / WhatsApp *</label>
                    <input type="tel" required placeholder="+Country code..." class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="phone" id="investment-phone" maxlength="32" autocomplete="tel">
                  </div>
                </div>

                <div>
                  <label for="investment-email" class="block text-xs font-semibold text-gray-700 mb-1">Corporate Email Address *</label>
                  <input type="email" required placeholder="investor@domain.com" class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="email" id="investment-email" maxlength="254" autocomplete="email">
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div>
                    <label for="investment-industry" class="block text-xs font-semibold text-gray-700 mb-1">Project of Primary Interest *</label>
                    <select required class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="industry" id="investment-industry">
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
                    <label for="investment-investment_range" class="block text-xs font-semibold text-gray-700 mb-1">Partnership / Investment Mode *</label>
                    <select required class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="investment_range" id="investment-investment_range">
                      <option value="joint_venture">Joint Venture (JV) Partnership</option>
                      <option value="equity">Equity Capital Investment</option>
                      <option value="tech_transfer">Technology Transfer & Licensing</option>
                      <option value="outgrower">Outgrower / Contract Agribusiness</option>
                      <option value="debt">Debt Financing / Expansion Loan</option>
                    </select>
                  </div>
                </div>

                <div>
                  <label for="investment-partnership_type" class="block text-xs font-semibold text-gray-700 mb-1">Investment Scale / Capital Bracket</label>
                  <select class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="partnership_type" id="investment-partnership_type">
                    <option value="bracket_1">LKR 10 Million – 50 Million (USD ~35k – 170k)</option>
                    <option value="bracket_2">LKR 50 Million – 200 Million (USD ~170k – 680k)</option>
                    <option value="bracket_3">LKR 200 Million – 500 Million (USD ~680k – 1.7M)</option>
                    <option value="bracket_4">Over LKR 500 Million (USD > 1.7M)</option>
                  </select>
                </div>

                <div>
                  <label for="investment-message" class="block text-xs font-semibold text-gray-700 mb-1">Message / Key Partnership Objectives</label>
                  <textarea rows="2" placeholder="Brief outline of your investment background, timeframe, and specific expectations..." class="w-full text-xs p-2.5 border rounded-lg focus:ring-1 focus:ring-emerald-700" name="message" id="investment-message" maxlength="5000"></textarea>
                </div>

                <div class="pt-2">
                  <button type="submit" class="btn-primary text-xs w-full py-3">
                    <i class="fas fa-handshake"></i> Submit Investment Expression of Interest (EOI)
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