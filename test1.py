#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-29 15:08:18
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$

from tkinter import *
def rtnkey(event=None):
    print(e.get())
root = Tk()
e = StringVar()
entry = Entry(root, validate='key', textvariable=e, width=50)
entry.pack()
entry.bind('<Return>', rtnkey)
root.title('测试回车获取文本框内容')
root.mainloop()
