import pytest
"""
ステップ_3
    「pytest chat/chat_test/test_sample0.py -s」でこのテストファイルが実行されることを確認
    chat\test_img\sample0\実行されないテストメソッド.PNGを参照
    「 -s」　-sとはprint文を表示させるオプション
        参考: https://syachiku.net/pytest-option/#toc8
        
    chat\chat_test\test_sample0.py 動く1が出ること確認
    何故 print文 動かない, 動かないは実行されない?
        =>testで始まる名前の関数が自動的にテスト対象となる
        参考: https://qiita.com/everylittle/items/1a2748e443d8282c94b2
"""


def none_sample1():
    print("動かない")
    a = 1
    b = 1
    assert a == b


def none_sample2_test():
    print("動かない2")
    a = 1
    b = 1
    assert a == b


def test_sample2():
    print("動く1")
    a = 1
    b = 1
    assert a == b
