import re

html_files = [
    'd:/Madhurya/Projects/Client Projects/prakaram/index.html',
    'd:/Madhurya/Projects/Client Projects/prakaram/gallery.html'
]

for html_file in html_files:
    if not __import__('os').path.exists(html_file): continue
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove the bg-watermark class
    html = html.replace(' bg-watermark', '')

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
