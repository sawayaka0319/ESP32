# タクトスイッチの使い方
import machine

pin13 = machine.Pin(13, machine.Pin.OUT)
pin35 = machine.Pin(35, machine.Pin.IN)

pin13.off()

while 1:
    i = pin35.value()
    if i == 1:
        pin13.on()
    else:
        pin13.off()
