import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

old_style = 'style="width: 100%; max-width: 450px; height: auto; border-radius: 12px; margin: 0 auto 2rem auto; display: block; box-shadow: 0 10px 30px rgba(0,0,0,0.1);"'
new_style = 'style="height: 250px; width: auto; max-width: 100%; object-fit: contain; border-radius: 8px; margin: 0 auto 1.5rem auto; display: block;"'

html = html.replace(old_style, new_style)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
