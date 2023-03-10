from rest_framework.decorators import api_view
from rest_framework.response import Response
from speechwriter.models import Request, ChatResponse, VoiceResponse
from speechwriter.speech_generator import text_generator, voice_generator


@api_view(['POST'])
def api_cycle(request):
    voice_data = {
        'Obama': ['Barack Obama', 'TM:58vtv7x9f32c'],
        'Deniro': ['Robert DeNiro', 'TM:msds8ma95f2f'],
        'Hank': ['Hank Hill', 'TM:63y8yd94ndds'],
    }
    print(request.body)
    print(request.data)
    for key in request.POST.keys():
        print(key)
    print(request.POST.keys())
    speaker = request.data['speakerName']
    speaker_name_full = voice_data[speaker][0]
    token = voice_data[speaker][1]

    r = Request.objects.create(
        request_text=request.data['userRequestText'], speaker_name=speaker_name_full, speaker_token=token)

    chat = ChatResponse.objects.create(
        response_text=text_generator(r.speaker_name, r.request_text), request=r,
    )

    voice = VoiceResponse.objects.create(
        response_audio_url=voice_generator(token, chat.response_text), chat_response=chat
    )
    data = {
        'speaker': speaker_name_full,
        'audio_url': voice.response_audio_url,
        'text': chat.response_text,
    }
    return Response(data)
