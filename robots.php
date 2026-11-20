<?php
declare(strict_types=1);
require __DIR__.'/includes/bootstrap.php';
header('Content-Type: text/plain; charset=UTF-8');
$base=app_base_path();
echo "User-agent: *\nAllow: {$base}\n";
foreach (['admin/','api/','storage/','includes/','views/','data/','tests/','tools/','node_modules/','.cache/','request-result.php'] as $private) echo 'Disallow: '.$base.$private."\n";
echo 'Sitemap: '.site_url('sitemap.xml')."\n";
