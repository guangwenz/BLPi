#!/bin/python
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN)
GPIO.setup(22, GPIO.OUTPUT)

on = False
try:
	while True:
		on = GPIO.input(12)
		GPIO.output(22, on)
except KeyboardInterrupt:
	print 'Cleaning up and exiting'
	GPIO.cleanup()