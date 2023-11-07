from django.urls import path
from .views import MessageView

app_name = 'chat'

urlpatterns = [
    path('', MessageView.as_view(), name='chat_bot_message'),
]
 