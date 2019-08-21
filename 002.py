#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-05 11:02:10
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$

def gold_room():
	print("This room is full of gold. How much do you take?")

	next=input(">")
	if '0' in next or '1' in next:
		how_much=int(next)
	else:
		dead("Man,learn to type a number.")

	if how_much<50:
		print("Nice,you're not gready,you win!")
		exit(0)
	else:
		dead("You gready bastard!")


def dead(self):
	print(input(self))
	exit(0)



def bear_room():
	print("There is a bear here")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	bear_moved=False

	while True:
		next=input(">")
		if next=="take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next=="taunt bear" and not bear_moved:
			print("The bear has moved from the door. You can go through it now.")
			bear_moved=True
		elif next=="taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next=="open door" and bear_moved:
			gold_room()
		else:
			print("I got no idea what that means.")

def start():
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")

	next=input(">")

	if next=="left":
		bear_room()
	elif next=="right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

start()

