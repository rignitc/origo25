import os
from PIL import Image

# Supported image formats (you can extend this if needed)
valid_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]

# Loop through files in current folder
for filename in os.listdir("."):
    name, ext = os.path.splitext(filename)
    if ext.lower() in valid_extensions:
        try:
            img = Image.open(filename).convert("RGB")  # convert to RGB for webp
            webp_name = f"{name}.webp"
            img.save(webp_name, "WEBP")
            print(f"Converted: {filename} -> {webp_name}")
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")
