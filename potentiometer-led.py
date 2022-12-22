#-----------------------------------------------------------------------------#
# Potentiometer & LED
#
# Micropython code for Raspberry Pi Pico w
#
# File     : potentiometer-led.py
# Source   : https://github.com/RPiSpy/pi-pico
#
# Desc     : Read a potentiometer using ADC and control LED brightness
# Hardware : Pi Pico or Pi Pico W
#            3 pin potentiometer
#            LED & resistor (56-330 ohm)
# Software : n/a
#
# Author   : Matt Hawkins
# Website  : https://www.raspberrypi-spy.co.uk/
#-----------------------------------------------------------------------------#

import time
from machine import Pin,ADC,PWM

# Define GPIO pins our hardware is connected to
ADC_GPIO = 27
LED_GPIO = 15

# Setup ADC
adc_pin = Pin(ADC_GPIO, mode=Pin.IN)
adc_obj = ADC(adc_pin)

# Setup PWM for LED
pwm = PWM(Pin(LED_GPIO))
pwm.freq(1000)

while True:
    
    # Read ADC value
    adc_val = adc_obj.read_u16()
    
    # Set PWM duty value to ADC value
    pwm.duty_u16(adc_val)
    
    # Wait 1 second
    time.sleep(1)
