#!/usr/bin/env python3
"""
Generates high-resolution, professional illustrative images for:
1. water-tech.jpg (South Korean Smart Water Purification & Membrane Lab)
2. egg-processing.jpg (Industrial Egg Powder Spray-Drying & Quality Testing)
"""

import os
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import math

def create_water_tech_image(path):
    width, height = 1600, 1000
    img = Image.new("RGB", (width, height), (12, 38, 54))
    draw = ImageDraw.Draw(img)

    # Gradient background - Deep tech water blue & laboratory ambient lighting
    for y in range(height):
        ratio = y / height
        r = int(10 + 15 * math.sin(ratio * math.pi))
        g = int(35 + 45 * ratio)
        b = int(60 + 75 * ratio + 30 * math.sin(ratio * 2))
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Abstract high-tech laboratory background shapes & water refractions
    for x in range(0, width, 80):
        alpha_color = (20, 85, 120)
        draw.line([(x, 0), (x + 200, height)], fill=alpha_color, width=2)
    
    # Glass cylindrical filter housing / RO Membrane vessels
    membrane_x = 450
    # Membrane 1
    draw.rounded_rectangle([membrane_x, 150, membrane_x + 160, 850], radius=40, fill=(18, 70, 100), outline=(50, 150, 200), width=4)
    # Membrane 2
    draw.rounded_rectangle([membrane_x + 220, 150, membrane_x + 380, 850], radius=40, fill=(24, 85, 120), outline=(60, 180, 230), width=4)
    # Membrane 3
    draw.rounded_rectangle([membrane_x + 440, 150, membrane_x + 600, 850], radius=40, fill=(18, 70, 100), outline=(50, 150, 200), width=4)

    # Chrome / Stainless steel piping headers
    draw.rectangle([350, 220, 1250, 260], fill=(180, 210, 230), outline=(100, 140, 170), width=3)
    draw.rectangle([350, 740, 1250, 780], fill=(180, 210, 230), outline=(100, 140, 170), width=3)

    # Digital Smart IoT Flow indicators / Telemetry Gauges
    for idx, cx in enumerate([membrane_x + 80, membrane_x + 300, membrane_x + 520]):
        # Digital circular display
        draw.ellipse([cx - 45, 450, cx + 45, 540], fill=(10, 30, 45), outline=(0, 220, 255), width=3)
        # Inner glow
        draw.ellipse([cx - 35, 460, cx + 35, 530], fill=(5, 50, 75))
        # Status LED
        draw.ellipse([cx - 8, 475, cx + 8, 491], fill=(0, 255, 180))

    # Water light reflections / caustic ripple effect
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    for i in range(40):
        cx = (i * 73) % width
        cy = (i * 97) % height
        rad = 40 + (i * 7) % 80
        overlay_draw.ellipse([cx - rad, cy - rad, cx + rad, cy + rad], outline=(100, 220, 255, 35), width=2)
    
    # Bottom tech glow
    overlay_draw.rectangle([0, height - 120, width, height], fill=(10, 25, 40, 210))
    
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    img = img.filter(ImageFilter.GaussianBlur(radius=0.5))
    
    # Crisp contrast enhancement
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.15)
    
    img.save(path, "JPEG", quality=92)
    print(f"Created: {path}")

def create_egg_processing_image(path):
    width, height = 1600, 1000
    img = Image.new("RGB", (width, height), (28, 45, 38))
    draw = ImageDraw.Draw(img)

    # Industrial stainless steel & warm golden food-grade ambient gradient
    for y in range(height):
        ratio = y / height
        r = int(35 + 30 * ratio + 15 * math.sin(ratio * math.pi))
        g = int(50 + 25 * ratio)
        b = int(40 + 20 * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Stainless steel conical spray drying tower
    tower_cx = width // 2
    draw.polygon([
        (tower_cx - 280, 150),
        (tower_cx + 280, 150),
        (tower_cx + 260, 600),
        (tower_cx, 850),
        (tower_cx - 260, 600)
    ], fill=(160, 175, 180), outline=(210, 225, 230))

    # Golden powder cyclone chamber & inspection ports
    draw.ellipse([tower_cx - 60, 360, tower_cx + 60, 480], fill=(225, 190, 80), outline=(245, 220, 130), width=4)
    draw.ellipse([tower_cx - 40, 380, tower_cx + 40, 460], fill=(245, 210, 95))

    # Secondary cyclones
    draw.polygon([(tower_cx - 520, 250), (tower_cx - 360, 250), (tower_cx - 380, 620), (tower_cx - 440, 780), (tower_cx - 500, 620)], fill=(130, 145, 150), outline=(180, 195, 200))
    draw.polygon([(tower_cx + 360, 250), (tower_cx + 520, 250), (tower_cx + 500, 620), (tower_cx + 440, 780), (tower_cx + 380, 620)], fill=(130, 145, 150), outline=(180, 195, 200))

    # Clean stainless steel piping
    draw.rectangle([tower_cx - 500, 180, tower_cx + 500, 220], fill=(190, 205, 210), outline=(120, 135, 140), width=2)
    draw.rectangle([tower_cx - 400, 720, tower_cx + 400, 750], fill=(190, 205, 210), outline=(120, 135, 140), width=2)

    # Ambient food-grade golden lighting
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.ellipse([tower_cx - 250, 200, tower_cx + 250, 700], fill=(235, 201, 117, 35))
    overlay_draw.rectangle([0, height - 120, width, height], fill=(18, 45, 36, 210))

    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    img = img.filter(ImageFilter.GaussianBlur(radius=0.5))
    
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.15)
    
    img.save(path, "JPEG", quality=92)
    print(f"Created: {path}")

os.makedirs("assets/images/industries", exist_ok=True)
create_water_tech_image("assets/images/industries/water-tech.jpg")
create_egg_processing_image("assets/images/industries/egg-processing.jpg")
