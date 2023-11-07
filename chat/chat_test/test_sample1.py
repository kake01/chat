import pytest
"""
ステップ_4
「pytest chat/chat_test/test_sample1.py -s」でこのテストファイルが実行されることを確認
テストケースのパターンをすべて実行したいその場合はどうするか
=> テストケースを辞書として実行する
chat\test_img\sample1\テストパターンの列挙.PNGを参照

    https://stackoverflow.com/questions/48192234/pytest-mark-parametrize-with-django-test-simpletestcase
"""


@pytest.mark.parametrize("x, y, want", [(1, 2, 3), (3, 4, 7), (4, 5, 9)])
def test(x, y, want):
    print(x, y, want)
    assert want == x + y
