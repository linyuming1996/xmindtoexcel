import logging
from config.conf import conf


class Logs:
    def __init__(self):
        self.logger = logging.getLogger()
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)
            #创建一个handle写入文件
            fh = logging.FileHandler(conf.log_file, encoding='utf-8')
            fh.setLevel(logging.INFO)
            #创建一个handle写入控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            formatter = logging.Formatter(self.cmf)
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    @property
    def cmf(self):
        return '%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'


log = Logs().logger

if __name__ == '__main__':
    log.info("hello world")