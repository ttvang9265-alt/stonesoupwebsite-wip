# fix_footer_remove_office_info.py
import os, glob

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

for filepath in glob.glob(os.path.join(dir_path, "*.html")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Pattern to remove: Stone Soup Administration block + Main Office Phone block
    old_footer = """                    <div class="footer-info">
                        <h3>Stone Soup Fresno</h3>
                        <div class="footer-contact">
                            <h4>Stone Soup Administration</h4>
                            <p>1345 E Bulldog Ln</p>
                            <p>Fresno, CA 93710</p>
                        </div>
                        <div class="footer-contact">
                            <h4>Main Office Phone</h4>
                            <p>Phone: (559) 224-7613</p>
                        </div>
                    </div>"""
    
    new_footer = """                    <div class="footer-info">
                        <h3>Stone Soup Fresno</h3>
                        <p style="color: rgba(255,255,255,0.7); line-height: 1.8;">1345 E Bulldog Ln<br>Fresno, CA 93710</p>
                        <p style="color: rgba(255,255,255,0.7); margin-top: 0.5rem;">Phone: (559) 224-7613</p>
                    </div>"""
    
    content = content.replace(old_footer, new_footer)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {os.path.basename(filepath)}")
    else:
        print(f"No change: {os.path.basename(filepath)}")

print("\nDone!")
