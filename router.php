<?php
declare(strict_types=1);
// Local PHP development server: php -S 127.0.0.1:8080 router.php
$path = rawurldecode(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH) ?: '/');
if (preg_match('~(?:^|/)\.|(?:^|/)(?:storage|includes|views|data|tests|tools|node_modules|__pycache__)(?:/|$)|\.(?:py|sqlite|db|zip|json|log|md|cjs)$~i', $path)
    || in_array($path, ['/config.php', '/router.php'], true)) {
    http_response_code(403); exit('Forbidden');
}
if (preg_match('~^/([a-z0-9-]+)\.html$~', $path, $match) && is_file(__DIR__ . '/' . $match[1] . '.php')) {
    header('Location: /' . $match[1] . '.php' . (isset($_SERVER['QUERY_STRING']) && $_SERVER['QUERY_STRING'] !== '' ? '?' . $_SERVER['QUERY_STRING'] : ''), true, 301); exit;
}
if ($path === '/sitemap.xml') { require __DIR__.'/sitemap.php'; exit; }
if ($path === '/robots.txt') { require __DIR__.'/robots.php'; exit; }
if ($path === '/' || $path === '/admin/' || is_file(__DIR__ . $path)) return false;
$page = '404'; require __DIR__ . '/includes/render.php';
