import pytest
from django.urls import reverse
from chat.models import Message
from chat.views import MessageView
from django.contrib.auth.models import User
from django.test import Client
"""
ステップ_5_2
client.getを理解する
「pytest chat/chat_test/test_sample5_2.py -s」でこのテストファイルが実行されることを確認
views.pyの
    class MessageView(LoginRequiredMixin, TemplateView):
    LoginRequiredMixinはログインしていなければログインぺージに飛ばされるためstatus_code = 302になる
"""


@pytest.mark.django_db
def test_sample():
    # Djangoのテストクライアントを作成
    client = Client()
    # ユーザーを作成してログインしてからリクエストを行う
    user = User.objects.create_user(username="testuser",
                                    password="testpassword")
    client.login(username="testuser", password="testpassword")

    # """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
    # ※補足
    # reverse('chat:chat_bot_message') ==>urlsのapp_name:pathのnameのurlにアクセスする
    response = client.get(reverse("chat:chat_bot_message"))
    assert response.status_code == 200
