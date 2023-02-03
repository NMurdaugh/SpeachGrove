from rest_framework.decorators import api_view
from rest_framework.response import Response
from speechwriter.models import Request, ChatResponse, VoiceResponse


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
    speaker = request.POST['speaker_name']
    Request.objects.create(
        request_text=request.POST['request_text'], speaker_name=speaker, speaker_token=voice_tokens[speaker])
