<?php
declare(strict_types=1);

// Re-encode generated photographs for delivery without altering their content.
if (PHP_SAPI !== 'cli') { http_response_code(404); exit; }
if (!extension_loaded('gd') || !function_exists('imagewebp')) {
    fwrite(STDERR, "PHP GD with WebP support is required.\n");
    exit(1);
}
$root = dirname(__DIR__);
$manifest = json_decode(file_get_contents($root . '/data/section-image-generation.json'), true, 512, JSON_THROW_ON_ERROR);
$destination = $root . '/assets/images/sections';
if (!is_dir($destination)) mkdir($destination, 0755, true);
foreach ($manifest['images'] as $record) {
    if (!preg_match('/^[a-z0-9-]+$/', $record['asset'])) throw new RuntimeException('Invalid asset name.');
    $source = imagecreatefrompng($record['source']);
    if (!$source) throw new RuntimeException('Cannot open ' . $record['asset']);
    foreach ([1536 => '', 768 => '-768'] as $width => $suffix) {
        $path = $destination . '/' . $record['asset'] . $suffix . '.webp';
        if (is_file($path)) continue;
        $height = (int)round(imagesy($source) * $width / imagesx($source));
        $output = imagescale($source, $width, $height, IMG_BICUBIC_FIXED);
        if (!$output || !imagewebp($output, $path, 84)) throw new RuntimeException('Cannot encode ' . $path);
    }
    echo $record['asset'], " prepared\n";
}
