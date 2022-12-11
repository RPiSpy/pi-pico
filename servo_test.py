#-----------------------------------------------------------------------------#
# Servo Test
#
# Micropython code for Raspberry Pi Pico w
#
# File     : police-lights.py
# Source   : https://github.com/RPiSpy/pi-pico
#
# Desc     : Test file to operate servo over operating range
# Hardware : Pi Pico or Pi Pico W
# Software : N/A
#
# Author   : Matt Hawkins
# Website  : https://www.raspberrypi-spy.co.uk/
#-----------------------------------------------------------------------------#

import time
from machine import Pin, PWM

# Prepare on-board LED
led = Pin("LED", Pin.OUT)

# Adjust for your servo.
# 0 duty cycle is 0
# Full duty cycle is 65535
# 1ms out of 20ms = 65535/20 = 3276
# 2ms out of 2oms = 65535/10 = 6552
# but cheap servos don't follow the maths.
# So getting the full range requires trial
# and error.
SERVO_MAX  = 7500
SERVO_MIN  = 2000

# Pulse width of 20ms is frequency of 50Hz
SERVO_FREQ = 50

# Set GPIO that servo signal is connected to
SERVO_GPIO = 16

# Create PWM channel
pwm = PWM(Pin(SERVO_GPIO))
pwm.freq(SERVO_FREQ)

max = SERVO_MAX
min = SERVO_MIN
mid = int((max+min)/2)

# Max position
pwm.duty_u16(max)
time.sleep(1)

# Middle position
pwm.duty_u16(mid)
time.sleep(1)

# Minimum position
pwm.duty_u16(min)
time.sleep(1)

while True:

    # Slowly rotate from min to max
    for position in range(min,max,50):
        pwm.duty_u16(position)
        print(position)
        led.toggle()
        time.sleep(0.1)
    led.off()
    time.sleep(2)

    # Slowly rotate from max to min
    for position in range(max,min,-50):
        pwm.duty_u16(position)
        print(position)
        led.toggle()
        time.sleep(0.01)
    led.off()
    time.sleep(2)
