# add_home_css2.py
import os

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find mobile media query and add new CSS before it
old_media = """        @media (max-width: 768px) {
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

new_css = """        /* Values Row */
        .values-row {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2rem;
            text-align: center;
        }

        .value-item {
            padding: 1.5rem;
        }

        .value-item .value-icon {
            font-size: 2.5rem;
            margin-bottom: 0.75rem;
        }

        .value-item h3 {
            color: var(--primary);
            margin-bottom: 0.5rem;
            font-size: 1.1rem;
        }

        .value-item p {
            color: var(--text-light);
            font-size: 0.95rem;
            margin: 0;
        }

        /* Contact Row */
        .contact-row {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
            text-align: center;
            margin-bottom: 2rem;
        }

        .contact-item-home h3 {
            color: var(--primary);
            margin-bottom: 0.75rem;
            font-size: 1.1rem;
        }

        .contact-item-home p {
            color: var(--text-light);
            line-height: 1.6;
            margin: 0;
        }

        @media (max-width: 768px) {
            .home-hero h1 { font-size: 2rem; }
            .home-hero { min-height: 45vh; padding: 4rem 1.5rem; }

            .two-column {
                grid-template-columns: 1fr;
                gap: 2rem;
            }

            .two-column.image-left .image-col { order: 1; }
            .two-column.image-left .text-col { order: 2; }

            .photo-gallery { grid-template-columns: 1fr; }

            .values-row { grid-template-columns: repeat(2, 1fr); }
            .contact-row { grid-template-columns: 1fr; }
        }"""

content = content.replace(old_media, new_css)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added CSS for values and contact sections!")
