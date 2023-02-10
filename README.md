This lightweight system implements text extraction for the purpose of answering questions posed in images automatically using LLMs. It is designed to be used in conjunction with the [OpenAI API](https://openai.com/). 

To setup, ensure to run:
```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

Also ensure to add your OpenAI API credentials, a home path variable, and email login credentials to a .env file in the form:
```
OPENAI_KEY='...'
HOME_PATH='...'
SENDING_EMAIL_ADDRESS='...'
RECEIVING_EMAIL_ADDRESS='...'
EMAIL_PASSWORD='...'
```
Your home path variable should be to a folder that contains the images you would like to extract text from. The images should be in .png or .jpg format. On Mac, it is possible to set this path so that all new screenshots are saved there; open screenshot settings using shift+command+5, and set the location to the home path variable.

See [Google Account Help](https://support.google.com/accounts/answer/185833?visit_id=638115306131809626-4056881382&p=InvalidSecondFactor&rd=1) for more information on how to obtain an email app password.

Finally, run `snap_gpt.py`, and run to see the results. Specify whether you would like the results to be sent to your email, printed out in the terminal, or both by passing in the notification type to the `file_watcher` function.