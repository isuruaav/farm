<?php
declare(strict_types=1);
require dirname(__DIR__) . '/includes/admin-layout.php';
$pdo = db();
$categories = array_column(industries_data(),'shortName','category');
$error = ''; $saved = false;
$selectedSku = is_string($_GET['sku'] ?? null) ? $_GET['sku'] : '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!admin_post_valid()) $error = 'Your session has expired. Reload this page before saving.';
    elseif (admin_text('action',20) === 'archive') {
        $sku=admin_text('sku',60);
        $pdo->prepare("UPDATE products SET publication='archived', updated_at=? WHERE sku=?")->execute([date('Y-m-d H:i:s'),$sku]);
        admin_activity('product.archived',$sku); header('Location: catalog.php?saved=1',true,303); exit;
    } else {
        $sku = strtoupper(admin_text('sku',60));
        $category = admin_text('category',40);
        $name = admin_text('name',180); $title = admin_text('title',200);
        $price = filter_var($_POST['price'] ?? '',FILTER_VALIDATE_FLOAT);
        $minimum = filter_var($_POST['minimum_order'] ?? '',FILTER_VALIDATE_INT);
        $publication = admin_text('publication',20); $availability=admin_text('availability',20); $priceType=admin_text('price_type',10);
        $image=admin_text('image',1500);
        $localImage = preg_match('~^assets/images/[a-zA-Z0-9_./-]+$~',$image) && !str_contains($image,'..');
        $remoteImage = filter_var($image,FILTER_VALIDATE_URL) && parse_url($image,PHP_URL_SCHEME)==='https' && parse_url($image,PHP_URL_HOST)==='images.unsplash.com';
        if (!preg_match('/^FL-[A-Z0-9-]{2,48}$/',$sku) || !isset($categories[$category]) || mb_strlen($name)<2 || mb_strlen($title)<2) $error='Enter a valid SKU, product name, title and category.';
        elseif ($price===false || $price<0 || $price>100000000 || $minimum===false || $minimum<1 || $minimum>9999) $error='Enter a valid price and minimum order between 1 and 9,999.';
        elseif (!in_array($publication,['draft','published','archived'],true) || !in_array($availability,['on_request','available','unavailable'],true) || !in_array($priceType,['quote','fixed'],true)) $error='Choose valid publication, availability and pricing options.';
        elseif ($image!=='' && !$localImage && !$remoteImage) $error='Use a local assets/images/ path or an HTTPS images.unsplash.com image URL.';
        else {
            $existing=$pdo->prepare('SELECT sku FROM products WHERE sku=?');$existing->execute([$sku]);
            if (admin_text('is_new',1)==='1' && $existing->fetch()) $error='That SKU already exists. Edit the existing product or choose another SKU.';
            else {
                $now=date('Y-m-d H:i:s');
                $pdo->prepare('INSERT INTO products(sku,category,name,title,description,detail_text,image,variant,industry,price,price_type,minimum_order,availability,publication,featured,seo_description,created_at,updated_at)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(sku) DO UPDATE SET category=excluded.category,name=excluded.name,title=excluded.title,description=excluded.description,detail_text=excluded.detail_text,image=excluded.image,variant=excluded.variant,industry=excluded.industry,price=excluded.price,price_type=excluded.price_type,minimum_order=excluded.minimum_order,availability=excluded.availability,publication=excluded.publication,featured=excluded.featured,seo_description=excluded.seo_description,updated_at=excluded.updated_at')
                    ->execute([$sku,$category,$name,$title,admin_text('description',1000),admin_text('detail_text',5000),$image,admin_text('variant',180),$categories[$category],round($price,2),$priceType,$minimum,$availability,$publication,isset($_POST['featured'])?1:0,admin_text('seo_description',300),$now,$now]);
                admin_activity('product.saved',$sku);header('Location: catalog.php?sku='.rawurlencode($sku).'&saved=1',true,303);exit;
            }
        }
    }
}
$row=null;
if ($selectedSku!=='') { $q=$pdo->prepare('SELECT * FROM products WHERE sku=?');$q->execute([$selectedSku]);$row=$q->fetch()?:null; }
$editing=$row!==null;
$values=$row?:['sku'=>'','name'=>'','title'=>'','description'=>'','detail_text'=>'','category'=>'poultry','variant'=>'','price'=>0,'price_type'=>'quote','minimum_order'=>1,'availability'=>'on_request','publication'=>'draft','featured'=>0,'image'=>'','seo_description'=>''];
if ($error && admin_text('action',20)!=='archive') foreach ($values as $key=>$value) {
    if (isset($_POST[$key]) && is_scalar($_POST[$key])) $values[$key]=(string)$_POST[$key];
}
$search=is_string($_GET['q']??null)?mb_substr(trim($_GET['q']),0,180):'';
$query=$pdo->prepare('SELECT * FROM products WHERE sku LIKE ? OR title LIKE ? ORDER BY updated_at DESC,position LIMIT 500');$query->execute(['%'.$search.'%','%'.$search.'%']);$rows=$query->fetchAll();
admin_begin('Product catalog','catalog');
?><div class="admin-title"><div><p class="eyebrow">CATALOG MANAGEMENT</p><h1>Products, ready for business.</h1><p>Edit the public catalog, pricing visibility, order minimums and availability.</p></div><a href="catalog.php?new=1" class="btn-primary">Add product</a></div>
<?php if ($error): ?><p class="form-feedback form-error" role="alert"><?= e($error) ?></p><?php endif; ?><?php if (isset($_GET['saved'])): ?><p class="form-feedback form-success" role="status">Catalog changes saved.</p><?php endif; ?>
<?php if ($editing || isset($_GET['new']) || $error): ?><section class="editor-panel"><h2><?= $editing?'Edit product':'New product' ?></h2><form method="post" class="admin-form"><input type="hidden" name="csrf_token" value="<?= e(csrf_token()) ?>"><input type="hidden" name="action" value="save"><input type="hidden" name="is_new" value="<?= $editing?'0':'1' ?>">
<div class="editor-grid"><div><label for="sku">SKU *</label><input id="sku" name="sku" required pattern="FL-[A-Z0-9-]{2,48}" maxlength="51" value="<?= e($values['sku']) ?>" <?= $editing?'readonly':'' ?>></div><div><label for="category">Industry *</label><select id="category" name="category"><?php foreach ($categories as $key=>$label): ?><option value="<?= e($key) ?>" <?= $values['category']===$key?'selected':'' ?>><?= e($label) ?></option><?php endforeach; ?></select></div><div><label for="name">Short product name *</label><input id="name" name="name" required maxlength="180" value="<?= e($values['name']) ?>"></div><div><label for="title">Catalog title *</label><input id="title" name="title" required maxlength="200" value="<?= e($values['title']) ?>"></div></div>
<label for="description">Catalog description</label><textarea id="description" name="description" rows="3" maxlength="1000"><?= e($values['description']) ?></textarea><label for="detail_text">Product detail text</label><textarea id="detail_text" name="detail_text" rows="5" maxlength="5000"><?= e($values['detail_text']) ?></textarea>
<div class="editor-grid"><div><label for="variant">Pack / variant</label><input id="variant" name="variant" maxlength="180" value="<?= e($values['variant']) ?>"></div><div><label for="minimum_order">Minimum order quantity *</label><input type="number" id="minimum_order" name="minimum_order" min="1" max="9999" required value="<?= (int)$values['minimum_order'] ?>"></div><div><label for="price">Indicative price (LKR) *</label><input type="number" id="price" name="price" min="0" max="100000000" step="0.01" required value="<?= e($values['price']) ?>"></div><div><label for="price_type">Price display</label><select id="price_type" name="price_type"><?php foreach (['quote'=>'Hide price / request quotation','fixed'=>'Show indicative price'] as $key=>$label): ?><option value="<?= e($key) ?>" <?= $values['price_type']===$key?'selected':'' ?>><?= e($label) ?></option><?php endforeach; ?></select></div><div><label for="availability">Availability</label><select id="availability" name="availability"><?php foreach (['on_request'=>'Confirm with our team','available'=>'Available for inquiry','unavailable'=>'Temporarily unavailable'] as $key=>$label): ?><option value="<?= e($key) ?>" <?= $values['availability']===$key?'selected':'' ?>><?= e($label) ?></option><?php endforeach; ?></select></div><div><label for="publication">Publication</label><select id="publication" name="publication"><?php foreach (['draft'=>'Draft / hidden','published'=>'Published','archived'=>'Archived / hidden'] as $key=>$label): ?><option value="<?= e($key) ?>" <?= $values['publication']===$key?'selected':'' ?>><?= e($label) ?></option><?php endforeach; ?></select></div></div>
<label for="image">Image URL or local asset path</label><input id="image" name="image" maxlength="1500" value="<?= e($values['image']) ?>"><label for="seo_description">Search description</label><input id="seo_description" name="seo_description" maxlength="300" value="<?= e($values['seo_description']) ?>"><label class="editor-checkbox"><input type="checkbox" name="featured" value="1" <?= $values['featured']?'checked':'' ?>> Feature on the homepage</label><div class="editor-actions"><button class="btn-primary" type="submit">Save product</button><?php if ($editing): ?><a class="btn-secondary" href="../product.php?sku=<?= rawurlencode($values['sku']) ?>">View published product</a><?php endif; ?></div></form></section><?php endif; ?>
<section class="records-panel"><form class="admin-filters" method="get"><div><label for="q">Find a product</label><input id="q" name="q" value="<?= e($search) ?>" placeholder="SKU or product title"></div><button type="submit" class="btn-primary">Search</button><a href="catalog.php">Reset</a></form><div class="table-scroll"><table><thead><tr><th>Product</th><th>Category</th><th>Price / MOQ</th><th>Publication</th><th>Actions</th></tr></thead><tbody><?php foreach ($rows as $product): ?><tr><td><strong><?= e($product['title']) ?></strong><small><?= e($product['sku']) ?></small></td><td><?= e($categories[$product['category']]??$product['category']) ?></td><td><?= $product['price_type']==='quote'?'Quotation':'LKR '.number_format((float)$product['price'],2) ?><small>Minimum <?= (int)$product['minimum_order'] ?></small></td><td><?= e(ucfirst($product['publication'])) ?><small><?= e(str_replace('_',' ',$product['availability'])) ?></small></td><td><a class="review-link" href="catalog.php?sku=<?= rawurlencode($product['sku']) ?>">Edit</a><?php if ($product['publication']!=='archived'): ?><form method="post" class="inline-admin-form"><input type="hidden" name="csrf_token" value="<?= e(csrf_token()) ?>"><input type="hidden" name="action" value="archive"><input type="hidden" name="sku" value="<?= e($product['sku']) ?>"><button type="submit">Archive</button></form><?php endif; ?></td></tr><?php endforeach; ?></tbody></table></div></section><?php admin_end(); ?>
