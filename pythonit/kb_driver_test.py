from ctypes import *
import pygame

keyboard = cdll.LoadLibrary("./t_kbrd")
print(keyboard.startDriver) 
print(keyboard.endDriver)
print(keyboard.readEvent) 
print(keyboard.waitEvent) 

pygame.mixer.init()
keyLabels = ["1","4","7","*","2","5","8","0","3","6","9","#"]

keyboard.startDriver()
while True:
	event = keyboard.waitEvent()
	key = event & 0xFF
	down = bool(event & 0xFF00)
	print ("KEY:",keyLabels[key], "DOWN:",down)
	if down:
		if key == 11:
			
			pygame.mixer.music.load("/home/pi/Downloads/YouSonuvaBitch.ogg")
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
				pass
			
keyboard.endDriver()
