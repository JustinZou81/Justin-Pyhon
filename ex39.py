#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-05 12:34:23
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$

ten_things="Apples Oranges Crows Telephone"

print("Wait there's not 10 things in that list, let's fix that.")

stuff=ten_things.split(' ')
print(stuff)
more_stuff=['Day','Night','Song','Frisbee',"Corn","Banan","girl","Boy"]

while len(stuff)!=10:

	next_one = more_stuff.pop()
	print("Adding:",next_one)
	stuff.append(next_one)
	print("There's %d items now."%len(stuff))

print("There we go:",stuff)

print("Let's do some things with stuff.")

print (stuff[1])
print (stuff[-1])
print (stuff.pop())

print(''.join(stuff))
print('#'.join(stuff[3:5]))