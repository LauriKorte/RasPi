#
#
#


import RPIO as GPIO
import time as time

import subprocess

cols = []
cols.append(14)
cols.append(15)
cols.append(18)

rows = []
rows.append(17)
rows.append(27)
rows.append(22)
rows.append(23)


def keycall(a,b):
	if b == 0:
		return
	print (a)
	if a == 17:
		print("SAATANA {}", a)	
	if a == 27:
		subprocess.Popen(["python3","/home/pi/pythonit/arnold.py"])
	if a == 22 or a == 23:
		subprocess.Popen(["bash","/home/pi/pythonit/speakStuff.sh"])



for pin in cols:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, True)

for pin in rows:
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_interrupt_callback(pin, keycall)


GPIO.wait_for_interrupts()
