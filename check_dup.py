import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/gallery.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

images = re.findall(r'<img src="(images/[^"]+)"', html)
# find duplicates
seen = set()
dups = []
for img in images:
    if img in seen:
        dups.append(img)
    else:
        seen.add(img)

print("Duplicates in HTML:", dups)
