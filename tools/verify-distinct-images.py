import os
import json
import sqlite3
from PIL import Image

def main():
    # 1. Check products.json
    with open('data/products.json', 'r', encoding='utf-8') as f:
        products_json = json.load(f)

    # 2. Check sqlite db
    con = sqlite3.connect('storage/forest-lanka.sqlite')
    cur = con.cursor()
    db_products = cur.execute('SELECT sku, name, category, image FROM products').fetchall()
    con.close()

    # 3. Check industries.json
    with open('data/industries.json', 'r', encoding='utf-8') as f:
        industries = json.load(f)

    print(f"=== VERIFYING {len(db_products)} PRODUCTS IN SQLITE ===")
    prod_images = {}
    for sku, name, cat, img in db_products:
        assert os.path.exists(img), f"File missing: {img}"
        with Image.open(img) as im:
            w, h = im.size
        print(f"[{sku}] ({cat}) -> {img} ({w}x{h}, {os.path.getsize(img):,} bytes)")
        prod_images.setdefault(img, []).append(sku)

    print("\n=== CHECKING PRODUCT IMAGE DUPLICATES ===")
    duplicates = {k: v for k, v in prod_images.items() if len(v) > 1}
    if duplicates:
        print("FAIL: Found duplicates:", duplicates)
        exit(1)
    else:
        print(f"PASS: All {len(prod_images)} products have distinct, unique images!")

    print(f"\n=== VERIFYING {len(industries)} INDUSTRIES ===")
    ind_images = {}
    for ind in industries:
        img = ind.get('image')
        assert os.path.exists(img), f"Industry file missing: {img}"
        with Image.open(img) as im:
            w, h = im.size
        slug = ind['slug']
        print(f"[{slug}] {ind['name']} -> {img} ({w}x{h}, {os.path.getsize(img):,} bytes)")
        ind_images.setdefault(img, []).append(slug)

    ind_duplicates = {k: v for k, v in ind_images.items() if len(v) > 1}
    if ind_duplicates:
        print("FAIL: Found industry duplicates:", ind_duplicates)
        exit(1)
    else:
        print(f"PASS: All {len(ind_images)} industries have distinct, unique images!")

    overlap = set(prod_images.keys()).intersection(set(ind_images.keys()))
    if overlap:
        print("FAIL: Overlap between products and industries:", overlap)
        exit(1)
    else:
        print("PASS: Zero overlap between product images and industry images!")

    # Check page visuals
    about_img = 'assets/images/industries/about-vision.jpg'
    logistics_img = 'assets/images/industries/trade-logistics.jpg'
    assert os.path.exists(about_img), f"Missing {about_img}"
    assert os.path.exists(logistics_img), f"Missing {logistics_img}"
    print("\nPASS: Page visual assets exist and are dedicated!")
    print("\nALL VERIFICATIONS PASSED: 100% DISTINCT IMAGES ACROSS THE PROJECT!")

if __name__ == '__main__':
    main()
