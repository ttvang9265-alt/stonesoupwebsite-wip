import os, re

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

for filename in ['index.html', 'about.html', 'eligibility.html', 'careers.html', 'contact.html']:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Find .nav-links a.active or .nav-links a:hover patterns (flexible spacing)
    # and add the button override right after
    
    # Pattern 1: .nav-links a.active {
    match = re.search(r'(\s+\.nav-links a\.(?:active|hover)[^}]+}\s*)', content)
    if match and '.nav-links .btn' not in content:
        end_pos = match.end()
        insert_text = """

        .nav-links .btn {
            color: white !important;
        }

        .nav-links .btn:hover {
            color: white !important;
        }"""
        content = content[:end_pos] + insert_text + content[end_pos:]
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filename}")
    else:
        print(f"No change: {filename}")

print("\nDone!")
