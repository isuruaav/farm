<?php
declare(strict_types=1);
require __DIR__ . '/bootstrap.php';
$pages = json_decode(file_get_contents(APP_ROOT . '/data/pages.json'), true, 512, JSON_THROW_ON_ERROR);
if (!isset($pages[$page]) || !is_file(APP_ROOT . '/views/' . $page . '.php')) {
    http_response_code(404);
    $page = '404';
    $meta = ['title' => 'Page not found | FOREST LANKA', 'description' => 'Find your way back to FOREST LANKA.'];
} else {
    $meta = $pages[$page];
}
$sectors = industries_data();
$industries = array_column($sectors, 'shortName', 'slug');
$currentSector = str_starts_with($page, 'industry-') ? sector_by_slug(substr($page, 9)) : null;
$site = site_content();
require __DIR__ . '/header.php';
require APP_ROOT . '/views/' . $page . '.php';
require __DIR__ . '/footer.php';
