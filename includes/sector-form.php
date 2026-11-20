<form class="dynamic-inquiry-form space-y-3" method="post" action="api/inquiries.php" data-inquiry="sector">
  <?php form_security('sector'); ?>
  <input type="hidden" name="industry" value="<?= e($sectorIndustry) ?>">
  <div><label for="sector-name" class="block text-xs font-semibold text-emerald-200 mb-1">Name / Company contact *</label><input id="sector-name" name="name" required minlength="2" maxlength="180" autocomplete="name" placeholder="Your full name" class="w-full p-2.5 rounded-sm bg-white text-charcoal border"></div>
  <div><label for="sector-phone" class="block text-xs font-semibold text-emerald-200 mb-1">Phone / WhatsApp *</label><input type="tel" id="sector-phone" name="phone" required maxlength="32" autocomplete="tel" placeholder="+94 7X XXX XXXX" class="w-full p-2.5 rounded-sm bg-white text-charcoal border"></div>
  <div><label for="sector-email" class="block text-xs font-semibold text-emerald-200 mb-1">Email (optional)</label><input type="email" id="sector-email" name="email" maxlength="254" autocomplete="email" placeholder="name@company.com" class="w-full p-2.5 rounded-sm bg-white text-charcoal border"></div>
  <div><label for="sector-message" class="block text-xs font-semibold text-emerald-200 mb-1">Your requirements *</label><textarea id="sector-message" name="message" rows="3" required maxlength="5000" placeholder="Quantities, delivery location and specifications" class="w-full p-2.5 rounded-sm bg-white text-charcoal border"></textarea></div>
  <div class="form-privacy"><label><input type="checkbox" name="consent" value="1" required><span>I agree to be contacted about this request. <a href="privacy-policy.php">Privacy Policy</a></span></label></div>
  <p class="form-feedback" role="status" aria-live="polite" tabindex="-1" hidden></p>
  <button type="submit" class="btn-gold w-full py-2.5 text-xs"><i class="fas fa-paper-plane" aria-hidden="true"></i> Submit quotation request</button>
</form>
