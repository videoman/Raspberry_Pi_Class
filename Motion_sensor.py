#!/usr/bin/python

import time
import RPi.GPIO as GPIO
# from Servo2-Angle.py import *

GPIO.setmode(GPIO.BCM)

door_pin = 23

# Setup the pull up resistor in the circuit.
GPIO.setup(door_pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) 

while True:
  if GPIO.input(door_pin):
    print("DOOR ALARM!") 
    time.sleep(0.5)
