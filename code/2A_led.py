#!/usr/bin/env python

#lass eine LED blinken

import RPi.GPIO as GPIO 
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21, GPIO.OUT)

while True:
    GPIO.output(21,1)
    print "blink"
    sleep(1)
    GPIO.output(21,0)
    sleep(1)

GPIO.cleanup()
