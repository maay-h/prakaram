import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Logo size
html = html.replace('style="height: 35px; width: auto;"', 'style="height: 55px; width: auto;"')

# 2. Kind words images
old_img_style = 'style="width: 80px; height: 80px; object-fit: cover; border-radius: 50%; margin: 0 auto 1.5rem auto; display: block;"'
new_img_style = 'style="width: 100%; max-width: 450px; height: auto; border-radius: 12px; margin: 0 auto 2rem auto; display: block; box-shadow: 0 10px 30px rgba(0,0,0,0.1);"'
html = html.replace(old_img_style, new_img_style)

# 3. Read More button (What We Do)
if "Read More" not in html:
    html = html.replace('elegance. Our values center on passion and excellence.\n        </p>', 'elegance. Our values center on passion and excellence.\n        </p>\n        <div style="margin-top: 2rem;"><a href="#about" class="btn btn--outline" style="border-color: var(--color-white); color: var(--color-white);">Read More</a></div>')
    html = html.replace('elegance. Our values center on passion and excellence.\r\n        </p>', 'elegance. Our values center on passion and excellence.\r\n        </p>\n        <div style="margin-top: 2rem;"><a href="#about" class="btn btn--outline" style="border-color: var(--color-white); color: var(--color-white);">Read More</a></div>')

# 4. Remove WhatsApp Image
html = html.replace('images/compressed/WhatsApp Image 2026-08-25 at 5.46.07 PM.jpg', 'images/main/JYO00274.JPG')
html = html.replace('images/main/WhatsApp Image 2026-08-25 at 5.46.07 PM.jpeg', 'images/main/JYO00274.JPG')

# 5. Phone number +91
html = html.replace('099008 63337', '+91 99008 63337')
# also handle tel:099008... if it exists
html = html.replace('tel:099008', 'tel:+9199008')

# 6. Service Card 4
card4 = r'''        <!-- Card 4: Artist & Entertainment -->
        <div class="svc-card reveal reveal-delay-4">
          <div class="svc-card__bg">
            <img loading="lazy" src="images/main/JYO06325.JPG" alt="Artist & Entertainment Management">
          </div>
          <div class="svc-card__overlay"></div>
          <div class="svc-card__content">
            <p class="svc-card__number">04</p>
            <h3 class="svc-card__title">Artist &amp; Entertainment Management</h3>
            <ul class="svc-card__list">
              <li>Live performers</li>
              <li>DJs</li>
              <li>Musicians</li>
              <li>Curated entertainment experiences</li>
            </ul>
          </div>
        </div>
'''
if "<!-- Card 4" not in html:
    html = html.replace('              <button class="svc-card__cta" data-modal="culinary">Explore →</button>\n            </div>\n          </div>', '              <button class="svc-card__cta" data-modal="culinary">Explore →</button>\n            </div>\n          </div>\n\n' + card4)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
