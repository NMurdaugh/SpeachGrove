from django.db import models

# Create your models here.


class Request(models.Model):
    datetime = models.DateTimeField('date published', auto_now_add=True)
    request_text = models.TextField()
    speaker_name = models.CharField(max_length=200)
    speaker_token = models.CharField(max_length=200)


class ChatResponse(models.Model):
    datetime = models.DateTimeField('date published', auto_now_add=True)
    response_text = models.TextField(blank=True, null=True)
    request = models.ForeignKey(
        Request, on_delete=models.CASCADE, null=True, blank=True)


class VoiceResponse(models.Model):
    datetime = models.DateTimeField('date published', auto_now_add=True)
    response_audio_file = models.FileField(blank=True, null=True)
    response_audio_url = models.CharField(
        max_length=255, blank=True, null=True)
    chat_response = models.ForeignKey(
        ChatResponse, on_delete=models.CASCADE, null=True, blank=True)
