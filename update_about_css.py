import os

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\about.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove old .about-hero CSS block
old_about_hero = """        .about-hero {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
            color: white;
            padding: 4rem 0;
            text-align: center;
        }

        .about-hero h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        .about-hero p {
            font-size: 1.2rem;
            opacity: 0.9;
            max-width: 700px;
            margin: 0 auto;
        }"""

new_css = r"""        /* About Hero - Full-bleed image with overlay */
        .about-hero {
            min-height: 50vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: white;
            position: relative;
            padding: 6rem 2rem;
        }

        .about-hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.35);
            z-index: 1;
        }

        .about-hero .container {
            position: relative;
            z-index: 2;
            max-width: 800px;
        }

        .about-hero h1 {
            font-size: 3rem;
            font-weight: 400;
            margin-bottom: 1rem;
            line-height: 1.2;
        }

        .about-hero p {
            font-size: 1.25rem;
            opacity: 0.95;
            line-height: 1.6;
        }

        /* About Section styles */
        .about-section {
            padding: 4rem 0;
        }

        .about-section.bg-alt {
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
            margin-bottom: 2rem;
        }

        .gallery-item {
            border-radius: 8px;
            overflow: hidden;
            background: var(--bg-alt);
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

        /* CTA Section on about page */
        .about-cta {
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
        }

        .btn-white {
            background: white;
            color: var(--primary);
            border: 2px solid white;
        }

        .btn-white:hover {
            background: transparent;
            color: white;
        }"""

content = content.replace(old_about_hero, new_css)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS updated for new About layout!")
