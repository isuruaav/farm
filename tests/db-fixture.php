<?php
declare(strict_types=1);
if (PHP_SAPI !== 'cli' || !getenv('FOREST_STORAGE_DIR')) exit(1);
require dirname(__DIR__) . '/includes/bootstrap.php';
$input=json_decode(file_get_contents('php://stdin'),true,512,JSON_THROW_ON_ERROR);
if ($input['action']==='create-admin') {
    db()->prepare('INSERT INTO admins(username,password_hash) VALUES (?,?)')->execute([$input['username'],password_hash($input['password'],PASSWORD_DEFAULT)]);
    echo "{}";
} elseif ($input['action']==='records') {
    echo json_encode(db()->query('SELECT * FROM inquiries ORDER BY id')->fetchAll(),JSON_THROW_ON_ERROR);
} elseif ($input['action']==='reset-rates') {
    db()->exec('DELETE FROM rate_limits'); echo '{}';
}
