#!/usr/bin/python

import time
import RPi.GPIO as io io.setmode(io.BCM)
import Servo2-Angle.py

door_pin = 23

io.setup(door_pin,io.IN,pull_up_down=io.PUD_UP) #activateinputwithPullUp

while True:
  if io.input(door_pin):
    print("DOOR ALARM!") 
    servo_turn(rand(0-180)
    time.sleep(0.5)
