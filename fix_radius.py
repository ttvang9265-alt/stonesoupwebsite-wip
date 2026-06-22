# fix_border_radius.py
import os

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\about.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add overflow: hidden to .column.image-col to ensure border-radius clips properly
old_css = """        .two-column .image-col img {
            width: 100%;
            height: auto;
            border-radius: 8px;
            object-fit: cover;
            display: block;
        }"""

new_css = """        .two-column .image-col {
            overflow: hidden;
            border-radius: 8px;
        }

        .two-column .image-col img {
            width: 100%;
            height: auto;
            display: block;
        }"""

if old_css in content:
    content = content.replace(old_css, new_css)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed! Added overflow:hidden to image containers")
else:
    print("Could not find exact match")
