import pytest
# 3、pytest 断言
# pytest里面的断言方法就只有一个
# assert 表达式
def add(x, y):
    return x+y
class TestADD:  # 定义的类名必须是以Test开头
    def test_add_01(self):  # 定义的测试方法必须是以test
# 开头
        result = add(1, 2)
        print(result)
    def test_add_02(self):
        result = add(2, 2)
        print(result)
if __name__ == '__main__':
    pytest.main(["-s","pytest.py"])