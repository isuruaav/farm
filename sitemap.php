<?php
declare(strict_types=1);
require __DIR__.'/includes/bootstrap.php';
header('Content-Type: application/xml; charset=UTF-8');
echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n";
echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">';
$pages=json_decode(file_get_contents(APP_ROOT.'/data/pages.json'),true,512,JSON_THROW_ON_ERROR);
foreach ($pages as $slug=>$meta) {
    echo '<url><loc>'.e(site_url($slug==='index'?'':$slug.'.php')).'</loc><lastmod>'.date('Y-m-d',filemtime(APP_ROOT.'/views/'.$slug.'.php')).'</lastmod></url>';
}
foreach (catalog() as $product) echo '<url><loc>'.e(site_url('product.php?sku='.rawurlencode($product['id']))).'</loc><lastmod>'.e(substr($product['updatedAt'],0,10)).'</lastmod></url>';
echo '</urlset>';
