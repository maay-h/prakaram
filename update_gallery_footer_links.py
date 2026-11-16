import re

gallery_file = 'd:/Madhurya/Projects/Client Projects/prakaram/gallery.html'

with open(gallery_file, 'r', encoding='utf-8') as f:
    gallery_html = f.read()

# Update the hash links in the footer of gallery.html
start_tag = '<footer class="footer bg-watermark">'
end_tag = '</footer>'
g_start_idx = gallery_html.find(start_tag)
g_end_idx = gallery_html.find(end_tag, g_start_idx) + len(end_tag)

footer_html = gallery_html[g_start_idx:g_end_idx]

footer_html = footer_html.replace('href="#portfolio"', 'href="index.html#portfolio"')
footer_html = footer_html.replace('href="#about"', 'href="index.html#about"')
footer_html = footer_html.replace('href="#services"', 'href="index.html#services"')
footer_html = footer_html.replace('href="#contact"', 'href="index.html#contact"')

new_gallery_html = gallery_html[:g_start_idx] + footer_html + gallery_html[g_end_idx:]

with open(gallery_file, 'w', encoding='utf-8') as f:
    f.write(new_gallery_html)
