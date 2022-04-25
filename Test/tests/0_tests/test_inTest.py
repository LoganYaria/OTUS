def test_1():
    assert "Test" == "test", "Строки не равны"


def test_2():
    #print("I am test 2")
    assert 2+2==4



def test_3():
    assert 0

class TestClass:
    def test_1(self):
        list_to_test_1=[]
        list_to_test_2=[]
        assert list_to_test_1 is list_to_test_2 ,"Два пустых массива?"
    def test_2(self):
        assert 1==1