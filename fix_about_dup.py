import os

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\about.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the second occurrence of "/* Mobile Menu Toggle */" and remove everything until "@media"
first_marker = "        /* Mobile Menu Toggle */"

# Find first occurrence
first_idx = content.find(first_marker)
# Find second occurrence
second_idx = content.find(first_marker, first_idx + 1)

if second_idx != -1:
    # Find the @media that comes after the second block
    media_idx = content.find("@media (max-width: 768px)", second_idx)
    if media_idx != -1:
        # Remove from second_idx to media_idx
        content = content[:second_idx] + content[media_idx:]
        print("Removed duplicate mobile menu CSS block")
    else:
        print("Could not find media query after second block")
else:
    print("No duplicate block found")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
