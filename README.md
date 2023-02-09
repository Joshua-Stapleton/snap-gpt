This lightweight system implements a text extraction system for the purpose of extracting the text from images and answering questions posed in them automatically using LLMs. It is designed to be used in conjunction with the [OpenAI API](https://openai.com/).
stock. 

Ensure to run:
```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

Also ensure to add your OpenAI API credentials and a home path variable to a .env file in the form:
```
OPENAI_KEY='...'
HOME_PATH='...'
```

Then run `automation.py`, and run to see the results.