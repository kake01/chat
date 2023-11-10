import pytest
from django.urls import reverse
from chat.models import Message
from chat.views import MessageView
from django.contrib.auth.models import User
from django.db import connection
import django
"""
ステップ_6
@pytest.fixture()を理解する
「pytest chat/chat_test/test_sample3.py -s」でこのテストファイルが実行されることを確認
@pytest.fixture()とは実際のテストに行う前に必要となるデータの準備や処理を記述するために使う

参考: https://qiita.com/_akiyama_/items/9ead227227d669b0564e#%E3%83%95%E3%82%A3%E3%82%AF%E3%82%B9%E3%83%81%E3%83%A3fixture%E3%81%A8%E3%81%AF
"""

# @pytest.fixture(autouse=True)
# def enable_db_access_for_all_tests(db):
# with connection.cursor() as cursor:
#     cursor.execute("CREATE SCHEMA IF NOT EXISTS app")
# schema_name = "your_schema_name"
# with django.db.connection.cursor() as cursor:
#     cursor.execute(f"SET search_path TO {schema_name}")


@pytest.fixture()
def setup_django_db():
    print("ここが先に実行")
    username = "testuser"
    password = "testpassword"
    user = User.objects.create_user(username=username, password=password)
    return username, password, user


@pytest.mark.django_db
def test_is_one_message(setup_django_db):
    username, password, user = setup_django_db
    content = "content内容"
    respond = "respond内容"
    print("その後に実行")

    saved_user = User.objects.all()[0]
    saved_user_count = User.objects.all().count()
    actual_message = MessageView.create_message(user, content, respond)
    saved_messages_count = Message.objects.all().count()

    assert saved_user_count == 1
    assert saved_user.username == username
    assert actual_message.owner == user
    assert saved_messages_count == 1
