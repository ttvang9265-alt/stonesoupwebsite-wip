# fix_image_scaling.py - Update all pages with responsive image handling
import os, glob

dir_path = r"C:\Users\Thai Vang\.openclaw\workspace\stonesoup-redesign"

image_css_rules = """
        /* Fluid image scaling */
        img {
            max-width: 100%;
            height: auto;
        }
        .column.image-col img,
        .hero-bg img,
        section img {
            width: 100%;
            height: auto;
            object-fit: cover;
            display: block;
        }
        @media (max-width: 768px) {
            .home-hero {
                min-height: 40vh;
                padding: 4rem 1rem;
            }
        }
"""

for filepath in glob.glob(os.path.join(dir_path, "*.html")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the closing </style> tag
    if '</style>' in content:
        # Insert before </style>
        content = content.replace('</style>', image_css_rules + '\n    </style>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {os.path.basename(filepath)}")
    else:
        print(f"No style tag found in: {os.path.basename(filepath)}")

print("\nDone! Added responsive image scaling rules to all pages.")
