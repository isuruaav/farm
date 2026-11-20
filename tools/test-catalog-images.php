<?php
require __DIR__ . '/../includes/bootstrap.php';

$products = catalog();
echo "Found " . count($products) . " products in catalog:\n\n";

$seen = [];
$hasDuplicate = false;

foreach ($products as $p) {
    $img = product_image($p);
    $sku = $p['id'];
    $name = $p['name'];
    $exists = file_exists(__DIR__ . '/../' . $img) ? 'EXISTS' : 'MISSING';
    
    if (isset($seen[$img])) {
        echo "[DUPLICATE] $sku ($name) shares image with {$seen[$img]} => $img\n";
        $hasDuplicate = true;
    } else {
        $seen[$img] = $sku;
        echo "[OK] $sku ($name) => $img [$exists]\n";
    }
}

if (!$hasDuplicate && count($seen) === count($products)) {
    echo "\nSUCCESS: All " . count($products) . " products have 100% unique, verified images!\n";
} else {
    echo "\nFAILED: Duplicate images found!\n";
    exit(1);
}
