#!/usr/bin/env python
from RPIO import PWM
import time

Servo1Pin=23
Servo2Pin=18

servo = PWM.Servo()

# Set servo on Servo1Pin to 1200us (1.2ms)
#servo.set_servo(Servo1Pin, 1200)


# Set servo on Servo1Pin to 2000s (2.0ms)
servo.set_servo(Servo1Pin, 2000)

time.sleep(5)

# Clear servo on Servo1Pin
servo.stop_servo(Servo1Pin)
