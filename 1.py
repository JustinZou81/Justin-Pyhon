#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-29 16:08:54
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$

from sys import argv

script,filename=argv

print("we are going to erase %r."%filename)
print("If you don't want that,hit CTRL-C(^C).")
print("If you do want that, hit Return.")

input("?")

print("Opening the file...")
target=open(filename,'w')

print("Truncate the file.Goodbye!")
target.truncate()

print("Now I'm goint to ask you for three lines.")

line1=input("line1:")
line2=input("line2:")
line3=input("line3:")

print("I'm going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally,we close it.")
target.close()