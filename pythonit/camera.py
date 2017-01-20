#!/usr/bin/env python

from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.image_effect = 'emboss'
sleep(10) #active time
camera.stop_preview()
