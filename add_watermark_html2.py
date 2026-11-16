import re

html_files = [
    'd:/Madhurya/Projects/Client Projects/prakaram/index.html',
    'd:/Madhurya/Projects/Client Projects/prakaram/gallery.html'
]

for html_file in html_files:
    if not __import__('os').path.exists(html_file): continue
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Apply to contact section
    html = html.replace('<section class="contact section" id="contact">', '<section class="contact section bg-watermark" id="contact">')
    # Apply to testimonials
    html = html.replace('<section class="testimonials section" id="testimonials">', '<section class="testimonials section bg-watermark" id="testimonials">')
    # Apply to about
    html = html.replace('<section class="about section" id="about">', '<section class="about section bg-watermark" id="about">')
    # Apply to footer
    html = html.replace('<footer class="footer">', '<footer class="footer bg-watermark">')

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
