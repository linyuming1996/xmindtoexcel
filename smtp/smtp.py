import smtplib
from email.mime.text import MIMEText
from email.header import Header

# emails name and pwd
sender = "linyuming@wps.cn"
password = "huawei@1234"
# 收件人
receiver = ['linyuming@wps.cn', ]
# malcontent
message = MIMEText('user python send a email', 'palin', 'utf-8')
# 发件人显式姓名
message['From'] = Header('python邮件', "utf-8")
# 收件人显式姓名
message['To'] = Header("邮件", "utf-8")
