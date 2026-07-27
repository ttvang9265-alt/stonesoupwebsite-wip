from PIL import Image
import os

src = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\images\cookies with cops event\LEA_4194.JPG"
img = Image.open(src)

max_dim = 1920
ratio = min(max_dim/img.width, max_dim/img.height)
new_size = (int(img.width*ratio), int(img.height*ratio))
img = img.resize(new_size, Image.LANCZOS)
img.save(src, 'JPEG', quality=80, optimize=True)

new_size_mb = os.path.getsize(src) / (1024*1024)
print(f"Done! Size: {new_size[0]}x{new_size[1]}, File: {new_size_mb:.2f}MB")
