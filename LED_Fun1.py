#!/usr/bin/python
#
# Raspberry Pi Class.
# David M. N. Bryan, dave@drstrangelove.net
#
# This is licend under creative commons license:
# http://creativecommons.org/licenses/by-nc-sa/3.0/
# Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)
#
# I am a comment in the code!
# This does not get interperted or used in any way!
# Comments are very useful to make things readable...
#

# import the Raspberry Pi GPIO Library
import RPi.GPIO as GPIO

# Define OUTPUT Pins on RPI
# Plug a 560ohm reisitor from each of the defined PINs into the + (long leg) side of an LED.
# Now connect the short leg to the ground rail.
GPIORed_PIN=27
GPIOGreen_PIN=17
GPIOBlue_PIN=22

# set the GPIO Pinout to the BCM chip
GPIO.setmode(GPIO.BCM)
# Set the pins to OUTPUTS
GPIO.setup(GPIORed_PIN, GPIO.OUT)
GPIO.setup(GPIOGreen_PIN, GPIO.OUT)
GPIO.setup(GPIOBlue_PIN, GPIO.OUT)

# Tell the user we are going to turn the lights on!
print "Ok, here is where we turn your lights on!"
print "PINs are assigned as follows:\nRed:",GPIORed_PIN,"\nGreen:",GPIOGreen_PIN,"\nBlue:",GPIOBlue_PIN
print "\nAll of the lights should be working\nType Ctrl-c to quit out of the program."

# Turn all of the lights on
while True:
	GPIO.output(GPIORed_PIN, True)
  	GPIO.output(GPIOGreen_PIN, True)
	GPIO.output(GPIOBlue_PIN, True)

# That's it.  All your lights should go on.
