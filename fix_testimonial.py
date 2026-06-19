import os

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace testimonial
old_testimonial = '            <p style="font-size: 1.25rem; color: var(--text); line-height: 1.8; margin-bottom: 1.5rem; font-style: italic;">Stone Soup Fresno has been an incredible resource for our family. The preschool program prepared our child so well for kindergarten, and the community support has been amazing. The teachers truly care about every child.</p>'

new_testimonial = '''            <p style="font-size: 1.15rem; color: var(--text); line-height: 1.8; margin-bottom: 0.75rem; font-style: italic;">This is an amazing campus for kids &#x1F60A;</p>
            <p style="font-size: 1.15rem; color: var(--text); line-height: 1.8; margin-bottom: 0.75rem; font-style: italic;">The staff is beyond nice and accommodating. I really enjoy the structure and the segway they do between different lessons.</p>
            <p style="font-size: 1.15rem; color: var(--text); line-height: 1.8; margin-bottom: 1.5rem; font-style: italic;">Great activities &#x1F60A;</p>
            <p style="color: var(--text-light); font-size: 0.9rem; margin-bottom: 0.5rem;">&#x2B50;&#x2B50;&#x2B50;&#x2B50;&#x2B50; &#x2022; 4 years ago</p>'''

content = content.replace(old_testimonial, new_testimonial)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated testimonial with real Google review!")
