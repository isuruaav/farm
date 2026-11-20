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
        echo '<a href="'.e($item[0]).'"'.($active===$key?' aria-current="page"':'').'>'.e($item[1]).'</a>';
    }
    echo '</nav>';
}

function admin_begin(string $title, string $active): void
{
    ?><!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title><?= e($title) ?> | FOREST LANKA</title><link rel="stylesheet" href="../assets/css/utilities.css?v=4.3.5-design"></head><body class="admin-body"><header class="admin-header"><a href="./" class="admin-brand">FOREST LANKA <span>BUSINESS DESK</span></a><div><a href="../index.php">View website</a><a href="./">Inquiry desk</a></div></header><main class="admin-main"><?php admin_tabs($active); ?><?php
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
