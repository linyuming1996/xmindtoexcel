import logging
import datetime
import os.path
import time
#第一步創建一個logger
def log():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)#LOG等級縂開關
    #第二步，創建一個handler，用於寫入日志文件
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))#trftime( )函数：实现本地时间\日期的格式化
    log_path =os.path.dirname(os.getcwd())
    log_name = log_path + rq + '.log'
    logfile = log_name
    #print(logfile)
    #創建一個handler用於寫入日志
    File_handler = logging.FileHandler(mode='w', encoding='utf-8', filename=logfile)
    #創建一個hangler用於輸出日志到控制臺
    Console_handler = logging.StreamHandler()
    #用於寫到file的等級開關
    File_handler.setLevel(logging.DEBUG)
    Console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    File_handler.setFormatter(formatter)
    Console_handler.setFormatter(formatter)
    #第四步，將logger添加到handler裏面
    logger.addHandler(File_handler)
    logger.addHandler(Console_handler)
    return logger
#级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
# def debuglog(message):
#     logger.debug(message)
# def infolog(message):
#     logger.info(message)
# def warninglog(message):
#     logger.warning(message)
# def errorlog(message):
#     logger.error(message)
# def riticallog(message):
#     logger.critical(message)


