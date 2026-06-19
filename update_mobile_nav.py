# update_mobile_nav.py
import os, glob

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

# New nav HTML to replace the old nav in all files
old_nav_start = '            <nav>'
old_nav_end = '            </nav>'

new_nav = """            <nav>
                <a href="index.html" class="logo">
                    <img src="logo.jpg" alt="Stone Soup Fresno">
                </a>
                <button class="menu-toggle" onclick="toggleMenu()" aria-label="Open menu">&#x2630;</button>
                <ul class="nav-links" id="mobileMenu">"""

# We need to keep the existing li items but add closing elements
# So let's find and replace the entire nav block

for filepath in glob.glob(os.path.join(dir_path, "*.html")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the nav section and replace it
    # The pattern is: <nav> ... </nav> with logo and nav-links inside
    
    # We'll replace just the opening part to add the menu toggle button
    old_opening = """            <nav>
                <a href="index.html" class="logo">
                    <img src="logo.jpg" alt="Stone Soup Fresno">
                </a>
                <ul class="nav-links">"""
    
    new_opening = """            <nav>
                <a href="index.html" class="logo">
                    <img src="logo.jpg" alt="Stone Soup Fresno">
                </a>
                <button class="menu-toggle" onclick="toggleMenu()">&#x2630;</button>
                <ul class="nav-links" id="mobileMenu">"""
    
    content = content.replace(old_opening, new_opening)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated: {os.path.basename(filepath)}")

print("\nHamburger button added to all pages.")
