from PIL import Image
import os

src = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\images\home-hero-hr.png"
img = Image.open(src)

# Convert to RGB if needed (in case it's RGBA)
if img.mode in ('RGBA', 'P'):
    img = img.convert('RGB')

max_dim = 1920
ratio = min(max_dim/img.width, max_dim/img.height)
new_size = (int(img.width*ratio), int(img.height*ratio))
img = img.resize(new_size, Image.LANCZOS)

# Save as JPEG for smaller file size
new_path = src.replace('.png', '.jpg')
img.save(new_path, 'JPEG', quality=85, optimize=True)

new_size_mb = os.path.getsize(new_path) / (1024*1024)
print(f"Done! Size: {new_size[0]}x{new_size[1]}, File: {new_size_mb:.2f}MB")
