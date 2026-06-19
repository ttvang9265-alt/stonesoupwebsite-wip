# update_nav_programs.py
import os

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

for filename in ['index.html', 'about.html', 'eligibility.html', 'careers.html', 'contact.html', 'programs.html']:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Add Programs link after About in nav
    # Pattern: About link followed by Eligibility link
    content = content.replace(
        '<li><a href="about.html">About</a></li>\n                    <li><a href="eligibility.html">Eligibility &amp; Fees</a></li>',
        '<li><a href="about.html">About</a></li>\n                    <li><a href="programs.html">Programs</a></li>\n                    <li><a href="eligibility.html">Eligibility &amp; Fees</a></li>'
    )
    
    # Also handle case where About has active class
    content = content.replace(
        '<li><a href="about.html" class="active">About</a></li>\n                    <li><a href="eligibility.html">Eligibility &amp; Fees</a></li>',
        '<li><a href="about.html" class="active">About</a></li>\n                    <li><a href="programs.html">Programs</a></li>\n                    <li><a href="eligibility.html">Eligibility &amp; Fees</a></li>'
    )
    
    # Also update footer links on all pages
    content = content.replace(
        '<li><a href="about.html">About</a></li>\n                            <li><a href="eligibility.html">Eligibility &amp; Fees</a></li>',
        '<li><a href="about.html">About</a></li>\n                            <li><a href="programs.html">Programs</a></li>\n                            <li><a href="eligibility.html">Eligibility &amp; Fees</a></li>'
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filename}")
    else:
        print(f"No changes: {filename}")

print("\nDone!")
