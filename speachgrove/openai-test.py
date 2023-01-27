from dotenv import load_dotenv
import openai
import os
from pprint import pprint
import requests
import uuid
import time


load_dotenv('.env')

openai.api_key = os.getenv("OPENAI_API_KEY")


response = openai.Completion.create(
    model="text-davinci-003", prompt="In the voice of Obama, give a ten second greeting to Nick.", temperature=0.7, max_tokens=500)

response_text = response['choices'][0]['text']
print(response_text)


# fake you
voice_tokens = {
    'Obama': 'TM:58vtv7x9f32c',
    'Gandhi': 'TM:cvw5qkye9y22',
    'Churchill': 'TM:3na2hzvbfqn7',
    'Kennedy': 'TM:a9pmkvtg2p6b',
    'FDR': 'TM:jh0bts33pn7x',
    'Teddy': 'TM:pn9edma33t2j',
}

myuuid = str(uuid.uuid4())
text = response_text
payload = {
    'uuid_idempotency_token': myuuid,
    'tts_model_token': voice_tokens['Obama'],
    'inference_text': text
}
heads_post = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}
head_get = {
    'Accept': 'application/json',
}

response3 = requests.post(
    'https://api.fakeyou.com/tts/inference', headers=heads_post, json=payload)

pprint(response3.json())
job_token = response3.json()['inference_job_token']


def status_checker(token):
    poll_response = requests.get(
        f'https://api.fakeyou.com/tts/job/{token}', headers=heads_post)

    pprint(poll_response.json())

    status = poll_response.json()['state']['status']
    progress = ['pending', 'started']
    audio_path = poll_response.json(
    )['state']['maybe_public_bucket_wav_audio_path']

    if audio_path:
        return f'https://storage.googleapis.com/vocodes-public{audio_path}'
    elif status in progress:
        time.sleep(3)
        return status_checker(token)
    else:
        return status


print(status_checker(job_token))
