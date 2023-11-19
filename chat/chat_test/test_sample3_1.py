import pytest
from django.contrib.auth.models import User
"""
ステップ_3
@pytest.mark.django_dbを理解する
 chatアプリケーションで使用しているmodelsのテストを行うプログラムを書いてみる
「pytest chat/chat_test/test_sample3_1.py -s」でこのテストファイルが実行されることを確認
 ※ このままではエラーが発生します

Django userモデルとは?
非推奨であるが今回は外部主キーがあるモデルのテストのために利用
参考: https://qiita.com/iwatsukayura/items/5f3ceb173dc151c0488b

"""

# def test_error_is_one_user():
#     print("このままではエラーが発生します")
#     username = "testuser"
#     password = "testpassword"

#     User.objects.create_user(username=username, password=password)
#     # 登録されているユーザーの1件を取得
#     saved_user = User.objects.all()[0]
#     # 登録されているユーザーの件数を取得
#     saved_user_count = User.objects.all().count()

#     assert saved_user_count == 1
#     assert saved_user.username == username
