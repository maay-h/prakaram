import re

css_file = 'd:/Madhurya/Projects/Client Projects/prakaram/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Hero background position
css = re.sub(
    r'(\.hero__bg img\s*\{[^}]*?object-fit:\s*cover;)',
    r'\1\n  object-position: top center;',
    css
)

# 2. Marquee font style
css = re.sub(
    r'\.marquee__item\s*\{[^}]*?\}',
    r'.marquee__item {\n  font-family: var(--font-sans);\n  font-size: var(--fs-h2);\n  font-weight: 300;\n  text-transform: uppercase;\n  letter-spacing: 0.15em;\n  white-space: nowrap;\n  padding: 0 3rem;\n  color: var(--color-gray-300);\n}',
    css
)

# 3. Services hover grid
css = re.sub(
    r'(\.services__hover-grid\s*\{[^}]*?grid-template-columns:\s*repeat\()3(, 1fr\);)',
    r'\g<1>4\g<2>',
    css
)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)
