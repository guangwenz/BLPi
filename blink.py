#!/bin/python
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

try:
	while True:
		GPIO.output(22, True)
		time.sleep(1)
		GPIO.output(22, False)
		time.sleep(1)
except KeyboardInterrupt:
	print 'Cleaning up and exiting'
	GPIO.cleanup()