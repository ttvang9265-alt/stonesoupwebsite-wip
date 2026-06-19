import os

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

for filename in ['index.html', 'about.html', 'eligibility.html', 'careers.html', 'contact.html']:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Revert .btn-primary back to green bg with white text (ensure text is white)
    content = content.replace(
        """        .btn-primary {
            background: white;
            color: var(--primary);
            border: 2px solid white;
        }

        .btn-primary:hover {
            background: var(--primary);
            color: white;
            border-color: var(--primary);
        }""",
        """        .btn-primary {
            background: var(--primary);
            color: white;
        }

        .btn-primary:hover {
            background: var(--primary-light);
            transform: translateY(-1px);
        }"""
    )
    
    # Revert .btn-secondary back to grey bg with white text (ensure text is white)
    content = content.replace(
        """        .btn-secondary {
            background: white;
            color: var(--secondary);
            border: 2px solid white;
        }

        .btn-secondary:hover {
            background: var(--secondary);
            color: white;
            border-color: var(--secondary);
        }""",
        """        .btn-secondary {
            background: var(--secondary);
            color: white;
        }

        .btn-secondary:hover {
            background: #5a6268;
            transform: translateY(-1px);
        }"""
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Reverted: {filename}")
    else:
        print(f"No changes: {filename}")

print("\nDone! Buttons back to colored backgrounds with white text.")
