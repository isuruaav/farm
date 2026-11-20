<?php
declare(strict_types=1);

final class InquiryValidation extends RuntimeException
{
    public function __construct(public readonly array $errors) { parent::__construct('Please check the highlighted fields.'); }
}

function validate_inquiry(array $input): array
{
    $type = is_string($input['type'] ?? null) ? $input['type'] : '';
    $schemas = json_decode(file_get_contents(APP_ROOT . '/data/forms.json'), true, 512, JSON_THROW_ON_ERROR);
    $schemas['order'] = [
        'name'=>['required'=>true,'max'=>180], 'email'=>['required'=>false,'type'=>'email','max'=>254],
        'phone'=>['required'=>true,'type'=>'tel','max'=>32], 'city'=>['required'=>true,'max'=>180],
        'address'=>['required'=>true,'max'=>300], 'message'=>['required'=>false,'max'=>5000],
        'payment_method'=>['required'=>true,'options'=>['cash_on_delivery','bank_transfer','b2b_quotation'],'max'=>40],
    ];
    if (!isset($schemas[$type])) throw new InquiryValidation(['type'=>'Choose a valid request type.']);
    $errors = [];
    $clean = ['type'=>$type];
    foreach ($schemas[$type] as $name=>$rules) {
        $value = $input[$name] ?? '';
        if (!is_scalar($value)) { $errors[$name] = 'Enter a valid value.'; continue; }
        $value = trim((string)$value);
        if (preg_match('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/', $value) || !mb_check_encoding($value, 'UTF-8')) {
            $errors[$name] = 'Enter valid text.';
        } elseif (($rules['required'] ?? false) && $value === '') {
            $errors[$name] = 'This field is required.';
        } elseif (mb_strlen($value) > ($rules['max'] ?? 180)) {
            $errors[$name] = 'This field is too long.';
        } elseif ($value !== '' && isset($rules['options']) && !in_array($value, $rules['options'], true)) {
            $errors[$name] = 'Choose an available option.';
        } elseif ($value !== '' && ($rules['type'] ?? '') === 'email' && !filter_var($value, FILTER_VALIDATE_EMAIL)) {
            $errors[$name] = 'Enter a valid email address.';
        } elseif ($value !== '' && ($rules['type'] ?? '') === 'tel' && (!preg_match('/^\+?[0-9 ()\-.]{7,32}$/', $value) || strlen(preg_replace('/\D/', '', $value)) < 7 || strlen(preg_replace('/\D/', '', $value)) > 15)) {
            $errors[$name] = 'Enter a phone number with 7–15 digits, including country code.';
        }
        $clean[$name] = $value;
    }
    if (mb_strlen($clean['name'] ?? '') < 2) $errors['name'] = 'Enter your full name.';
    if (($input['consent'] ?? '') !== '1') $errors['consent'] = 'Please agree to be contacted about your request.';
    if (!is_string($input['request_id'] ?? null) || !preg_match('/^[a-f0-9]{32}$/', $input['request_id'])) $errors['request_id'] = 'Reload the page and try again.';
    $items = [];
    $total = 0;
    if ($type === 'order') {
        $rawItems = $input['items'] ?? [];
        if (is_string($rawItems)) {
            try { $rawItems = json_decode($rawItems, true, 32, JSON_THROW_ON_ERROR); }
            catch (JsonException) { $rawItems = null; }
        }
        if (!is_array($rawItems) || !array_is_list($rawItems) || count($rawItems) < 1 || count($rawItems) > 50) {
            $errors['items'] = 'Add between 1 and 50 products to your cart.';
        } else {
            $products = array_column(catalog(), null, 'id');
            $quantities = [];
            foreach ($rawItems as $item) {
                $id = is_array($item) && is_string($item['id'] ?? null) ? $item['id'] : '';
                $quantity = is_array($item) ? filter_var($item['quantity'] ?? null, FILTER_VALIDATE_INT) : false;
                if (!isset($products[$id]) || $products[$id]['availability'] === 'unavailable' || $quantity === false || $quantity < 1 || $quantity > 9999) {
                    $errors['items'] = 'Some cart items are invalid. Refresh your cart and try again.'; break;
                }
                $quantities[$id] = ($quantities[$id] ?? 0) + $quantity;
                if ($quantities[$id] > 9999) { $errors['items'] = 'The maximum quantity per product is 9,999.'; break; }
            }
            if (!isset($errors['items'])) foreach ($quantities as $id=>$quantity) {
                $product = $products[$id];
                if ($quantity < ($product['minimumOrder'] ?? 1)) {
                    $errors['items'] = $product['name'] . ' requires a minimum quantity of ' . $product['minimumOrder'] . '.';
                    break;
                }
                $items[] = ['id'=>$id,'name'=>$product['name'],'variant'=>$product['variant'],'quantity'=>$quantity,'price'=>$product['price'],'priceType'=>$product['priceType']];
                if ($product['priceType'] === 'fixed') $total += $quantity * (float)$product['price'];
            }
        }
    }
    if ($errors) throw new InquiryValidation($errors);
    return ['fields'=>$clean,'items'=>$items,'total'=>round($total,2),'request_id'=>$input['request_id']];
}

function save_inquiry(array $validated): array
{
    $pdo = db();
    $fields = $validated['fields'];
    $prefix = ['contact'=>'INQ','sector'=>'SEC','export'=>'EXP','investment'=>'INV','partner'=>'PRT','order'=>'ORD'][$fields['type']];
    $reference = $prefix . '-' . date('ymd') . '-' . strtoupper(bin2hex(random_bytes(4)));
    $now = date('Y-m-d H:i:s');
    // A unique request ID makes retries safe if the network response was lost.
    $query = $pdo->prepare('INSERT INTO inquiries(reference,request_id,type,name,email,phone,company,country,industry,message,details,items,estimated_total,created_at,updated_at)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(request_id) DO NOTHING');
    $query->execute([$reference,$validated['request_id'],$fields['type'],$fields['name'],$fields['email'] ?? '',$fields['phone'],$fields['company'] ?? '',$fields['country'] ?? '',$fields['industry'] ?? '',$fields['message'] ?? '',json_encode($fields,JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR),json_encode($validated['items'],JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR),$validated['total'],$now,$now]);
    $query = $pdo->prepare('SELECT reference, estimated_total FROM inquiries WHERE request_id = ?');
    $query->execute([$validated['request_id']]);
    return $query->fetch();
}
