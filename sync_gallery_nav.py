import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/gallery.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update header class
html = html.replace('<header class="header" id="header">', '<header class="header header--scrolled" id="header">')

# 2. Insert mobile menu
mobile_menu = r'''
  <!-- ===================== MOBILE MENU ===================== -->
  <div class="mobile-menu" id="mobileMenu">
      <a href="#" class="mobile-menu__link" onclick="closeMobileMenu()" style="font-size: 2.5rem;">&times;</a>
      <a href="index.html" class="mobile-menu__link" onclick="closeMobileMenu()">Home</a>
      <a href="index.html#portfolio" class="mobile-menu__link" onclick="closeMobileMenu()">Celebrations</a>
    <a href="index.html#about" class="mobile-menu__link" onclick="closeMobileMenu()">About</a>
    <a href="index.html#services" class="mobile-menu__link" onclick="closeMobileMenu()">Services</a>
    <a href="gallery.html" class="mobile-menu__link" onclick="closeMobileMenu()">Gallery</a>
    <a href="index.html#contact" class="mobile-menu__link" onclick="closeMobileMenu()">Contact</a>
    <div class="mobile-menu__socials">
        <a href="https://www.instagram.com/prakaram_productions/" target="_blank">Instagram</a>
      </div>
  </div>
'''
html = html.replace('</header>', '</header>\n' + mobile_menu)

# 3. Replace JS
js_replace_start = html.find('    // ---- Header scroll effect ----')
if js_replace_start != -1:
    js_replace_end = html.find('</script>', js_replace_start)
    
    new_js = r'''
    // ---- Header scroll effect (Always scrolled in gallery) ----
    // Removed to keep header permanently visible

    // Mobile menu toggle
    const hamburger = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobileMenu');

    if (hamburger && mobileMenu) {
      hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        mobileMenu.classList.toggle('active');
        document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
      });
    }

    function closeMobileMenu() {
      hamburger.classList.remove('active');
      mobileMenu.classList.remove('active');
      document.body.style.overflow = '';
    }
  '''
    html = html[:js_replace_start] + new_js + html[js_replace_end:]

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
