
import smtplib                          #邮箱库
from email.mime.text import MIMEText    #邮件文本
from email.header import Header         #邮件头

smtp_obj = smtplib.SMTP("smtp.qq.com")                  #设置邮箱服务器
smtp_obj.login("123@qq.com", "授权码")                  #登录邮箱
msg_body = MIMEText("测试邮件", "html", "utf-8")        #邮件内容
msg_body["From"] = Header("jjj", "utf-8")               #设置邮件头：发送者
msg_body["Subject"] = Header("测试", "utf-8")           #设置邮件头：主题
smtp_obj.sendmail("123@qq.com", ["456@163.com"], msg_body.as_string())   #发送邮件

 