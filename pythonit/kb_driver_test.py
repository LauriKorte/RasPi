from ctypes import *
import pygame
import subprocess

from random import randint
from os import listdir
from os.path import isfile, join

keyboard = cdll.LoadLibrary("./kb_drv")
display = cdll.LoadLibrary("./display_drv")
print(keyboard.startDriver) 
print(keyboard.endDriver)
print(keyboard.readEvent) 
print(keyboard.waitEvent) 



print(display.displayStart) 
print(display.displayClear) 
print(display.displayPrint)

pygame.mixer.init()
keyLabels = ["1","4","7","*","2","5","8","0","3","6","9","#"]

display.displayStart()
keyboard.startDriver()
display.displayClear()
display.displayPrint(b"PASCAE")

onlyfiles = [f for f in listdir("/home/pi/arnold/") if isfile(join("/home/pi/arnold/", f))]
shutups = ["ShutUp1.ogg","ShutUp2.ogg","ShutUp3.ogg","ShutUp4.ogg"]
import time

global nextevent
randomarskatimer = time.time() + 600 + randint(0,3600*24)
nextevent = time.time() + 1

def randomArska(lista = onlyfiles):
	i = randint(0,len(lista)-1)
	pygame.mixer.music.load("/home/pi/arnold/"+lista[i])
	pygame.mixer.music.play()

def doTimeStuff():
	global nextevent
	global randomarskatimer
	now = time.time()
	if (now - nextevent) > 0:
		nextevent = now + 1
		display.displayClear()
		display.displayPrint(bytes(time.strftime("%H %M %S"), 'utf-8'))
	if (now - randomarskatimer) > 0:
		randomArska(shutups)
		randomarskatimer = time.time() + 600 + randint(0,3600*24)
		
while True:
	event = keyboard.readEvent()
	if event < 0:
		doTimeStuff()
		continue
	key = event & 0xFF
	down = bool(event & 0xFF00)
	print ("KEY:",keyLabels[key], "DOWN:",down)
	if down:
		if key == 4:
			f = open("temp")
			tmp = f.read().rstrip("\n")
			display.displayClear()
			display.displayPrint(bytes(tmp+"'C", 'utf-8'))
			nextevent = time.time() + 4.568743
		if key == 5:
			f = open("hum")
			tmp = f.read().rstrip("\n")
			display.displayClear()
			display.displayPrint(bytes(tmp+" %", 'utf-8'))
			nextevent = time.time() + 4.568743
		if key == 6:
			randomArska()
			
keyboard.endDriver() 
