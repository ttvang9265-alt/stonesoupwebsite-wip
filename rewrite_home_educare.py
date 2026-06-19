# rewrite_home_educare.py
import os

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    original = f.read()

# Find body content boundaries
body_start = original.find('    <!-- Hero: Full-bleed background image -->')
footer_start = original.find('    <!-- Footer -->')

top = original[:body_start]
bottom = original[footer_start:]

new_body = """    <!-- Hero: Full-bleed background image -->
    <section class="home-hero" style="background: linear-gradient(rgba(0,0,0,0.35), rgba(0,0,0,0.35)), url('images/preschool graduation pictures/Happy(343).JPG') center/cover no-repeat;">
        <div class="container">
            <h1>Inspiring Children, Nurturing Families</h1>
            <p class="hero-subtitle">Quality early education that prepares your child for kindergarten.</p>
            <div class="hero-buttons">
                <a href="about.html" class="btn btn-white">Learn More</a>
                <a href="contact.html" class="btn btn-hero-outline">Contact Us</a>
            </div>
        </div>
    </section>

    <!-- Intro Section: Two-column like Educare -->
    <section class="home-section">
        <div class="container">
            <div class="two-column">
                <div class="column text-col">
                    <p style="font-size: 1.35rem; color: var(--text); line-height: 1.5; margin-bottom: 1.5rem;">We provide a loving, supportive, and educational environment.</p>
                    <p style="font-size: 1.35rem; color: var(--text); line-height: 1.5; margin-bottom: 2rem;">A place to learn, play, and grow.</p>
                    <a href="about.html" class="btn btn-primary">The Stone Soup Story</a>
                </div>
                <div class="column text-col">
                    <p style="color: var(--text-light); line-height: 1.8; margin-bottom: 1rem;">Stone Soup Fresno is a community benefit organization serving preschool children and families in Fresno. Our programs help children to learn through play, with the guidance of experienced, friendly teachers and classrooms that feel like home.</p>
                    <p style="color: var(--text-light); line-height: 1.8;">Our goal is to set your child up for educational success &mdash; for the rest of their life.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Core Values -->
    <section class="home-section bg-alt">
        <div class="container">
            <h2 style="text-align: center; color: var(--primary); margin-bottom: 3rem;">Our Core Values</h2>
            <div class="values-row">
                <div class="value-item">
                    <div class="value-icon">&#x1F 🤝</div>
                    <h3>Community</h3>
                    <p>We believe in the power of coming together.</p>
                </div>
                <div class="value-item">
                    <div class="value-icon">&#x1F331;</div>
                    <h3>Growth</h3>
                    <p>We nurture every child&rsquo;s potential.</p>
                </div>
                <div class="value-item">
                    <div class="value-icon">&#x2764;&#xFE0F;</div>
                    <h3>Compassion</h3>
                    <p>We lead with empathy and understanding.</p>
                </div>
                <div class="value-item">
                    <div class="value-icon">&#x1F30F;</div>
                    <h3>Diversity</h3>
                    <p>We celebrate all cultures and traditions.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonial -->
    <section class="home-section">
        <div class="container" style="max-width: 800px; text-align: center;">
            <div style="font-size: 3rem; color: var(--primary); margin-bottom: 1rem;">&#x201C;</div>
            <p style="font-size: 1.25rem; color: var(--text); line-height: 1.8; margin-bottom: 1.5rem; font-style: italic;">Stone Soup Fresno has been an incredible resource for our family. The preschool program prepared our child so well for kindergarten, and the community support has been amazing. The teachers truly care about every child.</p>
            <p style="color: var(--text-light); font-weight: 600;">&mdash; Google Review</p>
        </div>
    </section>

    <!-- Contact Info -->
    <section class="home-section bg-alt">
        <div class="container">
            <h2 style="text-align: center; color: var(--primary); margin-bottom: 2rem;">Get In Touch</h2>
            <div class="contact-row">
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
            </div>
            <div style="text-align: center; margin-top: 2rem;">
                <a href="contact.html" class="btn btn-primary">Contact Us</a>
            </div>
        </div>
    </section>

"""

result = top + new_body + bottom

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(result)

print("Home page rewritten with cleaner Educare-style layout!")
