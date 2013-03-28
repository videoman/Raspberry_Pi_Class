#!/usr/bin/env python
#
# Example for Hack Factory Raspberry Pi Class.
# David M. N. Bryan, dave@drstrangelove.net
#
# This is licend under creative commons license:
# http://creativecommons.org/licenses/by-nc-sa/3.0/
# Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)
# 
# This needs more work. The code for the Humans appears to have gotten a higher priorty.
#

from RPIO import PWM
import time
import RPi.GPIO as GPIO

Servo1Pin=23
Servo2Pin=18

BeeperPin=24
GPIORed_PIN=17
GPIOGreen_PIN=27

# Setup the OUTPUTS , beeper & LEDS
GPIO.setmode(GPIO.BCM)
GPIO.setup(BeeperPin, GPIO.OUT)
GPIO.setup(GPIORed_PIN, GPIO.OUT)
GPIO.setup(GPIOGreen_PIN, GPIO.OUT)

GPIO.output(BeeperPin, False)
GPIO.output(GPIORed_PIN, False)
GPIO.output(GPIOGreen_PIN, False)

servo = PWM.Servo()

def servo_CW(ServoPIN,SleepTime):
  # Set servo on Servo1Pin to 1200us (1.2ms)
  # This rotates the servo CW.
  servo.set_servo(ServoPIN, 1200)
  time.sleep(SleepTime)
  servo.stop_servo(ServoPIN)
  time.sleep(.25)

def dual_servo_CW(Servo1PIN,Servo2PIN,SleepTime):
  # Set servo on Servo1Pin to 1200us (1.2ms)
  # This rotates the servo CW.
  servo.set_servo(Servo1PIN, 1200)
  servo.set_servo(Servo2PIN, 1200)
  time.sleep(SleepTime)
  servo.stop_servo(Servo1PIN)
  servo.stop_servo(Servo2PIN)
  time.sleep(.25)

def servo_CCW(ServoPIN,SleepTime):
  # Set servo on Servo1Pin to 2000s (2.0ms)
  # This rotates the servo CounterCW
  servo.set_servo(ServoPIN, 2000)
  time.sleep(SleepTime)
  # Clear servo on Servo1Pin
  servo.stop_servo(ServoPIN)
  time.sleep(.25)

def dual_servo_CCW(Servo1PIN,Servo2PIN,SleepTime):
  # Set servo on Servo1Pin to 1200us (1.2ms)
  # This rotates the servo CW.
  servo.set_servo(Servo1PIN, 2000)
  servo.set_servo(Servo2PIN, 2000)
  time.sleep(SleepTime)
  servo.stop_servo(Servo1PIN)
  servo.stop_servo(Servo2PIN)
  time.sleep(.25)

# Clear servo on Servo1Pin
#servo.stop_servo(Servo1Pin)
#servo.stop_servo(Servo2Pin)

while True:

  GPIO.output(GPIORed_PIN, True) 
  GPIO.output(BeeperPin, True) 
  time.sleep(.75)
  GPIO.output(BeeperPin, False) 

  dual_servo_CW(Servo1Pin,Servo2Pin,2)
  #servo_CW(Servo1Pin,2)
  #servo_CCW(Servo1Pin,2)
  #servo_CW(Servo2Pin,2)
  #dual_servo_CCW(Servo1Pin,Servo2Pin,2)
  #servo_CCW(Servo2Pin,2)
