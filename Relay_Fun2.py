#!/usr/bin/python
#
# Raspberry Pi Class.
# David M. N. Bryan, dave@drstrangelove.net
#

# import the Raspberry Pi GPIO Library
import RPi.GPIO as GPIO, time, os

# Define OUTPUT Pins on RPI
RELAY1_PIN=25
RELAY2_PIN=24

# Set the pins to OUTPUTS
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY1_PIN, GPIO.OUT)
GPIO.setup(RELAY2_PIN, GPIO.OUT)

while True:
	GPIO.output(RELAY1_PIN, False)
  	GPIO.output(RELAY2_PIN, False)
	time.sleep(.25)
	GPIO.output(RELAY1_PIN, True)
  	GPIO.output(RELAY2_PIN, True)
	time.sleep(.25)

