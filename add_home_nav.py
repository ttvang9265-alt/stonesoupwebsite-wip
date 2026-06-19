# add_home_nav.py
import os

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

for filename in ['index.html', 'about.html', 'programs.html', 'eligibility.html', 'careers.html', 'contact.html']:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Add Home link before About in nav
    # For pages where About has no active class
    content = content.replace(
        '<ul class="nav-links">\n                    <li><a href="about.html">About</a></li>',
        '<ul class="nav-links">\n                    <li><a href="index.html">Home</a></li>\n                    <li><a href="about.html">About</a></li>'
    )
    
    # For pages where About has active class
    content = content.replace(
        '<ul class="nav-links">\n                    <li><a href="about.html" class="active">About</a></li>',
        '<ul class="nav-links">\n                    <li><a href="index.html">Home</a></li>\n                    <li><a href="about.html" class="active">About</a></li>'
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filename}")
    else:
        print(f"No changes: {filename}")

print("\nDone! Home link added to all pages.")
