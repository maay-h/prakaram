import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Logo
html = re.sub(
    r'<a href="#" class="header__logo">\s*<span>Prakaram</span>\s*</a>',
    r'<a href="#" class="header__logo"><img src="images/logo1.jpeg" alt="Prakaram" style="height: 35px; width: auto;"></a>',
    html
)

# 2. Hero Title
html = re.sub(
    r'<h1 class="hero__title">Prakaram</h1>',
    r'<h1 class="hero__title" style="font-size: clamp(2.5rem, 5vw, 4.5rem); text-align: center;">Anirveda Prakaram<br>Productions Pvt.Ltd.</h1>',
    html
)

# 3. What We Do Background & Read More
html = re.sub(
    r'src="images/main/JYO03928\.JPG" alt="Event Decor Background"',
    r'src="images/whatwedobg.jpg" alt="Event Decor Background"',
    html
)

read_more_html = r'''
        <p class="intro__text">
          At Prakaram Productions, we don't just plan events &mdash; we create timeless memories that reflect your 
story, your style, and your dreams.
        </p>
        <div style="margin-top: 2rem;"><a href="#about" class="btn btn--outline" style="border-color: var(--color-white); color: var(--color-white);">Read More</a></div>
'''
html = re.sub(
    r'<p class="intro__text">\s*Our values center on passion and excellence\.\s*</p>',
    r'<p class="intro__text">\n          Our values center on passion and excellence.\n        </p>\n        <div style="margin-top: 2rem;"><a href="#about" class="btn btn--outline" style="border-color: var(--color-white); color: var(--color-white);">Read More</a></div>',
    html
)

# 4. Add second video
video_html = r'''
    <section class="video-highlight" style="display: flex; flex-direction: column; gap: 0;">
      <video src="images/IMG_1694.MP4" autoplay muted loop playsinline class="video-highlight__media"></video>
      <video src="images/AQN7TZqhNpx69yz52xViYJ7Mzxot6r2FvCXIgZaiPGtNBgLPVE2LzoBDfZU5xBkRCQQ4ljYCiEY9qDNP73P8mKJGtH_uALgX_E98REI.mp4" autoplay muted loop playsinline class="video-highlight__media"></video>
    </section>
'''
html = re.sub(
    r'<section class="video-highlight">\s*<video src="images/IMG_1694\.MP4"[^>]+></video>\s*</section>',
    video_html,
    html
)

# 5. Remove SRPR_12
html = html.replace('images/compressed/SRPR_12.jpg', 'images/compressed/SRPR_1.jpg')

# 6. Replace Grand Wedding Reception Image
html = html.replace('images/compressed/SRPR_10.jpg', 'images/grandweddingreception.png')

# 7. Replace Floral Image
html = html.replace('images/compressed/SRPR_7.jpg', 'images/florl&ambience.JPG')

# 8. Add counter ID
html = re.sub(
    r'<p class="about__stat-number">1,500\+</p>',
    r'<p class="about__stat-number" id="designsDelivered">1,500+</p>',
    html
)

# 9. Testimonials replacement
testimonials_html = r'''<div class="testimonial-slider">
            <div class="testimonial active" data-index="0">
              <img src="images/Bharath&Yashika.jpeg" alt="Bharath & Yashika" style="width: 80px; height: 80px; object-fit: cover; border-radius: 50%; margin: 0 auto 1.5rem auto; display: block;">
              <div class="testimonial__quote">
                Prakaram Productions turned our wedding into a dream come true. Every detail was thoughtfully planned and beautifully executed. From dAccor to coordination, everything felt seamless and elegant. We were stress-free and truly enjoyed every moment. Our guests still praise the magical ambiance they created.
              </div>
              <p class="testimonial__author">Bharath & Yashika</p>
            </div>
            
            <div class="testimonial" data-index="1">
              <img src="images/Ankit&Bhumika.jpeg" alt="Ankit & Bhumika" style="width: 80px; height: 80px; object-fit: cover; border-radius: 50%; margin: 0 auto 1.5rem auto; display: block;">
              <div class="testimonial__quote">
                From our first consultation to the final farewell, Prakaram Productions exceeded every expectation. They beautifully captured our vision and brought it to life with flawless execution and stunning aesthetics. Every celebration felt unique and perfectly organized.
              </div>
              <p class="testimonial__author">Ankit & Bhumika</p>
            </div>
            
            <div class="testimonial" data-index="2">
              <img src="images/SAgar&Ananya.jpeg" alt="Sagar & Ananya" style="width: 80px; height: 80px; object-fit: cover; border-radius: 50%; margin: 0 auto 1.5rem auto; display: block;">
              <div class="testimonial__quote">
                Our wedding felt like a beautiful dream, all thanks to Prakaram Productions. Their team blended elegance with flawless coordination, ensuring every event flowed perfectly. The dAccor was stunning, and the entire experience was smooth and stress-free.
              </div>
              <p class="testimonial__author">Sagar & Ananya</p>
            </div>

            <div class="testimonial" data-index="3">
              <img src="images/Divya&Jathin.jpeg" alt="Divya & Jathin" style="width: 80px; height: 80px; object-fit: cover; border-radius: 50%; margin: 0 auto 1.5rem auto; display: block;">
              <div class="testimonial__quote">
                Prakaram Productions made our wedding journey truly unforgettable. From conceptualizing the theme to executing every detail flawlessly, their team ensured everything reflected our personality and style. It was beyond perfect.
              </div>
              <p class="testimonial__author">Divya & Jathin</p>
            </div>

            <div class="testimonial" data-index="4">
              <img src="images/Aishwarya&Seshan.jpeg" alt="Aishwarya & Seshan" style="width: 80px; height: 80px; object-fit: cover; border-radius: 50%; margin: 0 auto 1.5rem auto; display: block;">
              <div class="testimonial__quote">
                Working with Prakaram Productions for our wedding was a dream come true. They have a remarkable eye for detail and managed to bring a sense of royal elegance to every corner of the venue. If you want a team that understands how to blend tradition with a high-end aesthetic, this is it!
              </div>
              <p class="testimonial__author">Aishwarya & Seshan</p>
            </div>

            <div class="testimonial" data-index="5">
              <img src="images/Prapthi&Pooernesh.jpeg" alt="Prapthi & Poornesh" style="width: 80px; height: 80px; object-fit: cover; border-radius: 50%; margin: 0 auto 1.5rem auto; display: block;">
              <div class="testimonial__quote">
                Our reception decor by Prakaram Production was a dream come true! They exceeded our expectations, executing every detail beautifully. Their coordination was amazing, making the process smooth and stress-free. The red and white theme they suggested gave a royal, elegant vibe to the entire setup. They gave 100% effort to bring our vision to life with perfect dedication. Thank you, Prakaram Production!
              </div>
              <p class="testimonial__author">Prapthi Poornesh</p>
            </div>
          </div>'''
html = re.sub(r'<div class="testimonial-slider">.*?</div>\s+<div class="testimonial-nav-container"', testimonials_html + '\n        <div class="testimonial-nav-container"', html, flags=re.DOTALL)

# 10. Service Card
service_html = r'''          <!-- Card 4: Artist & Entertainment -->
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
        </div>'''
html = re.sub(r'</div>\s*</div>\s*<div class="services__footer reveal">', service_html + '\n      <div class="services__footer reveal">', html)

# 11, 12, 13. Map, Location, FB Link
# Maps Embed
html = re.sub(
    r'src="https://www\.google\.com/maps[^"]+"',
    r'src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3887.8931980373854!2d77.60155207604312!3d12.978687787337346!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae17f45c0e2913%3A0x88da86538d3e49a9!2sPrakaram%20Productions%20Pvt%20Ltd!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin"',
    html
)
# FB Link
html = html.replace('https://www.facebook.com/prakaram.productions', 'https://www.facebook.com/people/Prakaram-Productions/61587802303752/')
# Location text
old_loc = 'HiProfiles Business Centre, 1/A, Mahatma Gandhi Rd, Shanthala Nagar,<br>Church St, Bengaluru, Karnataka 560001'
new_loc = 'Prakaram Productions Pvt Ltd<br>HiProfiles Business Centre, 1/A, Mahatma Gandhi Rd, Shanthala Nagar, Church St, Bengaluru, Karnataka 560001'
html = html.replace(old_loc, new_loc)
html = html.replace('HiProfiles Business Centre, 1/A, Mahatma Gandhi Rd, Shanthala Nagar, Church St, Bengaluru, Karnataka 560001', 'Prakaram Productions Pvt Ltd, HiProfiles Business Centre, 1/A, Mahatma Gandhi Rd, Shanthala Nagar, Church St, Bengaluru, Karnataka 560001')

# 14. Counter JS
counter_js = r'''
      // ---- Counter Animation ----
      const counterEl = document.getElementById('designsDelivered');
      if (counterEl) {
        let counted = false;
        const observer = new IntersectionObserver((entries) => {
          if(entries[0].isIntersecting && !counted) {
            counted = true;
            let startTimestamp = null;
            const duration = 2000;
            const step = (timestamp) => {
              if (!startTimestamp) startTimestamp = timestamp;
              const progress = Math.min((timestamp - startTimestamp) / duration, 1);
              counterEl.innerText = Math.floor(progress * 1500) + "+";
              if (progress < 1) {
                window.requestAnimationFrame(step);
              } else {
                counterEl.innerText = "1,500+";
              }
            };
            window.requestAnimationFrame(step);
          }
        }, { threshold: 0.5 });
        observer.observe(counterEl);
      }

      revealElements.forEach'''
html = html.replace('revealElements.forEach', counter_js)


with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
