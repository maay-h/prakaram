import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/gallery.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<nav class="header__nav" id="desktopNav">', '<nav class="header__nav" id="desktopNav">\n        <a href="index.html" class="header__nav-link" style="color: var(--color-black);">Home</a>')

html = html.replace('style="height: 55px; width: auto;"', 'style="height: 90px; width: auto; transform: scaleX(1.15); transform-origin: left;"')
html = html.replace('style="height: 75px; width: auto;"', 'style="height: 90px; width: auto; transform: scaleX(1.15); transform-origin: left;"')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
