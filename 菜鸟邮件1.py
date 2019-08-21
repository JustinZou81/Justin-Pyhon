#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-24 13:19:45
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage


#第三方SMTP服务
mail_host='smtp.qq.com'    #设置服务器
mail_user='190399374@qq.com'  #用户名
mail_pass='edcpupwexmkkbjgf'   #口令

sender='190399374@qq.com'
receivers='Justin.Zou@smartrac-group.com'

def sendEmail():
	#三个参数：第一个为文本内容，第二个Plain设置文本格式，第三个utf-8设置编码
	message=MIMEText('Python邮件发送测试。。。','plain','utf-8')
	message['From']=Header("菜鸟教程",'utf-8')
	message['To']=Header('测试','utf-8')
	subject='Python SMTP邮件测试'
	message['Subject']=Header(subject,'utf-8')

	try:
		smtpObj=smtplib.SMTP()
		smtpObj.connect(mail_host,25)
		# smtpObj=smtplib.SMTP_SSL(mail_host)
		smtpObj.login(mail_user,mail_pass)
		smtpObj.sendmail(sender,receivers,message.as_string())  #发送
		print("邮件发送成功")

	except smtplib.SMTPException:
		print("Error:无法发送邮件")

# def send_email2(SMTP_host,from_account,from_passwd,to_account,subject,content):
# 	email_client=smtplib.SMTP(SMTP_host)
# 	email_client.login(from_account,from_passwd)
# 	#create msg
# 	msg=MIMEText(content,'plain','utf-8')
# 	msg['Subject']=Header(subject,'utf-8') #subject
# 	msg['from']=from_account
# 	msg['To']=to_account
# 	email_client.sendmail(from_account,to_account,msg.as_string())
# 	email_client.quit()

if __name__=='__main__':
	sendEmail()
	#receiver='***'
	#send_email2(mail_host,mail_user,mail_pass,receiver,title,content)