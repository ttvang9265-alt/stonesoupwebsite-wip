import os

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Insert stars before Felipe line
old_text = '            <p style="color: var(--text-light); font-weight: 600;">&#x2014; Felipe</p>'
new_text = '            <p style="color: var(--text-light); font-size: 0.9rem; margin-bottom: 0.5rem;">⭐ ⭐ ⭐ ⭐ ⭐</p>\n            <p style="color: var(--text-light); font-weight: 600;">&#x2014; Felipe</p>'

content = content.replace(old_text, new_text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added star rating back!")
