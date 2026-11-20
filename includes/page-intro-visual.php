<?php
// Page copy stays in its view; image selection is shared across the portfolio.
$pageVisuals = json_decode(file_get_contents(APP_ROOT . '/data/page-visuals.json'), true, 512, JSON_THROW_ON_ERROR);
$introVisual = $pageVisuals[$page] ?? null;
if ($introVisual):
    $introImage = 'assets/images/sections/' . $introVisual['asset'];
?>
<figure class="page-intro-visual">
  <picture>
    <source type="image/webp" srcset="<?= e($introImage) ?>-768.webp 768w, <?= e($introImage) ?>.webp 1536w" sizes="(max-width: 760px) calc(100vw - 40px), (max-width: 1200px) 44vw, 560px">
    <img src="<?= e($introImage) ?>.webp" alt="<?= e($introVisual['alt']) ?>" width="1536" height="1024" fetchpriority="high" decoding="async">
  </picture>
  <figcaption><span class="intro-visual-line" aria-hidden="true"></span><?= e($introVisual['caption']) ?><span class="intro-visual-note">Illustrative visual</span></figcaption>
</figure>
<?php endif; ?>
