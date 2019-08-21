import requests
from lxml import etree

# 1. 请求下载包图网数据
response = requests.get("https://ibaotu.com/shipin/")
print(response)
# 2. 抽取想要数据 视频标题 视频链接
xml = etree.HTML(response.text) # 数据整理xml对象
tit_list = xml.xpath('//span[@class="video-title"]/text()')
src_list = xml.xpath('//div[@class="video-play"]/video/@src')
for tit, src in zip(tit_list, src_list):
    # 3. 下载视频
    response = requests.get("http:" + src)
    fileName = "video\\" + tit + ".mp4"
    print("正在保存视频文件：" + fileName)
    # 4. 保存视频
    with open(fileName, "wb") as f:
        f.write(response.content)
