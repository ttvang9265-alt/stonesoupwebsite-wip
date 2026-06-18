import os

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

for filename in ['index.html', 'about.html', 'eligibility.html', 'careers.html', 'contact.html']:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace current footer with advanced footer
    old_footer = """    <footer>
        <div class="container">
            <div class="social-links">
                <a href="https://www.facebook.com/stonesoupfresno/" target="_blank">Facebook</a>
            </div>
            <p>© 2026 Stone Soup Fresno. All rights reserved.</p>
        </div>
    </footer>"""
    
    new_footer = """    <!-- Advanced Footer -->
    <footer class="site-footer">
        <div class="footer-main">
            <div class="container">
                <div class="footer-grid">
                    <!-- Left: Company Info -->
                    <div class="footer-info">
                        <h3>Stone Soup Fresno</h3>
                        <div class="footer-contact">
                            <h4>Stone Soup Administration</h4>
                            <p class="placeholder">[Street Address]</p>
                            <p>Fresno, CA [ZIP Code]</p>
                        </div>
                        <div class="footer-contact">
                            <h4>Main Office Phone</h4>
                            <p class="placeholder">Phone: [Phone Number]</p>
                        </div>
                    </div>
                    
                    <!-- Right: Site Links -->
                    <div class="footer-links">
                        <h4>Company</h4>
                        <ul>
                            <li><a href="index.html">Home</a></li>
                            <li><a href="about.html">About</a></li>
                            <li><a href="eligibility.html">Eligibility & Fees</a></li>
                            <li><a href="careers.html">Careers</a></li>
                            <li><a href="contact.html">Contact Us</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="footer-bottom">
            <div class="container">
                <p>© 2026 Stone Soup Fresno. All rights reserved.</p>
                <div class="social-links">
                    <a href="https://www.facebook.com/stonesoupfresno/" target="_blank">Facebook</a>
                </div>
            </div>
        </div>
    </footer>"""
    
    content = content.replace(old_footer, new_footer)
    
    # Add advanced footer CSS before the existing footer CSS
    old_footer_css = """        footer {
            background: #1a1a1a;
            color: white;
            padding: 2rem 0;
            text-align: center;
        }

        .social-links { display: flex; justify-content: center; gap: 1.5rem; margin-bottom: 1rem; }
        .social-links a { color: white; text-decoration: none; font-size: 1.2rem; }
        .social-links a:hover { color: var(--accent); }"""
    
    new_footer_css = """        /* Advanced Footer */
        .site-footer {
            background: var(--primary);
            color: rgba(255,255,255,0.9);
        }

        .footer-main {
            padding: 3rem 0;
        }

        .footer-grid {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 3rem;
        }

        .footer-info h3 {
            color: white;
            font-size: 1.35rem;
            margin-bottom: 1.5rem;
            font-weight: 500;
        }

        .footer-contact {
            margin-bottom: 1.5rem;
        }

        .footer-contact h4 {
            color: rgba(255,255,255,0.65);
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 0.75rem;
            font-weight: 600;
        }

        .footer-contact p {
            margin-bottom: 0.35rem;
            font-size: 0.95rem;
        }

        .footer-links h4 {
            color: rgba(255,255,255,0.65);
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 1rem;
            font-weight: 600;
        }

        .footer-links ul {
            list-style: none;
        }

        .footer-links li {
            margin-bottom: 0.6rem;
        }

        .footer-links a {
            color: rgba(255,255,255,0.9);
            text-decoration: none;
            font-size: 0.95rem;
            transition: color 0.3s;
        }

        .footer-links a:hover {
            color: white;
            text-decoration: underline;
        }

        .footer-bottom {
            background: rgba(0,0,0,0.15);
            padding: 1.25rem 0;
        }

        .footer-bottom .container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .footer-bottom p {
            margin: 0;
            font-size: 0.9rem;
            color: rgba(255,255,255,0.7);
        }

        .footer-bottom .social-links {
            display: flex;
            gap: 1rem;
            margin: 0;
        }

        .footer-bottom .social-links a {
            color: rgba(255,255,255,0.8);
            text-decoration: none;
            font-size: 0.95rem;
            padding: 0.35rem 0.75rem;
            border: 1px solid rgba(255,255,255,0.3);
            border-radius: 4px;
            transition: all 0.3s;
        }

        .footer-bottom .social-links a:hover {
            background: white;
            color: var(--primary);
        }

        .placeholder { color: rgba(255,255,255,0.5); font-style: italic; }

        @media (max-width: 768px) {
            .footer-grid { grid-template-columns: 1fr; gap: 2rem; }
            .footer-bottom .container { flex-direction: column; gap: 1rem; text-align: center; }
        }"""
    
    content = content.replace(old_footer_css, new_footer_css)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated: {filename}")

print("\nDone! Advanced footer added to all pages.")
