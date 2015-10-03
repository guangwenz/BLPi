#!/bin/python
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN)

try:
	while True:
		sw = GPIO.input(22, True)
		if sw:
			print 'Turned on'
except KeyboardInterrupt:
	print 'Cleaning up and exiting'
	GPIO.cleanup()