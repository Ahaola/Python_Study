from time import sleep
#创建测试用例，以test_开头的函数 或者 以Test开头的类
def test_xiao(): #测试用例
    assert "xiaolang" == "xiaolang"   #测试用例中必须要有断言

class TestDemo:
    def test_a(self,driver):#测试用例
        sleep(2)

    def test_b(self,driver):#测试用例
        sleep(2)

