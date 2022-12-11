#-----------------------------------------------------------------------------#
# Potentiometer
#
# Micropython code for Raspberry Pi Pico w
#
# File     : potentiometer.py 
# Source   : https://github.com/RPiSpy/pi-pico
#
# Desc     : Read a potentiometer using ADC
# Hardware : Pi Pico or Pi Pico W
#            3 pin potentiometer 
# Software : n/a
#
# Author   : Matt Hawkins
# Website  : https://www.raspberrypi-spy.co.uk/
#-----------------------------------------------------------------------------#

import time
from machine import Pin,ADC

# Setup ADC
adc_pin = Pin(27, mode=Pin.IN)
adc_obj = ADC(adc_pin)

# ADC value when voltage is 3.3V
max_adc_val = 65535

while True:
    
    # Read ADC value
    adc_val = adc_obj.read_u16()
    
    # Calculate percentage based on max value
    adc_per = round((adc_val/max_adc_val)*100)

    # Output values
    print(adc_val, " - ", adc_per, "%")

    # Wait 1 second
    time.sleep(1)
