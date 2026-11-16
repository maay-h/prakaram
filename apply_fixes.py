import re
import sys

# 1. Fix duplicate image in index.html
index_file = 'd:/Madhurya/Projects/Client Projects/prakaram/index.html'
with open(index_file, 'r', encoding='utf-8') as f:
    html = f.read()

# The first occurrence is for "Wedding Ceremony". The second is for "Reception Night".
# Let's replace the src of the one for "Reception Night"
# We can find the block for "Reception Night"
reception_night_pattern = r'(<img loading="lazy" src=")images/compressed/SRPR_1.jpg(" alt="Reception event" class="story-card__image">)'
if re.search(reception_night_pattern, html):
    html = re.sub(reception_night_pattern, r'\1images/compressed/SRPR_10.jpg\2', html)
else:
    print("Could not find Reception Night duplicate")
    sys.exit(1)

with open(index_file, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update navbar color in style.css
css_file = 'd:/Madhurya/Projects/Client Projects/prakaram/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Change .header--scrolled background
css = re.sub(r'background:\s*rgba\(3,\s*65,\s*126,\s*0\.97\);', 'background: #101C36;', css)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixes applied successfully.")
