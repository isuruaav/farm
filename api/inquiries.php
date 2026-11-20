<?php
declare(strict_types=1);
require dirname(__DIR__) . '/includes/bootstrap.php';
require APP_ROOT . '/includes/inquiries.php';

$wantsJson = str_contains($_SERVER['HTTP_ACCEPT'] ?? '', 'application/json') || str_contains($_SERVER['CONTENT_TYPE'] ?? '', 'application/json');
function respond(int $status, array $body): never
{
    global $wantsJson;
    http_response_code($status);
    if ($wantsJson) {
        header('Content-Type: application/json; charset=UTF-8');
        echo json_encode($body, JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);
        exit;
    }
    $_SESSION['submission_result'] = ['status'=>$status] + $body;
    header('Location: ../request-result.php', true, 303);
    exit;
}

try {
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') { header('Allow: POST'); respond(405,['ok'=>false,'message'=>'Use the inquiry form to submit a request.']); }
    if ((int)($_SERVER['CONTENT_LENGTH'] ?? 0) > 65536) respond(413,['ok'=>false,'message'=>'The request is too large.']);
    $input = $_POST;
    if (str_contains($_SERVER['CONTENT_TYPE'] ?? '', 'application/json')) {
        try { $input = json_decode(file_get_contents('php://input'), true, 32, JSON_THROW_ON_ERROR); }
        catch (JsonException) { respond(400,['ok'=>false,'message'=>'The request could not be read.']); }
    }
    if (!is_array($input)) respond(400,['ok'=>false,'message'=>'Invalid request.']);
    if (!csrf_valid($input['csrf_token'] ?? $_SERVER['HTTP_X_CSRF_TOKEN'] ?? null)) respond(419,['ok'=>false,'message'=>'Your session has expired. Reload this page before submitting.']);
    if (!empty($input['website'])) respond(422,['ok'=>false,'message'=>'The request could not be accepted.']);
    if (!rate_allowed('inquiry', 12, 600)) { header('Retry-After: 600'); respond(429,['ok'=>false,'message'=>'Too many requests. Please try again in 10 minutes or contact us by phone.']); }
    $saved = save_inquiry(validate_inquiry($input));
    respond(201,['ok'=>true,'message'=>'Your request has been saved. Our team will review it and contact you.','reference'=>$saved['reference'],'estimated_total'=>(float)$saved['estimated_total']]);
} catch (InquiryValidation $error) {
    respond(422,['ok'=>false,'message'=>$error->getMessage(),'errors'=>$error->errors]);
} catch (Throwable $error) {
    error_log('Forest Lanka inquiry error: ' . $error->getMessage());
    respond(503,['ok'=>false,'message'=>'We could not save your request. Your form has been kept. Please try again or contact us by phone.']);
}
