from poium import Page,Element,Elements
class BaiduPage(Page):
    searchinput = Element(id_='kw',describe='百度搜索框',timeout=5)
    searchbutton = Element(xpath='//*[@id="su"]',describe='搜索按键',timeout=5)
    Emaillink = Element(xpath='//*[@id="1"]/h3/a[1]/em',describe='系统链接',timeout=5)
class EmailPage(Page):
    Emailuser = Element(id_='emp_DomainName',describe='用户名',timeout=5)
    Emailpassword = Element(id_='emp_Password',describe='用户密码',timeout=5)
    Emaillogin = Element(id_='BtnLogin',describe='登录')