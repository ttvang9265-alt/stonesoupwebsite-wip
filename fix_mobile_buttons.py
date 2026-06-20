# fix_mobile_button_colors.py
import os, glob

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

for filepath in glob.glob(os.path.join(dir_path, "*.html")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Add specific rules for buttons in mobile menu to keep white text
    old_css = """        .nav-links.show li a.btn {
            width: 100%;
            max-width: 300px;
            margin: 0 auto;
        }"""
    
    new_css = """        .nav-links.show li a.btn {
            width: 100%;
            max-width: 300px;
            margin: 0 auto;
            color: white !important;
        }

        .nav-links.show li a.btn-primary {
            background: var(--primary);
            color: white !important;
        }

        .nav-links.show li a.btn-secondary {
            background: var(--secondary);
            color: white !important;
        }"""
    
    content = content.replace(old_css, new_css)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {os.path.basename(filepath)}")
    else:
        print(f"No change: {os.path.basename(filepath)}")

print("\nDone!")
