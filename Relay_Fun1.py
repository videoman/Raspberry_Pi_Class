#!/usr/bin/python
#
# Hack Factory Raspberry Pi Class.
# David M. N. Bryan, dave@drstrangelove.net
#

# import the Raspberry Pi GPIO Library
import RPi.GPIO as GPIO

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
