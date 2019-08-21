#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-13 14:07:12
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$

import sys
import time
import urllib
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf-8')

def main():
	#用chrome driver打开页面
	driver=webdriver.Chrome()
	driver.get("https://www.zhihu.com/question/") #website base on yourself
#用driver进行点击操作并模拟点击查看更多

def execute_times(times):
	for i in range(times+1):
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
		time.sleep(2)
		try:
			driver.find_element_by_css_selector('button.QuestionMainAction').clock()
			print("page"+str(i))
			time.sleep(1)
		except:
			break
execute_times(3) #打开三个页面

#结构化HTML文件并用beautifulsoup解析
result_raw=driver.page_source
result_soup=BeautifulSoup(result_raw,'html.parser')
result_bf=result_soup.prettify()

#找到所有图片
with open("D:\\imaine\\raw_result.txt",'w') as girls:
	girls.write(result_bf)
girls.close()
print("Store raw data successfully!!!")

#找到所有<nonscript>标签并记录下来
with open("D:\\imaine\\raw_result.txt",'w') as noscript_meta:
	noscript_nodes=result_soup.find_all('noscript')
	noscript_inner_all=""
	for noscript in noscript_nodes:
		noscript_inner=noscript.get_text()
		noscript_inner_all+=noscript_inner+"\n"

	h=HTMLParser()
	noscript_all=h.unescape(noscript_inner_all)
	noscript_meta.write(noscript_all)
noscript_meta.close()
print("Store noscript meta data successfully!!!")  #成功找到图片


#开始下载图片
img_soup=BeautifulSoup(noscript_all,'html.parser')
img_nodes=img_soup.find_all('img')
with open ("D:\\imagine\\img_meta.txt", 'w') as img_meta:
	count=0
	for img in img_nodes:
		if img.get('src') is not None:
			img_url=img.get('src')
			line=src(count)+'\t'+img_url+"\n"
			img_meta.write(line)
			urllib.urlretrieve(img_url,"D:\\imagine\\"+str(count)+".jpg")#下载图片
			count+=1

	img_meta.close()
	print("Stroe meta data and images successfully!!!") #成功存储图片

if __name__=="__main__":
	main()