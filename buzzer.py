#-----------------------------------------------------------------------------#
# Buzzer control with Pulse Width Modulation
#
# Micropython code for Raspberry Pi Pico w
#
# File     : buzzer.py
# Source   : https://github.com/RPiSpy/pi-pico
#
# Desc     : Sound a buzzer using PWM
# Hardware : Pi Pico or Pi Pico W
#            Buzzer (passive type with "+" pin)
# Software : n/a
#
# Author   : Matt Hawkins
# Website  : https://www.raspberrypi-spy.co.uk/
#-----------------------------------------------------------------------------#

import time
from machine import Pin,PWM

# Create PWM object
buzzer = PWM(Pin(15))

# Set frequency
buzzer.freq(500)

# Sound tone
buzzer.duty_u16(5000)
time.sleep(0.5)
buzzer.duty_u16(0)

# Wait 0.5 seconds
time.sleep(0.5)

# Sound tone
buzzer.duty_u16(20000)
time.sleep(0.5)
buzzer.duty_u16(0)