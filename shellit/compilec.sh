#!/bin/bash
gcc -shared  -std=c11 -fpic -lwiringPi -pthread ./RasPi/ceet/kb_driver.c -o kb_drv
gcc -std=c11 -lwiringPi ./RasPi/ceet/kbrd.c -o display 
gcc -shared  -std=c11 -fpic -lwiringPi ./RasPi/ceet/kbrd.c -o display_drv