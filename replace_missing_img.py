import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/gallery.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace missing image in HTML grid and in JS array
html = html.replace('images/compressed/WhatsApp Image 2026-08-25 at 5.46.07 PM.jpg', 'images/grandweddingreception.jpg')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
