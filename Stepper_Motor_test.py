#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

Stepper_pin1=17
Stepper_pin2=18
#change the value of "pin3" to 27 if V2 Raspberry Pi
Stepper_pin3=27
Stepper_pin4=22

Stepper_pin5=23
Stepper_pin6=24
Stepper_pin7=25
Stepper_pin8=4

# set pin directions
GPIO.setmode(GPIO.BCM)
GPIO.setup(Stepper_pin1,GPIO.OUT)
GPIO.setup(Stepper_pin2,GPIO.OUT)
GPIO.setup(Stepper_pin3,GPIO.OUT)
GPIO.setup(Stepper_pin4,GPIO.OUT)

#
Apin1=[0,1,0,0,1]        
Apin2=[0,1,1,0,0]
Apin3=[0,0,1,1,0]
Apin4=[0,0,0,1,1]
current=0
target=0

def GO_THERE(target,current):
        if current<target:
                while current<target:
                        i=current&2 + 1
                        GPIO.output(Stepper_pin1,Apin1[i])
                        GPIO.output(Stepper_pin2,Apin2[i])
                        GPIO.output(Stepper_pin3,Apin3[i])
                        GPIO.output(Stepper_pin4,Apin4[i])
                        time.sleep(.003)
                        current= current + 1
        else:
                while current>target:
                        i=current&2 + 1
                        GPIO.output(Stepper_pin1,Apin1[i])
                        GPIO.output(Stepper_pin2,Apin2[i])
                        GPIO.output(Stepper_pin3,Apin3[i])
                        GPIO.output(Stepper_pin4,Apin4[i])
                        time.sleep(.003)
                        current= current - 1
        print current,target
        return current;
  #setup


target=4000
current=GO_THERE(target,current)

#time.sleep(2)
#target=200
#current=GO_THERE(target,current)

#target=2000
#current=GO_THERE(target,current)

#target=200
#current=GO_THERE(target,current)

