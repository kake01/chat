import pytest
from django.urls import reverse

# from .models import Message
# from .views import MessageView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
"""
ステップ_5
実際にchatアプリケーションのテストコードを書いていく_1
chatアプリケーションで使用しているmodelsのテストを行うプログラムを書いてみる

Django userモデルとは?
非推奨であるが今回は外部主キーがあるモデルのテストのために利用
参考: https://qiita.com/iwatsukayura/items/5f3ceb173dc151c0488b
"""

# @pytest.mark.django_db
# def test_is_one_message():
#     username = "testuser"
#     password = "testpassword"

#     User.objects.create_user(username=username, password=password)
#     saved_user = User.objects.all()[0]
#     saved_user_count = User.objects.all().count()

#     assert saved_user_count == 1
#     assert saved_user.username == username
#     assert check_password(password, saved_user.password)

# content = "content内容"
# respond = "respond内容"
# test_message = MessageView.create_message(user, content, respond)
# saved_messages = Message.objects.all()

# assert actual_message.owner == user

# def setUp(self):
#     # テストユーザーを作成し、ログインする
#     self.username = "testuser"
#     self.password = "testpassword"
#     self.user = User.objects.create_user(username=self.username,
#                                          password=self.password)

# class MessageModeTests(TestCase):
#     def setUp(self):
#         # テストユーザーを作成し、ログインする
#         self.username = "testuser"
#         self.password = "testpassword"
#         self.user = User.objects.create_user(username=self.username,
#                                              password=self.password)

#     def test_save_user(self):
#         saved_user = User.objects.all()
#         self.assertEqual(saved_user.count(), 1)

#     def test_is_none(self):
#         """初期状態では何も登録されていないことをチェック"""
#         saved_message = Message.objects.all()
#         self.assertEqual(saved_message.count(), 0)

#     def test_is_one_message(self):
#         content = "content内容"
#         respond = "respond内容"
#         test_message = MessageView.create_message(self.user, content, respond)

#         saved_messages = Message.objects.all()
#         actual_message = saved_messages[0]

#         self.assertEqual(actual_message.owner, self.user)
#         self.assertEqual(actual_message.owner.username, self.user.username)
#         self.assertEqual(actual_message.owner.password, self.user.password)
#         self.assertEqual(actual_message.content, content)
#         self.assertEqual(actual_message.respond, respond)
#         self.assertEqual(saved_messages.count(), 1)

#     def setUp(self):
#         # テストユーザーを作成し、ログインする
#         self.username = "testuser"
#         self.password = "testpassword"
#         self.user = User.objects.create_user(username=self.username,
#                                              password=self.password)

# assertEqual(actual_message.owner.username, user.username)
# assertEqual(actual_message.owner.password, user.password)
# assertEqual(actual_message.content, content)
# assertEqual(actual_message.respond, respond)
# assertEqual(saved_messages.count(), 1)

# saved_messages = Message.objects.all()
# actual_message = saved_messages[0]

# self.assertEqual(actual_message.owner, self.user)
# self.assertEqual(actual_message.owner.username, self.user.username)
# self.assertEqual(actual_message.owner.password, self.user.password)
# self.assertEqual(actual_message.content, content)
# self.assertEqual(actual_message.respond, respond)
# self.assertEqual(saved_messages.count(), 1)

# params = {"normal 1": (1, 2, 3), "normal 2": (3, 4, 7)}
# print("ここ")
# print(list(params.values()))
# print(list(params.keys()))

# @pytest.mark.django_db
# class MessageModeTests(TestCase):
#     @pytest.mark.parametrize("param", ["a", "b"])
#     def setUp(self):
#         # テストユーザーを作成し、ログインする
#         self.username = "testuser"
#         self.password = "testpassword"
#         self.user = User.objects.create_user(username=self.username,
#                                              password=self.password)

#     def test_save_user(self):
#         saved_user = User.objects.all()
#         self.assertEqual(saved_user.count(), 1)

#     def test_is_none(self):
#         """初期状態では何も登録されていないことをチェック"""
#         saved_message = Message.objects.all()
#         self.assertEqual(saved_message.count(), 0)

#     def test_is_one_message(self):
#         content = "content内容"
#         respond = "respond内容"
#         test_message = MessageView.create_message(self.user, content, respond)

#         saved_messages = Message.objects.all()
#         actual_message = saved_messages[0]

#         self.assertEqual(actual_message.owner, self.user)
#         self.assertEqual(actual_message.owner.username, self.user.username)
#         self.assertEqual(actual_message.owner.password, self.user.password)
#         self.assertEqual(actual_message.content, content)
#         self.assertEqual(actual_message.respond, respond)
#         self.assertEqual(saved_messages.count(), 1)

# class ChatBotMessageViewTest(TestCase):
#     """IndexViewのテストクラス"""

#     def setUp(self):
#         # MessageView.test('ここ来ます')
#         # テストユーザーを作成し、ログインする
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.client.login(username='testuser', password='testpassword')

#     def test_get(self):
#         # """GET メソッドでアクセスしてステータスコード200を返されることを確認"""
#         # """
#         # ※補足
#         # reverse('chat:chat_bot_message') ==>urlsのapp_name:pathのnameのurlにアクセスする
#         # """
#         response = self.client.get(reverse('chat:chat_bot_message'))
#         self.assertEqual(response.status_code, 200)
