<main id="main-content">
  <section class="home-hero" data-reveal="off">
    <div class="site-container hero-layout">
      <div class="hero-copy">
        <div class="hero-badge">
          <span class="hero-badge-pulse" aria-hidden="true"></span>
          <span>ROOTED IN SRI LANKA · GROWING GLOBALLY</span>
        </div>
        <h1><?php
          $headline = e($site['headline']);
          if (str_contains($headline, 'Building what’s next')) {
            echo str_replace('Building what’s next', '<span class="gradient-text-gold">Building what’s next</span>', $headline);
          } elseif (str_contains($headline, 'what’s next')) {
            echo str_replace('what’s next', '<span class="gradient-text-gold">what’s next</span>', $headline);
          } else {
            echo $headline;
          }
        ?></h1>
        <p class="hero-description"><?= e($site['summary']) ?></p>
        <div class="hero-buttons">
          <a href="industries.php" class="btn-gold"><i class="fas fa-layer-group" aria-hidden="true"></i> Explore our industries</a>
          <a href="products.php" class="btn-outline-white"><i class="fas fa-basket-shopping" aria-hidden="true"></i> Browse products</a>
        </div>
        <div class="hero-foundation">
          <span><i class="fas fa-location-dot" aria-hidden="true"></i> Polpithigama, Sri Lanka</span>
          <span><i class="fas fa-certificate" aria-hidden="true"></i> Business registration 16/2633</span>
          <span><i class="fas fa-leaf" aria-hidden="true"></i> Sustainable Bio-Loop</span>
        </div>
      </div>
      <div class="hero-photography-frame">
        <div class="hero-photography">
          <img src="assets/images/industries/landscape.jpg" alt="Illustrative agricultural landscape with cultivated fields in evening light" width="1800" height="1013" fetchpriority="high" decoding="async">
          <div class="hero-image-shade"></div>
          <div class="hero-floating-chip"><i class="fas fa-shield-halved" aria-hidden="true"></i><span>Eco-Friendly Agro-Tech</span></div>
          <div class="hero-image-caption">
            <span class="caption-tag"><i class="fas fa-seedling" aria-hidden="true"></i> OUR SHARED AMBITION</span>
            <p>Growing Agriculture.<br>Building Industries.<br>Connecting Global Markets.</p>
          </div>
          <div class="hero-sector-count">
            <strong class="sector-count-num">08</strong>
            <span class="sector-count-label">Connected<br>Industries</span>
          </div>
          <small class="image-credit">Illustrative photography</small>
        </div>
      </div>
    </div>

    <div class="site-container hero-metrics-container">
      <div class="hero-metrics-bar">
        <div class="metric-item">
          <div class="metric-icon metric-icon--emerald"><i class="fas fa-cubes" aria-hidden="true"></i></div>
          <div>
            <strong>8 Core Sectors</strong>
            <small>Integrated supply ecosystem</small>
          </div>
        </div>
        <div class="metric-divider" aria-hidden="true"></div>
        <div class="metric-item">
          <div class="metric-icon metric-icon--gold"><i class="fas fa-recycle" aria-hidden="true"></i></div>
          <div>
            <strong>100% Circular</strong>
            <small>Zero-waste bio recovery loop</small>
          </div>
        </div>
        <div class="metric-divider" aria-hidden="true"></div>
        <div class="metric-item">
          <div class="metric-icon metric-icon--teal"><i class="fas fa-globe" aria-hidden="true"></i></div>
          <div>
            <strong>Global Trade Ready</strong>
            <small>Direct B2B export partnerships</small>
          </div>
        </div>
        <div class="metric-divider" aria-hidden="true"></div>
        <div class="metric-item">
          <div class="metric-icon metric-icon--amber"><i class="fas fa-handshake" aria-hidden="true"></i></div>
          <div>
            <strong>Open Partnerships</strong>
            <small>Investment & retail opportunities</small>
          </div>
        </div>
      </div>
    </div>

    <div class="site-container hero-bottom">
      <p><i class="fas fa-wand-magic-sparkles text-gold" aria-hidden="true"></i> Agriculture with purpose. Industry with possibility.</p>
      <a href="about.php">Meet FOREST LANKA <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
    </div>
  </section>

  <section class="section-space telemetry-cockpit-section" id="agri-cockpit">
    <div class="site-container">
      <div class="telemetry-header">
        <div>
          <span class="telemetry-tag"><i class="fas fa-microchip" aria-hidden="true"></i> 2027 NEXT-GEN AGRI-TECH COCKPIT</span>
          <h2>Real-Time Industrial Telemetry &amp; Bio-Loop</h2>
        </div>
        <div>
          <span class="telemetry-status-pill"><span class="pulse-beacon" aria-hidden="true"></span> POLPITHIGAMA FACILITY SENSORS ACTIVE</span>
        </div>
      </div>
      <div class="telemetry-grid">
        <div class="telemetry-card">
          <div>
            <div class="telemetry-card-header">
              <div class="telemetry-card-title">
                <div class="telemetry-card-icon telemetry-card-icon--poultry"><i class="fas fa-egg" aria-hidden="true"></i></div>
                <div>
                  <h3>Smart Layer Complex</h3>
                  <p>Polpithigama Base · 125,000 Capacity</p>
                </div>
              </div>
              <span class="telemetry-card-badge"><span class="telemetry-status-dot"></span> Live</span>
            </div>
            <div class="telemetry-card-body">
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-temperature-half" aria-hidden="true"></i> Ambient Temp</span>
                <span class="telemetry-stat-val"><span data-telemetry="poultry-temp">24.2</span><span class="telemetry-stat-unit">°C</span></span>
              </div>
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-droplet" aria-hidden="true"></i> Relative Humidity</span>
                <span class="telemetry-stat-val"><span data-telemetry="poultry-hum">61.8</span><span class="telemetry-stat-unit">% RH</span></span>
              </div>
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-wind" aria-hidden="true"></i> Air NH₃ (Ammonia)</span>
                <span class="telemetry-stat-val"><span data-telemetry="poultry-nh3">7.6</span><span class="telemetry-stat-unit">ppm</span></span>
              </div>
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-basket-shopping" aria-hidden="true"></i> Daily Collection</span>
                <span class="telemetry-stat-val"><span data-telemetry="poultry-eggs">19,420</span><span class="telemetry-stat-unit">/ 25,000</span></span>
              </div>
              <div class="telemetry-progress-bar" role="progressbar" aria-valuenow="78" aria-valuemin="0" aria-valuemax="100" aria-label="Daily egg collection progress">
                <div class="telemetry-progress-fill" style="width:78%"></div>
              </div>
            </div>
          </div>
          <div class="telemetry-live-footer">
            <span>Automated egg conveyor line 3 active</span>
            <span class="text-gold">99.4% Grade A</span>
          </div>
        </div>

        <div class="telemetry-card">
          <div>
            <div class="telemetry-card-header">
              <div class="telemetry-card-title">
                <div class="telemetry-card-icon telemetry-card-icon--mushroom"><i class="fas fa-seedling" aria-hidden="true"></i></div>
                <div>
                  <h3>Mushroom Bio-Cleanrooms</h3>
                  <p>Controlled Atmosphere Chambers</p>
                </div>
              </div>
              <span class="telemetry-card-badge"><span class="telemetry-status-dot"></span> Optimal</span>
            </div>
            <div class="telemetry-card-body">
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-smog" aria-hidden="true"></i> CO₂ Concentration</span>
                <span class="telemetry-stat-val"><span data-telemetry="shroom-co2">845</span><span class="telemetry-stat-unit">ppm</span></span>
              </div>
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-water" aria-hidden="true"></i> Substrate Moisture</span>
                <span class="telemetry-stat-val"><span data-telemetry="shroom-moist">72.4</span><span class="telemetry-stat-unit">%</span></span>
              </div>
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-fan" aria-hidden="true"></i> HEPA Air Exchange</span>
                <span class="telemetry-stat-val">Stage 3<span class="telemetry-stat-unit">99.97%</span></span>
              </div>
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-boxes-stacked" aria-hidden="true"></i> Chamber Yield Rate</span>
                <span class="telemetry-stat-val"><span data-telemetry="shroom-yield">98.5</span><span class="telemetry-stat-unit">% Grade A</span></span>
              </div>
              <div class="telemetry-progress-bar" role="progressbar" aria-valuenow="98" aria-valuemin="0" aria-valuemax="100" aria-label="Mushroom export yield rate">
                <div class="telemetry-progress-fill" style="width:98%"></div>
              </div>
            </div>
          </div>
          <div class="telemetry-live-footer">
            <span>Oyster &amp; Shiitake flush cycle 2</span>
            <span class="text-gold">Temp: 18.5°C</span>
          </div>
        </div>

        <div class="telemetry-card">
          <div>
            <div class="telemetry-card-header">
              <div class="telemetry-card-title">
                <div class="telemetry-card-icon telemetry-card-icon--feed"><i class="fas fa-wheat-awn" aria-hidden="true"></i></div>
                <div>
                  <h3>Precision Feed Mill</h3>
                  <p>12-Stage Processing Plant</p>
                </div>
              </div>
              <span class="telemetry-card-badge"><span class="telemetry-status-dot"></span> Milling</span>
            </div>
            <div class="telemetry-card-body">
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-dna" aria-hidden="true"></i> NIR Crude Protein</span>
                <span class="telemetry-stat-val"><span data-telemetry="feed-protein">19.8</span><span class="telemetry-stat-unit">% ±0.2</span></span>
              </div>
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-gauge-high" aria-hidden="true"></i> Pelleting Throughput</span>
                <span class="telemetry-stat-val"><span data-telemetry="feed-throughput">12.6</span><span class="telemetry-stat-unit">Tons / Hr</span></span>
              </div>
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-temperature-arrow-up" aria-hidden="true"></i> Conditioner Steam</span>
                <span class="telemetry-stat-val">84.8<span class="telemetry-stat-unit">°C</span></span>
              </div>
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-warehouse" aria-hidden="true"></i> Raw Silo Reserves</span>
                <span class="telemetry-stat-val">420<span class="telemetry-stat-unit">MT Silo</span></span>
              </div>
              <div class="telemetry-progress-bar" role="progressbar" aria-valuenow="85" aria-valuemin="0" aria-valuemax="100" aria-label="Feed mill throughput capacity">
                <div class="telemetry-progress-fill" style="width:85%"></div>
              </div>
            </div>
          </div>
          <div class="telemetry-live-footer">
            <span>Pellet durability index (PDI): 97.2%</span>
            <span class="text-gold">ISO 22000 Ready</span>
          </div>
        </div>

        <div class="telemetry-card">
          <div>
            <div class="telemetry-card-header">
              <div class="telemetry-card-title">
                <div class="telemetry-card-icon telemetry-card-icon--water"><i class="fas fa-droplet" aria-hidden="true"></i></div>
                <div>
                  <h3>Korean Membrane Water RO</h3>
                  <p>Smart Filtration &amp; Ion Exchange</p>
                </div>
              </div>
              <span class="telemetry-card-badge"><span class="telemetry-status-dot"></span> Purifying</span>
            </div>
            <div class="telemetry-card-body">
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-vial" aria-hidden="true"></i> Permeate Purity</span>
                <span class="telemetry-stat-val"><span data-telemetry="water-tds">11</span><span class="telemetry-stat-unit">ppm TDS</span></span>
              </div>
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-arrows-spin" aria-hidden="true"></i> Membrane Recovery</span>
                <span class="telemetry-stat-val">94.6<span class="telemetry-stat-unit">%</span></span>
              </div>
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-bottle-water" aria-hidden="true"></i> Daily Purified Volume</span>
                <span class="telemetry-stat-val"><span data-telemetry="water-vol">146,800</span><span class="telemetry-stat-unit">L / Day</span></span>
              </div>
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-shield-virus" aria-hidden="true"></i> UV Sterilization</span>
                <span class="telemetry-stat-val">99.99<span class="telemetry-stat-unit">% Log-4</span></span>
              </div>
              <div class="telemetry-progress-bar" role="progressbar" aria-valuenow="94" aria-valuemin="0" aria-valuemax="100" aria-label="Membrane water recovery rate">
                <div class="telemetry-progress-fill" style="width:94%"></div>
              </div>
            </div>
          </div>
          <div class="telemetry-live-footer">
            <span>South Korean Tech Partnership</span>
            <span class="text-gold">Potable &amp; Food Grade</span>
          </div>
        </div>

        <div class="telemetry-card telemetry-card--wide">
          <div>
            <div class="telemetry-card-header">
              <div class="telemetry-card-title">
                <div class="telemetry-card-icon telemetry-card-icon--loop"><i class="fas fa-solar-panel" aria-hidden="true"></i></div>
                <div>
                  <h3>100% Circular Bio-Loop &amp; Clean Energy Microgrid</h3>
                  <p>Zero-Waste Material Recovery &amp; Solar Rooftop Generation</p>
                </div>
              </div>
              <span class="telemetry-card-badge"><span class="telemetry-status-dot"></span> Net-Zero Loop</span>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-4">
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-sun" aria-hidden="true"></i> Solar Generation</span>
                <span class="telemetry-stat-val"><span data-telemetry="solar-kw">246</span><span class="telemetry-stat-unit">kW Peak</span></span>
              </div>
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-leaf" aria-hidden="true"></i> Organic Bio-Fertilizer</span>
                <span class="telemetry-stat-val">4.8<span class="telemetry-stat-unit">Tons / Day Recovered</span></span>
              </div>
              <div class="telemetry-stat-row">
                <span class="telemetry-stat-label"><i class="fas fa-cloud-arrow-down" aria-hidden="true"></i> Carbon Offset</span>
                <span class="telemetry-stat-val">3.4<span class="telemetry-stat-unit">Tons CO₂e / Day</span></span>
              </div>
            </div>
            <p class="text-xs text-gray-300">
              Poultry manure and agricultural chaff are directly channeled into the in-vessel composter to manufacture enriched organic fertilizer and seedling growing media, closing the agricultural loop completely without landfill waste.
            </p>
          </div>
          <div class="telemetry-live-footer">
            <span>Circular Loop Stage: Material Recovery Phase 03</span>
            <span class="text-gold"><i class="fas fa-circle-check" aria-hidden="true"></i> Polpithigama Microgrid Sync Active</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section-space audience-section">
    <div class="site-container">
      <div class="section-heading heading-split">
        <div>
          <div class="section-badge section-badge--emerald"><i class="fas fa-compass" aria-hidden="true"></i> LET’S BUILD SOMETHING TOGETHER</div>
          <h2>Find your next opportunity.</h2>
        </div>
        <p>From your first product inquiry to a long-term business partnership, start with the path that fits you.</p>
      </div>
      <div class="audience-grid">
        <a class="audience-card audience-card--emerald" href="products.php">
          <div class="audience-top-bar" aria-hidden="true"></div>
          <div class="audience-card-inner">
            <span class="audience-icon audience-icon--emerald"><i class="fas fa-basket-shopping" aria-hidden="true"></i></span>
            <div class="audience-card-text">
              <span class="audience-pill">For Buyers & Retailers</span>
              <h3>I’m looking for products</h3>
              <p>Explore pack sizes, indicative prices and bulk quotation options across 8 categories.</p>
              <span class="audience-action">Browse catalog <i class="fas fa-arrow-right" aria-hidden="true"></i></span>
            </div>
          </div>
        </a>
        <a class="audience-card audience-card--teal" href="export.php">
          <div class="audience-top-bar" aria-hidden="true"></div>
          <div class="audience-card-inner">
            <span class="audience-icon audience-icon--teal"><i class="fas fa-globe" aria-hidden="true"></i></span>
            <div class="audience-card-text">
              <span class="audience-pill">For Importers & Wholesalers</span>
              <h3>I’m a trade partner</h3>
              <p>Discuss export capacity, distribution contracts and supply specifications with our trade desk.</p>
              <span class="audience-action">Explore global trade <i class="fas fa-arrow-right" aria-hidden="true"></i></span>
            </div>
          </div>
        </a>
        <a class="audience-card audience-card--gold" href="investment.php">
          <div class="audience-top-bar" aria-hidden="true"></div>
          <div class="audience-card-inner">
            <span class="audience-icon audience-icon--gold"><i class="fas fa-handshake" aria-hidden="true"></i></span>
            <div class="audience-card-text">
              <span class="audience-pill">For Strategic Investors</span>
              <h3>I see a bigger possibility</h3>
              <p>Discover project portfolios, high-yield scalable facilities, and co-development ventures.</p>
              <span class="audience-action">View opportunities <i class="fas fa-arrow-right" aria-hidden="true"></i></span>
            </div>
          </div>
        </a>
      </div>
    </div>
  </section>

  <section class="section-space industry-showcase" id="our-industries">
    <div class="site-container">
      <div class="section-heading heading-split">
        <div>
          <div class="section-badge section-badge--emerald"><i class="fas fa-layer-group" aria-hidden="true"></i> ONE VISION. EIGHT INDUSTRIES.</div>
          <h2>A connected world<br>of possibilities.</h2>
        </div>
        <div>
          <p><?= e($site['intro']) ?></p>
          <a class="text-link" href="industries.php">Explore the full portfolio <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
        </div>
      </div>
      <div class="industry-explorer" data-industry-explorer>
        <div class="industry-choices" aria-label="Explore an industry">
          <?php foreach ($sectors as $index=>$sector): ?><a id="sector-choice-<?= e($sector['slug']) ?>" class="industry-choice <?= $index===0?'is-selected':'' ?>" href="industry-<?= e($sector['slug']) ?>.php" data-industry-choice="<?= e($sector['slug']) ?>"><span class="choice-num"><?= sprintf('%02d', $index+1) ?></span><i class="fas <?= e($sector['icon']) ?>" aria-hidden="true"></i><span><?= e($sector['shortName']) ?></span></a><?php endforeach; ?>
        </div>
        <div class="industry-panels">
          <?php foreach ($sectors as $index=>$sector): ?><div id="sector-panel-<?= e($sector['slug']) ?>" class="industry-panel" data-industry-panel="<?= e($sector['slug']) ?>" <?= $index!==0?'hidden':'' ?>>
            <div class="industry-panel-image">
              <?php if ($sector['image']): ?><img loading="lazy" decoding="async" src="<?= e($sector['image']) ?>" alt="Illustrative <?= e(strtolower($sector['shortName'])) ?> photography" width="1536" height="1024"><?php else: ?><div class="water-visual"><i class="fas fa-droplet" aria-hidden="true"></i><span>SMART WATER TECHNOLOGY</span></div><?php endif; ?>
              <div class="panel-floating-chip"><i class="fas fa-layer-group" aria-hidden="true"></i> Sector <?= sprintf('%02d', $index+1) ?> of 08</div>
              <div class="panel-scale-chip"><i class="fas fa-bullseye" aria-hidden="true"></i> <?= e($sector['target']) ?></div>
            </div>
            <div class="industry-panel-copy">
              <div>
                <div class="flex items-center gap-2 mb-3">
                  <?= project_status($sector['status']) ?>
                  <span class="text-2xs font-semibold text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-200 uppercase tracking-wider">Polpithigama Base</span>
                </div>
                <h3><?= e($sector['name']) ?></h3>
                <p><?= e($sector['description']) ?></p>
                <div class="panel-highlights-grid">
                  <?php foreach (array_slice($sector['highlights'], 0, 4) as $item): ?>
                  <div class="panel-highlight-item"><i class="fas fa-circle-check" aria-hidden="true"></i><span><?= e($item) ?></span></div>
                  <?php endforeach; ?>
                </div>
                <div class="sector-focus"><i class="fas fa-tag" aria-hidden="true"></i> <?= e($sector['focus']) ?></div>
              </div>
              <div class="panel-actions">
                <a class="btn-primary" href="industry-<?= e($sector['slug']) ?>.php">Explore this industry <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
                <a class="btn-outline-dark" href="products.php?category=<?= e($sector['category']) ?>">Related products</a>
                <a class="text-link" href="contact.php?industry=<?= e($sector['formValue']) ?>">Direct inquiry</a>
              </div>
            </div>
          </div><?php endforeach; ?>
        </div>
      </div>
      <p class="section-footnote">Project stages reflect the current portfolio settings. Contact our team for confirmed capacity, supply and project information.</p>
    </div>
  </section>

  <section class="section-space circular-section">
    <div class="site-container circular-layout">
      <div>
        <div class="section-badge section-badge--dark"><i class="fas fa-arrows-spin" aria-hidden="true"></i> DESIGNED FOR CONNECTED GROWTH</div>
        <h2>More value from<br>every connection.</h2>
        <p>Our vision brings cultivation, manufacturing, packaging and material recovery into one connected portfolio. Each venture creates opportunities for the next.</p>
        <img class="section-context-photo" src="assets/images/sections/organic-fertilizer-768.webp" alt="Illustrative recovery of agricultural materials into compost and organic fertilizer for new growth" width="768" height="512" loading="lazy" decoding="async">
        <a href="about.php" class="text-link text-link-light">The vision behind FOREST LANKA <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
      </div>
      <div class="value-chain-grid">
        <div class="value-step-card">
          <div class="value-step-badge"><span>PHASE 01</span><i class="fas fa-arrow-right text-gold" aria-hidden="true"></i></div>
          <div class="value-step-icon value-step-icon--emerald"><i class="fas fa-seedling" aria-hidden="true"></i></div>
          <h3>Grow</h3>
          <p>Agricultural cultivation, smart layer farming and sustainable growing solutions.</p>
        </div>
        <div class="value-step-card">
          <div class="value-step-badge"><span>PHASE 02</span><i class="fas fa-arrow-right text-gold" aria-hidden="true"></i></div>
          <div class="value-step-icon value-step-icon--amber"><i class="fas fa-industry" aria-hidden="true"></i></div>
          <h3>Create</h3>
          <p>Modern animal feed, molded paper packaging and value-added food ingredients.</p>
        </div>
        <div class="value-step-card">
          <div class="value-step-badge"><span>PHASE 03</span><i class="fas fa-arrow-right text-gold" aria-hidden="true"></i></div>
          <div class="value-step-icon value-step-icon--teal"><i class="fas fa-recycle" aria-hidden="true"></i></div>
          <h3>Recover</h3>
          <p>A circular bio-approach transforming agricultural by-products into organic fertilizer.</p>
        </div>
        <div class="value-step-card">
          <div class="value-step-badge"><span>PHASE 04</span><i class="fas fa-circle-check text-gold" aria-hidden="true"></i></div>
          <div class="value-step-icon value-step-icon--blue"><i class="fas fa-globe" aria-hidden="true"></i></div>
          <h3>Connect</h3>
          <p>Reliable pipelines for local buyers, international trade and enterprise partners.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-space featured-section">
    <div class="site-container">
      <div class="catalog-section-story">
        <img src="assets/images/sections/catalog.webp" srcset="assets/images/sections/catalog-768.webp 768w, assets/images/sections/catalog.webp 1536w" sizes="(max-width: 760px) calc(100vw - 80px), 520px" alt="Illustrative agricultural product range with eggs, oyster mushrooms, feed pellets, grains and a seedling" width="1536" height="1024" loading="lazy" decoding="async">
        <div class="section-heading">
          <div class="section-badge section-badge--emerald"><i class="fas fa-boxes-stacked" aria-hidden="true"></i> FROM THE PRODUCT CATALOG</div>
          <h2>Explore. Select. Enquire.</h2>
          <p>Discover products across our portfolio, then send your requirements for a confirmed quotation.</p>
          <a href="products.php" class="text-link">View all <?= count(catalog()) ?> products</a>
        </div>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <?php $featured=array_values(array_filter(catalog(),static fn($item)=>$item['featured'])); foreach (array_slice($featured?:catalog(),0,4) as $product): require APP_ROOT.'/includes/product-card.php'; endforeach; ?>
      </div>
      <p class="section-footnote">Catalog photography is illustrative. Prices, availability, order minimums and delivery are confirmed with your quotation.</p>
    </div>
  </section>

  <section class="section-space market-section">
    <div class="site-container market-layout">
      <div class="market-photo-wrapper">
        <div class="market-photo-backdrop" aria-hidden="true"></div>
        <div class="market-photo">
          <img src="assets/images/sections/export-logistics.webp" loading="lazy" decoding="async" alt="Illustrative container shipping and agricultural export logistics at a tropical port" width="1536" height="1024">
          <span class="visual-label">Illustrative photography</span>
        </div>
      </div>
      <div class="market-copy">
        <div class="section-badge section-badge--emerald"><i class="fas fa-earth-americas" aria-hidden="true"></i> LOCAL ROOTS. WIDER HORIZONS.</div>
        <h2>Good partnerships<br>help possibilities grow.</h2>
        <p>Whether you represent a supermarket, hotel, food manufacturer, distributor or international trading business, tell us what you need. We’ll help you find the right conversation.</p>
        <div class="market-tags">
          <span class="market-tag-pill"><i class="fas fa-store" aria-hidden="true"></i> Retail & wholesale</span>
          <span class="market-tag-pill"><i class="fas fa-utensils" aria-hidden="true"></i> Hospitality & food</span>
          <span class="market-tag-pill"><i class="fas fa-ship" aria-hidden="true"></i> International buyers</span>
          <span class="market-tag-pill"><i class="fas fa-microchip" aria-hidden="true"></i> Technology partners</span>
        </div>
        <div class="panel-actions">
          <a href="partners.php" class="btn-primary"><i class="fas fa-handshake" aria-hidden="true"></i> Become a business partner</a>
          <a href="export.php" class="text-link">Discuss an export inquiry <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
        </div>
      </div>
    </div>
  </section>

  <section class="section-space">
    <div class="site-container">
      <div class="contact-banner contact-banner-gradient">
        <div>
          <div class="section-badge section-badge--dark"><i class="fas fa-comments" aria-hidden="true"></i> LET’S START A CONVERSATION</div>
          <h2>Your next step<br>starts here.</h2>
          <p>Products, projects or partnerships. We’re ready to hear what you have in mind.</p>
        </div>
        <div class="contact-banner-actions">
          <a href="contact.php" class="btn-gold"><i class="fas fa-paper-plane" aria-hidden="true"></i> Talk to our team</a>
          <a href="https://wa.me/<?= e($site['whatsapp']) ?>" class="contact-whatsapp-btn" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp" aria-hidden="true"></i> Connect on WhatsApp</a>
        </div>
      </div>
    </div>
  </section>
</main>
