# revert_about_add_email_contact.py
import os

# Fix About page - revert board section back to placeholders
about_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\about.html"
with open(about_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the email back to board member placeholders
old_section = """                <p><strong>Our Board of Directors:</strong></p>
                <ul style="margin-left: 1.5rem; color: var(--text-light); line-height: 1.8;">
                    <li>info@stonesoupfresno.org</li>
                </ul>"""

new_section = """                <p><strong>Our Board of Directors:</strong></p>
                <ul style="margin-left: 1.5rem; color: var(--text-light); line-height: 1.8;">
                    <li>[Board Member Name]</li>
                    <li>[Board Member Name]</li>
                    <li>[Board Member Name]</li>
                </ul>"""

content = content.replace(old_section, new_section)

with open(about_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Reverted About page board section")

# Fix Contact page - add email to Get In Touch section
contact_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\contact.html"
with open(contact_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the phone section and add email after it
old_contact = """                    <div class="contact-method">
                        <h4>&#x1F4F1; Phone</h4>
                        <p>(559) 224-7613</p>
                    </div>

                    <div class="contact-method">
                        <h4>&#x1F310; Website</h4>
                        <p>www.stonesoupfresno.com</p>
                    </div>"""

new_contact = """                    <div class="contact-method">
                        <h4>&#x1F4F1; Phone</h4>
                        <p>(559) 224-7613</p>
                    </div>

                    <div class="contact-method">
                        <h4>&#x1F4E7; Email</h4>
                        <p>info@stonesoupfresno.org</p>
                    </div>

                    <div class="contact-method">
                        <h4>&#x1F310; Website</h4>
                        <p>www.stonesoupfresno.com</p>
                    </div>"""

content = content.replace(old_contact, new_contact)

with open(contact_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added email to Contact page")
