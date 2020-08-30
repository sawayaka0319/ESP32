# 3つのLEDを点滅

import machine
import time

pin13 = machine.Pin(13, machine.Pin.OUT)
pin27 = machine.Pin(27, machine.Pin.OUT)
pin33 = machine.Pin(33, machine.Pin.OUT)

while True:
    pin13.on()
    time.sleep_ms(500)
    pin13.off()
    pin27.on()
    time.sleep_ms(500)
    pin27.off()
    pin33.on()
    time.sleep_ms(500)
    pin33.off()
