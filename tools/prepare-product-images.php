<?php
declare(strict_types=1);

// Encode generated product photographs; catalog assignment is a separate step.
if (PHP_SAPI !== 'cli') { http_response_code(404); exit; }
if (!extension_loaded('gd') || !function_exists('imagewebp')) {
    fwrite(STDERR, "PHP GD with WebP support is required.\n");
    exit(1);
}
$root = dirname(__DIR__);
$manifest = json_decode(file_get_contents($root . '/data/product-image-generation.json'), true, 512, JSON_THROW_ON_ERROR);
$destination = $root . '/assets/images/products/photo-v2';
if (!is_dir($destination)) mkdir($destination, 0755, true);
foreach ($manifest['images'] as $record) {
    if (!preg_match('/^[a-z0-9-]+$/', $record['asset'])) throw new RuntimeException('Invalid product asset name.');
    $path = $destination . '/' . $record['asset'] . '.webp';
    if (!is_file($path)) {
        $source = imagecreatefrompng($record['source']);
        if (!$source) throw new RuntimeException('Cannot open ' . $record['asset']);
        $output = imagescale($source, 1200, (int)round(imagesy($source) * 1200 / imagesx($source)), IMG_BICUBIC_FIXED);
        if (!$output || !imagewebp($output, $path, 85)) throw new RuntimeException('Cannot encode ' . $path);
    }
    echo $record['sku'], ' prepared: ', filesize($path), " bytes\n";
}
