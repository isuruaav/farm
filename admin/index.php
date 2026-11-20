<?php
declare(strict_types=1);
require dirname(__DIR__) . '/includes/bootstrap.php';
$pdo = db();
$error = '';
$statuses = ['new'=>'New','in_progress'=>'In progress','completed'=>'Completed','archived'=>'Archived'];
$types = ['contact'=>'General inquiries','sector'=>'Industry quotations','order'=>'Product quotations','export'=>'Export requests','investment'=>'Investment interest','partner'=>'Partnerships'];
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!csrf_valid($_POST['csrf_token'] ?? null)) {
        $error = 'Your session has expired. Reload the page and try again.';
        http_response_code(419);
    } elseif (($_POST['action'] ?? '') === 'login') {
        $username = is_string($_POST['username'] ?? null) ? trim($_POST['username']) : '';
        $password = is_string($_POST['password'] ?? null) ? $_POST['password'] : '';
        if (!rate_allowed('admin-login', 8, 900)) {
            $error = 'Too many sign-in attempts. Try again in 15 minutes.';
            http_response_code(429);
        } else {
            $query = $pdo->prepare('SELECT * FROM admins WHERE username = ?');
            $query->execute([mb_substr($username, 0, 80)]);
            $admin = $query->fetch();
            $dummyHash = '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2uheWG/igi';
            $valid = password_verify(mb_substr($password, 0, 1024), $admin['password_hash'] ?? $dummyHash);
            if ($admin && $valid) {
                session_regenerate_id(true);
                $_SESSION['admin_id'] = (int)$admin['id'];
                $_SESSION['admin_name'] = $admin['username'];
                $_SESSION['admin_last_active'] = time();
                $_SESSION['csrf'] = bin2hex(random_bytes(32));
                header('Location: ./', true, 303); exit;
            }
            $error = 'The username or password is incorrect.';
        }
    } elseif (admin_logged_in()) {
        if (($_POST['action'] ?? '') === 'logout') {
            $_SESSION = [];
            session_regenerate_id(true);
            header('Location: ./', true, 303); exit;
        }
        if (($_POST['action'] ?? '') === 'update') {
            $status = is_string($_POST['status'] ?? null) ? $_POST['status'] : '';
            $notes = is_string($_POST['notes'] ?? null) ? trim($_POST['notes']) : '';
            $id = filter_var($_POST['id'] ?? 0, FILTER_VALIDATE_INT);
            if (!isset($statuses[$status]) || mb_strlen($notes) > 5000 || !$id) $error = 'Check the status and notes before saving.';
            else {
                $pdo->prepare('UPDATE inquiries SET status = ?, notes = ?, updated_at = ? WHERE id = ?')->execute([$status,$notes,date('Y-m-d H:i:s'),$id]);
                $_SESSION['admin_flash'] = 'Request updated.';
                header('Location: ./?id=' . $id, true, 303); exit;
            }
        }
    }
}
$loggedIn = admin_logged_in();
if ($loggedIn) require APP_ROOT . '/includes/admin-layout.php';
$adminCount = (int)$pdo->query('SELECT COUNT(*) FROM admins')->fetchColumn();
$flash = $_SESSION['admin_flash'] ?? '';
unset($_SESSION['admin_flash']);
$queryText = is_string($_GET['q'] ?? null) ? mb_substr(trim($_GET['q']),0,180) : '';
$statusFilter = is_string($_GET['status'] ?? null) && isset($statuses[$_GET['status']]) ? $_GET['status'] : '';
$typeFilter = is_string($_GET['type'] ?? null) && isset($types[$_GET['type']]) ? $_GET['type'] : '';
$conditions = []; $params = [];
if ($queryText !== '') {
    $conditions[] = "(reference LIKE ? ESCAPE '\\' OR name LIKE ? ESCAPE '\\' OR email LIKE ? ESCAPE '\\' OR company LIKE ? ESCAPE '\\')";
    $needle = '%' . str_replace(['\\','%','_'],['\\\\','\\%','\\_'],$queryText) . '%';
    array_push($params,$needle,$needle,$needle,$needle);
}
if ($statusFilter) { $conditions[] = 'status = ?'; $params[] = $statusFilter; }
if ($typeFilter) { $conditions[] = 'type = ?'; $params[] = $typeFilter; }
$where = $conditions ? ' WHERE ' . implode(' AND ',$conditions) : '';

if ($loggedIn && ($_GET['download'] ?? '') === 'csv') {
    if (!csrf_valid($_GET['token'] ?? null)) { http_response_code(403); exit('Invalid export token.'); }
    $query = $pdo->prepare('SELECT reference,type,status,name,email,phone,company,country,industry,message,estimated_total,created_at,updated_at FROM inquiries' . $where . ' ORDER BY id DESC LIMIT 10000');
    $query->execute($params);
    header('Content-Type: text/csv; charset=UTF-8');
    header('Content-Disposition: attachment; filename="forest-lanka-inquiries-' . date('Y-m-d') . '.csv"');
    $output = fopen('php://output','w');
    fwrite($output, "\xEF\xBB\xBF");
    fputcsv($output,['Reference','Type','Status','Name','Email','Phone','Company','Country','Industry','Message','Estimated total (LKR)','Created (Asia/Colombo)','Updated (Asia/Colombo)'],',','"','');
    while ($row = $query->fetch()) {
        // Spreadsheet applications must treat untrusted user content as text.
        $row = array_map(static fn($value) => preg_match('/^[\s\x00-\x1f]*[=+@-]/u',(string)$value) ? "'" . $value : $value,$row);
        fputcsv($output,$row,',','"','');
    }
    fclose($output); exit;
}
$selected = null; $records = []; $total = 0; $counts = []; $pageNumber = 1; $pageCount = 1;
if ($loggedIn) {
    $counts = $pdo->query('SELECT status, COUNT(*) AS total FROM inquiries GROUP BY status')->fetchAll(PDO::FETCH_KEY_PAIR);
    $query = $pdo->prepare('SELECT COUNT(*) FROM inquiries' . $where); $query->execute($params); $total = (int)$query->fetchColumn();
    $pageCount = max(1,(int)ceil($total/20));
    $pageNumber = min($pageCount,max(1,(int)(is_scalar($_GET['page'] ?? null) ? $_GET['page'] : 1)));
    $query = $pdo->prepare('SELECT * FROM inquiries' . $where . ' ORDER BY id DESC LIMIT 20 OFFSET ' . (($pageNumber-1)*20)); $query->execute($params); $records = $query->fetchAll();
    if (isset($_GET['id']) && is_scalar($_GET['id'])) { $query = $pdo->prepare('SELECT * FROM inquiries WHERE id = ?'); $query->execute([(int)$_GET['id']]); $selected = $query->fetch() ?: null; }
}
function filter_url(array $changes): string { return './?' . http_build_query(array_merge(array_intersect_key($_GET,array_flip(['q','status','type','page'])),$changes)); }
?><!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex,nofollow"><title><?= $loggedIn?'Inquiry desk':'Staff sign in' ?> | FOREST LANKA</title><link rel="icon" href="../assets/images/logo.jpg"><link rel="stylesheet" href="../assets/css/utilities.css?v=4.3.5-design"></head>
<body class="admin-body">
<?php if (!$loggedIn): ?>
<main class="login-panel"><a class="wordmark" href="../index.php">FOREST LANKA</a><p class="eyebrow">STAFF PORTAL</p><h1>Welcome back.</h1><p>Sign in to manage customer inquiries and quotation requests.</p>
<?php if ($adminCount===0): ?><div class="admin-notice">This portal is ready for setup. The site owner can create the first account using the command in <strong>README.md</strong>.</div><?php endif; ?>
<?php if ($error): ?><p class="form-feedback form-error" role="alert"><?= e($error) ?></p><?php endif; ?>
<form method="post" class="admin-form"><input type="hidden" name="csrf_token" value="<?= e(csrf_token()) ?>"><input type="hidden" name="action" value="login"><label for="username">Username</label><input id="username" name="username" required maxlength="80" autocomplete="username"><label for="password">Password</label><input type="password" id="password" name="password" required maxlength="1024" autocomplete="current-password"><button class="btn-primary" type="submit">Sign in</button></form><a class="return-link" href="../index.php">Return to website</a></main>
<?php else: ?>
<header class="admin-header"><a class="admin-brand" href="./">FOREST LANKA <span>INQUIRY DESK</span></a><div><a href="../index.php">View website</a><form method="post"><input type="hidden" name="csrf_token" value="<?= e(csrf_token()) ?>"><input type="hidden" name="action" value="logout"><button type="submit">Sign out · <?= e($_SESSION['admin_name']) ?></button></form></div></header>
<main class="admin-main"><?php admin_tabs('inquiries'); ?><div class="admin-title"><div><p class="eyebrow">CUSTOMER RELATIONSHIPS</p><h1>Your inquiry desk</h1><p>Review requests, follow up with customers and track progress.</p></div><a class="btn-secondary" href="<?= e(filter_url(['download'=>'csv','token'=>csrf_token()])) ?>">Export CSV</a></div>
<?php if ($error): ?><p class="form-feedback form-error" role="alert"><?= e($error) ?></p><?php endif; ?><?php if ($flash): ?><p class="form-feedback form-success" role="status"><?= e($flash) ?></p><?php endif; ?>
<div class="stat-grid"><?php foreach ($statuses as $value=>$label): ?><a href="./?status=<?= e($value) ?>" class="stat-card"><span><?= e($label) ?></span><strong><?= (int)($counts[$value] ?? 0) ?></strong></a><?php endforeach; ?></div>
<?php if ($selected): $details = json_decode($selected['details'],true); $items = json_decode($selected['items'],true); ?>
<section class="request-detail"><div class="detail-title"><div><p class="eyebrow"><?= e($types[$selected['type']] ?? $selected['type']) ?></p><h2><?= e($selected['reference']) ?></h2><p><?= e($selected['created_at']) ?> · Asia/Colombo</p></div><a href="./" class="btn-secondary">Back to all requests</a></div>
<div class="detail-grid"><div><dl class="request-fields"><?php foreach ($details as $key=>$value): if ($key==='type' || $value==='') continue; ?><div><dt><?= e(ucwords(str_replace('_',' ',$key))) ?></dt><dd><?= nl2br(e($value)) ?></dd></div><?php endforeach; ?></dl>
<?php if ($items): ?><h3>Requested products</h3><div class="table-scroll"><table><thead><tr><th>Product</th><th>Quantity</th><th>Estimate</th></tr></thead><tbody><?php foreach ($items as $item): ?><tr><td><?= e($item['name']) ?><small><?= e($item['variant']) ?></small></td><td><?= (int)$item['quantity'] ?></td><td><?= $item['priceType']==='fixed'?'LKR '.number_format($item['price']*$item['quantity'],2):'Quote' ?></td></tr><?php endforeach; ?></tbody></table></div><p><strong>Listed estimate: LKR <?= number_format((float)$selected['estimated_total'],2) ?></strong> · excludes quotation-only items and delivery.</p><?php endif; ?></div>
<form method="post" class="admin-form status-form"><input type="hidden" name="csrf_token" value="<?= e(csrf_token()) ?>"><input type="hidden" name="action" value="update"><input type="hidden" name="id" value="<?= (int)$selected['id'] ?>"><label for="status">Request status</label><select id="status" name="status"><?php foreach ($statuses as $value=>$label): ?><option value="<?= e($value) ?>" <?= $selected['status']===$value?'selected':'' ?>><?= e($label) ?></option><?php endforeach; ?></select><label for="notes">Internal follow-up notes</label><textarea id="notes" name="notes" rows="7" maxlength="5000"><?= e($selected['notes']) ?></textarea><p class="admin-hint">Only signed-in staff can see these notes.</p><button type="submit" class="btn-primary">Save changes</button></form></div></section>
<?php endif; ?>
<section class="records-panel"><form method="get" class="admin-filters"><div><label for="search">Search requests</label><input id="search" name="q" value="<?= e($queryText) ?>" placeholder="Reference, name, email or company" maxlength="180"></div><div><label for="filter-type">Request type</label><select name="type" id="filter-type"><option value="">All types</option><?php foreach ($types as $value=>$label): ?><option value="<?= e($value) ?>" <?= $typeFilter===$value?'selected':'' ?>><?= e($label) ?></option><?php endforeach; ?></select></div><div><label for="filter-status">Status</label><select name="status" id="filter-status"><option value="">All statuses</option><?php foreach ($statuses as $value=>$label): ?><option value="<?= e($value) ?>" <?= $statusFilter===$value?'selected':'' ?>><?= e($label) ?></option><?php endforeach; ?></select></div><button class="btn-primary" type="submit">Filter</button><a href="./">Reset</a></form>
<div class="records-heading"><h2>Requests <span><?= $total ?></span></h2><p>Newest first · times in Asia/Colombo</p></div>
<?php if (!$records): ?><div class="empty-state"><h3>No requests found</h3><p>New customer requests will appear here. Try clearing your filters.</p></div><?php else: ?><div class="table-scroll"><table><thead><tr><th>Reference / date</th><th>Customer</th><th>Type</th><th>Status</th><th>Action</th></tr></thead><tbody><?php foreach ($records as $record): ?><tr><td><strong><?= e($record['reference']) ?></strong><small><?= e($record['created_at']) ?></small></td><td><?= e($record['name']) ?><small><?= e($record['email'] ?: $record['phone']) ?></small></td><td><?= e($types[$record['type']] ?? $record['type']) ?></td><td><span class="status-pill status-<?= e($record['status']) ?>"><?= e($statuses[$record['status']] ?? $record['status']) ?></span></td><td><a class="review-link" href="<?= e(filter_url(['id'=>$record['id']])) ?>">Review<span class="sr-only"> <?= e($record['reference']) ?></span></a></td></tr><?php endforeach; ?></tbody></table></div><?php endif; ?>
<nav class="pagination" aria-label="Request pages"><span>Page <?= $pageNumber ?> of <?= $pageCount ?></span><div><?php if ($pageNumber>1): ?><a class="btn-secondary" href="<?= e(filter_url(['page'=>$pageNumber-1])) ?>">Previous</a><?php endif; ?><?php if ($pageNumber<$pageCount): ?><a class="btn-secondary" href="<?= e(filter_url(['page'=>$pageNumber+1])) ?>">Next</a><?php endif; ?></div></nav></section></main>
<?php endif; ?></body></html>
