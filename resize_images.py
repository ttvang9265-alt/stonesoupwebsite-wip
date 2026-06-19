import os
from PIL import Image

base = r'C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\images'

for folder in os.listdir(base):
    folder_path = os.path.join(base, folder)
    if not os.path.isdir(folder_path):
        continue
    
    for fname in os.listdir(folder_path):
        if not fname.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        filepath = os.path.join(folder_path, fname)
        
        try:
            img = Image.open(filepath)
            # Convert to RGB if needed
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # Resize if width > 1920
            max_width = 1920
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.LANCZOS)
            
            # Save as optimized JPEG
            output = os.path.join(folder_path, fname)
            img.save(output, 'JPEG', quality=85, optimize=True)
            
            new_size = os.path.getsize(output) / 1024
            print(f"Done: {folder}/{fname} -> {new_size:.0f} KB")
        except Exception as e:
            print(f"Error: {folder}/{fname} - {e}")

print("\nAll images resized!")
