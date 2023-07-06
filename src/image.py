from wand.image import Image
import os
from src.tools import *





def prepareIcon(file_path):
    """Generates images for the icon label.

    This function must be used for '.ico' files.

    Args:
        file_path (string): The path to the icon file.
    """
    ico_img = Image(filename=os.path.abspath(file_path))

    for i in ico_img.sequence:
        print(i)
        if i.size[0] == 256:
            ico_img_big = Image(image=i)
        elif i.size[0] == 16:
            ico_img_sml = Image(image=i)

    ico_img_big.resize(135,135)
    ico_img_big_sh = addShadow(ico_img_big)

    checkTempFolder()
    ico_img_big_sh.save(filename=os.path.join(TEMP_PATH, "135_label.png"))
    ico_img_sml.save(filename=os.path.join(TEMP_PATH, "16_label.png"))
    ico_img_sml.resize(10,10)
    ico_img_sml.save(filename=os.path.join(TEMP_PATH, "10_label.png"))

    ico_img_big_sh.close()
    ico_img_big.close()
    ico_img_sml.close()
    ico_img.close()





def prepareImage(file_path):
    """Generates images for the icon label.

    This function must be used for image files.

    Args:
        file_path (string): The path to the icon file.
    """
    ico_img = Image(filename=os.path.abspath(file_path))

    ico_img_big = ico_img.clone()
    ico_img_big.resize(135,135)
    ico_img_big_sh = addShadow(ico_img_big)

    ico_img_sml = ico_img.clone()
    ico_img_sml.resize(16,16)

    checkTempFolder()
    ico_img_big_sh.save(filename=os.path.join(TEMP_PATH, "135_label.png"))
    ico_img_sml.save(filename=os.path.join(TEMP_PATH, "16_label.png"))
    ico_img_sml.resize(10,10)
    ico_img_sml.save(filename=os.path.join(TEMP_PATH, "10_label.png"))

    ico_img_big_sh.close()
    ico_img_big.close()
    ico_img_sml.close()
    ico_img.close()





def addShadow(ico_img):
    """Add a shadow to an image.

    Args:
        ico_img (wand.image.Image): The image to add a shadow to.

    Returns:
        wand.image.Image: The image with a shadow.
    """
    ico_img_sh = ico_img.clone()

    ico_img_sh.shadow(alpha=50, sigma=5, x=0, y=0)
    ico_img_sh.modulate(brightness=0)
    ico_img_sh.composite(ico_img, gravity='center')

    return ico_img_sh
