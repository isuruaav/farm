# Forest Lanka proposal review and improvements

Reference: `C:/Users/dmisa/Downloads/Forest Lanka.pdf` (32 pages, proposal ISD/FL/2026/108 dated November 18, 2026).

The PDF is a development proposal. Its supplier terms, prices and payment instructions are not website content or authorization to make payments, contact third parties, or publish the document. The later instruction to make the website English-only overrides the proposal's bilingual requirement.

## Completed in this improvement

| Area | What changed |
| --- | --- |
| Brand and presentation | New photographic homepage, buyer/partner entry points, interactive industry explorer, consistent page introductions, clearer typography and responsive layouts. Original forest green, emerald, gold, warm white, charcoal and water blue palette retained. |
| Industry information | Eight shared industry profiles backed by central metadata. Proposed feed and egg tray process stages match the proposal. Poultry and mushroom capacity figures are clearly planning targets. |
| Project stages | Planned, Under development, Operational and Temporarily unavailable are editable in the staff portal. All eight projects initially default to Planned because the proposal does not establish current operating status. |
| Catalog management | Staff can add/edit products, manage draft/published/archived states, feature items, hide prices for quotations, set indicative prices, set minimum quantities and mark availability. Archived products can be restored through editing. |
| Product pages | Individual product detail pages include SKU, pack/variant, indicative price or quotation mode, minimum order, availability and related products. |
| Quotation validation | Server-side product prices remain authoritative. Unavailable, draft and archived products are rejected at checkout; minimum quantities are enforced. Existing request history is preserved. |
| Content controls | Staff can edit the homepage headline, summary, company introduction and shared contact information. Catalog and project changes create audit records. |
| Inquiries | Existing contact, sector, export, investment, partnership and cart forms continue to save to the staff inquiry desk. Project links can preselect the appropriate investment or contact field. |
| Photography | Core industry photographs are stored locally. An unrelated spice photo previously used for mushrooms was replaced with oyster-mushroom imagery. Photography is labelled illustrative. |
| Content accuracy | Replaced unsupported construction announcements, guaranteed delivery claims, financial return claims and unverified certification assertions in the rewritten pages with proposal-grounded portfolio information. |
| SEO | Canonical links, Open Graph metadata, Organization structured data, a dynamic XML sitemap and robots configuration. The sitemap includes published products and excludes private routes. |
| Accessibility | Existing modal focus handling, visible focus, labelled forms and reduced-motion support retained. The industry explorer supports keyboard selection and tab-panel semantics. FAQ disclosure uses native details/summary controls. |

## Preserved implementation and remaining proposal scope

This is an enhancement of the existing PHP/WAMP application, using PHP, SQLite, vanilla JavaScript and Tailwind CSS 4.3.5. It is **not** a Laravel 13 / Filament 5 / Livewire 4 / MySQL migration. Customer inquiries and staff credentials remain in the existing SQLite database.

The following proposal items are not represented as completed:

- Live hosted payment processing, gateway webhook verification and payment history: merchant account approval and credentials are required. The site continues to accept quotation requests without charging cards.
- Customer accounts, customer order history, invoicing, numerical stock tracking, delivery fee calculation and fulfilment automation.
- Separate staff roles and permissions. The current staff account model gives authenticated administrators access to all staff tools.
- Full page/news/FAQ/navigation CMS and an upload-based media library. The new CMS covers homepage/contact information, product entries and project stages; other page content remains in the PHP templates.
- Independent WCAG AAA certification, browser visual review, production hosting/domain setup, email/SMS delivery and external API integrations.

The website does not control machinery or physical IoT devices, in line with the proposal's stated scope limits. Product prices and descriptions are editable seed catalog content, not independently verified product certification or stock information.

## Owner configuration

Open `/farm/admin/`. Use the existing account or run `php tools/create-admin.php admin` to create the first account. No default password has been added.

- **Product catalog:** confirm prices, image/pack information, minimum orders and publication/availability before public use.
- **Project stages:** confirm the actual stage and summary for each of the eight projects.
- **Website content:** update the homepage and shared contact information.
- Set `FOREST_SITE_URL` to the full production base URL, including a subdirectory if used, so canonical links and the sitemap use the intended domain. Local previews derive their own base URL.

## Backups and verification

`storage/backups/pre-proposal-improvements.zip` contains the application source before this review. `storage/backups/pre-proposal-database.sqlite` is a database backup made before the schema additions. Both are protected from public web access. Original static sources remain in their existing archive.

Automated checks use isolated disposable storage and do not send emails, WhatsApp messages or payments. They cover public routes, the inquiry system, administrator authentication, product creation/editing/archiving, draft visibility, minimum orders, canonical pricing, project/content updates, structured metadata, sitemap/robots, CSS coverage, keyboard tab interactions and local gallery actions.

The computer-use bridge did not expose a browser during this session. Visual browser QA could not be completed. WAMP HTTP checks, syntax checks, CSS parsing and integration tests provide the available verification.
