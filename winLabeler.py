from src.texts import *
from src.image import *
from src.tools import *

welcomeString()

file_path = input("> Enter the path of the icon label: ")

if not os.path.exists(file_path):
    print("    [!] File does not exist!")
    exit(1)

file_ext = os.path.splitext(file_path)[1]

if file_ext not in [".png", ".jpg", ".jpeg", ".ico"]:
    print("    [!] File is not a png, jpg, jpeg or ico file!")
    exit(1)

prepareLabel(file_path)

compositeLabel()

small_folder = input("> Use small folder? (y/n): ")

if small_folder.lower() in ["y", "yes"]:
    s = True
else:
    s = False

generateIcon(small_folder=s)

cleanUp()

print("\nDone! File 'out.ico' created in the root folder.")
