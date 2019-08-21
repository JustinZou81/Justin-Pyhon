#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-07 15:09:13
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$

from urllib import request,error
try:
	response=request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
	print(e.reason,e.code,e.headers,sep='\n')
except error.URLError as e:
	pring(e.reason)
else:
	print('Request Successfully')
