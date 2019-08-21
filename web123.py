# import urllib.request
from lxml import etree
import requests
from bs4 import BeautifulSoup
import lxml

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
         'Referer':'https://www.mzitu.com/'}
url="https://www.mzitu.com/"
# req = urllib.request.Request(url, headers=headers)
# response=urllib.request.urlopen(req)
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Content-Type'))
html = requests.get(url,headers = headers)
print(html.text)
soup=BeautifulSoup(html.text,'lxml')
li_list=soup.find_all('li')
for li in li_list:
	print(li)

all_a = soup.find('img', class_='lazy').find_all('lazy')
for lazy in all_a:
	print(lazy)
title=html.xpath('//img[@class='lazy']/@alt)

