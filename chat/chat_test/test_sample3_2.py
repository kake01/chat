import pytest
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
"""
ステップ_4
@pytest.mark.django_dbを理解する
「pytest chat/chat_test/test_sample3_2.py -s」でこのテストファイルが実行されることを確認

@pytest.mark.django_dbとは
pytestでDB関連のテストを行いたい場合にデコレータを付ける必要がある
参考:   https://blog.mtb-production.info/entry/2019/07/10/090000
    　　https://self-methods.com/django-pytest-fixture/
"""


@pytest.mark.django_db
def test_is_one_user():
    print("テストユーザーを作成します")
    username = "testuser"
    password = "testpassword"

    User.objects.create_user(username=username, password=password)
    # 登録されているユーザーの1件を取得
    saved_user = User.objects.all()[0]
    # 登録されているユーザーの件数を取得
    saved_user_count = User.objects.all().count()

    assert saved_user_count == 1
    assert saved_user.username == username

    # 補足
    # Userクラスは使っていないので見たい人のみ見てください
    # passwordが一致しているかを知らべたい場合には1ステップ挟む必要がある
    # assert check_password(password, saved_user.password) #　このままではダメ
    # assert check_password(password, saved_user.password) #　こっちに直す
