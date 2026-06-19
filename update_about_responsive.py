import os

filepath = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign\about.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the mobile media query and add responsive styles for two-column
old_media = """        @media (max-width: 768px) {
            .nav-links li:not(:last-child):not(:nth-last-child(2)) {
                display: none;
            }

            .page-title, .about-hero h1 {
                font-size: 1.75rem;
            }

            .program-meta {
                flex-direction: column;
                gap: 0.5rem;
            }
        }"""

new_media = """        @media (max-width: 768px) {
            .nav-links li:not(:last-child):not(:nth-last-child(2)) {
                display: none;
            }

            .page-title, .about-hero h1 {
                font-size: 1.75rem;
            }

            .program-meta {
                flex-direction: column;
                gap: 0.5rem;
            }

            .two-column {
                grid-template-columns: 1fr;
                gap: 2rem;
            }

            .two-column.image-left .image-col { order: 1; }
            .two-column.image-left .text-col { order: 2; }

            .about-hero {
                min-height: 40vh;
                padding: 4rem 1.5rem;
            }

            .about-hero h1 {
                font-size: 2rem;
            }

            .photo-gallery {
                grid-template-columns: 1fr;
            }
        }"""

content = content.replace(old_media, new_media)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added responsive styles for mobile!")
