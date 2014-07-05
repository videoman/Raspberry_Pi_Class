#!/usr/bin/env python
#
# Raspberry Pi Class.
# David M. N. Bryan, dave@drstrangelove.net
#
# This is licend under creative commons license:
# http://creativecommons.org/licenses/by-nc-sa/3.0/
# Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)
#

#import the Raspberry Pi GPIO Library
import RPi.GPIO as GPIO
import time

# Define OUTPUT Pins on RPI
GPIORed_PIN=27
GPIOGreen_PIN=17
GPIOBlue_PIN=22
# This is the delay that we are going to insert, in this case 1 second.
SLEEP_TIME=1

# Set our GPIO library up...
GPIO.setmode(GPIO.BCM)
# Set the pins to OUTPUTS
GPIO.setup(GPIORed_PIN, GPIO.OUT)
GPIO.setup(GPIOGreen_PIN, GPIO.OUT)
GPIO.setup(GPIOBlue_PIN, GPIO.OUT)

# Enter into a loop...
while True:

	#Turn on all LEDs...
	GPIO.output(GPIORed_PIN, True)
  	GPIO.output(GPIOGreen_PIN, True)
	GPIO.output(GPIOBlue_PIN, True)
	# Wait for "SLEEP_TIME" seconds before we do the next action.
	time.sleep(SLEEP_TIME)
	# Turn off all the LEDs.
	GPIO.output(GPIORed_PIN, False)
  	GPIO.output(GPIOGreen_PIN, False)
	GPIO.output(GPIOBlue_PIN, False)
	# Sleep for a period...
	time.sleep(SLEEP_TIME)
	
# Do this until we stop the program.
