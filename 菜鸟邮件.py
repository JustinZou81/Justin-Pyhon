#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-24 12:41:08
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender='Justin.Zou@smartrac-group.com'
receivers='frank.luo@smartrac-group.com'

#三个参数：第一个为文本内容，第二个Plain设置文本格式，第三个utf-8设置编码
message=MIMEText('Python邮件发送测试。。。','plain','utf-8')
message['From']=Header("菜鸟教程",'utf-8')
message['To']=Header('测试','utf-8')

subject='Python SMTP邮件测试'
message['Subject']=Header(subject,'utf-8')

try:
	smtpObj=smtplib.SMTP('localhost')
	smtpObj.sendmail(sender,receivers,message.as_string())
	print("邮件发送成功")
except smtplib.SMTPException:
	print("Error:无法发送邮件")