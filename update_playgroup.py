# update_playgroup.py
import os, re

filepath = r'C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\about.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the playgroup section and replace it
# Start marker
start_marker = '<div class="program-detail" id="playgroup">'
end_marker = '<div class="program-detail" id="hmong">'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    old_section = content[start_idx:end_idx]
    
    new_section = """                <div class="program-detail" id="playgroup">
                    <h3>Playgroup</h3>
                    <p>Playgroup is an enrichment program for parents/caring adults of children ages 0-5. Through teacher-led academic engagement, parent and child learn through play, participate in parent education sessions, and receive supportive services that are designed for families to strengthen social-emotional development, enhance school readiness skills, and build bonds between children and their families.</p>
                    <p><strong>What to Expect:</strong></p>
                    <ul>
                        <li>Children ages 0-5</li>
                        <li>1 parent or caregiver accompanies child to 1.5 hour class sessions</li>
                        <li>Creative classroom environment: Learning stations + indoor playroom</li>
                        <li>Choose cohort on Monday &amp; Wednesday, or Tuesday &amp; Thursday</li>
                    </ul>
                    <div style="margin-top: 1.5rem;">
                        <a href="eligibility.html" class="btn btn-outline">View Eligibility &amp; Fees</a>
                    </div>
                </div>

                """
    
    content = content.replace(old_section, new_section)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated about.html playgroup section!')
else:
    print('Could not find markers')
