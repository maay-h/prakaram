import re

css_file = 'd:/Madhurya/Projects/Client Projects/prakaram/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# The CSS block added was:
css_to_remove = r'''
\.bg-watermark \{
  position: relative;
  z-index: 1;
\}

\.bg-watermark::before \{
  content: "";
  position: absolute;
  top: 0; 
  left: 0;
  width: 100%; 
  height: 100%;
  background-image: url\('images/logo1\.png'\);
  background-position: center;
  background-repeat: no-repeat;
  background-size: 50%;
  opacity: 0\.15;
  z-index: -1;
  pointer-events: none;
\}

/\* Adjust footer background so watermark is visible if it's a black footer \*/
\.footer\.bg-watermark \{
  background-color: transparent;
\}
\.footer-wrap \{
  background-color: var\(--color-black\);
  position: relative;
  z-index: 1;
\}
\.footer-wrap::before \{
  content: "";
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background-image: url\('images/logo1\.png'\);
  background-position: center;
  background-repeat: no-repeat;
  background-size: 50%;
  opacity: 0\.15;
  z-index: -1;
  pointer-events: none;
\}
'''

# Use regex to strip it
css = re.sub(css_to_remove.replace('\n', r'\s*'), '', css, flags=re.DOTALL)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)
