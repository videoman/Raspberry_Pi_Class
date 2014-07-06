#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

Servo1Pin=18
Servo2Pin=23

# Tell python what pin mode to use
GPIO.setmode(GPIO.BCM)
# Setup the Servos Pins
GPIO.setup(Servo1Pin, GPIO.OUT)
GPIO.setup(Servo2Pin, GPIO.OUT)

# This function turns the servo Clock Wise
def servo_CW(ServoPIN):
  # Setup the frequency first (100Hz)
  servo = GPIO.PWM(ServoPIN, 100)
  # Then setup the duty cycle, 2.5pulses/100cycles
  servo.start(2.5)
  time.sleep(.7)
  servo.stop()

# This function turns the servo counter clock wise
def servo_CCW(ServoPIN):
  servo = GPIO.PWM(ServoPIN, 100)
  servo.start(18)
  time.sleep(.7)
  servo.stop()

while True:
  print "Sending CW signal to PIN:", Servo1Pin
  servo_CW(Servo1Pin)

  time.sleep(.8)

  print "Sending CCW signal to PIN:", Servo1Pin
  servo_CCW(Servo1Pin)

  time.sleep(.8)

