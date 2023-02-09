import openai
from dotenv import load_dotenv
import os 
load_dotenv()
openai_key = os.environ.get('OPENAI_KEY')

def generate_gpt3_response(prompt):
    openai.api_key = openai_key
    print("Prompt: " + prompt)
    print("Generating response...")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response["choices"][0]["text"]
    return message