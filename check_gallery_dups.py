import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/gallery.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the images array
start = html.find('const images = [')
end = html.find('];', start)
if start != -1:
    arr_str = html[start+15:end+1]
    # parse simple strings
    urls = re.findall(r'"([^"]+)"', arr_str)
    seen = set()
    dups = []
    for u in urls:
        if u in seen:
            dups.append(u)
        seen.add(u)
    print("Dups in gallery.html array:", dups)
