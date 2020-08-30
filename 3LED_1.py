# 3つのLEDを点滅改

import machine
import time

pin13 = [13,27,33]

while True:
    machine.Pin(33, machine.Pin.OUT).on()
    time.sleep_ms(500)
    machine.Pin(33, machine.Pin.OUT).off()
    time.sleep_ms(500)


