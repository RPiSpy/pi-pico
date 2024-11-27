from machine import I2C, Pin
import time

import fonts
from ST7567S import st7567s

# Configuration
I2C_SCL_PIN = 1  # GPIO pin for I2C SCL
I2C_SDA_PIN = 0  # GPIO pin for I2C SDA

# Screen configuration
LCD_I2C_ADDRESS = 0x3F
LCD_I2C_FREQ = 400000
LCD_WIDTH = 128
LCD_HEIGHT = 64

print("Setup LCD")
lcd = st7567s(I2C_SCL_PIN, I2C_SDA_PIN, LCD_WIDTH, LCD_HEIGHT, LCD_I2C_FREQ, LCD_I2C_ADDRESS)

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

lcd.mode(1)
lcd.display_pbm("example.pbm", 0, 0)
lcd.update_screen()

time.sleep(5)

lcd.mode(0)

print("Clear Screen")
lcd.clear()

lcd.draw_bitmap_from_file("example.bmp", 0, 0, 1)
lcd.update_screen()

time.sleep(5)

print("Clear Screen")
lcd.clear()

lcd.draw_text(0, 0, "ST7567 I2C LCD", fonts.FONT_5X8, 1, 1)
lcd.draw_text(0, 56, "RaspberryPi-Spy.co.uk", fonts.FONT_5X8, 1, 1)

lcd.draw_scaled_char(50, 10, 'A', fonts.FONT_5X8, 1, 1)
lcd.draw_scaled_char(58, 10, 'A', fonts.FONT_5X8, 2, 1)
lcd.draw_scaled_char(72, 10, 'A', fonts.FONT_5X8, 3, 1)

lcd.draw_text(50, 35, "123456", fonts.FONT_5X8, 2, 1)

lcd.update_screen()
time.sleep(1)

print("Draw filled circle")
lcd.fill_circle(10, 20, 10, 1)

print("Draw circle")
lcd.draw_circle(32, 20, 10, 1)

lcd.update_screen()
time.sleep(1)

print("Draw rectangle")
lcd.draw_rectangle(0, 32, 20, 20, 1)

print("Draw filled rectangle")
lcd.fill_rectangle(22, 32, 20, 20, 1)

lcd.update_screen()
time.sleep(1)

print("Invert")
lcd.mode(1)

time.sleep(2)

print("Normal")
lcd.mode(0)

time.sleep(2)

print("Display OFF")
lcd.display(0)

time.sleep(2)

print("Display ON")
lcd.display(1)

time.sleep(2)

print("Rotate display")
lcd.rotate_display(1)

time.sleep(2)

print("Rotate display")
lcd.rotate_display(0)
