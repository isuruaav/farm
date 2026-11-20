import math
import random
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

def create_egg_trays_image(path):
    width, height = 1100, 750
    # Background: clean modern industrial packing facility / neutral warm studio
    img = Image.new('RGB', (width, height), (225, 228, 222))
    draw = ImageDraw.Draw(img)
    
    # Gradient backdrop: soft studio light from top-left
    for y in range(height):
        factor = y / height
        r = int(235 * (1 - factor*0.4) + 180 * (factor*0.4))
        g = int(240 * (1 - factor*0.4) + 190 * (factor*0.4))
        b = int(232 * (1 - factor*0.4) + 180 * (factor*0.4))
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Table / wooden surface at bottom
    table_y = int(height * 0.58)
    for y in range(table_y, height):
        factor = (y - table_y) / (height - table_y)
        r = int(140 * (1 - factor*0.3) + 70 * factor*0.3)
        g = int(120 * (1 - factor*0.3) + 55 * factor*0.3)
        b = int(100 * (1 - factor*0.3) + 45 * factor*0.3)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Add soft table shadow
    shadow = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.ellipse([150, table_y - 20, 950, table_y + 160], fill=(0, 0, 0, 90))
    shadow = shadow.filter(ImageFilter.GaussianBlur(35))
    img.paste(shadow, (0, 0), shadow)

    # Draw stack of Molded Pulp Trays (greyish-beige recycled fiber paper)
    # Stack consists of 4 trays, bottom to top
    tray_colors = [
        (175, 172, 162),
        (185, 182, 172),
        (195, 192, 182),
        (205, 202, 192)
    ]
    
    # We draw an isometric perspective of 30-egg molded pulp trays (5 rows x 6 cols)
    center_x = 550
    base_y = table_y - 30

    for stack_idx in range(4):
        offset_y = base_y - stack_idx * 28
        t_color = tray_colors[stack_idx]
        
        # Tray body (rounded quadrilateral with molded edge lips)
        poly = [
            (center_x - 360, offset_y),
            (center_x, offset_y - 120),
            (center_x + 360, offset_y),
            (center_x, offset_y + 120)
        ]
        
        # Side depth
        depth_poly = [
            (center_x - 360, offset_y),
            (center_x - 360, offset_y + 18),
            (center_x, offset_y + 138),
            (center_x + 360, offset_y + 18),
            (center_x + 360, offset_y),
            (center_x, offset_y + 120)
        ]
        draw.polygon(depth_poly, fill=(int(t_color[0]*0.75), int(t_color[1]*0.75), int(t_color[2]*0.75)))
        draw.polygon(poly, fill=t_color, outline=(int(t_color[0]*0.85), int(t_color[1]*0.85), int(t_color[2]*0.85)))

        # On the top tray (stack_idx == 3), draw the 30 molded egg cups (cones/dimples)
        if stack_idx == 3:
            # Grid of 5 rows x 6 cols in isometric transform
            for r in range(5):
                for c in range(6):
                    # Isometric coordinates
                    u = (c - 2.5) / 3.0  # -0.83 to +0.83
                    v = (r - 2.0) / 2.5  # -0.80 to +0.80
                    
                    cup_x = center_x + int(u * 280) - int(v * 70)
                    cup_y = offset_y + int(v * 80) + int(u * 35)
                    
                    # Outer molded rim of cup
                    draw.ellipse([cup_x - 22, cup_y - 14, cup_x + 22, cup_y + 14], 
                                 fill=(int(t_color[0]*0.88), int(t_color[1]*0.88), int(t_color[2]*0.88)),
                                 outline=(int(t_color[0]*0.7), int(t_color[1]*0.7), int(t_color[2]*0.7)))
                    
                    # Deep depression shadow
                    draw.ellipse([cup_x - 14, cup_y - 9, cup_x + 14, cup_y + 9], 
                                 fill=(int(t_color[0]*0.65), int(t_color[1]*0.65), int(t_color[2]*0.65)))
                    
                    # Bottom point of depression
                    draw.ellipse([cup_x - 6, cup_y - 4, cup_x + 6, cup_y + 4], 
                                 fill=(int(t_color[0]*0.52), int(t_color[1]*0.52), int(t_color[2]*0.52)))
                    
                    # Put a few pristine Grade-A brown eggs in selected cups
                    if (r, c) in [(1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (1, 4), (2, 4), (3, 2)]:
                        egg_y = cup_y - 12
                        # Egg drop shadow in cup
                        draw.ellipse([cup_x - 16, cup_y - 5, cup_x + 16, cup_y + 10], fill=(60, 50, 40, 150))
                        
                        # Egg body (brown gradient)
                        for er in range(24, 0, -1):
                            fac = er / 24.0
                            egg_r = int(195 + (235 - 195) * (1 - fac))
                            egg_g = int(135 + (185 - 135) * (1 - fac))
                            egg_b = int(90 + (130 - 90) * (1 - fac))
                            y0 = egg_y - int(er * 1.1)
                            y1 = egg_y + int(er * 0.85)
                            x0 = cup_x - int(er * 0.8)
                            x1 = cup_x + int(er * 0.8)
                            if y1 > y0 and x1 > x0:
                                draw.ellipse([x0, y0, x1, y1], fill=(egg_r, egg_g, egg_b))
                        # Egg specular highlight
                        draw.ellipse([cup_x - 7, egg_y - 14, cup_x - 2, egg_y - 8], fill=(250, 240, 220))

    # Add recycled eco label text & tactile grain
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.05)
    img = img.filter(ImageFilter.SMOOTH_MORE)
    img.save(path, 'JPEG', quality=95)
    print(f"Created: {path}")

def create_egg_powder_image(path):
    width, height = 1100, 750
    # Rich warm culinary & food lab atmosphere
    img = Image.new('RGB', (width, height), (35, 30, 26))
    draw = ImageDraw.Draw(img)

    # Dark slate / rustic dark wooden kitchen table
    for y in range(height):
        factor = y / height
        r = int(45 * (1 - factor*0.3) + 25 * factor*0.3)
        g = int(40 * (1 - factor*0.3) + 22 * factor*0.3)
        b = int(36 * (1 - factor*0.3) + 20 * factor*0.3)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Ambient warm glow from top-right
    glow = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glow)
    g_draw.ellipse([300, -100, 1100, 700], fill=(245, 200, 110, 45))
    glow = glow.filter(ImageFilter.GaussianBlur(90))
    img.paste(glow, (0, 0), glow)

    # Large ceramic white bowl filled with Golden Spray-Dried Egg Powder
    bowl_cx, bowl_cy = 500, 420
    bowl_rx, bowl_ry = 320, 180

    # Bowl drop shadow
    b_shadow = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    bs_draw = ImageDraw.Draw(b_shadow)
    bs_draw.ellipse([bowl_cx - 360, bowl_cy - 10, bowl_cx + 360, bowl_cy + 250], fill=(0, 0, 0, 180))
    b_shadow = b_shadow.filter(ImageFilter.GaussianBlur(40))
    img.paste(b_shadow, (0, 0), b_shadow)

    # Bowl ceramic outer rim
    draw.ellipse([bowl_cx - bowl_rx - 15, bowl_cy - bowl_ry - 10, bowl_cx + bowl_rx + 15, bowl_cy + bowl_ry + 35], fill=(235, 238, 235), outline=(210, 215, 210))
    draw.ellipse([bowl_cx - bowl_rx, bowl_cy - bowl_ry, bowl_cx + bowl_rx, bowl_cy + bowl_ry + 20], fill=(250, 252, 250))

    # Golden Spray-Dried Egg Powder inside bowl
    # Powder mound has soft organic texture and micro dunes
    powder_inner_rx, powder_inner_ry = bowl_rx - 15, bowl_ry - 12
    draw.ellipse([bowl_cx - powder_inner_rx, bowl_cy - powder_inner_ry, bowl_cx + powder_inner_rx, bowl_cy + powder_inner_ry], fill=(242, 195, 60))

    # Powder shading and gradient layers
    for i in range(15):
        prx = int(powder_inner_rx * (1 - i * 0.05))
        pry = int(powder_inner_ry * (1 - i * 0.05))
        py_offset = int(-i * 4.5)
        # Gradient colors from rich golden yolk yellow to bright highlight
        col_r = min(255, int(235 + i * 1.5))
        col_g = min(255, int(185 + i * 3.5))
        col_b = min(255, int(45 + i * 6.5))
        draw.ellipse([bowl_cx - prx, bowl_cy - pry + py_offset, bowl_cx + prx, bowl_cy + pry + py_offset], fill=(col_r, col_g, col_b))

    # Fine powder particle texture
    random.seed(42)
    for _ in range(800):
        px = random.randint(bowl_cx - powder_inner_rx + 30, bowl_cx + powder_inner_rx - 30)
        py = random.randint(bowl_cy - powder_inner_ry, bowl_cy + powder_inner_ry - 20)
        pr = random.randint(1, 3)
        p_col = (random.randint(230, 255), random.randint(180, 220), random.randint(30, 90))
        draw.ellipse([px, py, px + pr, py + pr], fill=p_col)

    # Stainless steel measuring scoop resting diagonally in powder
    scoop = [
        (bowl_cx + 120, bowl_cy - 40),
        (bowl_cx + 340, bowl_cy - 160),
        (bowl_cx + 360, bowl_cy - 145),
        (bowl_cx + 140, bowl_cy - 25)
    ]
    draw.polygon(scoop, fill=(215, 220, 225), outline=(170, 175, 180))
    # Scoop head
    draw.ellipse([bowl_cx + 70, bowl_cy - 70, bowl_cx + 180, bowl_cy], fill=(195, 202, 208), outline=(160, 168, 175))
    draw.ellipse([bowl_cx + 85, bowl_cy - 60, bowl_cx + 165, bowl_cy - 10], fill=(245, 200, 65))

    # Background Elements: Whole fresh eggs and an industrial sealed Kraft foil pouch
    # Kraft pouch on the right (Commercial Food Grade 20kg packing symbol)
    pouch_x, pouch_y = 820, 160
    pouch_w, pouch_h = 220, 360
    draw.rounded_rectangle([pouch_x, pouch_y, pouch_x + pouch_w, pouch_y + pouch_h], radius=12, fill=(185, 148, 105), outline=(150, 115, 75))
    # Pouch top heat seal
    draw.rectangle([pouch_x, pouch_y, pouch_x + pouch_w, pouch_y + 35], fill=(160, 125, 85))
    # Pouch label
    draw.rectangle([pouch_x + 20, pouch_y + 80, pouch_x + pouch_w - 20, pouch_y + 240], fill=(245, 248, 245))
    draw.rectangle([pouch_x + 30, pouch_y + 95, pouch_x + pouch_w - 30, pouch_y + 115], fill=(18, 63, 50))
    draw.rectangle([pouch_x + 30, pouch_y + 130, pouch_x + pouch_w - 50, pouch_y + 140], fill=(235, 190, 60))
    draw.rectangle([pouch_x + 30, pouch_y + 155, pouch_x + pouch_w - 40, pouch_y + 165], fill=(150, 165, 155))
    draw.rectangle([pouch_x + 30, pouch_y + 180, pouch_x + pouch_w - 60, pouch_y + 190], fill=(150, 165, 155))

    # A couple of whole fresh eggs next to the bowl on the left
    for (ex, ey) in [(180, 520), (250, 560)]:
        draw.ellipse([ex - 42, ey - 10, ex + 42, ey + 40], fill=(15, 12, 10, 150))
        for er in range(35, 0, -1):
            fac = er / 35.0
            egg_r = int(210 + (245 - 210) * (1 - fac))
            egg_g = int(145 + (195 - 145) * (1 - fac))
            egg_b = int(100 + (140 - 100) * (1 - fac))
            draw.ellipse([ex - int(er*0.8), ey - er, ex + int(er*0.8), ey + int(er*0.85)], fill=(egg_r, egg_g, egg_b))
        draw.ellipse([ex - 12, ey - 22, ex - 4, ey - 12], fill=(255, 245, 230))

    img = img.filter(ImageFilter.SMOOTH_MORE)
    img.save(path, 'JPEG', quality=95)
    print(f"Created: {path}")

def create_feed_pellets_image(path):
    width, height = 1100, 750
    # Natural warm agricultural setting with wooden table and burlap sack
    img = Image.new('RGB', (width, height), (220, 215, 205))
    draw = ImageDraw.Draw(img)

    # Background farm silo / warm barn glow
    for y in range(height):
        factor = y / height
        r = int(210 * (1 - factor*0.4) + 160 * factor*0.4)
        g = int(200 * (1 - factor*0.4) + 145 * factor*0.4)
        b = int(185 * (1 - factor*0.4) + 130 * factor*0.4)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Wooden work surface
    table_y = int(height * 0.52)
    for y in range(table_y, height):
        factor = (y - table_y) / (height - table_y)
        r = int(120 * (1 - factor*0.25) + 85 * factor*0.25)
        g = int(90 * (1 - factor*0.25) + 60 * factor*0.25)
        b = int(65 * (1 - factor*0.25) + 40 * factor*0.25)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Burlap Jute Sack overflowing with Feed Pellets in center
    sack_cx, sack_cy = 550, 430
    
    # Shadow under sack
    sack_shadow = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    ss_draw = ImageDraw.Draw(sack_shadow)
    ss_draw.ellipse([200, table_y - 20, 900, table_y + 220], fill=(0, 0, 0, 160))
    sack_shadow = sack_shadow.filter(ImageFilter.GaussianBlur(35))
    img.paste(sack_shadow, (0, 0), sack_shadow)

    # Burlap sack shape (rolled rim)
    draw.polygon([
        (260, table_y + 160),
        (240, table_y + 30),
        (320, table_y - 40),
        (780, table_y - 40),
        (860, table_y + 30),
        (840, table_y + 160),
        (550, table_y + 190)
    ], fill=(175, 145, 105), outline=(140, 115, 80))

    # Sack rim fold
    draw.ellipse([320, table_y - 70, 780, table_y], fill=(190, 160, 120), outline=(150, 125, 90))
    draw.ellipse([340, table_y - 65, 760, table_y - 10], fill=(110, 85, 55))

    # Pellets mound overflowing from sack and spilling onto the wooden table
    mound_cx, mound_cy = 550, table_y - 30
    draw.ellipse([350, mound_cy - 70, 750, mound_cy + 40], fill=(165, 130, 80))
    draw.ellipse([380, mound_cy - 55, 720, mound_cy + 25], fill=(185, 145, 95))

    # Spill pile on table
    draw.ellipse([300, table_y + 30, 800, table_y + 150], fill=(155, 120, 75))

    # Individual extruded cylindrical pellets (each pellet is a tiny 3D cylinder)
    random.seed(101)
    
    def draw_pellet(px, py, angle, length=18, radius=6):
        dx = math.cos(angle) * length
        dy = math.sin(angle) * length
        # Pellet cylinder body
        base_col = (random.randint(150, 185), random.randint(120, 145), random.randint(70, 95))
        highlight_col = (min(255, base_col[0] + 30), min(255, base_col[1] + 25), min(255, base_col[2] + 20))
        shadow_col = (max(0, base_col[0] - 35), max(0, base_col[1] - 30), max(0, base_col[2] - 25))
        
        # End cap 1
        draw.ellipse([px - radius, py - radius*0.7, px + radius, py + radius*0.7], fill=shadow_col)
        # Body
        draw.polygon([
            (px - radius*0.6, py - radius*0.6),
            (px + dx - radius*0.6, py + dy - radius*0.6),
            (px + dx + radius*0.6, py + dy + radius*0.6),
            (px + radius*0.6, py + radius*0.6)
        ], fill=base_col)
        # End cap 2
        draw.ellipse([px + dx - radius, py + dy - radius*0.7, px + dx + radius, py + dy + radius*0.7], fill=highlight_col)

    # Generate 650 detailed extruded pellets in mound and spill
    for _ in range(450):
        # Inside the sack top
        u = random.uniform(-1, 1)
        v = random.uniform(-1, 1)
        if u*u + v*v <= 1.0:
            px = mound_cx + int(u * 170)
            py = mound_cy + int(v * 45) - 20
            ang = random.uniform(0, math.pi)
            draw_pellet(px, py, ang, length=random.randint(12, 22), radius=random.randint(4, 7))

    for _ in range(250):
        # Spilled onto table
        u = random.uniform(-1, 1)
        v = random.uniform(-1, 1)
        if u*u + v*v <= 1.0:
            px = 550 + int(u * 220)
            py = table_y + 80 + int(v * 45)
            ang = random.uniform(0, math.pi)
            draw_pellet(px, py, ang, length=random.randint(14, 24), radius=random.randint(5, 7))

    # A wooden scoop in the feed with grain
    draw.polygon([(260, table_y - 20), (380, table_y - 70), (410, table_y - 50), (290, table_y)], fill=(190, 140, 80), outline=(140, 95, 45))

    img = img.filter(ImageFilter.SMOOTH_MORE)
    img.save(path, 'JPEG', quality=95)
    print(f"Created: {path}")

if __name__ == '__main__':
    create_egg_trays_image('assets/images/industries/egg-trays.jpg')
    create_egg_powder_image('assets/images/industries/egg-powder.jpg')
    create_feed_pellets_image('assets/images/industries/feed-pellets.jpg')
