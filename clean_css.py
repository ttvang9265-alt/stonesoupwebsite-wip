import os

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

for filename in os.listdir(dir_path):
    if not filename.endswith('.html'): continue
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Remove old duplicate .btn-primary:hover (the one with primary-light/transform only)
    content = content.replace(
        """        .btn-primary:hover {
            background: var(--primary-light);
            transform: translateY(-1px);
        }

""", "")
    
    # Remove standalone old .btn-secondary:hover  
    content = content.replace(
        """        .btn-secondary:hover {
            background: #5a6268;
            transform: translateY(-1px);
        }

""", "")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned duplicates: {filename}")
    else:
        print(f"No duplicates: {filename}")

print("\nDone!")
