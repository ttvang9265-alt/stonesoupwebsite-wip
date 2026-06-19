# revert_home_contact.py
import os

# Revert Home page to 3 columns (remove Office Hours)
home_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\index.html"
with open(home_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the 4-column contact-row and revert to 3 columns
old_home = """            <div class="contact-row">
                <div class="contact-item-home">
                    <h3>&#x1F4CD; Address</h3>
                    <p>1345 E Bulldog Ln<br>Fresno, CA 93710</p>
                </div>
                <div class="contact-item-home">
                    <h3>&#x1F4DE; Phone</h3>
                    <p>(559) 224-7613</p>
                </div>
                <div class="contact-item-home">
                    <h3>&#x1F310; Website</h3>
                    <p>www.stonesoupfresno.com</p>
                </div>
                <div class="contact-item-home">
                    <h3>&#x1F551; Office Hours</h3>
                    <p>Monday &#x2013; Friday<br>8:00 AM &#x2013; 5:00 PM</p>
                </div>
            </div>"""

new_home = """            <div class="contact-row">
                <div class="contact-item-home">
                    <h3>&#x1F4CD; Address</h3>
                    <p>1345 E Bulldog Ln<br>Fresno, CA 93710</p>
                </div>
                <div class="contact-item-home">
                    <h3>&#x1F4DE; Phone</h3>
                    <p>(559) 224-7613</p>
                </div>
                <div class="contact-item-home">
                    <h3>&#x1F310; Website</h3>
                    <p>www.stonesoupfresno.com</p>
                </div>
            </div>"""

content = content.replace(old_home, new_home)

with open(home_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Reverted Home page to 3 columns")
