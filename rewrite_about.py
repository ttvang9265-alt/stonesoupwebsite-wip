# rewrite_about.py
import os

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\about.html"
with open(filepath, 'r', encoding='utf-8') as f:
    original = f.read()

# Split: head + header/nav | body content | footer
head_end = original.find("    <!-- Breadcrumb -->")
footer_start = original.find("    <!-- Footer -->")

top = original[:head_end]
bottom = original[footer_start:]

# New body content matching Educare layout
new_body = """    <!-- About Hero: Large image banner with text overlay -->
    <section class="about-hero" style="background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('images/preschool graduation pictures/Happy(343).JPG') center/cover no-repeat;">
        <div class="container">
            <h1>About Stone Soup Fresno</h1>
            <p>Inspiring children and nurturing families to realize their full potential in America.</p>
        </div>
    </section>

    <!-- Mission Statement: Image left, Text right -->
    <section class="about-section">
        <div class="container">
            <div class="two-column image-left">
                <div class="column image-col">
                    <img src="images/preschool graduation pictures/Happy(59).JPG" alt="Happy children at Stone Soup Fresno">
                </div>
                <div class="column text-col">
                    <h2>Mission Statement</h2>
                    <p>Founded on the belief that every child deserves access to quality early education and every family deserves support, Stone Soup Fresno has been serving the Fresno community for years.</p>
                    <p>Our name comes from the beloved folktale where a community comes together to share what they have, creating something wonderful from seemingly nothing. This spirit of collaboration and community support is at the heart of everything we do.</p>
                    <p>Our goal is to set your child up for educational success &mdash; for the rest of their life.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Stone Soup Experience: Text left, Image right -->
    <section class="about-section bg-alt">
        <div class="container">
            <div class="two-column text-left">
                <div class="column text-col">
                    <h2>The Stone Soup Experience</h2>
                    <p><strong>Warm welcomes and open doors.</strong> Whether your child is enrolled in our playgroup or early learning programs, you can expect to see a friendly teacher&rsquo;s face at drop off and pick up every day, without fail. Our staff members are fully engaged and strive to create a dialogue of open, ongoing communication through daily chats, orientations and events, regular texts, phone calls, and emails.</p>
                    <p><strong>Opportunities to engage and fun events.</strong> As a Stone Soup family, you will have the opportunity to engage with your community throughout the year with a variety of events. We host parent orientations, family fun days, and cultural celebrations that bring our diverse community together.</p>
                    <p><strong>Building strong communities.</strong> Sharing our gifts and talents to build a better community is at the core of our mission. We develop successful partnerships with local schools, organizations, and community leaders to deliver high quality education and support services.</p>
                </div>
                <div class="column image-col">
                    <img src="images/learn hmong program/HJR_0807.JPG" alt="Children learning together">
                </div>
            </div>
        </div>
    </section>

    <!-- Core Values -->
    <section class="about-section">
        <div class="container">
            <h2 style="text-align: center; color: var(--primary); margin-bottom: 2rem;">Our Core Values</h2>
            <div class="values-grid">
                <div class="value-card">
                    <div class="value-icon">&#x1F 🤝</div>
                    <h3>Community</h3>
                    <p>We believe in the power of coming together to support one another.</p>
                </div>
                <div class="value-card">
                    <div class="value-icon">🌱</div>
                    <h3>Growth</h3>
                    <p>We nurture every child&rsquo;s potential for learning and development.</p>
                </div>
                <div class="value-card">
                    <div class="value-icon">❤️</div>
                    <h3>Compassion</h3>
                    <p>We lead with empathy and understanding in all we do.</p>
                </div>
                <div class="value-card">
                    <div class="value-icon">🌍</div>
                    <h3>Diversity</h3>
                    <p>We celebrate and honor all cultures, backgrounds, and traditions.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Programs Summary -->
    <section class="about-section bg-alt">
        <div class="container">
            <h2 style="text-align: center; color: var(--primary); margin-bottom: 2rem;">Our Programs</h2>
            <div class="program-detail" id="preschool">
                <h3>🎓 Preschool Program</h3>
                <p>Our preschool program provides a structured, nurturing environment where children ages 3-5 develop the academic and social skills needed for kindergarten success.</p>
                <div class="program-meta">
                    <div class="program-meta-item"><strong>Age:</strong> 3-5 years</div>
                    <div class="program-meta-item"><strong>Schedule:</strong> Full &amp; Half Day Options</div>
                    <div class="program-meta-item"><strong>Focus:</strong> School Readiness</div>
                </div>
                <p><strong>Program Highlights:</strong></p>
                <ul>
                    <li>Age-appropriate curriculum aligned with California Early Learning Standards</li>
                    <li>Emphasis on literacy, numeracy, and social-emotional development</li>
                    <li>Small group instruction and individualized attention</li>
                    <li>Bilingual support available</li>
                    <li>Healthy meals and snacks provided</li>
                </ul>
                <div style="margin-top: 1.5rem;">
                    <a href="eligibility.html" class="btn btn-outline">View Eligibility &amp; Fees</a>
                </div>
            </div>

            <div class="program-detail" id="playgroup">
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

            <div class="program-detail" id="hmong">
                <h3>🌏 Learn Hmong</h3>
                <p>Our Learn Hmong program celebrates Hmong culture and language, providing families with the opportunity to connect with their heritage while building community bonds.</p>
                <div class="program-meta">
                    <div class="program-meta-item"><strong>Age:</strong> All Ages Welcome</div>
                    <div class="program-meta-item"><strong>Schedule:</strong> Monday to Wednesday</div>
                    <div class="program-meta-item"><strong>Focus:</strong> Cultural Preservation</div>
                </div>
                <p><strong>Program Highlights:</strong></p>
                <ul>
                    <li>Hmong language instruction for all skill levels</li>
                    <li>Traditional arts, crafts, and textile work</li>
                    <li>Cultural history and storytelling</li>
                    <li>Intergenerational learning opportunities</li>
                    <li>Community events and celebrations</li>
                    <li>Open to both Hmong and non-Hmong families</li>
                </ul>
                <div style="margin-top: 1.5rem;">
                    <a href="eligibility.html" class="btn btn-outline">View Eligibility &amp; Fees</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Community Impact / Photo Gallery -->
    <section class="about-section">
        <div class="container">
            <h2 style="text-align: center; color: var(--primary); margin-bottom: 2rem;">Our Community</h2>
            <div class="photo-gallery">
                <div class="gallery-item">
                    <img src="images/cookies with cops event/LEA_3871.JPG" alt="Cookies with Cops community event">
                    <p class="gallery-caption">Cookies with Cops community event</p>
                </div>
                <div class="gallery-item">
                    <img src="images/scholarship award event/Awards(166).JPG" alt="Scholarship awards celebration">
                    <p class="gallery-caption">Scholarship Awards Celebration</p>
                </div>
            </div>
            <p style="text-align: center; color: var(--text-light); margin-top: 2rem;">Stone Soup Fresno proudly serves the Fresno community through education, cultural programs, and community partnership.</p>
        </div>
    </section>

    <!-- CTA -->
    <section class="about-cta">
        <div class="container" style="text-align: center; padding: 3rem 0;">
            <h2 style="margin-bottom: 1rem;">Want to Learn More?</h2>
            <p style="margin-bottom: 1.5rem; opacity: 0.9;">Get in touch to schedule a tour or learn more about our programs.</p>
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                <a href="contact.html" class="btn btn-white">Contact Us</a>
                <a href="eligibility.html" class="btn btn-outline-light">View Eligibility</a>
            </div>
        </div>
    </section>

"""

# Combine
result = top + new_body + bottom

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(result)

print("About page rewritten with Educare-style layout!")
print("\nSections created:")
print("- Hero banner with photo background")
print("- Mission Statement (image left, text right)")
print("- The Stone Soup Experience (text left, image right)")
print("- Core Values")
print("- Programs (Preschool, Playgroup, Learn Hmong)")
print("- Community Photo Gallery")
print("- CTA")
