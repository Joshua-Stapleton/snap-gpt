import openai
from dotenv import load_dotenv
import os 
load_dotenv()
OPENAI_KEY = os.environ.get('OPENAI_KEY')


def generate_gpt3_response(prompt:str) -> str:
    openai.api_key = OPENAI_KEY
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


def generate_gpt4_response(prompt:str) -> str:
    openai.api_key = OPENAI_KEY
    print("Prompt: " + prompt)
    print("Generating response...")
    message = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        max_tokens=1024,
        temperature=0.5,
        messages = message
    )

    return response['choices'][0]['message']['content']