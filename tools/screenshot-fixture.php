<?php
declare(strict_types=1);

// CLI only. Never allow this helper to write into the real application storage.
$captureStorage = str_replace('\\', '/', (string)getenv('FOREST_STORAGE_DIR'));
$cacheRoot = str_replace('\\', '/', dirname(__DIR__)) . '/.cache/';
if (PHP_SAPI !== 'cli' || !str_starts_with($captureStorage, $cacheRoot . 'screenshots-')
    || !preg_match('~/screenshots-[^/]+/storage$~', $captureStorage)) {
    fwrite(STDERR, "Use npm run screenshots to prepare disposable screenshot data.\n");
    exit(1);
}
require dirname(__DIR__) . '/includes/bootstrap.php';
require APP_ROOT . '/includes/inquiries.php';
$input = json_decode(file_get_contents('php://stdin'), true, 512, JSON_THROW_ON_ERROR);
$pdo = db();

// Copy current public content through a read-only connection. Customer requests,
// staff credentials, sessions and activity records stay in the original database.
$sourceFile = rtrim($input['sourceStorage'], '/\\') . '/forest-lanka.sqlite';
if (is_file($sourceFile)) {
    $openFlags = defined('Pdo\\Sqlite::ATTR_OPEN_FLAGS') ? constant('Pdo\\Sqlite::ATTR_OPEN_FLAGS') : constant('PDO::SQLITE_ATTR_OPEN_FLAGS');
    $readOnly = defined('Pdo\\Sqlite::OPEN_READONLY') ? constant('Pdo\\Sqlite::OPEN_READONLY') : constant('PDO::SQLITE_OPEN_READONLY');
    $source = new PDO('sqlite:' . $sourceFile, null, null, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        $openFlags => $readOnly,
    ]);
    $source->beginTransaction();
    $pdo->beginTransaction();
    try {
        foreach (['products', 'industry_settings', 'site_settings'] as $table) {
            $exists = $source->prepare("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?");
            $exists->execute([$table]);
            if (!$exists->fetchColumn()) continue;
            $rows = $source->query('SELECT * FROM ' . $table)->fetchAll();
            $pdo->exec('DELETE FROM ' . $table);
            foreach ($rows as $row) {
                $columns = implode(',', array_map(static fn($key) => '"' . str_replace('"', '""', $key) . '"', array_keys($row)));
                $placeholders = implode(',', array_fill(0, count($row), '?'));
                $pdo->prepare("INSERT INTO $table ($columns) VALUES ($placeholders)")->execute(array_values($row));
            }
        }
        $pdo->commit();
        $source->commit();
    } catch (Throwable $error) {
        if ($pdo->inTransaction()) $pdo->rollBack();
        if ($source->inTransaction()) $source->rollBack();
        throw $error;
    }
    $source = null;
}

$pdo->prepare('INSERT INTO admins(username,password_hash) VALUES (?,?)')->execute([
    $input['username'], password_hash($input['password'], PASSWORD_DEFAULT),
]);
save_inquiry(validate_inquiry([
    'type' => 'contact', 'request_id' => bin2hex(random_bytes(16)),
    'name' => 'Demo Customer', 'email' => 'demo@example.test', 'phone' => '+94712345678',
    'company' => 'Demo Company', 'country' => 'Sri Lanka', 'industry' => 'ind_poultry',
    'inquiry_type' => 'other', 'message' => 'Sample inquiry for website screenshots only.', 'consent' => '1',
]));
echo json_encode([
    'products' => array_column(catalog(), 'id'),
    'requestId' => (int)$pdo->query('SELECT id FROM inquiries ORDER BY id LIMIT 1')->fetchColumn(),
], JSON_THROW_ON_ERROR);
