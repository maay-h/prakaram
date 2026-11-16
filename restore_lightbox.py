import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/gallery.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

lightbox_js = r'''
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightboxImg');

    function openLightbox(index) {
      currentIndex = index;
      updateLightboxImage();
      lightbox.classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function closeLightbox() {
      lightbox.classList.remove('active');
      document.body.style.overflow = '';
    }

    function prevImage() {
      currentIndex = (currentIndex > 0) ? currentIndex - 1 : images.length - 1;
      updateLightboxImage();
    }

    function nextImage() {
      currentIndex = (currentIndex < images.length - 1) ? currentIndex + 1 : 0;
      updateLightboxImage();
    }

    function updateLightboxImage() {
      lightboxImg.src = images[currentIndex];
    }

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (!lightbox.classList.contains('active')) return;
      if (e.key === 'Escape') closeLightbox();
      if (e.key === 'ArrowLeft') prevImage();
      if (e.key === 'ArrowRight') nextImage();
    });

    // Close on click outside image
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox || e.target.classList.contains('lightbox__content')) {
        closeLightbox();
      }
    });

    // ---- Header scroll effect (Always scrolled in gallery) ----
'''

# Replace the target comment with the lightbox JS + the comment itself
html = html.replace('// ---- Header scroll effect (Always scrolled in gallery) ----', lightbox_js)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
