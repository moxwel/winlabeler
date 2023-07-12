from src.texts import *
from src.image import *
from src.tools import *

import argparse 
parser = argparse.ArgumentParser() # Create the parser

parser.add_argument('path', type=str, help="Path of the image you want to use as the label icon") # example: python winLabeler.py "C:\Users\User\example.png"
parser.add_argument('-ns','--no-small-folder', action="store_true") #args.ns will be False if you not use -ns flag
parser.add_argument('-o','--output', type=str, help="Output file name. Default is out.ico",default="out.ico") 

args = parser.parse_args() # Parse the argument. you can access to -path by args.path

file_path = args.path
no_small_folder = args.no_small_folder #argparse automatically converts -'s to _'s in arguments
output = args.output

welcomeString()

if not os.path.exists(file_path):
    print("    [!] File does not exist!")
    exit(1)

file_ext = os.path.splitext(file_path)[1]

if file_ext not in [".png", ".jpg", ".jpeg", ".ico"]:
    print("    [!] File is not a png, jpg, jpeg or ico file!")
    exit(1)

prepareLabel(file_path)

compositeLabel()

generateIcon(no_small_folder, output)

cleanUp()

print("\nDone! File 'out.ico' created in the root folder.")
