from machine import Pin, Timer

led = Pin("LED", Pin.OUT)

# Create timer object
timer = Timer()

# Define function to toggle LED state
def blink(timer):
    led.toggle()

# Setup timer to call blink function every 2 seconds
timer.init(freq=2, mode=Timer.PERIODIC, callback=blink)
