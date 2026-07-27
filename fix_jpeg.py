from PIL import Image
import os

src = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\images\home-hero-hr.jpg"
img = Image.open(src)

if img.mode in ('RGBA', 'P'):
    img = img.convert('RGB')

# Force progressive=False and optimize
img.save(src, 'JPEG', quality=85, optimize=True, progressive=False)

size_mb = os.path.getsize(src) / (1024*1024)
print(f"Done! Baseline JPEG: {size_mb:.2f}MB")
