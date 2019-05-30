#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-05 12:22:59
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$


import win32com.client

#建立数据库连接
conn=win32com.client.Dispatch(r".Connection")
#DSN='PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE =%s'%(mdb_file)  #对于mdb的文件就要用.Jet。
#对于accdb文件就要用.ACEAC  Microsoft.Jet.OLEDB.4.0 is not supported for 64-bit OS
DSN='Provider=Microsoft.ACE.OLEDB.12.0;Data Source=//cngz-s-fp01\Prodatabase$\IT_Report_Test\Serial.accdb;'
conn.Open(DSN)

#打开一个记录集
rs=win32com.client.Dispatch(r'ADODB.Recordset')
rs_name="Scrap_Apply"
rs.open('['+rs_name+']',conn,1,3)

#对记录集操作
rs.AddNew()#添加一条新记录
rs.Fields.Item(0).value='data'  #新记录的第一个记录为"data"
rs.Update() #更新

#用SQL语句来增，删，改数据
#增
sql="Insert Into[rs_name](id,innerserial,mid) Values('002133800088980002', 2, '21338')" #sql语句
conn.Execute(sql) #执行sql语句
# 删
sql = "Delete * FROM " + rs_name + " where innerserial = 2"
conn.Execute(sql)
# 改
sql = "Update " + rs_name + " Set mid = 2016 where innerserial = 3"
conn.Execute(sql)

#遍历记录
rs.MoveFirst()#光标移到首条记录
count=0
while True:
	if rs.EOF:
		break
	else:
		for i in range(rs.Fields.Count):
			#字段名：字段内容
			print(rs.Fields[i].Name,':',rs.Fields[i].Value)
		count+=1
		rs.MoveNext()

#