#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-28 18:48:47
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$


import tkinter
import time
from datetime import datetime
# import tkinter as tk


def gettime():
    # 获取当前时间并转为字符串
    timestr=time.strftime("%y,%m,%d,%H:%M:%S")
    # 重新设置标签文本
    lb.configure(text=timestr)
    # 每隔一秒调用函数gettime自身获取时间
    root.after(1000, gettime)



root = tkinter.Tk()
root.title('电子时钟')
# 设置字体大小颜色
lb=tkinter.Text(root, text='', fg='blue', font=("黑体", 80))
lb.pack()
gettime()
root.mainloop()
# root=tkinter.Tk()
# root.title('电子时钟')
# lb=tkinter.lb(root, text='', fg='blue', font=("黑体", 80))
# lb.pack()
# gettime()
# root.mainloop()
