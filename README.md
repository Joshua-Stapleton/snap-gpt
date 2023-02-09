This lightweight system implements a text extraction system for the purpose of extracting the text from images and answering questions posed in them automatically using LLMs. It is designed to be used in conjunction with the [OpenAI API](https://openai.com/).
stock. 

Ensure to run:
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
See [Google Account Help](https://support.google.com/accounts/answer/185833?visit_id=638115306131809626-4056881382&p=InvalidSecondFactor&rd=1) for more information on how to obtain an email app password.

Finally, run `automation.py`, and run to see the results. Specify whether you would like the results to be sent to your email or printed out in the terminal by passing in the notification type to the .