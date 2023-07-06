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

if file_ext in [".png", ".jpg", ".jpeg"]:
    print("    File is an image.\n")
    prepareImage(file_path)
elif file_ext == ".ico":
    print("    File is an icon.\n")
    prepareIcon(file_path)
