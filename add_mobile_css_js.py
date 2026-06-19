# add_mobile_css_js.py
import os, glob

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

# CSS to add before mobile media query
mobile_css = """        /* Mobile Menu Toggle */
        .menu-toggle {
            display: none;
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            padding: 0.5rem;
            color: var(--text);
        }

        .nav-links {
            transition: all 0.3s ease;
        }

        .nav-links.show {
            display: flex !important;
            flex-direction: column;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: white;
            z-index: 200;
            padding: 5rem 2rem 2rem;
            align-items: center;
            justify-content: flex-start;
            gap: 2rem;
            list-style: none;
        }

        .nav-links.show li {
            display: block !important;
            width: 100%;
            text-align: center;
        }

        .nav-links.show li a {
            font-size: 1.5rem;
            color: var(--text) !important;
            display: block;
            padding: 0.75rem;
        }

        .nav-links.show li a.btn {
            width: 100%;
            max-width: 300px;
            margin: 0 auto;
        }

        .nav-links.show .menu-close {
            position: absolute;
            top: 1rem;
            right: 1rem;
            font-size: 2rem;
            background: none;
            border: none;
            cursor: pointer;
        }

        """

# JS to add before closing body tag
mobile_js = """
    <script>
        function toggleMenu() {
            const menu = document.getElementById('mobileMenu');
            menu.classList.toggle('show');
            document.body.style.overflow = menu.classList.contains('show') ? 'hidden' : '';
        }
    </script>
"""

for filepath in glob.glob(os.path.join(dir_path, "*.html")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Insert mobile CSS before the existing mobile media query
    old_media = "        @media (max-width: 768px) {"
    content = content.replace(old_media, mobile_css + old_media)
    
    # Show menu toggle on mobile
    old_media_css = """        @media (max-width: 768px) {
            .nav-links li:not(:last-child):not(:nth-last-child(2)) {
                display: none;
            }"""
    
    new_media_css = """        @media (max-width: 768px) {
            .menu-toggle { display: block; }
            .nav-links { display: none; }
            .nav-links li:not(:last-child):not(:nth-last-child(2)) {
                display: none;
            }"""
    
    content = content.replace(old_media_css, new_media_css)
    
    # Add JS before closing body tag
    content = content.replace("</body>\n</html>", mobile_js + "</body>\n</html>")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated: {os.path.basename(filepath)}")

print("\nMobile menu CSS and JS added to all pages.")
