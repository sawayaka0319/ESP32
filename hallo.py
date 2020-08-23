# ここにコードを書いてね :-
import machine
import time

pin = machine.Pin(27, machine.Pin.OUT)

while True:
    pin.on()
    time.sleep(1)
    pin.off()
    time.sleep(1)
