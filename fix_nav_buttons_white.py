import os

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

for filename in ['index.html', 'about.html', 'eligibility.html', 'careers.html', 'contact.html']:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Add nav button color override after .nav-links a styles
    nav_links_end = """        .nav-links a:hover, .nav-links a.active {
            color: var(--primary);
        }
"""
    
    nav_button_override = """        .nav-links a:hover, .nav-links a.active {
            color: var(--primary);
        }

        .nav-links .btn {
            color: white;
        }

        .nav-links .btn:hover {
            color: white;
        }
"""
    
    content = content.replace(nav_links_end, nav_button_override)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filename}")
    else:
        print(f"No changes: {filename}")

print("\nDone! Nav button text is now white.")
