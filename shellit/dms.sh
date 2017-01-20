
sdm=$( /home/pi/git/Adafruit_Python_DHT/examples/AdafruitDHT.py 2302 3 )

espeak -p 0 -vfi -a 200 -s 120 "$sdm"

