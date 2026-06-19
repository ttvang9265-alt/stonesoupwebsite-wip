# rewrite_home.py
import os

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    original = f.read()

# Find the body content boundaries
body_start = original.find('    <!-- Hero -->')
footer_start = original.find('    <!-- Footer -->')

top = original[:body_start]
bottom = original[footer_start:]

new_body = """    <!-- Hero: Full-bleed background image -->
    <section class="home-hero" style="background: linear-gradient(rgba(0,0,0,0.35), rgba(0,0,0,0.35)), url('images/preschool graduation pictures/Happy(343).JPG') center/cover no-repeat;">
        <div class="container">
            <h1>Inspiring Children, Nurturing Families</h1>
            <p class="hero-subtitle">To inspire children and nurture families to realize their full potential in America.</p>
            <div class="hero-buttons">
                <a href="about.html#programs" class="btn btn-white">Our Programs</a>
                <a href="contact.html" class="btn btn-hero-outline">Contact Us</a>
                <a href="#" class="btn btn-hero-outline">Donate</a>
            </div>
        </div>
    </section>

    <!-- Mission Statement: Image left, Text right -->
    <section class="home-section">
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

    <!-- The Stone Soup Experience: Text left, Image right -->
    <section class="home-section bg-alt">
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

    <!-- Programs Preview -->
    <section class="home-section">
        <div class="container">
            <h2 style="text-align: center; color: var(--primary); margin-bottom: 3rem;">Our Programs</h2>
            <div class="program-grid">
                <div class="program-card">
                    <div class="program-icon">&#x1F393;</div>
                    <h3>Preschool</h3>
                    <p>Quality early education preparing your child for kindergarten success. Ages 3-5 welcome.</p>
                    <a href="about.html#preschool" class="program-link">Learn More &rarr;</a>
                </div>
                <div class="program-card">
                    <div class="program-icon">&#x1F9F8;</div>
                    <h3>Playgroup</h3>
                    <p>Interactive play-based learning experiences that foster social and cognitive development. Ages 0-5.</p>
                    <a href="about.html#playgroup" class="program-link">Learn More &rarr;</a>
                </div>
                <div class="program-card">
                    <div class="program-icon">&#x1F30F;</div>
                    <h3>Learn Hmong</h3>
                    <p>Cultural and language programs celebrating Hmong heritage and building community connections.</p>
                    <a href="about.html#hmong" class="program-link">Learn More &rarr;</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Community Photo Gallery -->
    <section class="home-section bg-alt">
        <div class="container">
            <h2 style="text-align: center; color: var(--primary); margin-bottom: 3rem;">Our Community</h2>
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
        </div>
    </section>

    <!-- Contact CTA -->
    <section class="home-cta">
        <div class="container" style="text-align: center; padding: 4rem 0;">
            <h2 style="margin-bottom: 1rem;">Contact Us</h2>
            <p style="margin-bottom: 1.5rem; opacity: 0.95;">Feel free to reach out regarding eligibility, enrollment, or any questions you have.</p>
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                <a href="contact.html" class="btn btn-white">Contact Us</a>
                <a href="eligibility.html" class="btn btn-outline-light">View Eligibility</a>
            </div>
        </div>
    </section>

"""

result = top + new_body + bottom

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(result)

print("Home page redesigned with Educare-style layout!")
