import re

index_file = 'd:/Madhurya/Projects/Client Projects/prakaram/index.html'
gallery_file = 'd:/Madhurya/Projects/Client Projects/prakaram/gallery.html'

with open(index_file, 'r', encoding='utf-8') as f:
    index_html = f.read()

with open(gallery_file, 'r', encoding='utf-8') as f:
    gallery_html = f.read()

# Extract footer from index
start_tag = '<footer class="footer bg-watermark">'
end_tag = '</footer>'
start_idx = index_html.find(start_tag)
end_idx = index_html.find(end_tag, start_idx) + len(end_tag)

footer_html = index_html[start_idx:end_idx]

# Replace footer in gallery
g_start_idx = gallery_html.find(start_tag)
g_end_idx = gallery_html.find(end_tag, g_start_idx) + len(end_tag)

new_gallery_html = gallery_html[:g_start_idx] + footer_html + gallery_html[g_end_idx:]

with open(gallery_file, 'w', encoding='utf-8') as f:
    f.write(new_gallery_html)
