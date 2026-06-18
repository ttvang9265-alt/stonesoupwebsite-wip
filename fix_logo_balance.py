import os

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

for filename in ['index.html', 'about.html', 'eligibility.html', 'careers.html', 'contact.html']:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Bump from 55px to 70px - better balance
    content = content.replace('height: 55px;', 'height: 70px;')
    
    # Also make sure header padding is consistent
    # Find header padding and set to 0.5rem 0
    if 'padding: 0.5rem 0;' not in content:
        content = content.replace('padding: 1rem 0;', 'padding: 0.5rem 0;', 1)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed: {filename}")

print("\nLogo set to 70px across all pages.")
