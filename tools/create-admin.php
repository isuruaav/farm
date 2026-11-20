<?php
declare(strict_types=1);
if (PHP_SAPI !== 'cli') { http_response_code(404); exit; }
require dirname(__DIR__) . '/includes/bootstrap.php';
$username = $argv[1] ?? '';
if (!preg_match('/^[a-zA-Z0-9_.-]{3,80}$/', $username)) {
    fwrite(STDERR,"Usage: php tools/create-admin.php <username>\nUse 3–80 letters, numbers, dots, underscores or hyphens.\n"); exit(1);
}
// Read secrets from stdin, never command-line arguments or tracked files.
function password_prompt(string $prompt): string
{
    fwrite(STDOUT,$prompt);
    if (PHP_OS_FAMILY === 'Windows' && function_exists('shell_exec')) {
        $command = 'powershell.exe -NoProfile -Command "$p = Read-Host -AsSecureString; $b = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($p); try { [Runtime.InteropServices.Marshal]::PtrToStringBSTR($b) } finally { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($b) }"';
        return rtrim((string)shell_exec($command),"\r\n");
    }
    $hidden = PHP_OS_FAMILY !== 'Windows' && function_exists('shell_exec') && function_exists('stream_isatty') && stream_isatty(STDIN);
    if ($hidden) shell_exec('stty -echo');
    try { $password=rtrim((string)fgets(STDIN),"\r\n"); } finally { if ($hidden) shell_exec('stty echo'); }
    fwrite(STDOUT,"\n"); return $password;
}
$password = password_prompt('New password (at least 12 characters): ');
$confirmation = password_prompt('Confirm password: ');
if (mb_strlen($password)<12 || strlen($password)>72 || !hash_equals($password,$confirmation)) {
    fwrite(STDERR,"Passwords must match and contain at least 12 characters (at most 72 bytes).\n"); exit(1);
}
$pdo=db();
$query=$pdo->prepare('SELECT id FROM admins WHERE username=?');$query->execute([$username]);
if ($query->fetch()) { fwrite(STDERR,"That username already exists. No account was changed.\n"); exit(1); }
$pdo->prepare('INSERT INTO admins(username,password_hash) VALUES (?,?)')->execute([$username,password_hash($password,PASSWORD_DEFAULT)]);
fwrite(STDOUT,"Administrator created. Sign in at /farm/admin/ on WAMP.\n");
