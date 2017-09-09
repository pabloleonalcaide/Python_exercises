# -*- coding: utf-8 -*-
import random # To generate random number
import time	# To delay messages 


def introduction():
	"""Show the introduction"""
	print "Despiertas en una habitación vagamente iluminada, ante ti"
	print "hay dos puertas. Una de ellas lleva a la cámara del tesoro"
	print "y una salida segura que te llevará a casa. La otra puerta"
	print "lleva a la guarida de una terrible y hambrienta bestia."
	print
def selectDoor():
	"""Select the door"""
	door = ""
	while door!="1" and door!="2":
		print "¿Qué puerta escoges? (1 o 2)"
		door = raw_input()
	return door
def lookDoor(doorChoosen):
	"""Show the result"""
	print "Te aproximas a la puerta"
	time.sleep(2)
	print "Está oscuro y misterioso..."
	time.sleep(2)
	print "¡Un Caballero fiero y tosco se acerca hacia tí y..."
	print
	time.sleep(2)
	rightDoor = random.randint(1, 2)
	if doorChoosen == str(rightDoor):
		print "...¡Te entrega un cofre lleno de joyas!"
	else:
		print "...¡Revela unas garras terribles y te destroza de un sólo golpe!"
playAgain = "s"
while playAgain == "s" or playAgain == "S":
	introduction()
	numberDoor = selectDoor()
	lookDoor(numberDoor)
	print "¿Quieres jugar otra vez? (s o n)"
	playAgain = raw_input()
