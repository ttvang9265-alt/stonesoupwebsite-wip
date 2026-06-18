import os

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

for filename in ['index.html', 'about.html', 'eligibility.html', 'careers.html', 'contact.html']:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Reduce logo from 80px to 55px with max-width constraint
    old_css = """        .logo img {
            height: 80px;
            width: auto;
        }"""
    
    new_css = """        .logo img {
            height: 55px;
            width: auto;
            max-width: 180px;
            object-fit: contain;
        }"""
    
    content = content.replace(old_css, new_css)
    
    # Also tighten header padding
    content = content.replace('padding: 1rem 0;', 'padding: 0.5rem 0;', 1)  # Only replace first occurrence (header)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed: {filename}")

print("\nLogo reduced to 55px, header padding tightened.")
