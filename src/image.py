from wand.image import Image
import os
from src.tools import *




FOLDR_IMG_BIG = os.path.join(ROOT_PATH, "resources", "big.png")
FOLDR_IMG_SML = os.path.join(ROOT_PATH, "resources", "small.png")




def generateIcon(name="icon", small_folder=True):
    # combine different images resolutons to a single file icon.ico

    fld_img_256 = Image(filename=os.path.join(TEMP_PATH, "folder_256.png"))
    fld_img_48 = Image(filename=os.path.join(TEMP_PATH, "folder_48.png"))
    fld_img_32 = Image(filename=os.path.join(TEMP_PATH, "folder_32.png"))

    if small_folder:
        fld_img_16 = Image(filename=os.path.join(TEMP_PATH, "folder_16.png"))
    else :
        fld_img_16 = Image(filename=os.path.join(TEMP_PATH, "16_label.png"))

    # combine images into a single ico file with multiple resolutions
    fld_img_256.sequence.append(fld_img_48)
    fld_img_256.sequence.append(fld_img_32)
    fld_img_256.sequence.append(fld_img_16)

    fld_img_256.save(filename=os.path.join(TEMP_PATH, name + ".ico"))





def prepareIcon(file_path):
    """Generates images for the icon label.

    This function must be used for '.ico' files.

    Args:
        file_path (string): The path to the icon file.
    """
    ico_img = Image(filename=os.path.abspath(file_path))

    for i in ico_img.sequence:
        if i.size[0] == 256:
            ico_img_big = Image(image=i)
            ico_img_big.resize(135,135)
            ico_img_big_sh = addShadow(ico_img_big)

        elif i.size[0] == 16:
            ico_img_sml = Image(image=i)

    ico_img_min = ico_img_sml.clone()
    ico_img_min.resize(10,10)

    checkTempFolder()
    ico_img_big_sh.save(filename=os.path.join(TEMP_PATH, "135_label.png"))
    ico_img_sml.save(filename=os.path.join(TEMP_PATH, "16_label.png"))
    ico_img_min.save(filename=os.path.join(TEMP_PATH, "10_label.png"))

    composeFolderIcon(ico_img_big_sh, ico_img_min)

    ico_img_big_sh.close()
    ico_img_big.close()
    ico_img_sml.close()
    ico_img_min.close()
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

    ico_img_min = ico_img.clone()
    ico_img_min.resize(10,10)

    checkTempFolder()
    ico_img_big_sh.save(filename=os.path.join(TEMP_PATH, "135_label.png"))
    ico_img_sml.save(filename=os.path.join(TEMP_PATH, "16_label.png"))
    ico_img_min.save(filename=os.path.join(TEMP_PATH, "10_label.png"))

    composeFolderIcon(ico_img_big_sh, ico_img_min)

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





def composeFolderIcon(big_img, sml_img):
    fld_img_big = Image(filename=FOLDR_IMG_BIG)
    fld_img_sml = Image(filename=FOLDR_IMG_SML)

    fld_img_big.composite(big_img, left=94, top=91)
    fld_img_sml.composite(sml_img, gravity='south_east')

    fld_img_big.save(filename=os.path.join(TEMP_PATH, "folder_256.png"))

    fld_img_big.resize(48,48)
    fld_img_big.save(filename=os.path.join(TEMP_PATH, "folder_48.png"))

    fld_img_big.resize(32,32)
    fld_img_big.save(filename=os.path.join(TEMP_PATH, "folder_32.png"))

    fld_img_sml.save(filename=os.path.join(TEMP_PATH, "folder_16.png"))

    fld_img_big.close()
    fld_img_sml.close()





def printImageSpecs(img):
    """Prints all properties from a wand.image.Image object.

    Args:
        img (wand.image.Image): The wand image object.
    """
    print("Image Specs:")
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
    print("Colorspace: " + str(img.colorspace))
