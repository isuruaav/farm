import os
import math
import random
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

os.makedirs('assets/images/products', exist_ok=True)
os.makedirs('assets/images/industries', exist_ok=True)

W, H = 1000, 750

def make_egg_tray_30(path):
    img = Image.new('RGB', (W, H), (230, 232, 226))
    draw = ImageDraw.Draw(img)
    # Background gradient
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(240-f*40), int(242-f*35), int(235-f*30)))
    # Rustic table
    ty = int(H * 0.55)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(140-f*30), int(115-f*25), int(90-f*20)))
    # Shadow
    s = Image.new('RGBA', (W, H), (0,0,0,0))
    ImageDraw.Draw(s).ellipse([120, ty-10, 880, ty+170], fill=(0,0,0,140))
    img.paste(s.filter(ImageFilter.GaussianBlur(30)), (0,0), s.filter(ImageFilter.GaussianBlur(30)))
    # 30-egg tray (isometric grey-beige molded pulp)
    cx, cy = 500, ty - 30
    draw.polygon([(cx-320, cy), (cx, cy-110), (cx+320, cy), (cx, cy+110)], fill=(195, 192, 180), outline=(160, 155, 140))
    # Fill with 30 Grade-A brown eggs in 5x6 grid
    for r in range(5):
        for c in range(6):
            u = (c - 2.5) / 3.0
            v = (r - 2.0) / 2.5
            ex = cx + int(u * 250) - int(v * 60)
            ey = cy + int(v * 75) + int(u * 30) - 15
            # Egg
            draw.ellipse([ex-18, ey+8, ex+18, ey+22], fill=(80, 60, 45, 120))
            for er in range(22, 0, -1):
                fac = er / 22.0
                draw.ellipse([ex-int(er*0.8), ey-er, ex+int(er*0.8), ey+int(er*0.85)], 
                             fill=(int(205+35*(1-fac)), int(140+45*(1-fac)), int(95+35*(1-fac))))
            draw.ellipse([ex-6, ey-13, ex-2, ey-7], fill=(255, 245, 230))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_egg_pack_12(path):
    img = Image.new('RGB', (W, H), (235, 238, 232))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(245-f*35), int(248-f*30), int(240-f*25)))
    ty = int(H * 0.58)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(160-f*40), int(135-f*35), int(105-f*30)))
    # Open 12-egg molded carton (2 rows x 6 cols)
    cx, cy = 480, ty - 40
    # Carton base
    draw.polygon([(cx-260, cy), (cx+160, cy-100), (cx+360, cy+20), (cx-60, cy+120)], fill=(200, 195, 182), outline=(165, 160, 145))
    # Open lid tilted up
    draw.polygon([(cx-260, cy), (cx+160, cy-100), (cx+180, cy-220), (cx-240, cy-120)], fill=(215, 210, 195), outline=(175, 170, 155))
    # Brand label on lid
    draw.polygon([(cx-210, cy-20), (cx+130, cy-105), (cx+145, cy-185), (cx-195, cy-100)], fill=(18, 63, 50))
    # 12 brown eggs inside base
    for r in range(2):
        for c in range(6):
            u = (c - 2.5) / 3.0
            v = (r - 0.5) / 1.0
            ex = cx + int(u * 210) + int(v * 45) + 30
            ey = cy + int(v * 45) - int(u * 20) + 10
            for er in range(22, 0, -1):
                fac = er / 22.0
                draw.ellipse([ex-int(er*0.8), ey-er, ex+int(er*0.8), ey+int(er*0.85)], 
                             fill=(int(210+35*(1-fac)), int(145+45*(1-fac)), int(100+35*(1-fac))))
            draw.ellipse([ex-6, ey-13, ex-2, ey-7], fill=(255, 245, 230))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_egg_pack_6(path):
    img = Image.new('RGB', (W, H), (240, 242, 238))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(248-f*30), int(250-f*25), int(245-f*20)))
    ty = int(H * 0.58)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(150-f*35), int(125-f*30), int(100-f*25)))
    # Compact 6-egg carton (2 rows x 3 cols)
    cx, cy = 500, ty - 30
    draw.polygon([(cx-180, cy), (cx+80, cy-80), (cx+220, cy), (cx-40, cy+80)], fill=(205, 200, 185), outline=(170, 165, 150))
    # 6 eggs inside
    for r in range(2):
        for c in range(3):
            u = (c - 1.0) / 1.5
            v = (r - 0.5) / 1.0
            ex = cx + int(u * 110) + int(v * 40)
            ey = cy + int(v * 35) - int(u * 15)
            for er in range(26, 0, -1):
                fac = er / 26.0
                draw.ellipse([ex-int(er*0.8), ey-er, ex+int(er*0.8), ey+int(er*0.85)], 
                             fill=(int(215+35*(1-fac)), int(150+45*(1-fac)), int(105+35*(1-fac))))
            draw.ellipse([ex-7, ey-15, ex-2, ey-8], fill=(255, 245, 230))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_egg_crate_360(path):
    img = Image.new('RGB', (W, H), (220, 225, 220))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(230-f*40), int(235-f*35), int(225-f*30)))
    ty = int(H * 0.65)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(110-f*25), int(95-f*20), int(80-f*15)))
    # Large heavy-duty commercial egg shipping crate / box (360 eggs)
    bx, by = 300, 180
    bw, bh = 400, 360
    # Box body (kraft cardboard with industrial print)
    draw.rectangle([bx, by, bx+bw, by+bh], fill=(195, 155, 110), outline=(155, 120, 80))
    # Corner tape and straps
    draw.rectangle([bx+50, by, bx+70, by+bh], fill=(235, 201, 117))
    draw.rectangle([bx+bw-70, by, bx+bw-50, by+bh], fill=(235, 201, 117))
    # Box label
    draw.rectangle([bx+90, by+80, bx+bw-90, by+240], fill=(245, 248, 245), outline=(180, 190, 180))
    draw.rectangle([bx+110, by+100, bx+bw-110, by+130], fill=(18, 63, 50))
    draw.rectangle([bx+110, by+150, bx+bw-150, by+165], fill=(235, 201, 117))
    draw.rectangle([bx+110, by+180, bx+bw-120, by+195], fill=(100, 120, 110))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_feed_layer_50kg(path):
    img = Image.new('RGB', (W, H), (230, 228, 220))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(240-f*35), int(238-f*30), int(225-f*25)))
    ty = int(H * 0.6)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(130-f*30), int(105-f*25), int(75-f*20)))
    # 50kg feed sack (woven polypropylene bag, green and gold brand)
    sx, sy = 340, 140
    sw, sh = 320, 420
    draw.rounded_rectangle([sx, sy, sx+sw, sy+sh], radius=20, fill=(245, 245, 240), outline=(200, 200, 190))
    # Forest Lanka Green brand band
    draw.rectangle([sx, sy+90, sx+sw, sy+180], fill=(18, 63, 50))
    # Gold stripe
    draw.rectangle([sx, sy+180, sx+sw, sy+200], fill=(235, 201, 117))
    # Pellets spill at the base
    for _ in range(180):
        px = random.randint(sx-40, sx+sw+40)
        py = random.randint(sy+sh-30, sy+sh+45)
        draw.ellipse([px-6, py-3, px+6, py+3], fill=(random.randint(160, 190), random.randint(130, 150), random.randint(70, 95)))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_feed_chick_starter(path):
    img = Image.new('RGB', (W, H), (235, 235, 225))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(245-f*30), int(245-f*30), int(230-f*25)))
    ty = int(H * 0.58)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(125-f*25), int(100-f*20), int(70-f*15)))
    # 25kg chick starter bag + wooden bowl of fine golden crumbles
    sx, sy = 450, 150
    draw.rounded_rectangle([sx, sy, sx+280, sy+380], radius=16, fill=(240, 242, 235), outline=(190, 195, 180))
    draw.rectangle([sx, sy+80, sx+280, sy+150], fill=(235, 160, 40))
    # Bowl of starter crumbles on left
    bx, by = 300, ty - 20
    draw.ellipse([bx-120, by-40, bx+120, by+40], fill=(180, 130, 75))
    draw.ellipse([bx-110, by-35, bx+110, by+30], fill=(230, 190, 85))
    for _ in range(300):
        cpx = random.randint(bx-95, bx+95)
        cpy = random.randint(by-25, by+20)
        draw.point((cpx, cpy), fill=(random.randint(200, 255), random.randint(160, 210), random.randint(50, 100)))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_feed_cattle_50kg(path):
    img = Image.new('RGB', (W, H), (225, 228, 222))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(235-f*35), int(238-f*35), int(230-f*30)))
    ty = int(H * 0.6)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(115-f*25), int(95-f*20), int(75-f*15)))
    # Cattle Feed heavy bag (brown and teal)
    sx, sy = 340, 140
    sw, sh = 320, 420
    draw.rounded_rectangle([sx, sy, sx+sw, sy+sh], radius=20, fill=(240, 238, 230), outline=(195, 190, 180))
    draw.rectangle([sx, sy+100, sx+sw, sy+180], fill=(14, 81, 106))
    draw.rectangle([sx, sy+180, sx+sw, sy+200], fill=(235, 201, 117))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_feed_fish_pellets(path):
    img = Image.new('RGB', (W, H), (220, 235, 240))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(230-f*30), int(240-f*25), int(245-f*20)))
    # Clean blue water pond with floating fish pellets
    ty = int(H * 0.52)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(30+f*20), int(100+f*30), int(140+f*30)))
    # Floating pellets
    random.seed(88)
    for _ in range(120):
        px = random.randint(150, 850)
        py = random.randint(ty+10, H-40)
        # Pellet
        draw.ellipse([px-10, py-7, px+10, py+7], fill=(160, 115, 60))
        draw.ellipse([px-8, py-5, px+4, py+3], fill=(195, 145, 80))
        # Ripple ring around pellet
        draw.ellipse([px-20, py-12, px+20, py+12], outline=(100, 180, 220, 100))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_tray_bundle_100(path):
    img = Image.new('RGB', (W, H), (230, 232, 228))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(240-f*35), int(242-f*30), int(235-f*25)))
    ty = int(H * 0.65)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(130-f*25), int(110-f*20), int(85-f*15)))
    # Tall dense stack of 100 nested molded pulp egg trays
    bx, by = 350, 160
    bw, bh = 300, 360
    # Stack lines representing 100 trays
    for i in range(40):
        sy = by + int(i * 8.8)
        col = (195 + (i%2)*8, 192 + (i%2)*8, 182 + (i%2)*8)
        draw.rectangle([bx, sy, bx+bw, sy+7], fill=col, outline=(165, 160, 150))
    # Green tension straps securing bundle
    draw.rectangle([bx+60, by-10, bx+75, by+bh+10], fill=(18, 63, 50))
    draw.rectangle([bx+bw-75, by-10, bx+bw-60, by+bh+10], fill=(18, 63, 50))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_tray_cartons_50(path):
    img = Image.new('RGB', (W, H), (235, 238, 234))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(245-f*30), int(248-f*25), int(240-f*20)))
    ty = int(H * 0.6)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(140-f*30), int(115-f*25), int(90-f*20)))
    # Stack of closed 12-egg consumer cartons
    bx, by = 360, 200
    for i in range(8):
        sy = by + i * 36
        draw.rounded_rectangle([bx, sy, bx+280, sy+32], radius=6, fill=(210, 205, 190), outline=(175, 170, 155))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_mushrooms_shiitake(path):
    img = Image.new('RGB', (W, H), (38, 32, 28))
    draw = ImageDraw.Draw(img)
    # Dark rustic background
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(45-f*15), int(38-f*12), int(32-f*10)))
    # Large woven wooden basket filled with dried cracked-cap Shiitake mushrooms
    bx, by = 500, 420
    draw.ellipse([bx-320, by-140, bx+320, by+140], fill=(95, 70, 50), outline=(65, 45, 30))
    # Shiitake mushroom caps (brown with deep white cracks)
    random.seed(44)
    for _ in range(45):
        mx = random.randint(bx-240, bx+240)
        my = random.randint(by-90, by+90)
        mr = random.randint(28, 48)
        # Cap body
        draw.ellipse([mx-mr, my-int(mr*0.7), mx+mr, my+int(mr*0.7)], fill=(random.randint(90, 125), random.randint(60, 85), random.randint(40, 55)))
        # Deep white cracks typical of gourmet flower shiitake (Hua Gu)
        draw.line([(mx-int(mr*0.6), my), (mx+int(mr*0.6), my)], fill=(240, 235, 220), width=3)
        draw.line([(mx, my-int(mr*0.4)), (mx, my+int(mr*0.4))], fill=(240, 235, 220), width=3)
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_mushrooms_oyster(path):
    img = Image.new('RGB', (W, H), (235, 240, 235))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(245-f*30), int(250-f*25), int(245-f*20)))
    ty = int(H * 0.58)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(135-f*25), int(115-f*20), int(90-f*15)))
    # Clear retail punnet with fresh cluster of pearl oyster mushrooms
    px, py = 350, 280
    draw.rounded_rectangle([px, py, px+300, py+180], radius=12, fill=(245, 248, 245, 180), outline=(190, 205, 195))
    # Fan-shaped oyster mushroom cluster
    for i in range(14):
        ox = 450 + int(math.sin(i*0.6) * 90)
        oy = 320 + int(math.cos(i*0.6) * 50)
        draw.ellipse([ox-45, oy-25, ox+45, oy+25], fill=(225, 228, 225), outline=(195, 200, 195))
        draw.ellipse([ox-38, oy-20, ox+38, oy+15], fill=(245, 248, 245))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_egg_powder_whole(path):
    # Call the high quality golden powder
    from tools.generate_product_assets import create_egg_powder_image
    create_egg_powder_image(path)

def make_egg_powder_albumen(path):
    img = Image.new('RGB', (W, H), (30, 40, 35))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(40-f*20), int(55-f*25), int(48-f*22)))
    # Pure snow-white albumen egg white powder in glass bowl with stainless whisk
    bx, by = 480, 420
    draw.ellipse([bx-260, by-130, bx+260, by+130], fill=(245, 248, 250), outline=(215, 220, 225))
    # Pure white fine powder mound
    for i in range(12):
        prx = int(240 * (1 - i*0.06))
        pry = int(120 * (1 - i*0.06))
        draw.ellipse([bx-prx, by-pry - i*4, bx+prx, by+pry - i*4], fill=(255, 255, 255))
    # Whisk with whipped egg white foam
    draw.line([(bx+100, by-20), (bx+300, by-180)], fill=(200, 205, 210), width=10)
    # Fluffy meringue foam
    draw.ellipse([bx+80, by-60, bx+160, by+10], fill=(255, 255, 255))
    draw.ellipse([bx+120, by-80, bx+190, by-20], fill=(255, 255, 255))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_fertilizer_pellets_20kg(path):
    img = Image.new('RGB', (W, H), (230, 232, 225))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(240-f*30), int(242-f*30), int(235-f*25)))
    ty = int(H * 0.6)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(115-f*25), int(95-f*20), int(75-f*15)))
    # Green eco sack of 100% organic fertilizer pellets
    sx, sy = 340, 140
    sw, sh = 320, 420
    draw.rounded_rectangle([sx, sy, sx+sw, sy+sh], radius=20, fill=(240, 245, 235), outline=(180, 200, 175))
    draw.rectangle([sx, sy+90, sx+sw, sy+170], fill=(29, 98, 72))
    draw.rectangle([sx, sy+170, sx+sw, sy+190], fill=(235, 201, 117))
    # Spill of dark rich 4mm bio-fertilizer pellets
    for _ in range(180):
        px = random.randint(sx-30, sx+sw+30)
        py = random.randint(sy+sh-20, sy+sh+50)
        draw.ellipse([px-6, py-3, px+6, py+3], fill=(random.randint(45, 70), random.randint(35, 55), random.randint(25, 40)))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_fertilizer_compost_10kg(path):
    img = Image.new('RGB', (W, H), (235, 238, 230))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(245-f*30), int(248-f*30), int(240-f*25)))
    ty = int(H * 0.58)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(130-f*25), int(105-f*20), int(80-f*15)))
    # Rich dark crumbly compost mound with green garden trowel
    cx, cy = 460, ty
    draw.ellipse([cx-220, cy-70, cx+220, cy+70], fill=(55, 42, 32))
    draw.ellipse([cx-180, cy-50, cx+180, cy+50], fill=(70, 52, 38))
    # Texture
    for _ in range(400):
        px = random.randint(cx-170, cx+170)
        py = random.randint(cy-45, cy+45)
        draw.point((px, py), fill=(random.randint(80, 110), random.randint(65, 90), random.randint(45, 70)))
    # Green trowel
    draw.polygon([(cx+140, cy-50), (cx+260, cy-120), (cx+275, cy-105), (cx+165, cy-35)], fill=(18, 63, 50))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_media_seed_starting(path):
    img = Image.new('RGB', (W, H), (235, 240, 235))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(245-f*30), int(250-f*25), int(245-f*20)))
    ty = int(H * 0.6)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(140-f*30), int(120-f*25), int(95-f*20)))
    # Seedling plug tray (black plastic grid with tiny bright green sprouts)
    tx, ty_tray = 300, 260
    for r in range(4):
        for c in range(8):
            px = tx + c * 52
            py = ty_tray + r * 52
            draw.rectangle([px, py, px+46, py+46], fill=(30, 28, 25), outline=(50, 50, 50))
            # Seedling soil plug
            draw.ellipse([px+6, py+6, px+40, py+40], fill=(65, 50, 38))
            # Tiny green sprout
            draw.line([(px+23, py+28), (px+23, py+12)], fill=(40, 160, 80), width=3)
            draw.ellipse([px+16, py+10, px+23, py+16], fill=(50, 190, 90))
            draw.ellipse([px+23, py+10, px+30, py+16], fill=(50, 190, 90))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_media_potting_soil(path):
    img = Image.new('RGB', (W, H), (230, 235, 228))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(240-f*30), int(245-f*25), int(238-f*20)))
    ty = int(H * 0.58)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(135-f*25), int(115-f*20), int(90-f*15)))
    # Terracotta pot with rich potting soil & lush green indoor plant
    px, py = 500, 380
    # Pot
    draw.polygon([(px-120, py), (px+120, py), (px+90, py+180), (px-90, py+180)], fill=(195, 95, 55), outline=(160, 75, 40))
    draw.ellipse([px-125, py-18, px+125, py+18], fill=(210, 105, 60))
    draw.ellipse([px-115, py-12, px+115, py+12], fill=(60, 48, 38))
    # Plant foliage leaves
    for angle in [0, 45, 90, 135, 180, 225, 270, 315]:
        lx = px + int(math.cos(math.radians(angle)) * 140)
        ly = py - 70 + int(math.sin(math.radians(angle)) * 60)
        draw.ellipse([lx-35, ly-20, lx+35, ly+20], fill=(35, 135, 75))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_water_smart_ro(path):
    img = Image.new('RGB', (W, H), (235, 242, 245))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(245-f*25), int(250-f*20), int(252-f*15)))
    ty = int(H * 0.65)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(200-f*30), int(210-f*25), int(220-f*20)))
    # Modern white minimalist countertop RO purifier with LED touch UI
    rx, ry = 360, 160
    rw, rh = 280, 380
    draw.rounded_rectangle([rx, ry, rx+rw, ry+rh], radius=24, fill=(255, 255, 255), outline=(210, 220, 225))
    # Digital touchscreen panel (cyan glow)
    draw.rounded_rectangle([rx+40, ry+60, rx+rw-40, ry+160], radius=12, fill=(12, 35, 45))
    # TDS display: "011 ppm" in neon cyan
    draw.text((rx+60, ry+90), "011 ppm", fill=(45, 225, 240))
    # Dispensing faucet and clear glass of water
    draw.rectangle([rx+rw//2 - 6, ry+220, rx+rw//2 + 6, ry+270], fill=(180, 190, 195))
    # Glass of water
    gx, gy = rx+rw//2 - 35, ry+280
    draw.polygon([(gx, gy), (gx+70, gy), (gx+60, gy+90), (gx+10, gy+90)], fill=(200, 235, 250, 150), outline=(160, 210, 230))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_water_commercial_400gpd(path):
    img = Image.new('RGB', (W, H), (225, 230, 235))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(235-f*30), int(240-f*25), int(245-f*20)))
    ty = int(H * 0.65)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(160-f*30), int(170-f*25), int(180-f*20)))
    # Commercial 400 GPD stainless steel rack with dual pressure gauges and 3 membrane vessels
    fx, fy = 250, 140
    fw, fh = 500, 420
    # Stainless frame
    draw.rectangle([fx, fy, fx+fw, fy+fh], fill=(235, 240, 245), outline=(170, 180, 190), width=6)
    # Horizontal RO Membrane pressure vessels (cylindrical stainless tubes)
    for i in range(3):
        vy = fy + 80 + i * 85
        draw.rounded_rectangle([fx+40, vy, fx+fw-40, vy+55], radius=10, fill=(215, 225, 235), outline=(150, 165, 175))
    # Pressure gauges
    for gx in [fx+90, fx+160]:
        draw.ellipse([gx-25, fy+20, gx+25, fy+70], fill=(255, 255, 255), outline=(120, 130, 140))
        draw.line([(gx, fy+45), (gx+15, fy+35)], fill=(220, 40, 40), width=2)
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_about_vision(path):
    img = Image.new('RGB', (W, H), (230, 240, 235))
    draw = ImageDraw.Draw(img)
    # Modern agricultural enterprise headquarters / high-tech greenhouse landscape
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(220-f*40), int(245-f*30), int(235-f*20)))
    # Cultivated green terraces in Polpithigama
    ty = int(H * 0.45)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(25+f*20), int(95+f*30), int(60+f*25)))
    # Modern architectural greenhouse canopy
    draw.polygon([(150, ty), (500, ty-140), (850, ty), (500, ty+40)], fill=(235, 248, 240, 160), outline=(255, 255, 255))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

def make_trade_logistics(path):
    img = Image.new('RGB', (W, H), (225, 232, 238))
    draw = ImageDraw.Draw(img)
    # Port of Colombo container terminal & cold chain export logistics
    for y in range(H):
        f = y / H
        draw.line([(0, y), (W, y)], fill=(int(215-f*30), int(230-f*25), int(245-f*20)))
    # Deep blue harbor water
    ty = int(H * 0.55)
    for y in range(ty, H):
        f = (y - ty) / (H - ty)
        draw.line([(0, y), (W, y)], fill=(int(18+f*15), int(55+f*25), int(95+f*30)))
    # Modern white Reefer container (Cold Chain 2-4°C)
    cx, cy = 300, 240
    cw, ch = 450, 220
    draw.rectangle([cx, cy, cx+cw, cy+ch], fill=(245, 248, 250), outline=(190, 205, 215))
    # Vertical container corrugation ribs
    for x in range(cx+30, cx+cw-30, 24):
        draw.line([(x, cy+15), (x, cy+ch-15)], fill=(210, 225, 235), width=4)
    # Reefer refrigeration unit front panel
    draw.rectangle([cx+20, cy+30, cx+90, cy+ch-30], fill=(18, 63, 50))
    draw.text((cx+30, cy+50), "2-4 C", fill=(45, 225, 240))
    img.save(path, 'JPEG', quality=92)
    print("Done:", path)

if __name__ == '__main__':
    make_egg_tray_30('assets/images/products/egg-tray-30.jpg')
    make_egg_pack_12('assets/images/products/egg-pack-12.jpg')
    make_egg_pack_6('assets/images/products/egg-pack-6.jpg')
    make_egg_crate_360('assets/images/products/egg-crate-360.jpg')
    
    make_feed_layer_50kg('assets/images/products/feed-layer-50kg.jpg')
    make_feed_chick_starter('assets/images/products/feed-chick-starter.jpg')
    make_feed_cattle_50kg('assets/images/products/feed-cattle-50kg.jpg')
    make_feed_fish_pellets('assets/images/products/feed-fish-pellets.jpg')
    
    make_tray_bundle_100('assets/images/products/tray-bundle-100.jpg')
    make_tray_cartons_50('assets/images/products/tray-cartons-50.jpg')
    
    make_mushrooms_shiitake('assets/images/products/mushrooms-shiitake-dried.jpg')
    make_mushrooms_oyster('assets/images/products/mushrooms-oyster-fresh.jpg')
    
    make_egg_powder_albumen('assets/images/products/egg-powder-albumen.jpg')
    
    make_fertilizer_pellets_20kg('assets/images/products/fertilizer-pellets-20kg.jpg')
    make_fertilizer_compost_10kg('assets/images/products/fertilizer-compost-10kg.jpg')
    
    make_media_seed_starting('assets/images/products/media-seed-starting.jpg')
    make_media_potting_soil('assets/images/products/media-potting-soil.jpg')
    
    make_water_smart_ro('assets/images/products/water-smart-ro.jpg')
    make_water_commercial_400gpd('assets/images/products/water-commercial-400gpd.jpg')
    
    make_about_vision('assets/images/industries/about-vision.jpg')
    make_trade_logistics('assets/images/industries/trade-logistics.jpg')

