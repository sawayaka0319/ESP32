# 3つのLEDを点滅改(ダメな方)

from machine import Pin
import time

pin_no = [13, 27, 33]

while True:
    for i in pin_no:
        Pin(i, Pin.OUT).on()
        time.sleep(1)
        Pin(i, Pin.OUT).off()
        time.sleep(1)


