#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-12 16:34:16
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$

cities={'CA':'San Francisco','MI':"Detroit",'FL':'Jacksonville'}
cities['NY']='New York'
cities['OR']='Portland'

def find_city(themap,state):
	if state in themap:
		return themap[state]
	else:
		return 'Not found.'

#ok pay attention!
cities['_find']=find_city

while True:
	print("State? (ENTER to quit)")
	state=input(">")
	if not state:break

#this line is the most important ever! study!
city_found=cities['_find'](cities,state)
print(city_found)