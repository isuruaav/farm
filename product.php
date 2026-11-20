<?php
declare(strict_types=1);
require __DIR__ . '/includes/bootstrap.php';
$sku = is_string($_GET['sku'] ?? null) ? $_GET['sku'] : '';
$product = null;
foreach (catalog() as $item) if ($item['id'] === $sku) { $product = $item; break; }
$page = $product ? 'product' : '404';
if (!$product) http_response_code(404);
$meta = $product ? ['title'=>$product['title'].' | FOREST LANKA','description'=>$product['seoDescription'] ?: $product['description']] : ['title'=>'Product not found | FOREST LANKA','description'=>'Find products across the FOREST LANKA portfolio.'];
$canonicalPath = $product ? 'product.php?sku='.rawurlencode($product['id']) : 'products.php';
$sectors=industries_data();$industries=array_column($sectors,'shortName','slug');$site=site_content();
require __DIR__.'/includes/header.php';
require __DIR__.'/views/'.($product?'product-detail':'404').'.php';
require __DIR__.'/includes/footer.php';
