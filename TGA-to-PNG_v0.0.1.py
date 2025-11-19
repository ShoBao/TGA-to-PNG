from PIL import Image
import sys

# Creator: ShoBao https://github.com/ShoBao
# Version: 0.0.1

if len(sys.argv) < 2:
    print("Drag a TGA file onto the script to convert it to PNG")
    sys.exit(1)

for tga_name in sys.argv[1:]:
    img = Image.open(tga_name)
    img.save(tga_name.replace(".tga", ".png"))