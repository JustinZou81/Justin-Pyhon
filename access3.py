#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-06 19:46:47
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$

import win32com.client

conn=win32com.client.Dispatch(r'ADODB.Connection')
DSN='PROVIDER=Microsoft.ACE.OLEDB.12.0;DATA SOURCE=C:/Users/justin.zou/Documents/GitHub/Justin-Pyhon/Serial.accdb;'
conn.Open(DSN)

rs=win32com.client.Dispatch(r'ADODB.Recordset')
#rs_name='Serial'
rs.Open('SELECT*FROM Serial',conn,1,3)

rs.AddNew()#添加一条新记录
rs.Fields.Item(0).value='fields_dict'
rs.Update() #更新

# fields_dict = {'curSerial':10039390,'curDate':'2019/5/9 8:36:01','curUser':'罗','last9Date':'5/9 8:35:33','last9User':'罗'}
# for x in range(rs.Fields.Count):
# 	fields_dict[x]=rs.Fields.Item(x).Name
# 	# rs.AddNew()#添加一条新记录
# 	# rs.Fields.Item(x).value=fields_dict
# 	# rs.Update() #更新
# 	print(fields_dict[x], rs.Fields.Item(x).Value)#新记录的第一个记录为"data"
	

