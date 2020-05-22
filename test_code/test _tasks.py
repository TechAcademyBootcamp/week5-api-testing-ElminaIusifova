from test_add_simple.taskone import add
from pytest_simple.taskthree import divide
from api_test_hard.main import magic
import requests


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

def test_magic1():
    name = {"full_name": "Idris Shabanli", id:	int, "created_at": "($date-time)", "updated_at": "($date-time)" }
    fullName = requests.post("http://35.225.243.133/bloggers/", name)
    assert fullName.status_code == 201



def test_magic2():
    name = {"full_name": "abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd "}
    fullName = requests.post("http://35.225.243.133/bloggers/", name )
    assert fullName.status_code == 400


def test_magic3():
    name = {"full_name": ""}
    fullName = requests.post("http://35.225.243.133/bloggers/", name )
    assert fullName.status_code == 400

def test_magic4():
    name = {"id": 1223}
    fullName = requests.post("http://35.225.243.133/bloggers/", name)
    assert fullName.status_code == 400