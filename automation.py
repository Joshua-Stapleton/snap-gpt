import os 
from os import listdir
from os.path import isfile, join
from PIL import Image
import time
import pytesseract
from gpt_functions import generate_gpt3_response
from popup_module import send_email
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


def fileWatcher(watch_directory: str, notification_type:str):
    while True:
        if 'watching' not in locals(): # Check if this is the first time the function has run
            previousFileList = fileInDirectory(watch_directory)
        
        time.sleep(1)
        newFileList = fileInDirectory(watch_directory)
        fileDiff = listComparison(previousFileList, newFileList)
        previousFileList = newFileList

        if len(fileDiff) == 0: continue
        print(watch_directory+"/"+fileDiff[0])
        extracted_text = extract_text_from_image(watch_directory+"/"+fileDiff[0])
        response = generate_gpt3_response(extracted_text)
        if notification_type == "email":
            send_email(os.environ.get('SENDING_EMAIL_ADDRESS'), os.environ.get('RECEIVING_EMAIL_ADDRESS'), 'Answer', extracted_text + "\n-----------------------\n" + response, os.environ.get('EMAIL_PASSWORD'))
        # elif notification_type == "popup":
        #     popup(extracted_text)
        else: # print in terminal
            print(response)

fileWatcher(watch_directory, "email")
