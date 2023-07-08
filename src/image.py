from wand.image import Image
import os
from src.tools import *




FOLDR_IMG_BIG = os.path.join(ROOT_PATH, "resources", "big.png")
FOLDR_IMG_SML = os.path.join(ROOT_PATH, "resources", "small.png")




def generateIcon(small_folder=True):
    """Generate an .ico file with multiple resolutions.

    Args:
        small_folder (bool, optional): Indicates if the smallest icon shoud be a folder. Defaults to True.
    """
    # Load folder images
    fld_img_256 = Image(filename=os.path.join(TEMP_PATH, "folder_256.png"))
    fld_img_256.type = 'truecoloralpha'
    fld_img_48 = Image(filename=os.path.join(TEMP_PATH, "folder_48.png"))
    fld_img_48.type = 'truecoloralpha'
    fld_img_32 = Image(filename=os.path.join(TEMP_PATH, "folder_32.png"))
    fld_img_32.type = 'truecoloralpha'

    # Should the smallest icon be a folder?
    if small_folder:
        fld_img_16 = Image(filename=os.path.join(TEMP_PATH, "folder_16.png"))
    else:
        fld_img_16 = Image(filename=os.path.join(TEMP_PATH, "label_16.png"))
    fld_img_16.type = 'truecoloralpha'

    # Combine images into a single ico file
    fld_img_256.sequence.append(fld_img_48)
    fld_img_256.sequence.append(fld_img_32)
    fld_img_256.sequence.append(fld_img_16)

    # Save ico file
    checkTempFolder()
    fld_img_256.save(filename=os.path.join(TEMP_PATH, "out.ico"))

    # Close images
    fld_img_256.close()
    fld_img_48.close()
    fld_img_32.close()
    fld_img_16.close()





def prepareLabel(file_path):
    """Generates images for the icon label.

    Args:
        file_path (string): The path to the icon file.
    """
    # Load folder images
    ico_img = Image(filename=os.path.abspath(file_path))
    ico_img.type = 'truecoloralpha'

    # The .ico file format has multiple resolutions inside, we need to extract them
    file_ext = os.path.splitext(file_path)[1]
    if file_ext == ".ico":
        for i in ico_img.sequence:
            if i.size[0] == 256:
                ico_img_big = Image(image=i)
                ico_img_big.resize(135,135)
                ico_img_big_sh = addShadow(ico_img_big)

            elif i.size[0] == 16:
                ico_img_sml = Image(image=i)

        ico_img_min = ico_img_sml.clone()
        ico_img_min.resize(10,10)

    elif file_ext in [".png", ".jpg", ".jpeg"]:
        ico_img_big = ico_img.clone()
        ico_img_big.resize(135,135)
        ico_img_big_sh = addShadow(ico_img_big)

        ico_img_sml = ico_img.clone()
        ico_img_sml.resize(16,16)

        ico_img_min = ico_img.clone()
        ico_img_min.resize(10,10)

    # Save images
    checkTempFolder()
    ico_img_big_sh.save(filename=os.path.join(TEMP_PATH, "label_135.png"))
    ico_img_sml.save(filename=os.path.join(TEMP_PATH, "label_16.png"))
    ico_img_min.save(filename=os.path.join(TEMP_PATH, "label_10.png"))

    # Close images
    ico_img_big_sh.close()
    ico_img_big.close()
    ico_img_sml.close()
    ico_img_min.close()
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





def compositeLabel():
    """Generates the folder images with the label.
    """
    # Load images
    big_img = Image(filename=os.path.join(TEMP_PATH, "label_135.png"))
    big_img.type = 'truecoloralpha'
    min_img = Image(filename=os.path.join(TEMP_PATH, "label_10.png"))
    min_img.type = 'truecoloralpha'
    fld_img_big = Image(filename=FOLDR_IMG_BIG)
    fld_img_big.type = 'truecoloralpha'
    fld_img_sml = Image(filename=FOLDR_IMG_SML)
    fld_img_sml.type = 'truecoloralpha'

    fld_img_big.composite(big_img, left=94, top=91)
    fld_img_sml.composite(min_img, gravity='south_east')

    # Save images
    checkTempFolder()
    fld_img_big.save(filename=os.path.join(TEMP_PATH, "folder_256.png"))

    fld_img_big.resize(48,48)
    fld_img_big.save(filename=os.path.join(TEMP_PATH, "folder_48.png"))

    fld_img_big.resize(32,32)
    fld_img_big.save(filename=os.path.join(TEMP_PATH, "folder_32.png"))

    fld_img_sml.save(filename=os.path.join(TEMP_PATH, "folder_16.png"))

    # Close images
    big_img.close()
    min_img.close()
    fld_img_big.close()
    fld_img_sml.close()





def printImageSpecs(img):
    """Prints all properties from a wand.image.Image object.

    Args:
        img (wand.image.Image): The wand image object.
    """
    print("===\nImage Specs:")
    print("Width: " + str(img.width))
    print("Height: " + str(img.height))
    print("Depth: " + str(img.depth))
    print("Format: " + str(img.format))
    print("Size: " + str(img.size))
    print("Units: " + str(img.units))
    print("Resolution: " + str(img.resolution))
    print("Type: " + str(img.type))
    print("Signature: " + str(img.signature))
    print("Mime: " + str(img.mimetype))
    print("Compression: " + str(img.compression))
    print("Colorspace: " + str(img.colorspace) + "\n===")
