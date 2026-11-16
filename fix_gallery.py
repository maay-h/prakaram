import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/gallery.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('style="height: 35px; width: auto;"', 'style="height: 55px; width: auto;"')
html = html.replace('099008 63337', '+91 99008 63337')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
