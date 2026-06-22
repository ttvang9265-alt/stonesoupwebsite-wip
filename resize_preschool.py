# resize_preschool_activ.py
from PIL import Image
import os

# Load images
src = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\images\preschool-activ.jpg"

dst = src  # overwrite in place

with Image.open(src) as img:
    # Resize to 1920x1280 (landscape)
    resized = img.resize((1920, 1280), Image.LANCZOS)
    resized.save(dst, 'JPEG', quality=85)
    print(f"Resized preschool-activ.jpg to {resized.size[0]}x{resized.size[1]}")
