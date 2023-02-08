from rest_framework.decorators import api_view
from rest_framework.response import Response
from speechwriter.models import Request, ChatResponse, VoiceResponse
from speechwriter.speech_generator import text_generator, voice_generator


@api_view(['GET', 'POST'])
def api_cycle(request):
    voice_tokens = {
        'Obama': 'TM:58vtv7x9f32c',
        'Gandhi': 'TM:cvw5qkye9y22',
        'Churchill': 'TM:3na2hzvbfqn7',
        'Kennedy': 'TM:a9pmkvtg2p6b',
        'FDR': 'TM:jh0bts33pn7x',
        'Teddy': 'TM:pn9edma33t2j',
    }

    speaker = request.POST['speakerName']

    r = Request.objects.create(
        request_text=request.POST['requestText'], speaker_name=speaker, speaker_token=voice_tokens[speaker])

    chat = ChatResponse.objects.create(
        response_text=text_generator(r.speaker_name, r.request_text), request=r.id,
    )

    voice = VoiceResponse.objects.create(
        response_audio_url=voice_generator(voice_tokens[speaker], chat.response_text), chat_response=chat.id
    )
    data = {
        'speaker': speaker,
        'audio_url': voice.response_audio_url,
        'text': chat.response_text,
    }
    return Response(data)
