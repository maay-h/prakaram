import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace any ? or mangled chars inside that specific link with &times;
html = re.sub(
    r'<a href="#" class="mobile-menu__link" onclick="closeMobileMenu\(\)">[^<]*</a>\s*<a href="#" class="mobile-menu__link" onclick="window\.scrollTo',
    r'<a href="#" class="mobile-menu__link" onclick="closeMobileMenu()" style="font-size: 2.5rem;">&times;</a>\n      <a href="#" class="mobile-menu__link" onclick="window.scrollTo',
    html
)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
