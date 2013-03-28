#!/usr/bin/env python
#
# Example for Hack Factory Raspberry Pi Class.
# David M. N. Bryan, dave@drstrangelove.net
#
# This is licend under creative commons license:
# http://creativecommons.org/licenses/by-nc-sa/3.0/
# Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)

from RPIO import PWM
import time
import RPi.GPIO as GPIO

Servo1Pin=18
Servo2Pin=23

BeeperPin=24
GPIO_ButtonL_LED_PIN=4
GPIO_ButtonL_PIN=17

GPIO_ButtonR_LED_PIN=27
GPIO_ButtonR_PIN=22

# Setup the OUTPUTS , beeper & LEDS
GPIO.setmode(GPIO.BCM)
GPIO.setup(BeeperPin, GPIO.OUT)
GPIO.setup(GPIO_ButtonL_LED_PIN, GPIO.OUT)
GPIO.setup(GPIO_ButtonL_PIN, GPIO.IN)
GPIO.setup(GPIO_ButtonR_LED_PIN, GPIO.OUT)
GPIO.setup(GPIO_ButtonR_PIN, GPIO.IN)

GPIO.output(BeeperPin, False)
GPIO.output(GPIO_ButtonL_LED_PIN, False)
GPIO.output(GPIO_ButtonR_LED_PIN, False)

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
  GPIO.output(GPIO_ButtonL_LED_PIN, True)
  GPIO.output(GPIO_ButtonR_LED_PIN, True)

  bin_name = raw_input('Do you require food from the (L)eft or (R)ight bin?  []')

  if bin_name == "L" or bin_name == "l" or bin_name == "left" or bin_name == "Left":
    GPIO.output(GPIO_ButtonL_LED_PIN, False)
    GPIO.output(BeeperPin, True) 
    time.sleep(.25)
    GPIO.output(BeeperPin, False) 
    GPIO.output(GPIO_ButtonL_LED_PIN, True)
    servo_CCW(Servo1Pin,2)
  elif bin_name == "R" or bin_name == "r" or bin_name == "Right" or bin_name == "right":
    GPIO.output(GPIO_ButtonR_LED_PIN, False)
    GPIO.output(BeeperPin, True) 
    time.sleep(.25)
    GPIO.output(BeeperPin, False) 
    GPIO.output(GPIO_ButtonR_LED_PIN, True)
    servo_CW(Servo2Pin,2)
  elif bin_name == "B" or bin_name == "b" or bin_name == "Both" or bin_name == "both":
    dual_servo_CW(Servo1Pin,Servo2Pin,2)
    servo_CCW(Servo1Pin,2)
    servo_CW(Servo2Pin,2)
    dual_servo_CCW(Servo1Pin,Servo2Pin,2)
    servo_CCW(Servo2Pin,2)
