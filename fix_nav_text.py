import os

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

for filename in ['index.html', 'about.html', 'eligibility.html', 'careers.html', 'contact.html']:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Try multiple patterns for the nav-links hover/active rules
    patterns = [
        # Pattern 1: combined selector
        ("""        .nav-links a:hover, .nav-links a.active {
            color: var(--primary);
        }
""",
        """        .nav-links a:hover, .nav-links a.active {
            color: var(--primary);
        }

        .nav-links .btn {
            color: white !important;
        }

        .nav-links .btn:hover {
            color: white !important;
        }

"""),
        # Pattern 2: separate rules
        ("""        .nav-links a.active {
            color: var(--primary);
            font-weight: 600;
        }
""",
        """        .nav-links a.active {
            color: var(--primary);
            font-weight: 600;
        }

        .nav-links .btn {
            color: white !important;
        }

        .nav-links .btn:hover {
            color: white !important;
        }

"""),
        # Pattern 3: just hover rule (no active)
        ("""        .nav-links a:hover {
            color: var(--primary);
        }
""",
        """        .nav-links a:hover {
            color: var(--primary);
        }

        .nav-links .btn {
            color: white !important;
        }

        .nav-links .btn:hover {
            color: white !important;
        }

""")
    ]
    
    for old, new in patterns:
        if old in content:
            content = content.replace(old, new)
            break
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filename}")
    else:
        print(f"No match: {filename}")

print("\nDone!")
