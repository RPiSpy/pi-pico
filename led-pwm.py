#-----------------------------------------------------------------------------#
# LED Brightness control with Pulse Width Modulation
#
# Micropython code for Raspberry Pi Pico w
#
# File     : led-pwm.py
# Source   : https://github.com/RPiSpy/pi-pico
#
# Desc     : Cycle the brightness of an LED using PWM
# Hardware : Pi Pico or Pi Pico W
#            LED
#            LED & resistor (56-330 ohm)
# Software : n/a
#
# Author   : Matt Hawkins
# Website  : https://www.raspberrypi-spy.co.uk/
#-----------------------------------------------------------------------------#

import time
from machine import Pin,PWM

pwm = PWM(Pin(15))

pwm.freq(1000)

while True:

    # Loop brightness from min to max
    for duty in range(65535):
        pwm.duty_u16(duty)
        time.sleep_us(5)
    # Loop brightness from max to min
    for duty in range(65025, 0, -1):
        pwm.duty_u16(duty)
        time.sleep_us(5)