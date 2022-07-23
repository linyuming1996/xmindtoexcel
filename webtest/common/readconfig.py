import configparser
from config.conf import conf

HOST ='HOST'


class Readconfig:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read(conf.inf_file,encoding='utf-8')

    def getconfig(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def setconfig(self, section,option,value=None):
        """更新。。。给定的option设定值"""
        self.config.set(section, option, value)
        with open(conf.inf_file, 'w') as configfile:
            self.config.write(configfile)

    @property
    def url(self):
        """获取url"""
        return self.getconfig('HOST', 'HOST')

    @property
    def drivertype(self):
        """获取浏览器类型"""
        return self.getconfig('DriverType', 'DriverType')

    @property
    def emailname(self):
        """获取浏览器类型"""
        return self.getconfig('Email', 'username')

    @property
    def emailpassword(self):
        """获取浏览器类型"""
        return self.getconfig('Email', 'password')

    @property
    def SearchKey(self):
        """搜索关键字"""
        return  self.getconfig('SearchKey','SearchKey')


configini = Readconfig()

if __name__ == '__main__':
    print(configini.url)
    print(configini.drivertype)
    print(configini.SearchKey)
    # configini.setconfig('USER','XINGBIE','nan1')
    # print(configini.getconfig('USER','XINGBIE'))



