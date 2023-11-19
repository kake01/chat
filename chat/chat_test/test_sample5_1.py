import pytest
from django.urls import reverse
from chat.models import Message
from chat.views import MessageView
from django.contrib.auth.models import User
from django.test import Client
"""
ステップ_5
client.getを理解する
「pytest chat/chat_test/test_sample5_1.py -s」でこのテストファイルが実行されることを確認

urlマッピングされたurlにアクセスする
reverse('chat:chat_bot_message') ==>urlsのapp_name:pathのnameのurlにアクセスする
"""

# @pytest.mark.django_db
# def test_sample():
#     client = Client()
#     response = client.get(reverse("chat:chat_bot_message"))
#     assert response.status_code == 200
