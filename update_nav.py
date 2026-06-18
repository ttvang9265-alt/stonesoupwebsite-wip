import os
import re

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

for filename in ['index.html', 'about.html', 'eligibility.html', 'careers.html', 'contact.html']:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Increase logo image size (remove logo-text CSS, make img bigger)
    old_logo_css = """        .logo {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            text-decoration: none;
        }

        .logo img {
            height: 40px;
            width: auto;
        }

        .logo-text {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--primary);
        }"""
    
    new_logo_css = """        .logo {
            display: flex;
            align-items: center;
            text-decoration: none;
        }

        .logo img {
            height: 75px;
            width: auto;
        }"""
    
    content = content.replace(old_logo_css, new_logo_css)
    
    # 2. Remove the text span from HTML, keep only image
    old_html = """                <a href="index.html" class="logo">
                    <img src="logo.jpg" alt="Stone Soup Fresno Logo">
                    <span class="logo-text">Stone Soup Fresno</span>
                </a>"""
    
    new_html = """                <a href="index.html" class="logo">
                    <img src="logo.jpg" alt="Stone Soup Fresno">
                </a>"""
    
    content = content.replace(old_html, new_html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated: {filename}")

print("\nDone!")
