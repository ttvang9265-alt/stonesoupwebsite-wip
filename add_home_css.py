# add_home_css.py
import os

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the old .hero CSS and replace it with new home-hero CSS
old_hero = """        .hero {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
            color: white;
            padding: 5rem 0;
            text-align: center;
        }

        .hero h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            font-weight: 700;
        }

        .hero-subtitle {
            font-size: 1.25rem;
            margin-bottom: 2rem;
            opacity: 0.95;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
        }

        .hero-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
        }"""

new_hero_css = """        /* Home Hero - Full-bleed image */
        .home-hero {
            min-height: 60vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: white;
            position: relative;
            padding: 6rem 2rem;
        }

        .home-hero .container {
            position: relative;
            z-index: 2;
            max-width: 800px;
        }

        .home-hero h1 {
            font-size: 3rem;
            font-weight: 400;
            margin-bottom: 1rem;
            line-height: 1.2;
        }

        .home-hero .hero-subtitle {
            font-size: 1.25rem;
            margin-bottom: 2rem;
            opacity: 0.95;
            line-height: 1.6;
        }

        .home-hero .hero-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
        }

        .btn-hero-outline {
            background: transparent;
            color: white;
            border: 2px solid white;
        }

        .btn-hero-outline:hover {
            background: white;
            color: var(--primary);
        }

        /* Home Sections */
        .home-section {
            padding: 5rem 0;
        }

        .home-section.bg-alt {
            background: var(--bg-alt);
        }

        /* Two Column Layout */
        .two-column {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3rem;
            align-items: center;
        }

        .two-column .image-col img {
            width: 100%;
            height: auto;
            border-radius: 8px;
            object-fit: cover;
            display: block;
        }

        .two-column .text-col h2 {
            font-size: 2rem;
            color: var(--text);
            margin-bottom: 1.5rem;
            font-weight: 400;
        }

        .two-column .text-col p {
            color: var(--text-light);
            line-height: 1.8;
            margin-bottom: 1rem;
            font-size: 1.05rem;
        }

        .two-column .text-col p:last-child {
            margin-bottom: 0;
        }

        /* Photo Gallery */
        .photo-gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .gallery-item {
            border-radius: 8px;
            overflow: hidden;
            background: white;
            border: 1px solid var(--border);
        }

        .gallery-item img {
            width: 100%;
            height: 250px;
            object-fit: cover;
            display: block;
        }

        .gallery-caption {
            padding: 0.75rem;
            text-align: center;
            font-size: 0.9rem;
            color: var(--text-light);
            margin: 0;
        }

        /* Home CTA */
        .home-cta {
            background: var(--primary);
            color: white;
        }

        .btn-outline-light {
            background: transparent;
            color: white;
            border: 2px solid white;
        }

        .btn-outline-light:hover {
            background: white;
            color: var(--primary);
        }"""

content = content.replace(old_hero, new_hero_css)

# Also update mobile styles
old_media = """        @media (max-width: 768px) {
            .footer-grid { flex-direction: column; gap: 2rem; }
        }"""

new_media = """        @media (max-width: 768px) {
            .footer-grid { flex-direction: column; gap: 2rem; }

            .home-hero h1 { font-size: 2rem; }
            .home-hero { min-height: 45vh; padding: 4rem 1.5rem; }

            .two-column {
                grid-template-columns: 1fr;
                gap: 2rem;
            }

            .two-column.image-left .image-col { order: 1; }
            .two-column.image-left .text-col { order: 2; }

            .photo-gallery { grid-template-columns: 1fr; }
        }"""

content = content.replace(old_media, new_media)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Home page CSS updated!")
