<?php
declare(strict_types=1);
require_once __DIR__ . '/bootstrap.php';
if (!admin_logged_in()) { header('Location: ./', true, 303); exit; }

function admin_activity(string $action, string $target): void
{
    db()->prepare('INSERT INTO admin_activity(admin_id,action,target,created_at) VALUES (?,?,?,?)')
        ->execute([(int)$_SESSION['admin_id'],$action,$target,date('Y-m-d H:i:s')]);
}

function admin_tabs(string $active): void
{
    echo '<nav class="admin-tabs" aria-label="Staff tools">';
    foreach (['inquiries'=>['./','Inquiry desk'],'catalog'=>['catalog.php','Product catalog'],'industries'=>['industries.php','Project stages'],'site'=>['site.php','Website content']] as $key=>$item) {
        echo '<a href="'.e($item[0]).'"'.($active===$key?' aria-current="page"':'').'>'.admin_icon($key).e($item[1]).'</a>';
    }
    echo '</nav>';
}

function admin_icon(string $name): string
{
    $paths = [
        'inquiries'=>'<path d="M4 4h16v12H8l-4 4V4Z"/><path d="M8 8h8M8 12h5"/>',
        'catalog'=>'<path d="m12 3 9 5-9 5-9-5 9-5Z"/><path d="M3 8v9l9 5 9-5V8M12 13v9M7.5 5.5l9 5"/>',
        'industries'=>'<path d="M4 20V10h5v10M9 20V4h6v16M15 20v-7h5v7M2 20h20"/>',
        'site'=>'<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M8 9v11M6 6.5h.01M9 6.5h.01"/>',
        'new'=>'<path d="M4 4h16v16H4zM4 14h5l2 3h2l2-3h5M12 7v4M10 9h4"/>',
        'in_progress'=>'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
        'completed'=>'<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>',
        'archived'=>'<rect x="3" y="3" width="18" height="5" rx="1"/><path d="M5 8v13h14V8M10 12h4"/>',
        'download'=>'<path d="M12 3v12m-5-5 5 5 5-5M4 15v6h16v-6"/>',
        'arrow'=>'<path d="M5 12h14m-5-5 5 5-5 5"/>',
        'logout'=>'<path d="M9 4H4v16h5M9 12h12m-4-4 4 4-4 4"/>',
    ];
    return '<svg class="admin-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'.($paths[$name] ?? $paths['inquiries']).'</svg>';
}

function admin_header(string $label = 'BUSINESS DESK', bool $showLogout = false): void
{
    ?><header class="admin-header"><a href="./" class="admin-brand"><img src="../assets/images/logo.jpg" width="46" height="46" alt=""><div><strong>FOREST LANKA</strong><span><?= e($label) ?></span></div></a><div><a href="../index.php">View website &nearr;</a><?php if ($showLogout): ?><form method="post"><input type="hidden" name="csrf_token" value="<?= e(csrf_token()) ?>"><input type="hidden" name="action" value="logout"><button type="submit"><?= admin_icon('logout') ?> Sign out <span class="admin-user-name">&middot; <?= e($_SESSION['admin_name']) ?></span></button></form><?php else: ?><a href="./">Inquiry desk &rarr;</a><?php endif; ?></div></header><?php
}

function admin_begin(string $title, string $active): void
{
    ?><!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title><?= e($title) ?> | FOREST LANKA</title><link rel="stylesheet" href="../assets/css/utilities.css?v=4.3.5-light"></head><body class="admin-body"><?php admin_header(); ?><main class="admin-main"><?php admin_tabs($active); ?><?php
}
function admin_end(): void { echo '</main></body></html>'; }
function admin_post_valid(): bool
{
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') return false;
    if (!csrf_valid($_POST['csrf_token'] ?? null)) { http_response_code(419); return false; }
    return true;
}
function admin_text(string $name, int $max = 5000): string
{
    return is_string($_POST[$name] ?? null) ? mb_substr(trim($_POST[$name]), 0, $max) : '';
}
