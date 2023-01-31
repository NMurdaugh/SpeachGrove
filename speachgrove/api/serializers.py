from rest_framework import serializers
from speechwriter.models import Request, ChatResponse, VoiceResponse


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('datetime', 'request_text', 'id',
                  'speaker_name', 'speaker_token')


class ChatResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatResponse
        fields = ('datetime', 'response_text', 'request', 'id')

    class VoiceResponseSerializer(serializers.ModelSerializer):
        class Meta:
            model = VoiceResponse
            fields = ('datetime', 'response_audio_file',
                      'response_audio_url', 'chat_response')
