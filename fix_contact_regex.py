# fix_contact_regex.py
import re

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\contact.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Use regex to find Get In Touch section and replace its contents
pattern = r'(<h3>Get In Touch</h3>\s*<div class="contact-method">\s*<h4>.*?</h4>.*?)(<div style="margin-top)'

def replace_func(match):
    return """<h3>Get In Touch</h3>

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

                    <div style="margin"""

result = re.sub(pattern, replace_func, content, flags=re.DOTALL)

if result != content:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(result)
    print("Fixed! Email and location restored")
else:
    print("Regex didn't match")
    # Show what we have
    match = re.search(r'<h3>Get In Touch</h3>(.*?)</div>\s*<div class="contact-form-wrapper">', content, re.DOTALL)
    if match:
        print(f"Current section:\n{match.group()[:300]}")
