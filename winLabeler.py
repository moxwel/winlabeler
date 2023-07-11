from src.texts import *
from src.image import *
from src.tools import *

import argparse 
parser = argparse.ArgumentParser() # Create the parser
parser.add_argument('--path', type=str, help="Path of the image you want to use as the label icon", required=True) # Add an argument
parser.add_argument('size', type=str, help="Image Size. small or large")
args = parser.parse_args() # Parse the argument. you can access to -path by args.path

if args.size.lower() not in ["small","large"]: #check for size argument. must be "large" or "small"
    parser.error('Size has to be "large" or "small"')

welcomeString()

file_path = args.path

if not os.path.exists(file_path):
    print("    [!] File does not exist!")
    exit(1)

file_ext = os.path.splitext(file_path)[1]

if file_ext not in [".png", ".jpg", ".jpeg", ".ico"]:
    print("    [!] File is not a png, jpg, jpeg or ico file!")
    exit(1)

prepareLabel(file_path)

compositeLabel()

small_folder = args.size.lower()

if small_folder.lower() == "small":
    s = True
else:
    s = False

generateIcon(small_folder=s)

cleanUp()

print("\nDone! File 'out.ico' created in the root folder.")
