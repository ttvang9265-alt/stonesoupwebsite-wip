import os

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

for filename in ['index.html', 'about.html', 'eligibility.html', 'careers.html', 'contact.html']:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Add missing .btn-secondary CSS if it's NOT there (careers page is missing it)
    if ".btn-secondary {" not in content:
        # Insert it right after .btn-primary
        content = content.replace(
            """        .btn-primary {
            background: var(--primary);
            color: white;
        }""",
            """        .btn-primary {
            background: var(--primary);
            color: white;
        }

        .btn-secondary {
            background: var(--secondary);
            color: white;
        }"""
        )
    
    # 2. Change nav button colors to white for visibility against green header
    # Update .btn-primary nav button styles - white bg with green text/border
    content = content.replace(
        """        .btn-primary {
            background: var(--primary);
            color: white;
        }""",
        """        .btn-primary {
            background: white;
            color: var(--primary);
            border: 2px solid white;
        }

        .btn-primary:hover {
            background: var(--primary);
            color: white;
            border-color: var(--primary);
        }"""
    )
    
    # Update .btn-secondary - white bg with grey text/border
    content = content.replace(
        """        .btn-secondary {
            background: var(--secondary);
            color: white;
        }""",
        """        .btn-secondary {
            background: white;
            color: var(--secondary);
            border: 2px solid white;
        }

        .btn-secondary:hover {
            background: var(--secondary);
            color: white;
            border-color: var(--secondary);
        }"""
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filename}")
    else:
        print(f"No changes: {filename}")

print("\nDone!")
