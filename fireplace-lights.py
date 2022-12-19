#-----------------------------------------------------------------------------#
# Fireplace Lights
#
# Micropython code for Raspberry Pi Pico w
#
# File     : fireplace-lights.py 
# Source   : https://github.com/RPiSpy/pi-pico
#
# Desc     : Simulate a fire place with two neopixels
# Hardware : Pi Pico or Pi Pico W
#            2 WS2812 NeoPixels
# Software : Requires neopixel.py
#
# Author   : Matt Hawkins
# Website  : https://www.raspberrypi-spy.co.uk/
#
# In memory of Diana Keating who taught me to make stuff
# as soon as I could hold a pen.
#
#-----------------------------------------------------------------------------#

import time
import random
from neopixel import Neopixel

# NeoPixel settings
NEOPIXEL_GPIO  = 26
NEOPIXEL_COUNT = 2

BRIGHTNESS_MAX = 200
BRIGHTNESS_MIN = 10

# Amound of Red, Green and Blue to use
COLOUR_RED   = 255
COLOUR_GREEN = 80
COLOUR_BLUE  = 0

pixels = Neopixel(NEOPIXEL_COUNT, 0, NEOPIXEL_GPIO, "GRB")

while True:

    # For each pixel ...
    for pixel in range(0,NEOPIXEL_COUNT):

        # Set random brightness between Min and Max values
        brightness_p = random.randint(BRIGHTNESS_MIN,BRIGHTNESS_MAX)
        
        # Set starting colours of neopixels
        # Max red, zero blue and enough random green to give yellows and oranges
        colour_p = (COLOUR_RED,random.randint(0,COLOUR_GREEN),COLOUR_BLUE)

        # Set pixel colour and brightness
        pixels.set_pixel(pixel, colour_p, brightness_p)
        pixels.show()

        # Wait random time between 50-80 milliseconds
        # to give a flicker effect
        time.sleep_ms(random.randint(50,80))