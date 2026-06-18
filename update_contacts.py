import os, re

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

for filename in [f for f in os.listdir(dir_path) if f.endswith('.html')]:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # --- Footer left column ---
    content = content.replace(
        '<p class="placeholder">[Street Address]</p>',
        '<p>1345 E Bulldog Ln</p>'
    )
    content = content.replace(
        '<p>Fresno, CA [ZIP Code]</p>',
        '<p>Fresno, CA 93710</p>'
    )
    content = content.replace(
        '<p class="placeholder">Phone: [Phone Number]</p>',
        '<p>Phone: (559) 224-7613</p>'
    )
    
    # --- Contact page / general placeholders ---
    content = content.replace(
        '<p class="placeholder">[Address placeholder]</p>',
        '<p>1345 E Bulldog Ln</p>'
    )
    content = content.replace(
        '<p class="placeholder">[Phone placeholder]</p>',
        '<p>(559) 224-7613</p>'
    )
    content = content.replace(
        '<p class="placeholder">[Email placeholder]</p>',
        '<p>www.stonesoupfresno.com</p>'
    )
    content = content.replace(
        '<p class="placeholder">[Phone Number]</p>',
        '<p>(559) 224-7613</p>'
    )
    content = content.replace(
        '<p class="placeholder">[Email Address]</p>',
        '<p>www.stonesoupfresno.com</p>'
    )
    
    # --- Contact page specific blocks ---
    # Pattern: Address label followed by placeholders on next lines
    content = re.sub(
        r'(<p><strong>Address:</strong></p>)\s*<p[^>]*>\[.*?\]</p>\s*<p>.*?</p>',
        r'\1\n                    <p>1345 E Bulldog Ln</p>\n                    <p>Fresno, CA 93710</p>',
        content
    )
    content = re.sub(
        r'(<p><strong>Main Phone:</strong></p>)\s*<p[^>]*>\[.*?\]</p>',
        r'\1\n                    <p>(559) 224-7613</p>',
        content
    )
    content = re.sub(
        r'(<p><strong>Website:</strong></p>)\s*<p[^>]*>\[.*?\]</p>',
        r'\1\n                    <p><a href="https://www.stonesoupfresno.com" target="_blank">www.stonesoupfresno.com</a></p>',
        content
    )
    # Remove Hours of Operation if it's a placeholder
    content = re.sub(
        r'(<div class="contact-info-card">)\s*<h3>Hours of Operation</h3>\s*<p[^>]*>\[.*?\]</p>\s*<p[^>]*>\[.*?\]</p>\s*(</div>)',
        r'',  # remove the whole card
        content
    )
    
    # --- Remove leftover placeholder classes on real data ---
    content = content.replace('<p class="placeholder">Phone:', '<p>Phone:')
    content = content.replace('<p class="placeholder">', '<p>')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filename}")
    else:
        print(f"No changes: {filename}")

print("\nDone!")
