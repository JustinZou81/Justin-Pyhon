#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-16 10:49:07
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$

import pytesseract
from sys import argv
from PIL import Image
import re

script,filename=argv

if __name__=='__main__':
	text=pytesseract.image_to_string(Image.open('64541.png'),lang='eng')
	# print(text)
	file= open(filename,'w')
	file.write(text)
	print(text)
	file=open(filename,'r')
	# buff=file.read()
	# # print(buff)
	# # lines=file.readlines()
	# for lines in file.readlines():
	# 	if 'Vendor' in file:
	# 		print('lines')
	# 	else:
	# 		print('ok')
# w1='vendor'
# w2='Vendor: NXP'
for lines in file.readlines():
	# print(lines)

	matchObj = re.match( r'(.*) batch: (.*?) .*', lines, re.M|re.I)
	if matchObj:
			print ("matchObj.group() : ", matchObj.group())
			print ("matchObj.group(1) : ", matchObj.group(1))
			print ("matchObj.group(2) : ", matchObj.group(2))
			file1=open('sn.txt','w')
			file1.write(matchObj.group(2))
	else:
			print ("No match!!")



# file=open(filename,'r')
# buff=file.read()
# p=r"batch"
# for t in re.match(p,buff)
# 	# file.write(t)
# 	print(t)
# pat=re.compile(w1+'*:?'+w2,re.split)
# result=pat.findall(buff)
# print(result)


# dataMat=[]
# # res=[]
# for line in file.readlines():
# 	# if V=="Vendor batch":
# 	curline=line.strip().split("\n")
# 	# floatLine = map(float,curline)
# 	a='vendor batch'
# 	b=a[2:3]
# 	dataMat.append(b)
# 	print(dataMat)

# l=len(dataMat(x))
# zip_list=zip(*range(1),x)
# id1=[z[0] for i,z in ]
# 	# labelMat.append(line[-1])

# # print('labelMat:',labelMat)
# id1=[i for i,x in enumerate(x) if x=1]
# def find(dataMat):
# 	for list0 in dataMat:
# 		if list0.find('Verdor') in dataMat:
# 			if list0.find('Vendor') in dataMat:
# 				print("vendor")
# 			else:
# 				return 0 #有一行不带#号的set internet Active，那么返回0
# 				return -1 #若没有不带号的set internet Active，那么返回-1
# if __name__=='__main':
# 	# lists = dataMat #lists 是从文件中读出内容的列表
# 	findout=find(dataMat) #调用函数
# 	print(findout)