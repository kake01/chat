import pytest
"""
ステップ_1
    「pytest chat/chat_test/test_sample1.py -s」でこのテストファイルが実行されることを確認
    「 -s」　-sとはprint文を表示させるオプション
        参考: https://syachiku.net/pytest-option/#toc8
        
    何故 print文 動かない, 動かないは実行されない?
        =>testで始まる名前の関数が自動的にテスト対象となる
        参考: https://qiita.com/everylittle/items/1a2748e443d8282c94b2
"""


def none_sample1():
    print("このテストプログラムは動かない")
    a = 1
    b = 1
    assert a == b


def none_sample2_test():
    print("このテストプログラムは動かない")
    a = 1
    b = 1
    assert a == b


def test_sample2():
    print("testから始まっているので動く")
    a = 1
    b = 1
    assert a == b
