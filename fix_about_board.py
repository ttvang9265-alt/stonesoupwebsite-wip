# fix_about_board.py
import re

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\about.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the Board section - replace all email instances with placeholders
old_section = """                <p><strong>Our Board of Directors:</strong></p>
                <ul style="margin-left: 1.5rem; color: var(--text-light); line-height: 1.8;">
                    <li>info@stonesoupfresno.org</li>
                    <li>info@stonesoupfresno.org</li>
                    <li>info@stonesoupfresno.org</li>
                </ul>"""

new_section = """                <p><strong>Our Board of Directors:</strong></p>
                <ul style="margin-left: 1.5rem; color: var(--text-light); line-height: 1.8;">
                    <li>[Board Member Name]</li>
                    <li>[Board Member Name]</li>
                    <li>[Board Member Name]</li>
                </ul>"""

if old_section in content:
    content = content.replace(old_section, new_section)
    print("Fixed board section!")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
else:
    # Check what's actually there
    match = re.search(r'Our Board of Directors.*?(</ul>)', content, re.DOTALL)
    if match:
        print(f"Found: {match.group()[:150]}...")
        print("Trying individual replacements...")
        content = content.replace('info@stonesoupfresno.org', '[Board Member Name]')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed with global replace!")

print("Done!")
