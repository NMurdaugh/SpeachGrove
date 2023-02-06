from dotenv import load_dotenv
import openai
import os


def text_generator(speaker, prompt):
    load_dotenv('.env')

    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-003", prompt="In the voice of Obama, give a 30 second greeting to Nick.", temperature=0.7, max_tokens=500)

    response_text = response['choices'][0]['text']
    print(response_text)
    return response_text
