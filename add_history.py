# add_history.py
import os

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\about.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the end of Stone Soup Experience section
marker = "    <!-- Core Values -->"
idx = content.find(marker)

if idx == -1:
    print("Could not find Core Values marker")
    exit()

# Insert History section before Core Values
history_section = """    <!-- History of Stone Soup Fresno -->
    <section class="about-section">
        <div class="container">
            <h2 style="text-align: center; color: var(--primary); margin-bottom: 2rem;">History of Stone Soup Fresno</h2>
            <div style="max-width: 800px; margin: 0 auto;">
                <p style="color: var(--text-light); line-height: 1.8; margin-bottom: 1.5rem; font-size: 1.05rem;">Stone Soup Fresno was founded on the belief that every child deserves access to quality early education and every family deserves support. Inspired by the beloved folktale where a community comes together to share what they have, creating something wonderful from seemingly nothing, our organization embodies this spirit of collaboration and community support.</p>
                <p style="color: var(--text-light); line-height: 1.8; margin-bottom: 1.5rem; font-size: 1.05rem;">Located in the heart of Fresno, California, Stone Soup Fresno has grown to serve hundreds of families through our preschool, playgroup, and cultural education programs. We believe that when families and communities work together, we can create lasting positive change for children and future generations.</p>
                <p style="color: var(--text-light); line-height: 1.8; margin-bottom: 1.5rem; font-size: 1.05rem;">Over the years, we have developed successful partnerships with local schools, organizations, and community leaders to deliver high quality education and support services. Our programs are designed to nurture growth, celebrate diversity, and build strong community bonds.</p>
                <p><strong>Our Board of Directors:</strong></p>
                <ul style="margin-left: 1.5rem; color: var(--text-light); line-height: 1.8;">
                    <li>[Board Member Name]</li>
                    <li>[Board Member Name]</li>
                    <li>[Board Member Name]</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Photo Gallery -->
    <section class="about-section bg-alt">
        <div class="container">
            <h2 style="text-align: center; color: var(--primary); margin-bottom: 2rem;">Our Community in Action</h2>
            <div class="photo-gallery-grid">
                <div class="gallery-photo"><img src="images/cookies with cops event/LEA_3871.JPG" alt="Community event"></div>
                <div class="gallery-photo"><img src="images/cookies with cops event/LEA_3968.JPG" alt="Community event"></div>
                <div class="gallery-photo"><img src="images/cookies with cops event/LEA_3992.JPG" alt="Community event"></div>
                <div class="gallery-photo"><img src="images/learn hmong program/HJR_0667.JPG" alt="Learn Hmong program"></div>
                <div class="gallery-photo"><img src="images/learn hmong program/HJR_0691.JPG" alt="Learn Hmong program"></div>
                <div class="gallery-photo"><img src="images/learn hmong program/HJR_0763.JPG" alt="Learn Hmong program"></div>
                <div class="gallery-photo"><img src="images/preschool graduation pictures/Happy(105).JPG" alt="Preschool graduation"></div>
                <div class="gallery-photo"><img src="images/preschool graduation pictures/Happy(131).JPG" alt="Preschool graduation"></div>
                <div class="gallery-photo"><img src="images/preschool graduation pictures/Happy(136).JPG" alt="Preschool graduation"></div>
            </div>
        </div>
    </section>

"""

content = content[:idx] + history_section + content[idx:]

# Also add CSS for the photo gallery grid
old_media = """        @media (max-width: 768px) {
            .footer-grid { flex-direction: column; gap: 2rem; }
        }"""

new_media = """        /* Photo Gallery Grid */
        .photo-gallery-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1rem;
        }

        .gallery-photo {
            border-radius: 8px;
            overflow: hidden;
            aspect-ratio: 4/3;
        }

        .gallery-photo img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.3s;
        }

        .gallery-photo:hover img {
            transform: scale(1.05);
        }

        @media (max-width: 768px) {
            .footer-grid { flex-direction: column; gap: 2rem; }
            .photo-gallery-grid { grid-template-columns: repeat(2, 1fr); }
        }"""

content = content.replace(old_media, new_media)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added History section and Photo Gallery to About page!")
