import os





TEMP_FOLD_NAME = 'temp'

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TEMP_PATH = os.path.join(ROOT_PATH, TEMP_FOLD_NAME)





def checkTempFolder():
    """Check if the temp folder exists. If not, create it.
    """
    if not os.path.exists(TEMP_PATH):
        os.mkdir(TEMP_PATH)





def isTempFolderEmpty():
    """Check if the temp folder is empty.

    Returns:
        bool: If the temp folder is empty, return True. Otherwise, return False.
    """
    return len(os.listdir(TEMP_PATH)) == 0





def clearTempFolder():
    """Delete all files in the temp folder.
    """
    for file in os.listdir(TEMP_PATH):
        os.remove(os.path.join(TEMP_PATH, file))




def cleanUp():
    """Move the output file to the root folder and delete the temp folder.
    """
    os.rename(os.path.join(TEMP_PATH, "out.ico"), os.path.join(ROOT_PATH, "out.ico"))
    clearTempFolder()
    os.rmdir(TEMP_PATH)
