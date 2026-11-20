<?php
declare(strict_types=1);
require dirname(__DIR__) . '/includes/admin-layout.php';
$error='';
if ($_SERVER['REQUEST_METHOD']==='POST') {
    $slug=admin_text('slug',50);$status=admin_text('status',25);$summary=admin_text('summary',1200);
    if (!admin_post_valid()) $error='Your session has expired. Reload this page.';
    elseif (!sector_by_slug($slug) || !isset(project_statuses()[$status]) || mb_strlen($summary)<20) $error='Choose a valid project stage and enter a summary of at least 20 characters.';
    else {
        db()->prepare('UPDATE industry_settings SET status=?,summary=?,updated_at=? WHERE slug=?')->execute([$status,$summary,date('Y-m-d H:i:s'),$slug]);
        admin_activity('industry.updated',$slug);header('Location: industries.php?saved=1',true,303);exit;
    }
}
admin_begin('Project stages','industries');
?><div class="admin-title"><div><p class="eyebrow">INDUSTRY PORTFOLIO</p><h1>Keep every project stage clear.</h1><p>Stages appear on the homepage, industry pages and investment portfolio. Change them only when confirmed.</p></div></div><?php if ($error): ?><p class="form-feedback form-error" role="alert"><?= e($error) ?></p><?php endif; ?><?php if (isset($_GET['saved'])): ?><p class="form-feedback form-success" role="status">Project stage and summary updated.</p><?php endif; ?>
<div class="industry-editors"><?php foreach (industries_data() as $sector): ?><section class="editor-panel"><div class="editor-heading"><h2><?= e($sector['shortName']) ?></h2><?= project_status($sector['status']) ?></div><form method="post" class="admin-form"><input type="hidden" name="csrf_token" value="<?= e(csrf_token()) ?>"><input type="hidden" name="slug" value="<?= e($sector['slug']) ?>"><label for="status-<?= e($sector['slug']) ?>">Public project stage</label><select id="status-<?= e($sector['slug']) ?>" name="status"><?php foreach (project_statuses() as $key=>$label): ?><option value="<?= e($key) ?>" <?= $sector['status']===$key?'selected':'' ?>><?= e($label) ?></option><?php endforeach; ?></select><label for="summary-<?= e($sector['slug']) ?>">Public summary</label><textarea id="summary-<?= e($sector['slug']) ?>" name="summary" rows="4" required minlength="20" maxlength="1200"><?= e($sector['description']) ?></textarea><button type="submit" class="btn-primary">Save project</button><a href="../industry-<?= e($sector['slug']) ?>.php">View industry page</a></form></section><?php endforeach; ?></div><?php admin_end(); ?>
