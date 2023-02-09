from django.urls import path
from .views import api_cycle

urlpatterns = [
    path('speech/', api_cycle, name='speech'),
]
