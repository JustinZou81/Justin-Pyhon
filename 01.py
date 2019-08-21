#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-07 15:14:32
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$

# import socket
# import urllib.request
# import urllib.error

# try:
# 	response=urllib.request.urlopen('https://baidu.com',timeout=0.01)
# except urllib.error.URLError as e:
# 	print(type(e.reason))
# 	if isinstance(e.reason,socket.timeout):
# 		print("TIME OUT")



# from urllib.parse import urlparse
# result=urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(result)

# from urllib.parse import urlparse

# result=urlparse('http://www.baiud.com/index.html#comment',allow_fragments=False)
# print(result.scheme,result[0],result.netloc,result[1],sep='\n')


# from urllib.parse import urlunparse
# data=['http','www.baidu.com','index.html','user','a=6','comment']
# print(urlunparse(data))

# from urllib.parse import urlsplit
# result=urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
# print(result.scheme,result[3])

# import urllib.parse
# import urllib.request

# data=bytes(urllib.parse.urlencode({'word':"Hello"}),encoding='utf8')
# response=urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())


# import urllib.request

# response=urllib.request.urlopen('http://httpbin.org/get',timeout=1)
# print(response.read())

# import socket
# import urllib.request

# import urllib.error

# try:
# 	response=urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
# 	if isinstance(e.reason,socket.timeout):
# 		print('TIMEOUT')


# import requests
# headers={'Referer':'https://www.jianshu.com/',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}

# r=requests.get('http://www.jianshu.com',headers=headers)
# print(r)
# print(type(r.status_code),r.status_code)
# print(type(r.headers),r.headers)
# print(type(r.cookies),r.cookies)
# print(type(r.url),r.url)
# print(type(r.history),r.history)

# import requests

# headers={'Referer':'https://www.jianshu.com/',
#           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}
# r=requests.get('http://www.jianshu.com',headers=headers)
# exit() if not r.status_code==requests.codes.ok else print('Request Successfully')


#读取ico文件并写入本地盘

# import requests

# headers={'Referer':'https://github.com/favicon.ico',
#          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}

# r=requests.get("https://github.com/favicon.ico",headers=headers)
# print(r)
# with open('favicon.ico','wb') as f:
# 	f.write(r.content)


#文件上传

# import requests

# headers={'Referer':'http://httpbin.org/post',
#          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}

# files={'file':open('favicon.ico','rb')}
# r=requests.post('http://httpbin.org/post',files=files)
# print(r.text)


import requests
import webbrowser

headers={'Cookies':'_zap=9bd36907-8b25-4db3-9b8f-b6f1ba4626f3; _xsrf=mZxTZsIVDxF6ldl1dXKU1FqYk6FZWLt3; d_c0="AMApdsy5kg-PTk3dRap_fRPh1GBQVoWBTJM=|1560324637"; capsion_ticket="2|1:0|10:1560324657|14:capsion_ticket|44:YzhjOTYzNGY3YzBjNDA0ZWFjOTMxNjZjY2E4ODNiOTQ=|dcb727fa1cc37a8f72e57d8aef680dae3230114259547622b90f673a1c2768b2"; z_c0="2|1:0|10:1560324674|4:z_c0|92:Mi4xczVTQkNRQUFBQUFBd0NsMnpMbVNEeVlBQUFCZ0FsVk5Rdmp0WFFETTFzMGhDaGFxWTFnR09vX290SjJ0ZkY5eUt3|bf7eb9e60e0aec84306f0cffe5a1ac468787c34a66d408ac4aec1b7bd9bbfb8e"; tst=r; q_c1=49354cb85ca8480b8a7972032e26083f|1560324675000|1560324675000; tgw_l7_route=060f637cd101836814f6c53316f73463',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
'referer':'https://www.zhihu.com/signin?next=%2F'
}

webbrowser.open("https://www.zhihu.com/signin?next=%2F")
r=requests.get('https://www.zhihu.com',headers=headers)

print(r.text)


# #测试发现运行不了，会死机
# import requests

# cookies='_zap=9bd36907-8b25-4db3-9b8f-b6f1ba4626f3; _xsrf=mZxTZsIVDxF6ldl1dXKU1FqYk6FZWLt3; d_c0="AMApdsy5kg-PTk3dRap_fRPh1GBQVoWBTJM=|1560324637"; capsion_ticket="2|1:0|10:1560324657|14:capsion_ticket|44:YzhjOTYzNGY3YzBjNDA0ZWFjOTMxNjZjY2E4ODNiOTQ=|dcb727fa1cc37a8f72e57d8aef680dae3230114259547622b90f673a1c2768b2"; z_c0="2|1:0|10:1560324674|4:z_c0|92:Mi4xczVTQkNRQUFBQUFBd0NsMnpMbVNEeVlBQUFCZ0FsVk5Rdmp0WFFETTFzMGhDaGFxWTFnR09vX290SjJ0ZkY5eUt3|bf7eb9e60e0aec84306f0cffe5a1ac468787c34a66d408ac4aec1b7bd9bbfb8e"; tst=r; q_c1=49354cb85ca8480b8a7972032e26083f|1560324675000|1560324675000; tgw_l7_route=060f637cd101836814f6c53316f73463'

# jar =requests.cookies.RequestsCookieJar()

# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
# 'referer':'https://www.zhihu.com/signin?next=%2F'}

# for cookies in cookies.split(';'):
# 	key,value=cookies.split('=',1)
# 	jar.set(key,value)
# r=requests.get("http://www.zhihu.com",cookies=jar,headers=headers)
# print(r.text)


