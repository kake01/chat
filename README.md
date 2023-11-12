# このアプリケーションはlineのりんなをイメージとしてchatボットがオウム返しする機能を提供しています。
![パクリ元](README_img/パクリ元アプリケーション.jpg)
![実際のアプリケーションイメージ](README_img/オウム返し.jpg)
## testコードは「chat」アプリケーションで実装しています。
### テストコードは「chat」アプリケーションのtest.pyをご覧ください。
### 実際にアプリケーションを触ってどんなテストが必要かイメージしながら触って見てください。

# pytestを行う前に行うこと
1. conda create -n 環境名
    * 仮想環境を作成
2. activate 仮想環境名
    * activate化する
3. pip install -r requirements.txt
    * pi listを行い「pytest - django がインストールされていることを確認
4. postgreSQLの設定を行う
* ![postgreSQLの設定](README_img/postgresql.PNG)
* * データベース名: chatapp
* * スキーマ名: app
* * python manage.py migrateを実行しデータベース「chatapp」のスキーマ「app」にテーブルが作成されていることを確認
5. chatbot2/settings.pyと同階層にtest_settings.pyファイルがあることを確認
* ここでsetting.pyとteset_settingファイルの違いは?
* * => データベースの接続先をpostgresqlかmemoryにするかの差分
* ![setting差分](README_img/setting差分.PNG)
6. manage.py と同階層に「pytest.ini」ファイルがあること
```
    [pytest]
    DJANGO*SETTINGS_MODULE = chatBot2.test_settings
    python_files = test*\*.py
```
* 少し解説
* * DJANGO\*SETTINGS_MODULE = chatBot2.test_settings
* * * 本番時のDBとは別のDBでテストしたい(まっさらなDB（サンドボックス）)ため
* * python_files = test_*.py
* * * test_と命名されているファイルのみをpytestのコマンドを実行したときにテストファイルとしてみなすように設定
* * * 参考: https://self-methods.com/django-pytest-basic/#index_id3
7. 事前準備が完了