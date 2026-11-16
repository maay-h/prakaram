import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

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
      </div>
'''

html = html.replace('        </div>\n      </div>\n\n    </div>\n  </div>\n\n  <!-- ===================== TESTIMONIALS ===================== -->', '        </div>\n      </div>\n\n' + modal_html + '\n    </div>\n  </div>\n\n  <!-- ===================== TESTIMONIALS ===================== -->')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
