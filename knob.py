#!/usr/bin/env python
#
# Raspberry Pi Rotary Test Encoder Class
#
# Author : Bob Rathbone
# Site   : http://www.bobrathbone.com
#
# This class uses a standard rotary encoder with push switch
#
import subprocess
import sys
import time
from rotary_class import RotaryEncoder

# Define GPIO inputs (BCM)
PIN_A = 23              # Pin 16
PIN_B = 24             # Pin 18
BUTTON = 25     # Pin 22

# This is the event callback routine to handle events
def switch_event(event):
        if event == RotaryEncoder.CLOCKWISE:
              subprocess.call(['mpc', 'volume', '+2' ])
              time.sleep(.2)
        elif event == RotaryEncoder.ANTICLOCKWISE:
              subprocess.call(['mpc', 'volume', '-2' ])
              time.sleep(.2)
        elif event == RotaryEncoder.BUTTONDOWN:
              subprocess.call(['mpc', 'toggle' ])
        #elif event == RotaryEncoder.BUTTONUP:
              #print "Button up"
        return

# Define the switch
rswitch = RotaryEncoder(PIN_A,PIN_B,BUTTON,switch_event)

while True:
        time.sleep(0.5)
