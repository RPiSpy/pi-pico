#-----------------------------------------------------------------------------#
# LED
#
# Micropython code for Raspberry Pi Pico w
#
# File     : led.py 
# Source   : https://github.com/RPiSpy/pi-pico
#
# Desc     : Control an LED
# Hardware : Pi Pico or Pi Pico W
#            LED & resistor (56-330 ohm)
# Software : n/a
#
# Author   : Matt Hawkins
# Website  : https://www.raspberrypi-spy.co.uk/
#-----------------------------------------------------------------------------#

import time
from machine import Pin

# Configure GPIO pin 15 as output
led = Pin(15, Pin.OUT)

while True:
    # Toggle LED on/off
    led.toggle()
    
    # Wait 1 second
    time.sleep(1)