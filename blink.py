#-----------------------------------------------------------------------------#
# Blink
#
# Micropython code for Raspberry Pi Pico w
#
# File     : blink.py 
# Source   : https://github.com/RPiSpy/pi-pico
#
# Desc     : Blink the on-board LED
# Hardware : Pi Pico or Pi Pico W
# Software : n/a
#
# Author   : Matt Hawkins
# Website  : https://www.raspberrypi-spy.co.uk/
#-----------------------------------------------------------------------------#

from machine import Pin, Timer

led = Pin("LED", Pin.OUT)

# Create timer object
timer = Timer()

# Define function to toggle LED state
def blink(timer):
    led.toggle()

# Setup timer to call blink function every 2 seconds
timer.init(freq=2, mode=Timer.PERIODIC, callback=blink)
