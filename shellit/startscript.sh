#!/bin/bash
sleep 10
espeak -s 80 -p 0 "get ready son"
sleep 5
espeak "runnin this son of a bitch"
amixer set PCM 100%


forever start -c bash /home/pi/pythonit/speakStuff.sh
#forever start -c python3 /home/pi/pythonit/kbrd.py
#forever start -c python3 /home/pi/pythonit/mfes.py
