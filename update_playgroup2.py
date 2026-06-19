import os

filepath = r'C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\about.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the playgroup section bounds
start_text = '                <div class="program-detail" id="playgroup">\u0027
start_idx = content.find(start_text)
end_text = '                <div class="program-detail" id="hmong">'
end_idx = content.find(end_text, start_idx)

if start_idx == -1 or end_idx == -1:
    print("Could not find markers!")
    # Try finding with different whitespace
    start_idx = content.find('id="playgroup"')
    print(f"Found playgroup at index {start_idx}")
    raise SystemExit

old_section = content[start_idx:end_idx]

# New section with original layout but real information
new_section = """                <div class="program-detail" id="playgroup">
                    <h3>🧸 Playgroup</h3>
                    <p>Playgroup is an enrichment program for parents/caring adults of children ages 0-5. Through teacher-led academic engagement, parent and child learn through play, participate in parent education sessions, and receive supportive services that are designed for families to strengthen social-emotional development, enhance school readiness skills, and build bonds between children and their families.</p>
                    <div class="program-meta">
                        <div class="program-meta-item"><strong>Age:</strong> 0-5 years</div>
                        <div class="program-meta-item"><strong>Schedule:</strong> Monday &amp; Wednesday or Tuesday &amp; Thursday</div>
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

print("Updated about.html - old layout restored with real information.")
