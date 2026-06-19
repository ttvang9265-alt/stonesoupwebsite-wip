with open(r'C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

marker = '            <p style=\"color: var(--text-light); font-weight: 600;\">&mdash; Felipe</p>'

if marker in content:
    # Insert stars line before the marker
    stars_line = '            <p style=\"color: var(--text-light); font-size: 0.9rem; margin-bottom: 0.5rem;\">&#x2B50; &#x2B50; &#x2B50; &#x2B50; &#x2B50;</p>'
    content = content.replace(marker, stars_line + '\n' + marker)
    with open(r'C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Added stars')
else:
    print('Marker not found')
