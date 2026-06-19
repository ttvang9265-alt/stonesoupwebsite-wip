# update_donate_links.py
import os, glob

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

for filepath in glob.glob(os.path.join(dir_path, "*.html")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Replace all Donate buttons that link to #
    content = content.replace(
        '<a href="#" class="btn btn-secondary">Donate</a>',
        '<a href="https://www.paypal.com/paypalme/StoneSoupFresnoCA" target="_blank" class="btn btn-secondary">Donate</a>'
    )
    
    # Also catch any with just href="#" that are donate buttons
    content = content.replace(
        'href="#" class="btn btn-secondary"',
        'href="https://www.paypal.com/paypalme/StoneSoupFresnoCA" target="_blank" class="btn btn-secondary"'
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {os.path.basename(filepath)}")
    else:
        print(f"No changes: {os.path.basename(filepath)}")

print("\nDone! All Donate buttons link to PayPal.")
