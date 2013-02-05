#!/usr/bin/python
#
# Hack Factory Raspberry Pi Class.
# David M. N. Bryan, dave@drstrangelove.net
#

# import the Raspberry Pi GPIO Library
import RPi.GPIO as GPIO

# Define OUTPUT Pins on RPI
GPIORed_PIN=27
GPIOGreen_PIN=17
GPIOBlue_PIN=22

# Set the pins to OUTPUTS
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIORed_PIN, GPIO.OUT)
GPIO.setup(GPIOGreen_PIN, GPIO.OUT)
GPIO.setup(GPIOBlue_PIN, GPIO.OUT)

while True:
	GPIO.output(GPIORed_PIN, True)
  	GPIO.output(GPIOGreen_PIN, True)
	GPIO.output(GPIOBlue_PIN, True)
