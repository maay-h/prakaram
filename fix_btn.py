import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

if "Read More" not in html:
    html = re.sub(
        r'(passion and excellence\.\s*</p>)',
        r'\1\n        <div style="margin-top: 2rem;"><a href="#about" class="btn btn--outline" style="border-color: var(--color-white); color: var(--color-white);">Read More</a></div>',
        html
    )

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
