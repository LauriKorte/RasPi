#!/bin/bash

sdm=$( /home/pi/git/Adafruit_Python_DHT/examples/AdafruitDHT.py 2302 3 )
for sana in $sdm; do
	d="m"
	a=$(( RANDOM%7 + 1))
	tmd="$RANDOM"
	if [ "$tmd" -lt 12000 ]
	then
		d="f"
		a=$(( RANDOM%4 + 1))
	fi
	espeak -p $(( RANDOM%100 )) -vfi+$d$a -a 200 -s 120 "$sana"
done
