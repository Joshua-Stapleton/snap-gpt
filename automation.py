import os 
from os import listdir
from os.path import isfile, join
from PIL import Image
import time
import pytesseract
from gpt_functions import generate_gpt3_response
from dotenv import load_dotenv
load_dotenv()
watch_directory = os.environ.get('HOME_PATH')


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


def fileWatcher(my_dir: str, pollTime: int):
    while True:
        if 'watching' not in locals(): # Check if this is the first time the function has run
            previousFileList = fileInDirectory(watch_directory)
            watching = 1
            print('First Time')
            print(previousFileList)
        
        time.sleep(pollTime)
        
        newFileList = fileInDirectory(watch_directory)
        
        fileDiff = listComparison(previousFileList, newFileList)
        
        previousFileList = newFileList
        if len(fileDiff) == 0: continue
        print(watch_directory+"/"+fileDiff[0])
        extracted_text = extract_text_from_image(watch_directory+"/"+fileDiff[0])
        print(generate_gpt3_response(extracted_text))

fileWatcher(watch_directory, 1)
