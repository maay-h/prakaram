import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/gallery.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

scroll_js = r'''
    // ---- Header scroll effect ----
    const header = document.getElementById('header');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
      const scrollY = window.scrollY;
      if (scrollY > 80) {
        header.classList.add('header--scrolled');
      } else {
        header.classList.remove('header--scrolled');
      }
      lastScroll = scrollY;
    });
'''

html = html.replace('const lightbox = document.getElementById(\'lightbox\');', scroll_js + '\n    const lightbox = document.getElementById(\'lightbox\');')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
