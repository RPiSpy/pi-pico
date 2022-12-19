#-----------------------------------------------------------------------------#
# Police Lights
#
# Micropython code for Raspberry Pi Pico w
#
# File     : police-lights.py 
# Source   : https://github.com/RPiSpy/pi-pico
#
# Desc     : Police style light pattern with two neopixels
# Hardware : Pi Pico or Pi Pico W
#            2 WS2812 NeoPixels
# Software : Requires neopixel.py
#
# Author   : Matt Hawkins
# Website  : https://www.raspberrypi-spy.co.uk/
#-----------------------------------------------------------------------------#

import time
from neopixel import Neopixel

# NeoPixel settings
NEOPIXEL_GPIO = 26
NEOPIXEL_BRIGHTNESS_LOW  = 1
NEOPIXEL_BRIGHTNESS_HIGH = 100

COLOUR_BLUE = (0,0,255)
COLOUR_RED  = (255, 0, 0)

pixels = Neopixel(2, 0, NEOPIXEL_GPIO, "GRB")

brightness_l = NEOPIXEL_BRIGHTNESS_LOW
brightness_h = NEOPIXEL_BRIGHTNESS_HIGH

# Quick flash delay (ms)
delay_short = 35
# Delay between switching pixels (ms)
delay_long = 300

# Set starting colours of neopixels
colour_p1 = COLOUR_RED
colour_p2 = COLOUR_BLUE

while True:

    # Quick flash Pixel #1
    for x in range(0,3):
        time.sleep_ms(delay_short)

        pixels.set_pixel(0, colour_p1, brightness_l)
        pixels.set_pixel(1, colour_p2, brightness_h)
        pixels.show()
    
        time.sleep_ms(delay_short)

        pixels.set_pixel(0, colour_p1, brightness_l)
        pixels.set_pixel(1, colour_p2, brightness_l)
        pixels.show()

    time.sleep_ms(delay_long)

    # Quick Flash Pixel #2
    for x in range(0,3):
        time.sleep_ms(delay_short)

        pixels.set_pixel(0, colour_p1, brightness_h)
        pixels.set_pixel(1, colour_p2, brightness_l)
        pixels.show()
    
        time.sleep_ms(delay_short)

        pixels.set_pixel(0, colour_p1, brightness_l)
        pixels.set_pixel(1, colour_p2, brightness_l)
        pixels.show()

    time.sleep_ms(delay_long)
    
    # Swap pixel colours
    if colour_p1 == COLOUR_RED:
        colour_p1 = COLOUR_BLUE
        colour_p2 = COLOUR_RED
    else:
        colour_p1 = COLOUR_RED
        colour_p2 = COLOUR_BLUE