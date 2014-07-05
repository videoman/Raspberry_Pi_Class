#!/usr/bin/env python
#
# Raspberry Pi Class.
# David M. N. Bryan, dave@drstrangelove.net
#
# Info on how to wire up the Light sensor can be found at: 
#  http://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading
#
# This is licend under creative commons license:
# http://creativecommons.org/licenses/by-nc-sa/3.0/
# Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)
#

#import the Raspberry Pi GPIO Library
import RPi.GPIO as GPIO, time, os
import time

COLOR=0
light_level=0

# Define OUTPUT Pins on RPI for the LEDs
GPIORed_PIN=27
GPIOGreen_PIN=17
GPIOBlue_PIN=22

# How about some input please?
BUTTON1_PIN=24
BUTTON2_PIN=25
BUTTON3_PIN=23

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
GPIO.setup(BUTTON2_PIN, GPIO.IN)
GPIO.setup(BUTTON3_PIN, GPIO.IN)

def blink_all_leds(SLEEP_TIME):
        GPIO.output(GPIORed_PIN, True)
        GPIO.output(GPIOGreen_PIN, True)
        GPIO.output(GPIOBlue_PIN, True)
        time.sleep(SLEEP_TIME)
        GPIO.output(GPIORed_PIN, False)
        GPIO.output(GPIOGreen_PIN, False)
        GPIO.output(GPIOBlue_PIN, False)
        time.sleep(SLEEP_TIME)

def blink_led(COLOR, SLEEP_TIME):
    if (COLOR == 'RED'):
        GPIO.output(GPIORed_PIN, True)
        time.sleep(SLEEP_TIME)
        GPIO.output(GPIORed_PIN, False)
        time.sleep(SLEEP_TIME)

    if (COLOR == 'GREEN'):
        GPIO.output(GPIOGreen_PIN, True)
        time.sleep(SLEEP_TIME)
        GPIO.output(GPIOGreen_PIN, False)
        time.sleep(SLEEP_TIME)

    if (COLOR == 'BLUE'):
        GPIO.output(GPIOBlue_PIN, True)
        time.sleep(SLEEP_TIME)
        GPIO.output(GPIOBlue_PIN, False)
        time.sleep(SLEEP_TIME)

def RCtime (RCpin):
  reading = 0
  GPIO.setup(RCpin, GPIO.OUT)
  GPIO.output(RCpin, GPIO.LOW)
  time.sleep(0.1)
 
  GPIO.setup(RCpin, GPIO.IN)
  # This takes about 1 millisecond per loop cycle
  while (GPIO.input(RCpin) == GPIO.LOW):
    reading += 1
  return reading

while True:
  light_level=RCtime(18)

  if ( light_level >= 200 ):
#    blink_all_leds(0.25)
    blink_led('RED',0.5 )
    blink_led('GREEN',0.5 )
    blink_led('BLUE',0.5 )

  #if ( GPIO.input(BUTTON1_PIN) == True ):
	#blink_led('RED',0.5)

  #if ( GPIO.input(BUTTON2_PIN) == True ):
	#blink_led('GREEN',0.5)

  #if ( GPIO.input(BUTTON3_PIN) == True ):
	#blink_led('BLUE',0.5)
