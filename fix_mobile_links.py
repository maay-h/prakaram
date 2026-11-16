import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Insert Home and Back in mobile nav
html = re.sub(
    r'(<div class="mobile-menu" id="mobileMenu">)\s*<a href="#portfolio"',
    r'\1\n      <a href="#" class="mobile-menu__link" onclick="closeMobileMenu()">Back / Close</a>\n      <a href="#header" class="mobile-menu__link" onclick="closeMobileMenu()">Home</a>\n      <a href="#portfolio"',
    html
)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
