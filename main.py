import os
from wand.image import Image

big_template_path = os.path.abspath("big.png")
big_template_image = Image(filename=big_template_path)

temp_dir = os.path.abspath("temp")
if not os.path.exists(temp_dir):
    print("Creating temp directory at", temp_dir, "...")
    os.mkdir(temp_dir)

icon_image_path = os.path.abspath(input("Enter the path of the icon image: "))
print("    Loading icon image at", icon_image_path, "...")

if not os.path.exists(icon_image_path):
    print("    Icon image does not exist!")
    exit(1)

icon_image = Image(filename=icon_image_path)
print("    Icon image loaded.")

if icon_image_path.endswith(".ico"):
    print("Image is an icon file.")
    for i in icon_image.sequence:
        if i.size[0] in [256, 32, 24, 16]:
            print("    Saving icon image with size", i.size[0], "...")
            Image(i).save(filename=os.path.join(temp_dir, f"{i.size[0]}.png"))
else:
    print("Image is not an icon file.")
    print("    Resizing icon image to 256x256 ...")
    icon_image.resize(256, 256)
    icon_image.save(filename=os.path.join(temp_dir, "256.png"))
    icon_image.resize(10, 10)
    icon_image.save(filename=os.path.join(temp_dir, "10.png"))


print("    Resizing 256x256 image to 135x135 ...")
with Image(filename=os.path.join(temp_dir, "256.png")) as img:
    resized_img = img.clone()
    resized_img.resize(135, 135)
    resized_img.save(filename=os.path.join(temp_dir, "135.png"))

# resize the 256x256 image from the temp directory to 135x135

image_135 = Image(filename=os.path.join(temp_dir, "135.png"))
image_135_shadow = Image(filename=os.path.join(temp_dir, "135.png"))

# add a black shadow to the 135x135 image
print("    Adding a black shadow to the 135x135 image ...")
image_135_shadow.shadow(alpha=50, sigma=5, x=0, y=0)

# reduce the lightness of the shadow to the minimum
print("    Reducing the lightness of the shadow ...")
image_135_shadow.modulate(brightness=0, saturation=100, hue=100)


# add the 135x135 image to the big template
print("    Adding the 135x135 image to the big template ...")
big_template_image.composite(image_135_shadow, left=94, top=91)
big_template_image.composite(image_135, left=104, top=101)


#save the big template as a png file
print("    Saving the big template as a png file ...")
big_template_image.save(filename=os.path.join(temp_dir, "big_template2.png"))
image_135.save(filename=os.path.join(temp_dir, "135.png"))
image_135_shadow.save(filename=os.path.join(temp_dir, "135_shadow.png"))
