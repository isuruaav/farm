<main id="main-content"><div class="page-intro page-intro--visual"><div class="page-intro-layout site-container"><div class="page-intro-copy"><p class="brand-eyebrow">GLOBAL TRADING &amp; EXPORT</p><h1>Local possibilities.<br>International conversations.</h1><p>Share your product, packaging and destination requirements. Explore the portfolio and request a quotation, samples or a discussion about long-term supply.</p></div><?php require APP_ROOT . "/includes/page-intro-visual.php"; ?></div></div><section class="section-space"><div class="site-container">
<div class="export-calc-section">
  <div class="export-calc-header">
    <span class="telemetry-tag"><i class="fas fa-calculator" aria-hidden="true"></i> 2027 B2B LOGISTICS &amp; FREIGHT COCKPIT</span>
    <h2>Interactive Global Trade Route &amp; Freight Estimator</h2>
  </div>
  <div class="export-calc-body">
    <div>
      <div class="export-calc-row">
        <div>
          <label for="calc-destination">Destination Port</label>
          <select id="calc-destination" class="export-calc-select" onchange="updateExportCalc()">
            <option value="dubai" data-days="4" data-port="Jebel Ali, UAE" data-country="United Arab Emirates" data-freight="Fast Reefer Route">Jebel Ali (Dubai, UAE) — 4 Transit Days</option>
            <option value="doha" data-days="5" data-port="Hamad Port, Qatar" data-country="Qatar" data-freight="Gulf Express Line">Hamad Port (Doha, Qatar) — 5 Transit Days</option>
            <option value="male" data-days="2" data-port="Malé Port, Maldives" data-country="Maldives" data-freight="Daily Island Feeder">Malé Port (Maldives) — 2 Transit Days</option>
            <option value="singapore" data-days="5" data-port="PSA Singapore" data-country="Singapore" data-freight="Southeast Asia Trunk">PSA Singapore — 5 Transit Days</option>
            <option value="rotterdam" data-days="18" data-port="Rotterdam, Netherlands" data-country="Netherlands (EU)" data-freight="Euro-Med Deepsea">Port of Rotterdam (EU) — 18 Transit Days</option>
          </select>
        </div>
        <div>
          <label for="calc-cargo">Target Cargo Line</label>
          <select id="calc-cargo" class="export-calc-select" onchange="updateExportCalc()">
            <option value="egg_powder" data-container="20ft Food-Grade Dry" data-cap="14 MT" data-temp="Ambient &lt; 25°C" data-code="egg_powder">Whole Egg Powder (Food-Grade 20ft)</option>
            <option value="albumen_powder" data-container="20ft Moisture Controlled" data-cap="12 MT" data-temp="Ambient dry" data-code="albumen_powder">Albumen Powder (High-Whip 20ft)</option>
            <option value="fresh_table_eggs" data-container="40ft High-Cube Reefer" data-cap="1,248 Cartons" data-temp="Cold Chain 2-4°C" data-code="fresh_table_eggs">Fresh Table Eggs (Cold Reefer 40ft)</option>
            <option value="shiitake_oyster" data-container="20ft Dry / Air Cargo" data-cap="6 MT Dehydrated" data-temp="Dry vacuum" data-code="shiitake_oyster">Dehydrated Gourmet Mushrooms (Air/Sea)</option>
            <option value="egg_trays" data-container="40ft HC Molded Fiber" data-cap="220,000 Trays" data-temp="Standard Dry" data-code="egg_trays">Molded Pulp Egg Trays (Bulk HC 40ft)</option>
          </select>
        </div>
      </div>
      <div class="export-calc-row">
        <div>
          <label for="calc-volume">Container Volume</label>
          <select id="calc-volume" class="export-calc-select" onchange="updateExportCalc()">
            <option value="1">1 Container (Full Container Load - FCL)</option>
            <option value="2">2 Containers (Scheduled Bi-Weekly)</option>
            <option value="4">4 Containers (Monthly Supply Contract)</option>
            <option value="sample">Lab Sample (Air Express Courier)</option>
          </select>
        </div>
        <div>
          <label for="calc-incoterm">Preferred Incoterm</label>
          <select id="calc-incoterm" class="export-calc-select" onchange="updateExportCalc()">
            <option value="FOB Colombo">FOB Colombo (Port of Departure)</option>
            <option value="CIF Destination">CIF Destination (Cost, Insurance &amp; Freight)</option>
            <option value="CFR Destination">CFR Destination (Cost &amp; Freight)</option>
          </select>
        </div>
      </div>
    </div>
    <div class="export-calc-result">
      <div class="export-calc-stat">
        <span>Port of Departure</span>
        <strong>Port of Colombo (CMB)</strong>
      </div>
      <div class="export-calc-stat">
        <span>Estimated Sea Transit</span>
        <strong id="calc-stat-transit">4 Transit Days</strong>
      </div>
      <div class="export-calc-stat">
        <span>Packaging Standard</span>
        <strong id="calc-stat-pack">20ft Food-Grade Dry</strong>
      </div>
      <div class="export-calc-stat">
        <span>Temperature Regimen</span>
        <strong id="calc-stat-temp">Ambient &lt; 25°C</strong>
      </div>
      <div class="export-calc-action">
        <button type="button" class="btn-gold" onclick="applyCalcToForm()">
          <i class="fas fa-arrow-down" aria-hidden="true"></i> Apply to Quotation Form
        </button>
      </div>
    </div>
  </div>
</div>
<div class="export-layout"><div class="export-copy"><p class="eyebrow">FOR INTERNATIONAL BUYERS &amp; TRADE PARTNERS</p><h2>Let your requirements<br>lead the conversation.</h2><p>Tell us your country, destination port, target quantity and packaging preferences. Our team reviews the request and discusses confirmed product availability, order minimums, documentation and freight arrangements individually.</p><div class="export-sector-list"><?php foreach ($sectors as $sector): ?><a href="products.php?category=<?= e($sector['category']) ?>" class="export-sector-link"><i class="fas <?= e($sector['icon']) ?>" aria-hidden="true"></i><span><strong><?= e($sector['shortName']) ?></strong><small><?= e($sector['focus']) ?></small></span></a><?php endforeach; ?></div><div class="project-context"><h3>A quotation comes first.</h3><p>Catalog details are indicative. Export quantities, samples, certifications, shipping terms and supply commitments require individual confirmation. No payment is collected through this form.</p></div></div><div class="export-form-panel"><p class="brand-eyebrow">START AN EXPORT INQUIRY</p><h2>What are you looking for?</h2><p>Provide as much detail as you can. A reference number is shown after your request has been saved.</p><form id="export-inquiry-form" class="space-y-3.5" method="post" action="api/inquiries.php" data-inquiry="export">
<?php form_security("export"); ?>
                <div>
                  <label for="export-name" class="block text-xs font-semibold text-emerald-800 mb-1">Contact Person Name *</label>
                  <input type="text" required placeholder="Full Name" class="w-full text-xs p-2.5 rounded-sm bg-white text-charcoal border focus:ring-1 focus:ring-gold" name="name" id="export-name" maxlength="180" autocomplete="name">
                </div>

                <div>
                  <label for="export-company" class="block text-xs font-semibold text-emerald-800 mb-1">Company / Importer Name *</label>
                  <input type="text" required placeholder="Corporate entity name" class="w-full text-xs p-2.5 rounded-sm bg-white text-charcoal border focus:ring-1 focus:ring-gold" name="company" id="export-company" maxlength="180" autocomplete="organization">
                </div>

                <div class="grid grid-cols-2 gap-2">
                  <div>
                    <label for="export-country" class="block text-xs font-semibold text-emerald-800 mb-1">Buyer Country *</label>
                    <input type="text" required placeholder="e.g. UAE, Qatar, Maldives" class="w-full text-xs p-2.5 rounded-sm bg-white text-charcoal border focus:ring-1 focus:ring-gold" name="country" id="export-country" maxlength="180" autocomplete="country-name">
                  </div>
                  <div>
                    <label for="export-port" class="block text-xs font-semibold text-emerald-800 mb-1">Port of Destination</label>
                    <input type="text" placeholder="e.g. Jebel Ali, Malé" class="w-full text-xs p-2.5 rounded-sm bg-white text-charcoal border focus:ring-1 focus:ring-gold" name="port" id="export-port" maxlength="180">
                  </div>
                </div>

                <div class="grid grid-cols-2 gap-2">
                  <div>
                    <label for="export-email" class="block text-xs font-semibold text-emerald-800 mb-1">Email Address *</label>
                    <input type="email" required placeholder="procurement@company.com" class="w-full text-xs p-2.5 rounded-sm bg-white text-charcoal border focus:ring-1 focus:ring-gold" name="email" id="export-email" maxlength="254" autocomplete="email">
                  </div>
                  <div>
                    <label for="export-phone" class="block text-xs font-semibold text-emerald-800 mb-1">WhatsApp / Phone *</label>
                    <input type="tel" required placeholder="+Country code..." class="w-full text-xs p-2.5 rounded-sm bg-white text-charcoal border focus:ring-1 focus:ring-gold" name="phone" id="export-phone" maxlength="32" autocomplete="tel">
                  </div>
                </div>

                <div>
                  <label for="export-industry" class="block text-xs font-semibold text-emerald-800 mb-1">Target Product Line *</label>
                  <select required class="w-full text-xs p-2.5 rounded-sm bg-white text-charcoal border focus:ring-1 focus:ring-gold" name="industry" id="export-industry">
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
                  <label for="export-quantity" class="block text-xs font-semibold text-emerald-800 mb-1">Estimated Target Volume & Incoterms</label>
                  <input type="text" placeholder="e.g. 5 Metric Tons, FOB Colombo or CIF Jebel Ali" class="w-full text-xs p-2.5 rounded-sm bg-white text-charcoal border focus:ring-1 focus:ring-gold" name="quantity" id="export-quantity" maxlength="180">
                </div>

                <div class="flex items-center gap-2 pt-1 text-xs text-emerald-800">
                  <input type="checkbox" id="request-sample-check" class="rounded-sm text-emerald-600 focus:ring-gold" name="sample" maxlength="180">
                  <label for="export-message" for="request-sample-check">Request Product Lab Sample for Evaluation</label>
                </div>

                <div>
                  <label for="export-message" class="block text-xs font-semibold text-emerald-800 mb-1">Commercial Specifications / Requirements</label>
                  <textarea rows="2" placeholder="Custom packaging, certification requests, delivery schedules..." class="w-full text-xs p-2.5 rounded-sm bg-white text-charcoal border focus:ring-1 focus:ring-gold" name="message" id="export-message" maxlength="5000"></textarea>
                </div>

                <div class="pt-2">
                  <button type="submit" class="btn-gold text-xs w-full py-3">
                    <i class="fas fa-paper-plane"></i> Submit Export Inquiry & Sample Request
                  </button>
                </div>
              <div class="form-privacy"><label><input type="checkbox" name="consent" value="1" required> <span>I agree to be contacted about this request. See our <a href="privacy-policy.php">Privacy Policy</a>.</span></label></div><p class="form-feedback" role="status" aria-live="polite" tabindex="-1" hidden></p>
</form></div></div></div></section></main>