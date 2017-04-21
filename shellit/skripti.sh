#!/bin/bash

cd /home/pi

display $(date | cut -f 4 -d ' ')

trap 'kill $(jobs -p)' EXIT
bash -c "while true; do bash gettemp.sh; sleep 10; done"&

python3 ./kb_driver_test.py