<?php
declare(strict_types=1);
require dirname(__DIR__) . '/includes/admin-layout.php';
$values=site_content();$error='';
if ($_SERVER['REQUEST_METHOD']==='POST') {
    if (!admin_post_valid()) $error='Your session has expired. Reload this page.';
    else {
        foreach ($values as $key=>$default) $values[$key]=admin_text($key,in_array($key,['summary','intro','address'],true)?1000:180);
        if (mb_strlen($values['headline'])<10 || mb_strlen($values['summary'])<30 || mb_strlen($values['intro'])<30) $error='Enter a headline and clear introductory text.';
        elseif (!filter_var($values['email'],FILTER_VALIDATE_EMAIL) || !preg_match('/^\+?[0-9 ()-]{7,32}$/',$values['phone']) || !preg_match('/^[0-9]{7,15}$/',$values['whatsapp'])) $error='Enter a valid email, telephone number and WhatsApp number (digits only, including country code).';
        else {
            $query=db()->prepare('INSERT INTO site_settings(key,value) VALUES (?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value');
            db()->beginTransaction();try { foreach ($values as $key=>$value) $query->execute([$key,$value]);db()->commit(); } catch (Throwable $exception) { db()->rollBack();throw $exception; }
            admin_activity('website.updated','homepage and contact');header('Location: site.php?saved=1',true,303);exit;
        }
    }
}
admin_begin('Website content','site');
?><div class="admin-title"><div><p class="eyebrow">WEBSITE CONTENT</p><h1>Make your first impression count.</h1><p>Update the homepage introduction and the shared contact details without editing code.</p></div></div><?php if ($error): ?><p class="form-feedback form-error" role="alert"><?= e($error) ?></p><?php endif; ?><?php if (isset($_GET['saved'])): ?><p class="form-feedback form-success" role="status">Website content saved.</p><?php endif; ?>
<section class="editor-panel"><form method="post" class="admin-form"><input type="hidden" name="csrf_token" value="<?= e(csrf_token()) ?>"><?php foreach (['headline'=>'Homepage headline','summary'=>'Homepage summary','intro'=>'Company introduction','phone'=>'Telephone','whatsapp'=>'WhatsApp number (country code and digits only)','email'=>'Email address','address'=>'Registered contact address','hours'=>'Office hours'] as $key=>$label): ?><label for="site-<?= e($key) ?>"><?= e($label) ?></label><?php if (in_array($key,['summary','intro','address'],true)): ?><textarea id="site-<?= e($key) ?>" name="<?= e($key) ?>" required maxlength="1000" rows="3"><?= e($values[$key]) ?></textarea><?php else: ?><input id="site-<?= e($key) ?>" name="<?= e($key) ?>" type="<?= $key==='email'?'email':'text' ?>" required maxlength="180" value="<?= e($values[$key]) ?>"><?php endif; ?><?php endforeach; ?><button type="submit" class="btn-primary">Save website content</button></form></section><?php admin_end(); ?>
