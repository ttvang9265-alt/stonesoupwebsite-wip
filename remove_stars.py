import os

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the star rating line
content = content.replace(
    '            <p style="color: var(--text-light); font-size: 0.9rem; margin-bottom: 0.5rem;">⭐⭐⭐⭐⭐</p>',
    ''
)

# Also remove any leftover encoded versions
content = content.replace(
    '<p style="color: var(--text-light); font-size: 0.9rem; margin-bottom: 0.5rem;">\u0026#x2B50;\u0026#x2B50;\u0026#x2B50;\u0026#x2B50;\u0026#x2B50;</p>',
    ''
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed star rating line")
