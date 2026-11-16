import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/gallery.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove inline styles from header
html = html.replace('<header class="header" id="header" style="background: var(--color-white); border-bottom: 1px solid var(--color-gray-200);">', '<header class="header" id="header">')

# 2. Remove inline styles from nav links
html = html.replace('style="color: var(--color-black);"', '')

# 3. Remove inline styles from hamburger spans
html = html.replace('style="background: var(--color-black);"', '')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
