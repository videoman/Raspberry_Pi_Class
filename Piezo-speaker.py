#!/usr/bin/env python
from RPIO import PWM
import time

BeeperPIN=24

# Setup PWM and DMA channel 0
PWM.setup()
PWM.init_channel(0)

# Add some pulses to the subcycle
PWM.add_channel_pulse(0, BeeperPIN, 10, 10)
time.sleep(2)
PWM.add_channel_pulse(0, BeeperPIN, 100, 50)
time.sleep(2)

# Stop PWM for specific GPIO on channel 0
PWM.clear_channel_gpio(0, BeeperPIN)

# Shutdown all PWM and DMA activity
PWM.cleanup()
