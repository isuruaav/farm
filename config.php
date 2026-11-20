<?php
declare(strict_types=1);

// Optional environment configuration; no database server or dependencies required.
return [
    'name' => 'FOREST LANKA',
    'timezone' => 'Asia/Colombo',
    'storage' => getenv('FOREST_STORAGE_DIR') ?: __DIR__ . '/storage',
    'session_name' => 'forest_lanka_session',
    'admin_idle_seconds' => 1800,
    'whatsapp' => '94719740798',
];
