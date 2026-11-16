from PIL import Image
import os

input_path = 'd:/Madhurya/Projects/Client Projects/prakaram/images/IMG_5732.JPG'
output_path = 'd:/Madhurya/Projects/Client Projects/prakaram/images/compressed/IMG_5732.jpg'

if not os.path.exists(output_path):
    img = Image.open(input_path)
    # Convert to RGB if needed
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Resize if too large
    max_size = (1200, 1200)
    img.thumbnail(max_size, Image.Resampling.LANCZOS)
    
    img.save(output_path, "JPEG", optimize=True, quality=80)
    print("Compressed image created.")
else:
    print("Compressed image already exists.")

