#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-31 19:01:36
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$

import os
from string import Template

tpm1=Template("Hello, $who! $what enough for ya?")
value=('world','Hot')
tpm1.substitute(who='M',what='D')
tpm1