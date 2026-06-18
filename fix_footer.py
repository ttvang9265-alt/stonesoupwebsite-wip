import os

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

# Read index.html to get the current broken footer CSS
filepath = os.path.join(dir_path, 'index.html')
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# The broken footer CSS - replace it entirely
old_footer_css = """        /* Advanced Footer */
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

new_footer_css = """        /* Advanced Footer */
        .site-footer {
            background: #1a3c1b;
            color: rgba(255,255,255,0.85);
        }

        .footer-main {
            padding: 3rem 0;
        }

        .footer-grid {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            text-align: left;
        }

        .footer-info {
            flex: 1;
        }

        .footer-info h3 {
            color: white;
            font-size: 1.3rem;
            margin-bottom: 1.5rem;
            font-weight: 400;
        }

        .footer-contact {
            margin-bottom: 1.5rem;
        }

        .footer-contact h4 {
            color: white;
            font-size: 0.95rem;
            margin-bottom: 0.5rem;
            font-weight: 600;
        }

        .footer-contact p {
            margin-bottom: 0.2rem;
            font-size: 0.9rem;
        }

        .footer-links {
            flex: 0 0 200px;
            text-align: left;
        }

        .footer-links h4 {
            color: rgba(255,255,255,0.65);
            font-size: 1.1rem;
            margin-bottom: 1rem;
            font-weight: 400;
        }

        .footer-links ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .footer-links li {
            margin-bottom: 0.5rem;
        }

        .footer-links a {
            color: rgba(255,255,255,0.85);
            text-decoration: underline;
            font-size: 0.95rem;
            transition: color 0.3s;
        }

        .footer-links a:hover {
            color: white;
        }

        .footer-bottom {
            background: rgba(0,0,0,0.2);
            padding: 1.25rem 0;
            text-align: center;
        }

        .footer-bottom .container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 1.5rem;
        }

        .footer-bottom p {
            margin: 0;
            font-size: 0.9rem;
            color: rgba(255,255,255,0.7);
        }

        .footer-bottom .social-links {
            display: flex;
            gap: 0.75rem;
            margin: 0;
        }

        .footer-bottom .social-links a {
            color: rgba(255,255,255,0.8);
            text-decoration: none;
            font-size: 0.9rem;
            transition: color 0.3s;
        }

        .footer-bottom .social-links a:hover {
            color: white;
        }

        .placeholder { color: rgba(255,255,255,0.5); font-style: italic; }

        @media (max-width: 768px) {
            .footer-grid { flex-direction: column; gap: 2rem; }
        }"""

# Apply to all files
for filename in ['index.html', 'about.html', 'eligibility.html', 'careers.html', 'contact.html']:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(old_footer_css, new_footer_css)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed: {filename}")

print("\nDone! Footer layout fixed.")
