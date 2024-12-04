#--------------------------------------
#    ___  ___  _ ____          
#   / _ \/ _ \(_) __/__  __ __ 
#  / , _/ ___/ /\ \/ _ \/ // / 
# /_/|_/_/  /_/___/ .__/\_, /  
#                /_/   /___/   
#
#  ST7567S LCD 128x64 Screen Library 
#
#  Demo script
#
# Author : Matt Hawkins
# Date   : 28/11/2024
#
# https://www.raspberrypi-spy.co.uk/
#
# The MIT License (MIT)
# Copyright 2024 Matt Hawkins
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#--------------------------------------

#Import standard libraries
from machine import I2C, Pin
import time

# Import local libraries
import fonts
from ST7567S import st7567s

# Configuration
I2C_SCL_PIN = 1  # GPIO pin for I2C SCL
I2C_SDA_PIN = 0  # GPIO pin for I2C SDA

# Screen configuration
LCD_WIDTH = 128
LCD_HEIGHT = 64
LCD_I2C_ADDRESS = 0x3F

print("Setup LCD")
lcd = st7567s(I2C_SCL_PIN,I2C_SDA_PIN,LCD_I2C_ADDRESS)

devices = lcd.i2c.scan()
if devices:
    for d in devices:
        print(hex(d))
else:
    print('no i2c devices')

print("Initialise")
lcd.init()

print("Set Contrast")
lcd.set_contrast(10)

print("Clear Screen")
lcd.clear()

lcd.draw_pbm_file("example.pbm", 0, 0)
lcd.update_screen()

time.sleep(2)

print("Clear Screen")
lcd.clear()

lcd.draw_bmp_file("example.bmp", 0, 0, True)
lcd.update_screen()

time.sleep(2)

print("Clear Screen")
lcd.clear()

lcd.draw_text(0, 0, "ST7567 I2C LCD", fonts.FONT_5X8, 1, 1)
lcd.draw_text(0, 56, "RaspberryPi-Spy.co.uk", fonts.FONT_5X8, 1, 1)

print("Draw filled circle")
lcd.fill_circle(10, 20, 10, 1)

print("Draw circle")
lcd.draw_circle(32, 20, 10, 1)

print("Draw rectangle")
lcd.draw_rectangle(0, 32, 20, 20, 1)

print("Draw filled rectangle")
lcd.fill_rectangle(22, 32, 20, 20, 1)

lcd.update_screen()
time.sleep(1)

lcd.draw_scaled_char(50, 10, 'A', fonts.FONT_5X8, 1, 1)
lcd.draw_scaled_char(58, 10, 'A', fonts.FONT_5X8, 2, 1)
lcd.draw_scaled_char(72, 10, 'A', fonts.FONT_5X8, 3, 1)

lcd.draw_text(50, 35, "123456", fonts.FONT_5X8, 2, 1)

lcd.draw_line(50, 52, 120, 52, 1)

lcd.draw_bmp_file("example32x32.bmp", 96, 0, True)

lcd.update_screen()
time.sleep(1)

print("Invert")
lcd.mode(1)

time.sleep(2)

print("Normal")
lcd.mode(0)

time.sleep(1)

print("Display OFF")
lcd.display(0)

time.sleep(1)

print("Display ON")
lcd.display(1)

time.sleep(1)

print("Rotate display")
lcd.rotate_display(1)

time.sleep(1)

print("Rotate display")
lcd.rotate_display(0)
