import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# find images in portfolio section
start = html.find('id="portfolio"')
end = html.find('</section>', start)
portfolio_html = html[start:end]

images = re.findall(r'<img src="(images/[^"]+)"', portfolio_html)
print("Images in portfolio:", images)

seen = set()
dups = []
for img in images:
    if img in seen:
        dups.append(img)
    else:
        seen.add(img)

print("Duplicates in index.html portfolio:", dups)
