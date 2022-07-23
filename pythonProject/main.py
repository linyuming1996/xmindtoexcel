import os
''''*args的用法：当传入的参数个数未知，且不需需要知道参数名称时'''
# def func_c(a,*args):
#     print('这个参数是:%s' %a)
#     for b in args:
#         print('another arg:{}'.format(b))
# func_c(1,'linyuming','nan','25')
# print('------')
import datetime

'''**args的用法：当传入的参数个数未知，但需要知道的参数的名称时'''
# def func(*args,**kwargs):
#     for arg in args:
#         print('这是传入的参数arg：%s' %arg)
#     for kwarg in kwargs:
#         print('这是传入的参数kwarg:{}'.format(kwarg))
# if __name__ == '__main__':
#     func('1','2','3',xingbian='nan',aihao='nv',a='1')

'''%.3f输出浮点数后的3位小数'''
# print("校验元素done！用时%.3f秒！" %3.1234567)
# 校验元素done！用时3.123秒！

'''os.path
    os.abspath
'''
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.dirname(__file__)))
# print(os.path.abspath(__file__))
# print(BASE_DIR)
# os.path.dirname(__file__)获取文件所在目录的完整路径：os.path.dirname(__file__)
# os.path.abspath(__file__)os.path.abspath(__file__)返回的是.py文件的绝对路径