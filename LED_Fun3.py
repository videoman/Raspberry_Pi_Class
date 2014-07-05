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

# Define OUTPUT Pins on RPI for the LEDs
GPIORed_PIN=27
GPIOGreen_PIN=17
GPIOBlue_PIN=22

# How about some input please?
# This will define what pin we want to use for a button input...
BUTTON1_PIN=24

# How long do we sleep between cycles, we can set this to .25 for 1/4
# of a second. 
SLEEP_TIME=1

# Set the pins on the GPIO up.

# Setup the OUTPUTS (LEDS)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIORed_PIN, GPIO.OUT)
GPIO.setup(GPIOGreen_PIN, GPIO.OUT)
GPIO.setup(GPIOBlue_PIN, GPIO.OUT)

#Setup the INPUTs (Buttons)
GPIO.setup(BUTTON1_PIN, GPIO.IN)

# Do this thing that I say until someone kills this loop...
while True:
  # Has the button been pushed?
  if ( GPIO.input(BUTTON1_PIN) == True ):
	# Looks like it was pushed, and while it's still pushed, lets
	# make some pretty blinks...
	# All on!
	GPIO.output(GPIORed_PIN, True)
  	GPIO.output(GPIOGreen_PIN, True)
	GPIO.output(GPIOBlue_PIN, True)
	# ZZzzzzzzz....
	time.sleep(SLEEP_TIME)
	# All off!  
	GPIO.output(GPIORed_PIN, False)
  	GPIO.output(GPIOGreen_PIN, False)
	GPIO.output(GPIOBlue_PIN, False)
	# Sleeepy time..zzzz
	time.sleep(SLEEP_TIME)
	
