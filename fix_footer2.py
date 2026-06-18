import os
import re

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

footer_css = """        /* Footer */
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
        }

        .footer-info {
            flex: 1;
            text-align: left;
        }

        .footer-info h3 {
            color: white;
            font-size: 1.3rem;
            margin-bottom: 1.5rem;
            font-weight: 400;
        }

        .footer-contact {
            margin-bottom: 1.25rem;
        }

        .footer-contact h4 {
            color: white;
            font-size: 0.9rem;
            margin-bottom: 0.4rem;
            font-weight: 600;
        }

        .footer-contact p {
            margin: 0 0 0.2rem 0;
            font-size: 0.9rem;
        }

        .footer-links {
            flex: 0 0 140px;
            text-align: left;
        }

        .footer-links h4 {
            color: rgba(255,255,255,0.6);
            font-size: 1.05rem;
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
            padding: 0;
        }

        .footer-links a {
            color: rgba(255,255,255,0.85);
            text-decoration: underline;
            font-size: 0.9rem;
        }

        .footer-links a:hover {
            color: white;
        }

        .footer-bottom {
            background: rgba(0,0,0,0.2);
            padding: 1rem 0;
            text-align: center;
        }

        .footer-bottom .container {
            display: block;
        }

        .footer-bottom p {
            margin: 0;
            font-size: 0.9rem;
            color: rgba(255,255,255,0.7);
        }

        .footer-bottom .social-links {
            display: inline-block;
            margin: 0.5rem 0 0 0;
        }

        .footer-bottom .social-links a {
            color: rgba(255,255,255,0.8);
            text-decoration: none;
            font-size: 0.9rem;
        }

        .footer-bottom .social-links a:hover {
            color: white;
        }

        .placeholder { color: rgba(255,255,255,0.5); font-style: italic; }

        @media (max-width: 768px) {
            .footer-grid { flex-direction: column; gap: 2rem; }
        }"""

for filename in ['index.html', 'about.html', 'eligibility.html', 'careers.html', 'contact.html']:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove any existing footer CSS blocks (all variations)
    content = re.sub(r'        /\* Advanced Footer \*/.*?        @media \(max-width: 768px\) \{.*?\}&#x27,
                       '', content, flags=re.DOTALL)
    content = re.sub(r'        /\* Footer \*/.*?        @media \(max-width: 768px\) \{.*?\}&#x27;,
                       '', content, flags=re.DOTALL)
    
    # Also remove old simple footer CSS if still there
    content = re.sub(r'        footer \{.*?\}&#x27;, '', content, flags=re.DOTALL)
    content = re.sub(r'        \.social-links \{.*?\}&#x27;, '', content, flags=re.DOTALL)
    
    # Find </style> and insert footer CSS before it
    content = content.replace('    </style>', footer_css + &#x27;\n    </style>&#x27;)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed: {filename}")

print("\nFooter CSS added to all pages.")
