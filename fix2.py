import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. 1500 count load speed
html = html.replace('const duration = 2000;', 'const duration = 800;')

# 2. Mobile nav: remove Vimeo, Youtube, update Instagram, add Back button
mobile_socials_old = r'''      <div class="mobile-menu__socials">
        <a href="#">Instagram</a>
        <a href="#">YouTube</a>
        <a href="#">Vimeo</a>
      </div>'''
mobile_socials_new = r'''      <div class="mobile-menu__socials">
        <a href="https://www.instagram.com/prakaram_productions/" target="_blank">Instagram</a>
      </div>'''
html = html.replace(mobile_socials_old, mobile_socials_new)

# Insert Home in mobile nav
mobile_links_old = r'''<div class="mobile-menu" id="mobileMenu">
      <a href="#portfolio" class="mobile-menu__link" onclick="closeMobileMenu()">Celebrations</a>'''
mobile_links_new = r'''<div class="mobile-menu" id="mobileMenu">
      <a href="#" class="mobile-menu__link" onclick="closeMobileMenu()">Back / Close</a>
      <a href="#header" class="mobile-menu__link" onclick="closeMobileMenu()">Home</a>
      <a href="#portfolio" class="mobile-menu__link" onclick="closeMobileMenu()">Celebrations</a>'''
html = html.replace(mobile_links_old, mobile_links_new)

# Insert Home in desktop nav
desktop_nav_old = r'''<nav class="header__nav" id="desktopNav">
        <a href="#portfolio" class="header__nav-link">Celebrations</a>'''
desktop_nav_new = r'''<nav class="header__nav" id="desktopNav">
        <a href="#header" class="header__nav-link">Home</a>
        <a href="#portfolio" class="header__nav-link">Celebrations</a>'''
html = html.replace(desktop_nav_old, desktop_nav_new)

# 3. Logo size (85px)
html = html.replace('style="height: 55px; width: auto;"', 'style="height: 75px; width: auto;"')

# 4. Remove parallax JS
html = re.sub(r'const hero = document\.querySelector\(\'.hero__bg img\'\);.*?hero\.style\.transform = scale\(1\.05\) translateY\(\$\{scrolled \* 0\.15\}px\);\s*\}', '', html, flags=re.DOTALL)

# 5. View Full Gallery hover state
html = html.replace('class="btn btn--outline" style="border: 1px solid var(--color-black); color: var(--color-black);"', 'class="btn btn--gallery"')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
