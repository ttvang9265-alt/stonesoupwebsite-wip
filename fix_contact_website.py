# fix_contact_website.py
import os

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\contact.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the Website section
old = """                    <div class="contact-method">
                        <h4>&#x1F310; Website</h4>
                        <p>www.stonesoupfresno.com</p>
                    </div>

                    <div class="contact-method">
                        <h4>&#x1F4AC; Social Media</h4>"""

new = """                    <div class="contact-method">
                        <h4>&#x1F4AC; Social Media</h4>"""

if old in content:
    content = content.replace(old, new)
    print("Removed Website section")
else:
    # Try without the emoji
    old2 = """                    <div class="contact-method">
                        <h4>Website</h4>
                        <p>www.stonesoupfresno.com</p>
                    </div>

                    <div class="contact-method">
                        <h4>Social Media</h4>"""
    if old2 in content:
        content = content.replace(old2, new)
        print("Removed Website section (without emoji)")
    else:
        print("Could not find Website section")
        import re
        # Show what's there
        match = re.search(r'<h4>.*Website.*</h4>.*?<p>.*?</p>.*?(?=<h4>.*Social)', content, re.DOTALL)
        if match:
            print(f"Found: {match.group()[:100]}...")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
