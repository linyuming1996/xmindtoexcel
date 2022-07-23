import time
from datetime import datetime
from functools import wraps
def timestamp():
    """时间戳"""
    return time.time()
def dt_strtime(fmt="%Y%m%d"):
    """datetime格式化
    :param fmt "%Y%m%d %H%M%S
    """
    return datetime.now().strftime(fmt)
def sleep(second=1.0):
    """睡眠时间"""
    return time.sleep(second)
def running_time(func):
    """函数运行时间"""
    @wraps(func)
    def wrapper(*args,**kwargs):
        starttime = timestamp()
        restime = func(*args,**kwargs)
        print('校验元素done用时%.3秒' %(timestamp()-starttime))
        return restime
    return wrapper()
if __name__ == '__main__':
    print(timestamp())
    print(dt_strtime('%Y%m%d%H%M%S'))