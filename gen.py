import os

# Supported image extensions
IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif", ".webp")

# Scan current folder for images
images = [f for f in os.listdir(".") if f.lower().endswith(IMAGE_EXTENSIONS)]
images.sort()  # alphabetical order

if not images:
    print("No images found in this folder.")
    exit()

# Start writing README.md
with open("README.md", "w") as readme:
    readme.write("# 🖼️ Image Gallery\n\n")
    readme.write("এই ফোল্ডারের সব ইমেজ নিচে দেখানো হলো:\n\n")

    for img in images:
        readme.write(f"### {img}\n")
        readme.write(f"![{img}]({img})\n\n")

print(f"✅ README.md generated with {len(images)} images!")
