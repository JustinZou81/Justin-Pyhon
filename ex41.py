#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-17 16:25:04
# @Author  : Justin Zou (wh6343868@163.com)
# @Link    : http://www.cnblogs.com/JustinZou/
# @Version : $Id$

from sys import exit
from random import randint

def death():
	quips=["You died. You kinda suck at this.",
	       "Nice job,you died...jackass.",
	       "Such a luser.",
	       "I have a small puppy that's better at this."]
	print(quips[randint(0,len(quips)-1)])
	exit(1)

def central_corridor():
	print("The Gothons of Plant Percal #25 have invaded your ship and destroyed")
	print("Your entire crew.You are the last surviving member and your last")
	print("mission is to get the neutron bomb from the Weapons Armory,")
	print("put it in the bridge, and blow the ship up after getting into an")
	print("escape pod.")
	print("\n")
	print("You're running down the central corridor ot the Weapons Armory when")
	print("a Gothon jumps out, red scaly skin, dark grimy teeth and evil clown costume")
	print("flowing around his hate filled body. He's blocking the door to the")
	print("Armory and about to pull a weapon to blast you.")

	action=input(">")

	if action=="shoot!":
		print("Quick on the draw you yank out your blaster and fire it at the Gothon.")
		print("His clown costume is flowing and moving around his body, which throws")
		print("off your aim. Your laster hits his costume but misses him entirely. This")
		print("completely ruins his brand new costume his mother bought him, which")
		print("makes him fly into an insane rage and blast you repeatedly in the face until")
		print("you are dead. Then he eats you.")
		return("death")
	elif action=="dodge!":
		print("Like a world class boxer you dodge,weave,slip and slide right")
		print("as the Gothon's blaster cranks a laster past your head.")
		print("In the middle of your artful dodge your foot slops and you ")
		print("bang your head on the metal wall and pass out.")
		print("You wake up shortly after only to die as the GOthon stomps on")
		print("your head and eats you.")
		return('death')
	elif action=="tell a joke":
		print("Lucky for you they made you learn Gothon insults in the academy.")
		print("You tell the one Gothon joke you know:")
		print("Lbhe zbgure vf fb sng,jura fur fvgf nebhaq gur ubhfr,fur fvgf nebhaq gur ubhfr.")
		print("The Gothon stops,tries not to laugh,then busts out laughting and can't move.")
		print("While he's laughing you run up and shoot him square in the head")
		print("putting him down, then jump through the Weapon Armory door.")
		return()
