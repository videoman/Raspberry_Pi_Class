#!/usr/bin/env python
#
# Hack Factory Raspberry Pi Class.
# David M. N. Bryan, dave@drstrangelove.net
#

#import the Raspberry Pi GPIO Library
import RPi.GPIO as GPIO
import time

# Define OUTPUT Pins on RPI for the LEDs
GPIORed_PIN=27
GPIOGreen_PIN=17
GPIOBlue_PIN=22

# How about some input please?
BUTTON1_PIN=24

# How long do we sleep between cycles
SLEEP_TIME=1

# Set the pins on the GPIO up.

# Setup the OUTPUTS (LEDS)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIORed_PIN, GPIO.OUT)
GPIO.setup(GPIOGreen_PIN, GPIO.OUT)
GPIO.setup(GPIOBlue_PIN, GPIO.OUT)

#Setup the INPUTs (Buttons)
GPIO.setup(BUTTON1_PIN, GPIO.IN)

while True:
  if ( GPIO.input(BUTTON1_PIN) == True ):
	GPIO.output(GPIORed_PIN, True)
  	GPIO.output(GPIOGreen_PIN, True)
	GPIO.output(GPIOBlue_PIN, True)
	time.sleep(SLEEP_TIME)
	GPIO.output(GPIORed_PIN, False)
  	GPIO.output(GPIOGreen_PIN, False)
	GPIO.output(GPIOBlue_PIN, False)
	time.sleep(SLEEP_TIME)
