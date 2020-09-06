import pytest


class A(object):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value


class B(object):
    def __init__(self):
        self._dic = {"key1":1, "key2":2}

    @property
    def dic(self):
        return self._dic

    def dic(self, name):
        return self._dic.get(name)


def test_Aクラスで属性を参照する():
    assert A(123).value == 123


def test_Aクラスで属性のタイプは整数である():
    assert isinstance(A(123).value, int)


def test_Aクラスで属性の設定はできない():
    obj = A(123)
    with pytest.raises(AttributeError):
        obj.value = 234


def test_Bクラスで属性を参照する():
    assert B().dic == {"key1":1, "key2":2}


def test_Bクラスで属性は辞書である():
    print(type(B().dic))
    assert isinstance(B().dic, dict)


def test_Bクラスで属性の設定はできない():
    obj = B()
    with pytest.raises(AttributeError):
        obj.dic = {"key3":3}


def test_listsを参照する():
    o = C()
    assert o.lists == [10,20,30]


def test_listsの要素を限定する条件を与える():
    o = C()
    assert o.lists(index=1) == 10
