"""Genera un ícono simple para GCsoft mientras no hay uno real."""
from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    sizes = [16, 32, 48, 64, 128, 256]
    images = []
    
    for size in sizes:
        img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Fondo redondeado
        margin = size // 10
        draw.rounded_rectangle(
            [margin, margin, size - margin, size - margin],
            radius=size // 5,
            fill=(233, 69, 96, 255)   # color highlight de GCsoft
        )
        
        # Texto "GC"
        font_size = max(size // 3, 8)
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        except Exception:
            font = ImageFont.load_default()
        
        text = "GC"
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        tx = (size - tw) // 2
        ty = (size - th) // 2
        draw.text((tx, ty), text, fill="white", font=font)
        
        images.append(img)
    
    out = "/home/claude/gcsoft_reminder/gcsoft.ico"
    images[0].save(out, format="ICO", sizes=[(s, s) for s in sizes],
                   append_images=images[1:])
    print(f"Ícono creado: {out}")

create_icon()
