#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-23 23:34:25
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$

import os
import requests
from lxml import etree

response=requests.get("https://www.mzitu.com/tag/ugrils")
xml=etree.HTML(response.text)

alt_list=xml.xpath()