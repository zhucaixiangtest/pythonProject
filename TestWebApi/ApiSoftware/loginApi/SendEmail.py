# coding:utf-8

import smtplib
from email.mime.text import MIMEText


class SendEmail():



    def  sendEmailForUsr(self,vercode,username_recvs):
        self.mailserver = "smtp.mxhichina.com"  # 邮箱服务器地址
        self.username_send = 'admin@zcx-t.top'  # 邮箱用户名
        self.password = '031230Zcx'   # 邮箱密码
        self.username_recv = username_recvs

        self.mail = MIMEText("您正在注册自动化平台,验证码是: "+vercode+"  如果您未注册此平台，请忽略。")  # 邮件内容
        self.mail['Subject'] = 'ApiSoftware自动化平台--验证码邮件'   # 邮件主题


        self.mail['From'] = self.username_send  # 发件人
        self.mail['To'] = self.username_recv  # 收件人；[]里的三个是固定写法，别问为什么，我只是代码的搬运工
        smtp = smtplib.SMTP(self.mailserver, port=25)  # 连接邮箱服务器，smtp的端口号是25
        # smtp=smtplib.SMTP_SSL('smtp.qq.com',port=465) #QQ邮箱的服务器和端口号
        smtp.login(self.username_send, self.password)  # 登录邮箱
        smtp.sendmail(self.username_send, self.username_recv, self.mail.as_string())  # 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
        smtp.quit()  # 发送完毕后退出smtp
        # print ('success')
        return True



