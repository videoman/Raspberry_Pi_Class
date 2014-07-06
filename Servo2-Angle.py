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

# This function will turn a servo from 0 - 180 Degrees
def servo_turn(ServoPIN,degree_n):
  servo = GPIO.PWM(ServoPIN, 100)
  servo.start(5)
  duty = float(degree_n) / 10.0 + 2.5
  servo.ChangeDutyCycle(duty)
  time.sleep(.7)
  servo.stop()

while True:
  my_input = '90'
  user_input = raw_input("Enter a number between 0 and 180 (default: %s):\n" % my_input) or my_input

  print "Sending angle", user_input, "to servo on PIN:", Servo1Pin
  servo_turn(Servo1Pin, user_input)


# time.sleep(5)

