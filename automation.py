from os import listdir
from os.path import isfile, join
from PIL import Image
import time
import pytesseract


def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

#function to return files in a directory
def fileInDirectory(my_dir: str):
    onlyfiles = [f for f in listdir(my_dir) if isfile(join(my_dir, f))]
    return(onlyfiles)


#function comparing two lists
def listComparison(OriginalList: list, NewList: list):
    differencesList = [x for x in NewList if x not in OriginalList] #Note if files get deleted, this will not highlight them
    return(differencesList)


watchDirectory = '/Users/joshuastapleton/Desktop/mozart_sonatas'

def fileWatcher(my_dir: str, pollTime: int):
    while True:
        if 'watching' not in locals(): # Check if this is the first time the function has run
            previousFileList = fileInDirectory(watchDirectory)
            watching = 1
            print('First Time')
            print(previousFileList)
        
        time.sleep(pollTime)
        
        newFileList = fileInDirectory(watchDirectory)
        
        fileDiff = listComparison(previousFileList, newFileList)
        
        previousFileList = newFileList
        if len(fileDiff) == 0: continue
        print(fileDiff)

fileWatcher(watchDirectory, 1)
