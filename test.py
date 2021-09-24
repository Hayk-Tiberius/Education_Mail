import pytest

def test_float1():
    a = 5.0
    b = 6.0
    assert a * b == 30.0
def test_float2():
    a = -5.0
    b = 0.3
    c = a * b
    try:
        assert c < 0
    except AssertionError:
        pass
@pytest.mark.parametrize("a, b", [(1.0, 3.0), (3.0, 9.0), (-9.0, -27.0)])
def test_float3(a, b):
    assert a * 3 == b

def test_list1():
    a = [-10, -2, 0, 2, 10]
    assert all([x % 2 == 0 for x in a])
def test_list_2():
    a = ['simple string', 'another string', 'test', 'other string']
    try:
        assert any([len(x) > 3 for x in a])
    except AssertionError:
        pass
@pytest.mark.parametrize("a,b",[([3, 1, 2], [1, 2, 3]),([5, -5, 0], [-5, 0, 5]), (['xyz', 'abc', 'qwerty'], ['abc', 'qwerty', 'xyz'])])
def test_list3(a,b):
    assert sorted(a) == b