#!/bin/bash
dsa=$(./AdafruitDHT.py 2302 3)

echo $dsa |cut -f 1 -d ' '|tee /home/pi/temp
echo $dsa |cut -f 2 -d ' '|tee /home/pi/hum