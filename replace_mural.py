# replace_mural.py
import re

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\about.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find Board of Directors section
pattern = r'<p><strong>Our Board of Directors:</strong></p>\s*<ul[^>]*>.*?\[Board Member Name\].*?</ul>'

replacement = '<div style="margin-top: 2rem; text-align: center;"><img src="images/stonesoup-mural.jpg" alt="Stone Soup Fresno mural" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></div>'

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

if new_content != content:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success! Replaced Board section with mural")
else:
    print("Pattern not found, checking file...")
    match = re.search(r'Our Board of Directors', content)
    if match:
        start = max(0, match.start() - 50)
        end = min(len(content), match.end() + 200)
        print(f"Context: {content[start:end]}")
