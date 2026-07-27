# fix_contact_complete.py
import re

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\contact.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the div with class contact-info and replace everything inside it
pattern = r'(<div class="contact-info">\s*<h3>Get In Touch</h3>)(.*?)(\s*</div>\s*<div class="contact-form-wrapper">)'

def replace_func(match):
    return match.group(1) + """

                    <div class="contact-method">
                        <h4>&#x1F4CD; Location</h4>
                        <p>1345 E Bulldog Ln<br>Fresno, CA 93710</p>
                    </div>

                    <div class="contact-method">
                        <h4>&#x1F4F1; Phone</h4>
                        <p>(559) 224-7613</p>
                    </div>

                    <div class="contact-method">
                        <h4>&#x1F4E7; Email</h4>
                        <p>info@stonesoupfresno.org</p>
                    </div>

                    <div class="contact-method">
                        <h4>&#x1F4AC; Social Media</h4>
                        <p><a href="https://www.facebook.com/stonesoupfresno/" target="_blank">Facebook: @stonesoupfresno</a></p>
                    </div>

                    <div style="margin-top: 2rem; padding: 1.5rem; background: var(--bg-alt); border-radius: 10px;">
                        <h4 style="color: var(--primary); margin-bottom: 0.75rem;">&#x1F551; Office Hours</h4>
                        <p style="color: var(--text-light);">Monday &#x2013; Friday<br>8:00 AM &#x2013; 5:00 PM</p>
                    </div>
                """ + match.group(3)

result = re.sub(pattern, replace_func, content, flags=re.DOTALL)

if result != content:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(result)
    print("Successfully fixed contact info section!")
else:
    print("Pattern didn't match")

print("Done!")
