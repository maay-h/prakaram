import os
import glob
from PIL import Image
import re

html_file = 'd:/Madhurya/Projects/Client Projects/prakaram/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

images_dir = 'd:/Madhurya/Projects/Client Projects/prakaram/images'
target_images = [
    'DivyaTiwari&VishalJain.jpeg',
    'Akshath&Vageesha.jpeg',
    'grandweddingreception.png',
    'florl&ambience.JPG'
]

max_dimension = 1600

for img_name in target_images:
    img_path = os.path.join(images_dir, img_name)
    if not os.path.exists(img_path):
        continue
        
    try:
        with Image.open(img_path) as img:
            # Convert RGBA to RGB for JPEG compatibility
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # Calculate new size maintaining aspect ratio
            width, height = img.size
            if width > max_dimension or height > max_dimension:
                if width > height:
                    new_width = max_dimension
                    new_height = int(max_dimension * height / width)
                else:
                    new_height = max_dimension
                    new_width = int(max_dimension * width / height)
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # New filename if converting from PNG
            base, ext = os.path.splitext(img_name)
            new_ext = '.jpg'
            new_name = base + new_ext
            new_path = os.path.join(images_dir, new_name)
            
            # Save compressed
            img.save(new_path, 'JPEG', quality=80, optimize=True)
            print(f"Compressed {img_name} to {new_name}")
            
            # Update HTML
            html = html.replace('images/' + img_name, 'images/' + new_name)
            
            # Delete original if we created a new file with different extension
            if img_name != new_name:
                os.remove(img_path)
    except Exception as e:
        print(f"Error compressing {img_name}: {e}")

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
