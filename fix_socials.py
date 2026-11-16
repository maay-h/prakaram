import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace mobile socials
html = re.sub(
    r'<div class="mobile-menu__socials">.*?</div>',
    r'<div class="mobile-menu__socials">\n        <a href="https://www.instagram.com/prakaram_productions/" target="_blank">Instagram</a>\n      </div>',
    html,
    flags=re.DOTALL
)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
