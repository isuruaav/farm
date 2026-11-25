<?php
declare(strict_types=1);
require __DIR__ . '/includes/bootstrap.php';
$result = $_SESSION['submission_result'] ?? null;
unset($_SESSION['submission_result']);
if (!$result) { header('Location: contact.php'); exit; }
$success = !empty($result['ok']);
?><!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Request <?= $success?'saved':'needs attention' ?> | FOREST LANKA</title><link rel="stylesheet" href="assets/css/utilities.css?v=4.3.5-light"></head><body><main class="standalone-panel"><a href="index.php" class="wordmark">FOREST LANKA</a><h1><?= $success?'Thank you. Your request is saved.':'Please check your request.' ?></h1><p><?= e($result['message']) ?></p><?php if (!empty($result['reference'])): ?><p class="reference-number"><?= e($result['reference']) ?></p><p>Keep this reference when contacting our team.</p><?php endif; ?><?php if (!empty($result['errors'])): ?><ul class="list-disc pl-5"><?php foreach ($result['errors'] as $name=>$message): ?><li><?= e(ucwords(str_replace('_',' ',$name))) ?>: <?= e($message) ?></li><?php endforeach; ?></ul><?php endif; ?><div class="drawer-buttons"><?php if (!$success): ?><button class="btn-primary" onclick="history.back()">Return to form</button><?php endif; ?><a href="contact.php" class="btn-secondary">Contact our team</a><a href="products.php" class="btn-primary">Explore products</a></div></main></body></html>
