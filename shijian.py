#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-29 10:58:43
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$

# import tkinter 
# # import tkinter as tk
# import time

# def gettime():
# 	timestr=time.strftime("%y,%m,%d,%H,%M,%S")
# 	lb.configure(text=timestr)
# 	root.after(1000,gettime)

# root=tkinter.Tk()
# root.title("电子时钟")
# lb=tkinter.Label(root, text='', fg='blue', font=("黑体", 80))
# lb.pack()
# gettime()
# root.mainloop()

import tkinter 
# import tkinter as tk
import time

timestr=time.strftime("%y,%m,%d,%H,%M,%S")


root=tkinter.Tk()
root.title("电子时钟")
lb=tkinter.con(text=timestr)
lb=tkinter.Label(root, text='', fg='blue', font=("黑体", 80))
lb.pack()
gettime()
root.mainloop()
