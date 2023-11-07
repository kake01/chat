from django.db import models
from django.utils import timezone  # django で日付を管理するためのモジュール


# class Post(models.Model):
#     fromAdre = models.CharField('送り者メールアドレス', max_length=100)
#     toAdre = models.CharField('送り先メールアドレス', max_length=100)
#     title = models.CharField('タイトル', max_length=200)
#     text = models.TextField('本文')
#     date = models.DateTimeField('日付', default=timezone.now)

#     def __str__(self):  # Post モデルが直接呼び出された時に返す値を定義
#         return self.title  # 記事タイトルを返す
