# ここにコードを書いてね :-
from machine import Pin
import time

pin = Pin(2, Pin.OUT)

while True:
    pin.on()
    time.sleep(1)
    pin.off()
    time.sleep(1)

