import os

filepath = r'C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\about.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the playgroup section
start_text = 'id="playgroup"'
end_text = 'id="hmong"'
start_idx = content.find(start_text)
end_idx = content.find(end_text, start_idx)

if start_idx == -1 or end_idx == -1:
    print("Could not find markers!")
    raise SystemExit

# Navigate back to the start of the div tag
actual_start = content.rfind('<div', 0, start_idx)
old_section = content[actual_start:end_idx]

# New section: original layout with real info
new_section = """<div class="program-detail" id="playgroup">
                    <h3>&#x1F9F8; Playgroup</h3>
                    <p>Playgroup is an enrichment program for parents/caring adults of children ages 0-5. Through teacher-led academic engagement, parent and child learn through play, participate in parent education sessions, and receive supportive services that are designed for families to strengthen social-emotional development, enhance school readiness skills, and build bonds between children and their families.</p>
                    <div class="program-meta">
                        <div class="program-meta-item"><strong>Age:</strong> 0-5 years</div>
                        <div class="program-meta-item"><strong>Schedule:</strong> Mon &amp; Wed or Tue &amp; Thu</div>
                        <div class="program-meta-item"><strong>Focus:</strong> Social-Emotional Development</div>
                    </div>
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

print("Done! Old layout restored with real information.")
