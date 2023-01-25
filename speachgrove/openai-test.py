# failed attempt at using chronological
# from chronological import main, read_prompt, gather, cleaned_completion


# async def logic():
#     prompt = 'Write me a greeting in the voice of Robert Deniro'
#     completion = await cleaned_completion(prompt,  max_tokens=500, engine="davinci", temperature=0.5)

#     print('Completion Response: {0}'.format(completion))


# main(logic)

from dotenv import load_dotenv
import openai
import os

load_dotenv('.env')

openai.api_key = os.getenv("OPENAI_API_KEY")


response = openai.Completion.create(
    model="text-davinci-003", prompt="Give a short polite greeting. My name is Nick", temperature=0.7, max_tokens=100)


print(response['choices'][0]['text'])
