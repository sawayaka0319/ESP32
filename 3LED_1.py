# 3つのLEDを点滅改

from machine import Pin
import time

pin_no = [13, 27, 33]
led = {}

led[0] = Pin(pin_no[0], Pin.OUT)
led[1] = Pin(pin_no[1], Pin.OUT)
led[2] = Pin(pin_no[2], Pin.OUT)

while True:
    for i in [0, 1, 2]:
        led[i].on()
        time.sleep(1)
        led[i].off()
        time.sleep(1)


