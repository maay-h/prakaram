from PIL import Image
img = Image.open('d:/Madhurya/Projects/Client Projects/prakaram/images/logo1.png')
print("Format:", img.format)
print("Mode:", img.mode)
print("Size:", img.size)
# Sample a few pixels to see if it's mostly white or transparent
extrema = img.getextrema()
print("Extrema:", extrema)
