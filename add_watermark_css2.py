import os

css_file = 'd:/Madhurya/Projects/Client Projects/prakaram/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

watermark_css = r'''
.bg-watermark {
  position: relative;
  z-index: 1;
}

.bg-watermark::before {
  content: "";
  position: absolute;
  top: 0; 
  left: 0;
  width: 100%; 
  height: 100%;
  background-image: url('images/IMG_5195.PNG');
  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
  opacity: 0.15;
  z-index: -1;
  pointer-events: none;
}
'''
if '.bg-watermark' not in css:
    css += watermark_css

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)
