import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add 2 reviews
reviews_html = r'''
            <div class="testimonial" data-index="6">
              <img src="images/DivyaTiwari&VishalJain.jpeg" alt="Divya Tiwari & Vishal Jain" style="height: 250px; width: auto; max-width: 100%; object-fit: contain; border-radius: 8px; margin: 0 auto 1.5rem auto; display: block;">
              <div class="testimonial__quote">
                Prakaram Production did an amazing job managing our event! Everything was planned and executed so professionally, from the arrangements to the coordination. The team was creative, responsive, and made sure everything went smoothly. Highly recommended for anyone looking for a reliable and professional event management team in India!
              </div>
              <p class="testimonial__author">Divya Tiwari & Vishal Jain</p>
            </div>
            
            <div class="testimonial" data-index="7">
              <img src="images/Akshath&Vageesha.jpeg" alt="Akshat And Vageehsa" style="height: 250px; width: auto; max-width: 100%; object-fit: contain; border-radius: 8px; margin: 0 auto 1.5rem auto; display: block;">
              <div class="testimonial__quote">
                Had a wonderful experience with Prakaram Production! Their attention to detail, creativity, and professionalism really stood out. The entire event was handled seamlessly, and the team made the whole experience stress-free and enjoyable. Truly a fantastic event management company, would definitely choose them again!
              </div>
              <p class="testimonial__author">Akshat And Vageehsa</p>
            </div>
'''
# Insert before </div></div> <!-- End of testimonial slider -->
html = re.sub(
    r'(<p class="testimonial__author">Prapthi Poornesh</p>\s*</div>)',
    r'\1\n' + reviews_html,
    html
)

# 2. Add dots
dots_html = r'''            <button class="testimonial__dot" data-slide="6" aria-label="Testimonial 7"></button>
            <button class="testimonial__dot" data-slide="7" aria-label="Testimonial 8"></button>'''
html = html.replace('<button class="testimonial__dot" data-slide="5" aria-label="Testimonial 6"></button>', '<button class="testimonial__dot" data-slide="5" aria-label="Testimonial 6"></button>\n' + dots_html)

# 3. Logo Expand (index)
html = html.replace('style="height: 75px; width: auto;"', 'style="height: 90px; width: auto; transform: scaleX(1.15); transform-origin: left;"')

# 4. Explore Button & Modal for Artist & Entertainment
explore_btn = r'''              <button class="svc-card__cta" data-modal="entertainment">Explore ?</button>'''
html = re.sub(r'(<li>Curated entertainment experiences</li>\s*</ul>)\s*</div>\s*</div>', r'\1\n' + explore_btn + '\n            </div>\n          </div>', html)

modal_html = r'''      <!-- Artist & Entertainment -->
      <div class="svc-modal__content" id="modal-entertainment">
        <p class="svc-modal__label">04</p>
        <h2 class="svc-modal__title">Artist &amp; Entertainment Management</h2>
        <div class="svc-modal__grid">
          <div class="svc-modal__item">
            <h4>Live Performers</h4>
            <p>Captivating live bands, singers, and instrumentalists to set the perfect mood for your celebration.</p>
          </div>
          <div class="svc-modal__item">
            <h4>DJs &amp; Emcees</h4>
            <p>Professional DJs to keep the dance floor alive and charismatic emcees to host your event seamlessly.</p>
          </div>
          <div class="svc-modal__item">
            <h4>Curated Experiences</h4>
            <p>Specialty acts, dancers, magicians, and customized entertainment tailored exclusively for your guests.</p>
          </div>
        </div>
      </div>'''

html = re.sub(r'(<div class="svc-modal__content" id="modal-culinary">.*?</select>\s*</div>\s*</div>\s*</div>)', r'\1\n\n' + modal_html, html, flags=re.DOTALL)


with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
