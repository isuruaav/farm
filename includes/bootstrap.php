<?php
declare(strict_types=1);

define('APP_ROOT', dirname(__DIR__));
$config = require APP_ROOT . '/config.php';
date_default_timezone_set($config['timezone']);

function config(string $key): mixed { global $config; return $config[$key] ?? null; }
function e(mixed $value): string { return htmlspecialchars((string)$value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'); }

function storage_path(string $file = ''): string
{
    $base = rtrim((string)config('storage'), '/\\');
    if (!is_dir($base) && !mkdir($base, 0700, true) && !is_dir($base)) {
        throw new RuntimeException('Application storage is unavailable.');
    }
    return $base . ($file !== '' ? DIRECTORY_SEPARATOR . $file : '');
}

if (PHP_SAPI !== 'cli') {
    header('Content-Type: text/html; charset=UTF-8');
    header('X-Content-Type-Options: nosniff');
    header('X-Frame-Options: DENY');
    header('Referrer-Policy: strict-origin-when-cross-origin');
    header('Permissions-Policy: camera=(), microphone=(), geolocation=()');
    header("Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https://images.unsplash.com; connect-src 'self'; frame-src 'none'; object-src 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'none'");
    header('Cache-Control: no-store');
    $sessionDir = storage_path('sessions');
    if (!is_dir($sessionDir)) mkdir($sessionDir, 0700, true);
    session_save_path($sessionDir);
    session_name((string)config('session_name'));
    session_set_cookie_params([
        'lifetime' => 0,
        'path' => '/',
        'secure' => !empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off',
        'httponly' => true,
        'samesite' => 'Lax',
    ]);
    ini_set('session.use_strict_mode', '1');
    session_start();
    $_SESSION['csrf'] ??= bin2hex(random_bytes(32));
}

function csrf_token(): string { return $_SESSION['csrf'] ?? ''; }
function csrf_valid(mixed $token): bool { return is_string($token) && csrf_token() !== '' && hash_equals(csrf_token(), $token); }
function form_security(string $type): void
{
    echo '<input type="hidden" name="csrf_token" value="' . e(csrf_token()) . '">';
    echo '<input type="hidden" name="type" value="' . e($type) . '">';
    echo '<input type="hidden" name="request_id" value="' . bin2hex(random_bytes(16)) . '">';
    echo '<div class="honeypot" aria-hidden="true"><label>Leave this field empty<input name="website" type="text" tabindex="-1" autocomplete="off"></label></div>';
}

function catalog(): array
{
    static $products;
    return $products ??= array_map('product_from_row', db()->query("SELECT * FROM products WHERE publication = 'published' ORDER BY position, sku")->fetchAll());
}

function product_from_row(array $row): array
{
    return ['id'=>$row['sku'],'category'=>$row['category'],'name'=>$row['name'],'title'=>$row['title'],
        'description'=>$row['description'],'detailText'=>$row['detail_text'],'image'=>$row['image'],
        'variant'=>$row['variant'],'industry'=>$row['industry'],'price'=>(float)$row['price'],'priceType'=>$row['price_type'],
        'minimumOrder'=>(int)$row['minimum_order'],'availability'=>$row['availability'],'publication'=>$row['publication'],
        'featured'=>(bool)$row['featured'],'seoDescription'=>$row['seo_description'],'updatedAt'=>$row['updated_at']];
}

function industries_data(): array
{
    static $sectors;
    if ($sectors !== null) return $sectors;
    $defaults = json_decode(file_get_contents(APP_ROOT . '/data/industries.json'), true, 512, JSON_THROW_ON_ERROR);
    $overrides = db()->query('SELECT slug, status, summary FROM industry_settings')->fetchAll(PDO::FETCH_UNIQUE);
    return $sectors = array_map(static function (array $sector) use ($overrides): array {
        if (isset($overrides[$sector['slug']])) {
            $sector['status'] = $overrides[$sector['slug']]['status'];
            $sector['description'] = $overrides[$sector['slug']]['summary'];
        }
        return $sector;
    }, $defaults);
}

function sector_by_slug(string $slug): ?array
{
    foreach (industries_data() as $sector) if ($sector['slug'] === $slug) return $sector;
    return null;
}

function project_statuses(): array { return ['planned'=>'Planned','development'=>'Under development','operational'=>'Operational','unavailable'=>'Temporarily unavailable']; }
function project_status(string $status): string
{
    $statuses = project_statuses();
    if (!isset($statuses[$status])) $status = 'planned';
    return '<span class="project-status project-status--' . e($status) . '">' . e($statuses[$status]) . '</span>';
}

function product_image(array $product): string
{
    if (!empty($product['image']) && !str_starts_with($product['image'], 'https://images.unsplash.com/')) {
        return $product['image'];
    }
    return match ($product['id'] ?? '') {
        'FL-EGG-30' => 'assets/images/products/photo-v2/egg-tray-30.webp',
        'FL-EGG-12' => 'assets/images/products/photo-v2/egg-pack-12.webp',
        'FL-EGG-06' => 'assets/images/products/photo-v2/egg-pack-6.webp',
        'FL-EGG-360' => 'assets/images/products/photo-v2/egg-crate-360.webp',
        'FL-FEED-L50' => 'assets/images/products/photo-v2/feed-layer-50kg.webp',
        'FL-FEED-C25' => 'assets/images/products/photo-v2/feed-chick-starter.webp',
        'FL-FEED-CAT50' => 'assets/images/products/photo-v2/feed-cattle-50kg.webp',
        'FL-FEED-FISH25' => 'assets/images/products/photo-v2/feed-fish-pellets.webp',
        'FL-TRAY-B100' => 'assets/images/products/photo-v2/tray-bundle-100.webp',
        'FL-TRAY-C50' => 'assets/images/products/photo-v2/tray-cartons-50.webp',
        'FL-MUSH-SH1' => 'assets/images/products/photo-v2/mushrooms-shiitake-dried.webp',
        'FL-MUSH-OY200' => 'assets/images/products/photo-v2/mushrooms-oyster-fresh.webp',
        'FL-EP-WHOLE20' => 'assets/images/products/photo-v2/egg-powder-whole.webp',
        'FL-EP-ALB1' => 'assets/images/products/photo-v2/egg-powder-albumen.webp',
        'FL-FERT-20KG' => 'assets/images/products/photo-v2/fertilizer-pellets-20kg.webp',
        'FL-FERT-10KG' => 'assets/images/products/photo-v2/fertilizer-compost-10kg.webp',
        'FL-GM-SEED25' => 'assets/images/products/photo-v2/media-seed-starting.webp',
        'FL-GM-POT50' => 'assets/images/products/photo-v2/media-potting-soil.webp',
        'FL-WT-SMART-RO' => 'assets/images/products/photo-v2/water-smart-ro.webp',
        'FL-WT-COMM-400' => 'assets/images/products/photo-v2/water-commercial-400gpd.webp',
        default => match ($product['category'] ?? '') {
            'poultry' => 'assets/images/industries/poultry.jpg',
            'trays' => 'assets/images/industries/egg-trays.jpg',
            'egg-powder' => 'assets/images/industries/egg-processing.jpg',
            'mushrooms' => 'assets/images/industries/mushrooms.jpg',
            'feed' => 'assets/images/industries/feed.jpg',
            'fertilizer' => 'assets/images/industries/fertilizer.jpg',
            'growing-media' => 'assets/images/industries/growing-media.jpg',
            'water-tech' => 'assets/images/industries/water-tech.jpg',
            default => 'assets/images/logo.jpg',
        }
    };
}

function site_content(): array
{
    static $settings;
    if ($settings !== null) return $settings;
    $defaults = ['headline'=>'Growing agriculture. Building what’s next.',
        'summary'=>'Eight connected industries. One ambition to bring agriculture, responsible manufacturing and global trade closer together.',
        'intro'=>'Rooted in Polpithigama, Sri Lanka, FOREST LANKA brings together a planned portfolio of agricultural, food, packaging and water technology ventures.',
        'phone'=>'+94 70 601 0108','whatsapp'=>'94719740798','email'=>'thilankaherath7@gmail.com',
        'address'=>'434, Thalpathwewa, Polpithigama, Kurunegala 60620, Sri Lanka.',
        'hours'=>'Mon–Sat · 8:00 AM–5:30 PM'];
    return $settings = array_replace($defaults, db()->query('SELECT key, value FROM site_settings')->fetchAll(PDO::FETCH_KEY_PAIR));
}

function app_base_path(): string
{
    $script = str_replace('\\', '/', $_SERVER['SCRIPT_NAME'] ?? '/index.php');
    $path = dirname($script);
    if (in_array(basename($path), ['admin','api'], true)) $path = dirname($path);
    return rtrim(str_replace('\\', '/', $path), '/.') . '/';
}

function site_url(string $path = ''): string
{
    $configured = trim((string)(getenv('FOREST_SITE_URL') ?: ''));
    if ($configured !== '') return rtrim($configured, '/') . '/' . ltrim($path, '/');
    $host = $_SERVER['HTTP_HOST'] ?? 'localhost';
    if (!preg_match('/^[a-z0-9.\-\[\]:]+$/i', $host)) $host = 'localhost';
    $scheme = !empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off' ? 'https' : 'http';
    return $scheme . '://' . $host . app_base_path() . ltrim($path, '/');
}

function db(): PDO
{
    static $pdo;
    if ($pdo) return $pdo;
    $pdo = new PDO('sqlite:' . storage_path('forest-lanka.sqlite'), null, null, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC]);
    $pdo->exec('PRAGMA busy_timeout = 5000; PRAGMA journal_mode = WAL; PRAGMA foreign_keys = ON;');
    if ((int)$pdo->query('PRAGMA user_version')->fetchColumn() >= 1) return $pdo;
    $pdo->exec("CREATE TABLE IF NOT EXISTS inquiries (
        id INTEGER PRIMARY KEY AUTOINCREMENT, reference TEXT NOT NULL UNIQUE, request_id TEXT NOT NULL UNIQUE,
        type TEXT NOT NULL, name TEXT NOT NULL, email TEXT NOT NULL DEFAULT '', phone TEXT NOT NULL,
        company TEXT NOT NULL DEFAULT '', country TEXT NOT NULL DEFAULT '', industry TEXT NOT NULL DEFAULT '',
        message TEXT NOT NULL DEFAULT '', details TEXT NOT NULL, items TEXT NOT NULL DEFAULT '[]',
        estimated_total REAL NOT NULL DEFAULT 0, status TEXT NOT NULL DEFAULT 'new', notes TEXT NOT NULL DEFAULT '',
        created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
        CREATE INDEX IF NOT EXISTS inquiries_status_date ON inquiries(status, created_at);
        CREATE TABLE IF NOT EXISTS admins (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE COLLATE NOCASE, password_hash TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS rate_limits (bucket TEXT PRIMARY KEY, attempts INTEGER NOT NULL, expires_at INTEGER NOT NULL);
        CREATE TABLE IF NOT EXISTS products (
            sku TEXT PRIMARY KEY, category TEXT NOT NULL, name TEXT NOT NULL, title TEXT NOT NULL,
            description TEXT NOT NULL, detail_text TEXT NOT NULL DEFAULT '', image TEXT NOT NULL DEFAULT '',
            variant TEXT NOT NULL, industry TEXT NOT NULL, price REAL NOT NULL DEFAULT 0 CHECK(price >= 0),
            price_type TEXT NOT NULL DEFAULT 'quote', minimum_order INTEGER NOT NULL DEFAULT 1 CHECK(minimum_order BETWEEN 1 AND 9999),
            availability TEXT NOT NULL DEFAULT 'on_request', publication TEXT NOT NULL DEFAULT 'published', featured INTEGER NOT NULL DEFAULT 0,
            seo_description TEXT NOT NULL DEFAULT '', position INTEGER NOT NULL DEFAULT 0, created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS industry_settings (slug TEXT PRIMARY KEY, status TEXT NOT NULL, summary TEXT NOT NULL, updated_at TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS site_settings (key TEXT PRIMARY KEY, value TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS admin_activity (id INTEGER PRIMARY KEY AUTOINCREMENT, admin_id INTEGER NOT NULL, action TEXT NOT NULL, target TEXT NOT NULL, created_at TEXT NOT NULL);");
    $now = date('Y-m-d H:i:s');
    $pdo->beginTransaction();
    try {
        if ((int)$pdo->query('SELECT COUNT(*) FROM products')->fetchColumn() === 0) {
            $products = json_decode(file_get_contents(APP_ROOT . '/data/products.json'), true, 512, JSON_THROW_ON_ERROR);
            $insert = $pdo->prepare('INSERT OR IGNORE INTO products(sku,category,name,title,description,image,variant,industry,price,price_type,featured,position,created_at,updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)');
            foreach ($products as $index=>$product) $insert->execute([$product['id'],$product['category'],$product['name'],$product['title'],$product['description'],$product['image'],$product['variant'],$product['industry'],$product['price'],$product['priceType'],in_array($product['id'],['FL-EGG-30','FL-FEED-L50','FL-TRAY-B100','FL-EP-WHOLE20'],true)?1:0,$index,$now,$now]);
        }
        $insert = $pdo->prepare('INSERT OR IGNORE INTO industry_settings(slug,status,summary,updated_at) VALUES (?,?,?,?)');
        foreach (json_decode(file_get_contents(APP_ROOT . '/data/industries.json'), true, 512, JSON_THROW_ON_ERROR) as $sector) $insert->execute([$sector['slug'],$sector['status'],$sector['description'],$now]);
        $pdo->exec('PRAGMA user_version = 1');
        $pdo->commit();
    } catch (Throwable $error) { $pdo->rollBack(); throw $error; }
    return $pdo;
}

// Atomic counters prevent parallel requests from bypassing rate limits. Never trust proxy headers.
function rate_allowed(string $scope, int $limit, int $window): bool
{
    $pdo = db();
    $bucket = $scope . ':' . hash('sha256', (string)($_SERVER['REMOTE_ADDR'] ?? 'cli'));
    $now = time();
    $query = $pdo->prepare('INSERT INTO rate_limits(bucket, attempts, expires_at) VALUES (?, 1, ?)
        ON CONFLICT(bucket) DO UPDATE SET attempts = CASE WHEN expires_at <= ? THEN 1 ELSE attempts + 1 END,
        expires_at = CASE WHEN expires_at <= ? THEN excluded.expires_at ELSE expires_at END RETURNING attempts');
    $query->execute([$bucket, $now + $window, $now, $now]);
    $allowed = (int)$query->fetchColumn() <= $limit;
    $query->closeCursor();
    $pdo->prepare('DELETE FROM rate_limits WHERE expires_at < ?')->execute([$now - 86400]);
    return $allowed;
}

function admin_logged_in(): bool
{
    if (empty($_SESSION['admin_id'])) return false;
    if (time() - (int)($_SESSION['admin_last_active'] ?? 0) > (int)config('admin_idle_seconds')) {
        unset($_SESSION['admin_id'], $_SESSION['admin_name'], $_SESSION['admin_last_active']);
        return false;
    }
    $_SESSION['admin_last_active'] = time();
    return true;
}
