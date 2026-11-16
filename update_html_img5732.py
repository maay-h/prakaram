import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('src="images/florl&ambience.jpg"', 'src="images/compressed/IMG_5732.jpg"')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
