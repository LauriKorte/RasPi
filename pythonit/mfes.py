import pygame
import time as time
import RPi.GPIO as GPIO

pygame.mixer.init()
pinnit = {}
pinnit[4] = 10
pinnit[5] = 9
pinnit[6] = 11

pinnit[7] = 5
pinnit[8] = 6
pinnit[9] = 13
pinnit[10] = 19

pinnit[11] = 26
pinnit[12] = 16
pinnit[13] = 20
pinnit[14] = 12

GPIO.setmode(GPIO.BCM)
for num, pin in pinnit.items():
	GPIO.setup(pin, GPIO.OUT)
	print (pin)
	GPIO.output(pin, GPIO.LOW)
time.sleep(0.5)


#init

for i in range(0,4):
	GPIO.output(pinnit[9], GPIO.LOW)
	GPIO.output(pinnit[10], GPIO.LOW)
	GPIO.output(pinnit[11], GPIO.HIGH)
	GPIO.output(pinnit[12], GPIO.HIGH)
	GPIO.output(pinnit[6], GPIO.HIGH)
	time.sleep(0.01)
	
	GPIO.output(pinnit[6], GPIO.LOW)
	GPIO.output(pinnit[9], GPIO.LOW)
	GPIO.output(pinnit[10], GPIO.LOW)
	GPIO.output(pinnit[11], GPIO.LOW)
	GPIO.output(pinnit[12], GPIO.LOW)
	time.sleep(0.1)


#gursoiri
GPIO.output(pinnit[7], GPIO.LOW)
GPIO.output(pinnit[8], GPIO.LOW)
GPIO.output(pinnit[9], GPIO.LOW)
GPIO.output(pinnit[10], GPIO.HIGH)
GPIO.output(pinnit[6], GPIO.HIGH)
time.sleep(0.01)

GPIO.output(pinnit[6], GPIO.LOW)
GPIO.output(pinnit[7], GPIO.LOW)
GPIO.output(pinnit[8], GPIO.LOW)
GPIO.output(pinnit[9], GPIO.LOW)
GPIO.output(pinnit[10], GPIO.LOW)
time.sleep(0.01)
#mdfs

GPIO.output(pinnit[7], GPIO.HIGH)
GPIO.output(pinnit[6], GPIO.HIGH)
time.sleep(0.01)
GPIO.output(pinnit[6], GPIO.LOW)
GPIO.output(pinnit[7], GPIO.LOW)

time.sleep(0.1)

#entry mode set

GPIO.output(pinnit[9], GPIO.HIGH)
GPIO.output(pinnit[6], GPIO.HIGH)
time.sleep(0.01)
GPIO.output(pinnit[6], GPIO.LOW)
GPIO.output(pinnit[9], GPIO.LOW)

time.sleep(0.1)

#mdfs

GPIO.output(pinnit[8], GPIO.HIGH)
GPIO.output(pinnit[6], GPIO.HIGH)
time.sleep(0.01)
GPIO.output(pinnit[6], GPIO.LOW)
GPIO.output(pinnit[8], GPIO.LOW)

time.sleep(0.1)
#muuta bullshgittiä

#gursoiri
GPIO.output(pinnit[7], GPIO.HIGH)
GPIO.output(pinnit[8], GPIO.HIGH)
GPIO.output(pinnit[9], GPIO.HIGH)
GPIO.output(pinnit[10], GPIO.HIGH)
GPIO.output(pinnit[6], GPIO.HIGH)
time.sleep(0.01)

GPIO.output(pinnit[6], GPIO.LOW)
GPIO.output(pinnit[7], GPIO.LOW)
GPIO.output(pinnit[8], GPIO.LOW)
GPIO.output(pinnit[9], GPIO.LOW)
GPIO.output(pinnit[10], GPIO.LOW)

time.sleep(0.1)

#ddram osoite
GPIO.output(pinnit[14], GPIO.HIGH)
GPIO.output(pinnit[6], GPIO.HIGH)
time.sleep(0.01)

GPIO.output(pinnit[6], GPIO.LOW)
GPIO.output(pinnit[14], GPIO.LOW)

time.sleep(0.5)


GPIO.output(pinnit[4], GPIO.HIGH)
GPIO.output(pinnit[7], GPIO.LOW)
GPIO.output(pinnit[8], GPIO.LOW)
GPIO.output(pinnit[9], GPIO.LOW)
GPIO.output(pinnit[10], GPIO.LOW)
GPIO.output(pinnit[11], GPIO.HIGH)
GPIO.output(pinnit[12], GPIO.HIGH)
GPIO.output(pinnit[13], GPIO.LOW)
GPIO.output(pinnit[14], GPIO.HIGH)
GPIO.output(pinnit[6], GPIO.HIGH)
time.sleep(0.01)


GPIO.output(pinnit[6], GPIO.LOW)
GPIO.output(pinnit[4], GPIO.LOW)
GPIO.output(pinnit[7], GPIO.LOW)
GPIO.output(pinnit[8], GPIO.LOW)
GPIO.output(pinnit[9], GPIO.LOW)
GPIO.output(pinnit[10], GPIO.LOW)
GPIO.output(pinnit[11], GPIO.LOW)
GPIO.output(pinnit[12], GPIO.LOW)
GPIO.output(pinnit[13], GPIO.LOW)
GPIO.output(pinnit[14], GPIO.LOW)

time.sleep(0.1)

for i in range(0,100):
	GPIO.output(pinnit[9], GPIO.HIGH)
	GPIO.output(pinnit[10], GPIO.HIGH)
	GPIO.output(pinnit[11], GPIO.HIGH)
	GPIO.output(pinnit[6], GPIO.HIGH)
	time.sleep(0.01)
	
	GPIO.output(pinnit[6], GPIO.LOW)
	GPIO.output(pinnit[9], GPIO.LOW)
	GPIO.output(pinnit[10], GPIO.LOW)
	GPIO.output(pinnit[11], GPIO.LOW)
	
	time.sleep(0.1)
	
	
	GPIO.output(pinnit[4], GPIO.HIGH)

	GPIO.output(pinnit[7], GPIO.LOW)
	GPIO.output(pinnit[8], GPIO.LOW)
	GPIO.output(pinnit[9], GPIO.LOW)
	GPIO.output(pinnit[10], GPIO.LOW)

	GPIO.output(pinnit[11], GPIO.HIGH)
	GPIO.output(pinnit[12], GPIO.LOW)
	GPIO.output(pinnit[13], GPIO.HIGH)
	GPIO.output(pinnit[14], GPIO.HIGH)

	time.sleep(0.03)
	GPIO.output(pinnit[6], GPIO.HIGH)
	time.sleep(0.01)
	
	
	GPIO.output(pinnit[6], GPIO.LOW)
	GPIO.output(pinnit[4], GPIO.LOW)
	GPIO.output(pinnit[7], GPIO.LOW)
	GPIO.output(pinnit[8], GPIO.LOW)
	GPIO.output(pinnit[9], GPIO.LOW)
	GPIO.output(pinnit[10], GPIO.LOW)
	GPIO.output(pinnit[11], GPIO.LOW)
	GPIO.output(pinnit[12], GPIO.LOW)
	GPIO.output(pinnit[13], GPIO.LOW)
	GPIO.output(pinnit[14], GPIO.LOW)
	
	time.sleep(0.1)

	GPIO.output(pinnit[9], GPIO.HIGH)
	GPIO.output(pinnit[10], GPIO.HIGH)
	GPIO.output(pinnit[11], GPIO.HIGH)
	GPIO.output(pinnit[6], GPIO.HIGH)
	time.sleep(0.01)
	
	GPIO.output(pinnit[6], GPIO.LOW)
	GPIO.output(pinnit[9], GPIO.LOW)
	GPIO.output(pinnit[10], GPIO.LOW)
	GPIO.output(pinnit[11], GPIO.LOW)
	
	time.sleep(0.1)
	
	
	GPIO.output(pinnit[4], GPIO.HIGH)

	GPIO.output(pinnit[7], GPIO.LOW)
	GPIO.output(pinnit[8], GPIO.HIGH)
	GPIO.output(pinnit[9], GPIO.LOW)
	GPIO.output(pinnit[10], GPIO.LOW)

	GPIO.output(pinnit[11], GPIO.LOW)
	GPIO.output(pinnit[12], GPIO.LOW)
	GPIO.output(pinnit[13], GPIO.HIGH)
	GPIO.output(pinnit[14], GPIO.LOW)

	time.sleep(0.03)
	GPIO.output(pinnit[6], GPIO.HIGH)
	time.sleep(0.01)
	
	
	GPIO.output(pinnit[6], GPIO.LOW)
	GPIO.output(pinnit[4], GPIO.LOW)
	GPIO.output(pinnit[7], GPIO.LOW)
	GPIO.output(pinnit[8], GPIO.LOW)
	GPIO.output(pinnit[9], GPIO.LOW)
	GPIO.output(pinnit[10], GPIO.LOW)
	GPIO.output(pinnit[11], GPIO.LOW)
	GPIO.output(pinnit[12], GPIO.LOW)
	GPIO.output(pinnit[13], GPIO.LOW)
	GPIO.output(pinnit[14], GPIO.LOW)
	
	time.sleep(0.1)


