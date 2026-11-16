import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

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

if "Card 4: Artist" not in html:
    html = re.sub(
        r'(data-modal="culinary">[^<]+</button>\s*</div>\s*</div>)',
        r'\1\n\n' + card4,
        html
    )

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
