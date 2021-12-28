import pytest
from app.py import add

class TestClass:
    def Test_One(self):
        x = 'Suryawanshi'
        assert 'r' in x

    @pytest.mark.one
    def Test_Two(self):
        x = "Hello"
        assert hasattr(x, "check")

    def fun(x):
        return x + 5

    @pytest.mark.one
    def test_method(self):
        assert self.fun(3) == 5

    @pytest.mark.two
    def test_method1(self):
        x = 5
        y = 10
        assert x == y

    def test_method2():
        a = 16
        b = 20
        assert a + 4 == b

    def uname(name):
        if name == "mangesh":
            return True

    @pytest.mark.one
    def test_uname(self):
        assert TestClass.uname("mangesh") == True
        
    def test_add():
        assert add(3, 2) == 5
    
    def test_multiply():
        assert multiply(3, 2) == 6
