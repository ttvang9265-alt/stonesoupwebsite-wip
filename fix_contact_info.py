# fix_contact_info.py
import os

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\contact.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_section = """                    <div class="contact-method">
                        <h4>📱 Phone</h4>
                        <p>Contact us for phone number</p>
                    </div>

                    <div class="contact-method">
                        <h4>📧 Email</h4>
                        <p>Contact us for email address</p>
                    </div>

                    <div class="contact-method">
                        <h4>📍 Location</h4>
                        <p>Stone Soup Fresno<br>Fresno, California</p>
                    </div>

                    <div class="contact-method">
                        <h4>💬 Social Media</h4>
                        <p><a href="https://www.facebook.com/stonesoupfresno/" target="_blank">Facebook: @stonesoupfresno</a></p>
                    </div>

                    <div style="margin-top: 2rem; padding: 1.5rem; background: var(--bg-alt); border-radius: 10px;">
                        <h4 style="color: var(--primary); margin-bottom: 0.75rem;">🕒 Office Hours</h4>
                        <p style="color: var(--text-light);">Please contact us for current office hours.</p>
                    </div>"""

new_section = """                    <div class="contact-method">
                        <h4>📱 Phone</h4>
                        <p>(559) 224-7613</p>
                    </div>

                    <div class="contact-method">
                        <h4>🌐 Website</h4>
                        <p>www.stonesoupfresno.com</p>
                    </div>

                    <div class="contact-method">
                        <h4>📍 Location</h4>
                        <p>1345 E Bulldog Ln<br>Fresno, CA 93710</p>
                    </div>

                    <div class="contact-method">
                        <h4>💬 Social Media</h4>
                        <p><a href="https://www.facebook.com/stonesoupfresno/" target="_blank">Facebook: @stonesoupfresno</a></p>
                    </div>

                    <div style="margin-top: 2rem; padding: 1.5rem; background: var(--bg-alt); border-radius: 10px;">
                        <h4 style="color: var(--primary); margin-bottom: 0.75rem;">🕒 Office Hours</h4>
                        <p style="color: var(--text-light);">Monday – Friday<br>8:00 AM – 5:00 PM</p>
                    </div>"""

if old_section in content:
    content = content.replace(old_section, new_section)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated contact info!")
else:
    print("Could not find exact match - checking file...")
    # Try finding parts
    if "Contact us for phone number" in content:
        print("Found phone placeholder")
    if "Please contact us for current office hours" in content:
        print("Found office hours placeholder")
