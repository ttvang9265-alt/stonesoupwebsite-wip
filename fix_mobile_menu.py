import os, glob

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

missing_css = """.menu-toggle { display: block; }
            .nav-links { display: none; }
            """

for filepath in glob.glob(os.path.join(dir_path, "*.html")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if the mobile menu CSS is missing
    if ".menu-toggle { display: block; }" not in content:
        # Insert it into the media query
        old = "@media (max-width: 768px) {\n            .footer-grid { flex-direction: column; gap: 2rem; }"
        new = "@media (max-width: 768px) {\n            .menu-toggle { display: block; }\n            .nav-links { display: none; }\n            .footer-grid { flex-direction: column; gap: 2rem; }"
        content = content.replace(old, new)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {os.path.basename(filepath)}")
    else:
        print(f"Already OK: {os.path.basename(filepath)}")

print("\nDone!")
