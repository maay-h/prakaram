import re

css_file = 'd:/Madhurya/Projects/Client Projects/prakaram/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

gallery_btn_css = r'''
.btn--gallery {
  border: 1px solid var(--color-black);
  color: var(--color-black);
  background-color: transparent;
}

.btn--gallery:hover {
  background-color: var(--color-black);
  color: var(--color-white);
}
'''

if ".btn--gallery" not in css:
    css += gallery_btn_css

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)
