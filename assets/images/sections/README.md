# Contextual section imagery

Created on 20 November 2026 with the built-in `image_gen` tool. These generated scenes illustrate the website's content; they do not document actual Forest Lanka facilities, employees, products or operating capacity.

Each photograph is stored here as a 1536px WebP and a 768px WebP for responsive page introductions. Existing assets were retained. Page selection and accessible descriptions are in `data/page-visuals.json`; industry cards, gallery, news and homepage explorer use `data/industries.json`.

The homepage catalog story uses `catalog.webp`; its trade story uses `export-logistics.webp`. The company vision uses `agriculture-vision.webp`. Additional images support circular growth and investment project cards.

Browser visual QA was unavailable because the computer-use bridge exposed no browser or native application. Automated PHP, CSS, HTTP and asset checks are recorded in the task handoff.

## Verification

- Production CSS build and stylesheet checks passed (588 template classes).
- PHP syntax, cart and industry/gallery JavaScript checks passed.
- WAMP served the updated catalog and all 34 WebP files successfully.
- All 21 page-introduction assignments resolve to valid local image pairs. The 34 WebP files total about 5.36 MiB.
- The unchanged integration test initially stopped because it treats the pre-existing browser-only `ai-chat-form` as a server inquiry. Its footer markup matches the source backup. Running the same test in memory with only that form excluded passed all 1,918 HTTP, form, security, persistence, catalog and admin checks across 22 pages. The test file and chatbot were left unchanged.

## Final prompts and saved files

### catalog

Files: `assets/images/sections/catalog.webp`, `assets/images/sections/catalog-768.webp`.

Use case: photorealistic-natural. Asset type: wide website section photograph for a Sri Lankan agro-industrial product catalog. Primary request: a premium editorial still life showing a carefully arranged commercial agricultural product range: brown eggs in a realistic molded pulp carton, a small cluster of fresh oyster mushrooms, bowls of golden grain and cylindrical animal feed pellets, a kraft pouch without writing, a small seedling in dark growing medium, and a clear glass of water. Scene: clean deep forest-green studio backdrop and natural dark wood tabletop. Composition: landscape 3:2, products grouped naturally across the middle and right, all main subjects visible with generous breathing room; no collage or frame. Lighting: soft directional daylight, authentic textures, sophisticated forest-green and warm gold palette. Constraints: photoreal photograph, no text, no logos, no watermarks, no invented labels, no people. This is illustrative product photography, not a real brand facility.

### agriculture-vision

Files: `assets/images/sections/agriculture-vision.webp`, `assets/images/sections/agriculture-vision-768.webp`.

Use case: photorealistic-natural. Asset type: landscape website section photograph for FOREST LANKA, a Sri Lankan agriculture, industry and trade portfolio. Primary request: An elevated landscape view of a plausible Sri Lankan tropical agro-industrial planning landscape: vibrant cultivated fields, coconut trees, a modest contemporary greenhouse and clean low-rise agricultural buildings integrated into the land, soft mist in distant hills. No futuristic megastructures. Wide open view, carefully composed foreground rows and depth. Style: premium natural editorial photography with realistic textures, soft daylight, subtle deep forest green and warm gold tones. Composition: landscape 3:2, clear main subject and enough breathing room for responsive cropping, one continuous photograph. Constraints: illustrative concept only, no logos, no text, no watermarks, no graphic overlays or collage.

### export-logistics

Files: `assets/images/sections/export-logistics.webp`, `assets/images/sections/export-logistics-768.webp`.

Use case: photorealistic-natural. Asset type: landscape website section photograph for FOREST LANKA, a Sri Lankan agriculture, industry and trade portfolio. Primary request: A realistic tropical international container port inspired by Colombo, seen from a slightly elevated quay at sunrise: cargo vessel alongside container cranes, orderly stacked unbranded shipping containers, refrigerated containers in foreground. No readable ship names or writing. International agricultural trade theme. Style: premium natural editorial photography with realistic textures, soft daylight, subtle deep forest green and warm gold tones. Composition: landscape 3:2, clear main subject and enough breathing room for responsive cropping, one continuous photograph. Constraints: illustrative concept only, no logos, no text, no watermarks, no graphic overlays or collage.

### investment-planning

Files: `assets/images/sections/investment-planning.webp`, `assets/images/sections/investment-planning-768.webp`.

Use case: photorealistic-natural. Asset type: landscape website section photograph for FOREST LANKA, a Sri Lankan agriculture, industry and trade portfolio. Primary request: Two Sri Lankan business professionals and an agronomist discussing an agricultural development plan at a timber meeting table next to a greenhouse. Three quarter documentary view, hands naturally resting on a blank plan and a tablet with no legible screen content, small seedling on table, tropical cultivated fields behind glass. Purposeful calm conversation. Style: premium natural editorial photography with realistic textures, soft daylight, subtle deep forest green and warm gold tones. Composition: landscape 3:2, clear main subject and enough breathing room for responsive cropping, one continuous photograph. Constraints: illustrative concept only, no logos, no text, no watermarks, no graphic overlays or collage.

### business-partnerships

Files: `assets/images/sections/business-partnerships.webp`, `assets/images/sections/business-partnerships-768.webp`.

Use case: photorealistic-natural. Asset type: landscape website section photograph for FOREST LANKA, a Sri Lankan agriculture, industry and trade portfolio. Primary request: Close documentary photograph of two Sri Lankan agricultural business partners sharing a natural handshake across a wooden table in a bright greenhouse, cropped at shoulders, no faces necessary, seedlings and a tray of eggs softly visible at the side, warm professional collaborative mood. Realistic hands and anatomy. Style: premium natural editorial photography with realistic textures, soft daylight, subtle deep forest green and warm gold tones. Composition: landscape 3:2, clear main subject and enough breathing room for responsive cropping, one continuous photograph. Constraints: illustrative concept only, no logos, no text, no watermarks, no graphic overlays or collage.

### poultry-farming

Files: `assets/images/sections/poultry-farming.webp`, `assets/images/sections/poultry-farming-768.webp`.

Use case: photorealistic-natural. Asset type: wide photographic industry header and content image for a Sri Lankan agriculture portfolio. Primary request: A clean well ventilated modern tropical layer-hen barn with healthy brown hens on a litter floor, organized nesting areas and a small foreground molded pulp egg tray containing brown eggs. Natural husbandry documentary photography, no crowds of birds, no cages dominating. Composition: landscape 3:2, subject visible in center with generous breathing room for responsive cropping. Premium natural editorial photo, authentic detail, forest-green and warm neutral palette. Constraints: one continuous photograph, illustrative concept, no text, no logos, no watermarks, no labels, no collage.

### animal-feed

Files: `assets/images/sections/animal-feed.webp`, `assets/images/sections/animal-feed-768.webp`.

Use case: photorealistic-natural. Asset type: wide photographic industry header and content image for a Sri Lankan agriculture portfolio. Primary request: Close editorial photograph in a clean feed mill: an open burlap sack of uniform cylindrical golden animal feed pellets, bowls of maize and wheat alongside, stainless mixing machinery softly visible behind. Pellets must be realistic small extruded cylinders, distinct from whole grain. Composition: landscape 3:2, subject visible in center with generous breathing room for responsive cropping. Premium natural editorial photo, authentic detail, forest-green and warm neutral palette. Constraints: one continuous photograph, illustrative concept, no text, no logos, no watermarks, no labels, no collage.

### recycled-egg-trays

Files: `assets/images/sections/recycled-egg-trays.webp`, `assets/images/sections/recycled-egg-trays-768.webp`.

Use case: photorealistic-natural. Asset type: wide photographic industry header and content image for a Sri Lankan agriculture portfolio. Primary request: Stacks of realistic gray recycled molded pulp 30-egg trays on an orderly packaging workshop table. Foreground empty tray clearly shows a regular 5 by 6 molded pocket grid; one tray of brown eggs nearby. Soft natural daylight, subtle clean industrial background. Composition: landscape 3:2, subject visible in center with generous breathing room for responsive cropping. Premium natural editorial photo, authentic detail, forest-green and warm neutral palette. Constraints: one continuous photograph, illustrative concept, no text, no logos, no watermarks, no labels, no collage.

### mushroom-cultivation

Files: `assets/images/sections/mushroom-cultivation.webp`, `assets/images/sections/mushroom-cultivation-768.webp`.

Use case: photorealistic-natural. Asset type: wide photographic industry header and content image for a Sri Lankan agriculture portfolio. Primary request: Fresh cream-colored oyster mushroom clusters growing from substrate bags on organized racks in a clean controlled cultivation room, one beautiful foreground cluster in crisp focus, rows fall into natural soft focus. Realistic mushroom gills and organic irregularity. Composition: landscape 3:2, subject visible in center with generous breathing room for responsive cropping. Premium natural editorial photo, authentic detail, forest-green and warm neutral palette. Constraints: one continuous photograph, illustrative concept, no text, no logos, no watermarks, no labels, no collage.

### egg-processing

Files: `assets/images/sections/egg-processing.webp`, `assets/images/sections/egg-processing-768.webp`.

Use case: photorealistic-natural. Asset type: landscape photographic header and industry content image for a Sri Lankan agro-industrial portfolio. Primary request: A realistic clean food ingredient processing environment. Foreground a shallow ceramic bowl of fine pale golden whole egg powder with a stainless scoop, a small pitcher of liquid egg and a few intact brown eggs on a stainless worktop; background softly focused stainless pasteurization vessels and food-grade piping, not a fantasy factory. Composition: landscape 3:2, center main subject with enough breathing room for responsive crops. Style: premium editorial photography, lifelike materials, coherent forest-green and warm natural palette. Constraints: illustrative concept only, one continuous photograph, no text, no logos, no watermarks, no graphic overlays, no collage.

### organic-fertilizer

Files: `assets/images/sections/organic-fertilizer.webp`, `assets/images/sections/organic-fertilizer-768.webp`.

Use case: photorealistic-natural. Asset type: landscape photographic header and industry content image for a Sri Lankan agro-industrial portfolio. Primary request: A close editorial view of rich mature compost and organic fertilizer pellets in two shallow bins on a rustic workbench at a tidy agricultural composting site, gloved hands gently supporting a small young plant with a dark root ball. Background orderly covered compost bays and tropical greenery, earthy and green. Composition: landscape 3:2, center main subject with enough breathing room for responsive crops. Style: premium editorial photography, lifelike materials, coherent forest-green and warm natural palette. Constraints: illustrative concept only, one continuous photograph, no text, no logos, no watermarks, no graphic overlays, no collage.

### growing-media

Files: `assets/images/sections/growing-media.webp`, `assets/images/sections/growing-media-768.webp`.

Use case: photorealistic-natural. Asset type: landscape photographic header and industry content image for a Sri Lankan agro-industrial portfolio. Primary request: A nursery potting workbench with vigorous young green seedlings in propagation trays, separate small bowls of fibrous brown coco coir, dark potting mix and white perlite, a modest scoop. A bright greenhouse with leafy plants softly behind. Authentic roots, soil texture and nursery materials. Composition: landscape 3:2, center main subject with enough breathing room for responsive crops. Style: premium editorial photography, lifelike materials, coherent forest-green and warm natural palette. Constraints: illustrative concept only, one continuous photograph, no text, no logos, no watermarks, no graphic overlays, no collage.

### water-purification

Files: `assets/images/sections/water-purification.webp`, `assets/images/sections/water-purification-768.webp`.

Use case: photorealistic-natural. Asset type: landscape photographic header and industry content image for a Sri Lankan agro-industrial portfolio. Primary request: A clean practical water filtration demonstration: realistic compact domestic reverse osmosis filter unit with white cartridges, tubing and stainless fittings on a workbench, a glass of clear drinking water beside it; commercial stainless membrane housings softly visible behind, cool daylight, subtle deep green details. No impossible piping. Composition: landscape 3:2, center main subject with enough breathing room for responsive crops. Style: premium editorial photography, lifelike materials, coherent forest-green and warm natural palette. Constraints: illustrative concept only, one continuous photograph, no text, no logos, no watermarks, no graphic overlays, no collage.

### customer-support

Files: `assets/images/sections/customer-support.webp`, `assets/images/sections/customer-support-768.webp`.

Use case: photorealistic-natural. Asset type: landscape website page photograph for a Sri Lankan agricultural and trade company. Primary request: A welcoming contemporary Sri Lankan agricultural business inquiry desk. One friendly professional woman adviser seated with a laptop and headset, looking naturally toward an off-camera visitor, a small notebook and product sample tray with eggs and grains at the edge of the desk, leafy office background and daylight. Not a crowded call center; no text on screens. Composition: landscape 3:2, balanced subject in center with breathing room for responsive crops. Premium natural editorial photograph, lifelike textures, subtle forest-green and warm neutral palette. Constraints: illustrative scene only, no logos, no text, no watermarks, no collage, no graphic overlays.

### delivery-care

Files: `assets/images/sections/delivery-care.webp`, `assets/images/sections/delivery-care-768.webp`.

Use case: photorealistic-natural. Asset type: landscape website page photograph for a Sri Lankan agricultural and trade company. Primary request: A careful agricultural packing scene: a Sri Lankan warehouse worker in a clean green work shirt gently checking a molded pulp egg carton before placing it in a protective unbranded shipping box. Nearby sealed plain kraft packages on a tidy workbench, organized shelves softly blurred. Careful handling and realistic packaging, no text. Composition: landscape 3:2, balanced subject in center with breathing room for responsive crops. Premium natural editorial photograph, lifelike textures, subtle forest-green and warm neutral palette. Constraints: illustrative scene only, no logos, no text, no watermarks, no collage, no graphic overlays.

### business-documents

Files: `assets/images/sections/business-documents.webp`, `assets/images/sections/business-documents-768.webp`.

Use case: photorealistic-natural. Asset type: landscape website page photograph for a Sri Lankan agricultural and trade company. Primary request: An editorial still life for commercial terms and privacy: closed forest-green business folder, neatly stacked paper with no visible writing, a silver pen and a closed laptop on a tidy dark wood desk, soft plant shadows, daylight. Calm, discreet, professional, no locks or floating cybersecurity graphics. Composition: landscape 3:2, balanced subject in center with breathing room for responsive crops. Premium natural editorial photograph, lifelike textures, subtle forest-green and warm neutral palette. Constraints: illustrative scene only, no logos, no text, no watermarks, no collage, no graphic overlays.

### agriculture-journal

Files: `assets/images/sections/agriculture-journal.webp`, `assets/images/sections/agriculture-journal-768.webp`.

Use case: photorealistic-natural. Asset type: landscape website page photograph for a Sri Lankan agricultural and trade company. Primary request: A Sri Lankan agronomist in a greenhouse carefully recording observations in a notebook beside young seedlings and a healthy row of leafy plants. Three quarter side view, realistic hands and plants, softly lit tropical greenery through glass. Thoughtful agricultural research and project notes theme, no legible writing. Composition: landscape 3:2, balanced subject in center with breathing room for responsive crops. Premium natural editorial photograph, lifelike textures, subtle forest-green and warm neutral palette. Constraints: illustrative scene only, no logos, no text, no watermarks, no collage, no graphic overlays.
