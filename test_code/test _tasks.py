from 01_test_add_simple.taskone import add
from 03_pytest_simple.taskthree import divide

def test_divide1():
    arg1=3
    arg2=2
    expected = 1.5
    assert divide(arg1, arg2) == expected
    pass

def test_divide2():
    arg1=4
    arg2=2
    expected = 2.0
    assert divide(arg1, arg2) == expected

    pass

def test_divide3():
    arg1 = 10
    arg2 = 0
    expected = "You cannot divide 0!"
    assert divide(arg1, arg2) == expected

    pass

def test_add1():
    num1 = 1
    expected = 2
    assert add(num1) == expected

def test_add2():
    num1 = -1
    expected = 0
    assert add(num1) == expected
