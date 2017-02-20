#!/usr/bin/python
# -*- coding: UTF-8 -*-
#https://segmentfault.com/q/1010000007162074/a-1020000007602959
#136授权码y1990724
#1.163的SMTP必须打开，记住授权密码
#2. 不能给ＱＱ邮箱发送
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sendEmail():
    # 设置服务器所需信息
    # 163邮箱服务器地址
    mail_host = 'smtp.163.com'
    # 163用户名
    mail_user = 'ymq655'
    # 密码
    mail_pass = 'y1990724' ##'你的客户端授权密码' NOT 邮箱密码
    # 邮件发送方邮箱地址
    sender = 'ymq655@163.com'
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ['ymq655@126.com']

    # 设置email信息
    # 邮件内容设置
    message = MIMEText('content', 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = 'title'
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(mail_host, 25)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误



if __name__ == '__main__':

    sendEmail()
