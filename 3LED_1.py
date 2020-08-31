# 3つのLEDを点滅改

import machine
import time

pin3 = [13,27,33]

while True:
    machine.Pin(pin3.pop(), machine.Pin.OUT).on()
    time.sleep(1)
    machine.Pin(pin3.pop(), machine.Pin.OUT).off()
    time.sleep(1)


