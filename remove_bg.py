#!/usr/bin/env python3
try:
    from PIL import Image
except ImportError:
    print("Installing pillow...")
    import subprocess
    subprocess.check_call(['pip3', 'install', 'pillow'])
    from PIL import Image

# Open the image
img = Image.open('logo_text.png').convert('RGBA')
pixels = img.load()
width, height = img.size

# Remove black background (make it transparent)
for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        # If pixel is very dark (black background), make it transparent
        if r < 30 and g < 30 and b < 30:
            pixels[x, y] = (r, g, b, 0)

# Save the transparent version
img.save('logo_text_transparent.png')
print("Created logo_text_transparent.png with transparent background")
