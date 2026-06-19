# update_about_remove_programs.py
import os

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\about.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find and remove the Programs Summary section
start_marker = '    <!-- Programs Summary -->'
end_marker = '    <!-- Community Impact / Photo Gallery -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + content[end_idx:]
    print("Removed Programs Summary section")
else:
    print("Could not find markers")

# Also update the CTA to mention programs
old_cta = """            <h2 style="margin-bottom: 1rem;">Want to Learn More?</h2>
            <p style="margin-bottom: 1.5rem; opacity: 0.9;">Get in touch to schedule a tour or learn more about our programs.</p>
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                <a href="contact.html" class="btn btn-white">Contact Us</a>
                <a href="eligibility.html" class="btn btn-outline-light">View Eligibility</a>
            </div>"""

new_cta = """            <h2 style="margin-bottom: 1rem;">Want to Learn More?</h2>
            <p style="margin-bottom: 1.5rem; opacity: 0.9;">Get in touch to schedule a tour or learn more about our programs.</p>
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                <a href="programs.html" class="btn btn-white">Our Programs</a>
                <a href="contact.html" class="btn btn-outline-light">Contact Us</a>
            </div>"""

content = content.replace(old_cta, new_cta)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated About page CTA")
