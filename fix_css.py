import re

css_file = 'd:/Madhurya/Projects/Client Projects/prakaram/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('  object-position: top center;\n', '')

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)
