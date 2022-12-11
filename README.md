# pi-pico
This repository contains scripts relating to the Raspberry Pi Pico and Pi Pico W. They are most likely to be written in MicroPython.
They assume you have a working Pico and are familiar with uploading and running scripts on it.

# Scripts
Here is a full list of scripts with any relevant details. Each script also contains comments at the top of the file.
## blink.py
This script blinks the on-board LED. It doesn't require any additional hardware.
## led.py
This script turns an LED on and off.
## led_pwm.py
This script controls the brightness
## police-lights.py
This script flashes two neopixels in a police style pattern. It requires two neopixels to be connected to a GPIO pin, The pin number can be defined in the script.
## potentiometer.py
This script uses a potentiometer to feed an ADC channel with 0-3.3V and print the percentage.
## potentiometer_led.py
This script uses a potentiometer to define the brightness level of an LED using PWM.
## servo_test.py
This script operates a standard servo between the defined

# Editor
The scripts were tested using Thonny.