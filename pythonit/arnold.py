
import pygame
from random import randint
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("/home/pi/pythonit/arnold/") if isfile(join("/home/pi/pythonit/arnold/", f))]
global i
i = randint(0,len(onlyfiles))

pygame.mixer.init()
def playArnold():
	global i
	pygame.mixer.music.load("/home/pi/pythonit/arnold/"+onlyfiles[i])
	pygame.mixer.music.set_volume(0.5)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		pass
playArnold();
