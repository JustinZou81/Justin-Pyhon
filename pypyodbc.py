#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-05 12:54:56
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$

__author__='mayi'

#导入模块
import pypyodbc

#建立数据库连接
def mdb_conn(db_name,password=""):
	"""
	功能：创建数据库连接
	：param db_name:数据库名称
	：param db_name:数据库密码，默认为空
	：return：返回数据库连接

	[description]
	
	Arguments:
		db_name {[type]} -- [description]
	
	Keyword Arguments:
		password {str} -- [description] (default: {""})
	"""
	str='Driver={Mircrosoft Access Driver(*.mdb)};PWD'+password+";DBQ="+db_name
	conn=pypyodbc.win_connect_mdb(str)

	return conn

#创建游标
cur=conn.cursor()

#增
def mdb_add(conn,cur,sql):
	"""
	功能：向数据库删除数据
	：param conn:数据库连接
	：param cur:游标
	：param sql:sql语句
	：return:sql语句是否执行成功
	[summary]
	
	[description]
	
	Arguments:
		conn {[type]} -- [description]
		cur {[type]} -- [description]
		sql {[type]} -- [description]
	"""
	try:
		cur.execute(sql)
		conn.commit()
		return True
	except:
		return False

#删
def mdb_del(conn,cur,sql):
	"""
	功能：向数据库删除数据
	：param conn:数据库连接
	：param cur:游标
	：param sql:sql语句
	：return:sql语句是否执行成功
	[summary]
	
	[description]
	
	Arguments:
		conn {[type]} -- [description]
		cur {[type]} -- [description]
		sql {[type]} -- [description]
	"""
	try:
		cur.execute(sql)
		conn.commit()
		return True
	except:
		return False

#改
def mdb_ modi(conn,cur,sql):
	"""
	功能：向数据库删除数据
	：param conn:数据库连接
	：param cur:游标
	：param sql:sql语句
	：return:sql语句是否执行成功
	[summary]
	
	[description]
	
	Arguments:
		conn {[type]} -- [description]
		cur {[type]} -- [description]
		sql {[type]} -- [description]
	"""
	try:
		cur.execute(sql)
		conn.commit()
		return True
	except:
		return False

#查
def mdb_sel(conn,cur,sql):
	"""
	功能：向数据库删除数据
	：param conn:数据库连接
	：param cur:游标
	：param sql:sql语句
	：return:sql语句是否执行成功
	[summary]
	
	[description]
	
	Arguments:
		conn {[type]} -- [description]
		cur {[type]} -- [description]
		sql {[type]} -- [description]
	"""
	try:
		cur.execute(sql)
		conn.commit()
		return True
	except:
		return False

#关闭游标
cur.close()
#关闭数据库连接
conn.close()
