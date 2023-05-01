import os 
import re
from os import listdir
from os.path import isfile, join
from PIL import Image
import time
import pytesseract
from functions.gpt_functions import generate_gpt4_response
from functions.notification_functions import send_email
from dotenv import load_dotenv
load_dotenv()
watch_directory = os.environ.get('HOME_PATH')


def extract_text_from_image(image_path:str, crop:bool=False):
    image = Image.open(image_path)
    if crop:
        width, height = image.size
        left = width / 4
        top = height / 6
        right = 3 * width / 4
        bottom = 3 * height / 4
        image = image.crop((left, top, right, bottom))
    text = pytesseract.image_to_string(image)
    return text


# function to return files in a directory
def file_in_directory(my_dir: str):
    only_files = [f for f in listdir(my_dir) if isfile(join(my_dir, f))]
    return(only_files)


# function comparing two lists
def list_comparison(original_list: list, new_list: list):
    differences_list = [x for x in new_list if x not in original_list] # Note if files get deleted, this will not highlight them
    return(differences_list)


def file_watcher(watch_directory: str, notification_type:str="print"):
    while True:
        if 'watching' not in locals(): # Check if this is the first time the function has run
            previous_file_list = file_in_directory(watch_directory)
        
        time.sleep(1)
        new_file_list = file_in_directory(watch_directory)
        file_diff = list_comparison(previous_file_list, new_file_list)
        previous_file_list = new_file_list
        if len(file_diff) == 0: continue
        print(watch_directory+"/"+file_diff[0])
        extracted_text = extract_text_from_image(watch_directory+"/"+file_diff[0])
        # remove any characters which cannot be processed by gpt3
        extracted_text = re.sub(u"(\u2018|\u2019|\xa9|\u201d|\xae|\u2014|\u201c|\xbb)", "", extracted_text)
        response = generate_gpt4_response(extracted_text)
        if notification_type == "all":
            print(response)
            send_email(os.environ.get('SENDING_EMAIL_ADDRESS'), os.environ.get('RECEIVING_EMAIL_ADDRESS'), 'Answer', extracted_text + "\n-----------------------\n" + response, os.environ.get('EMAIL_PASSWORD'))
        elif notification_type == "email":
            send_email(os.environ.get('SENDING_EMAIL_ADDRESS'), os.environ.get('RECEIVING_EMAIL_ADDRESS'), 'Answer', extracted_text + "\n-----------------------\n" + response, os.environ.get('EMAIL_PASSWORD'))
        # elif notification_type == "popup":
        #     popup(extracted_text)
        else: # print in terminal
            print(response)

file_watcher(watch_directory, notification_type="all")
