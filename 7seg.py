# 7seg
from machine import Pin
import time

pin_no = [21, 23, 26, 33, 25, 22, 19, 32]
pin_com = [15, 2, 4, 5]
pattern = ((0,0,0,0,0,0,1,1),(1,0,0,1,1,1,1,1),(0,0,1,0,0,1,0,1),(0,0,0,0,1,1,0,1),
           (1,0,0,1,1,0,0,1),(0,1,0,0,1,0,0,1),(0,1,0,0,0,0,0,1),(0,0,0,1,1,1,1,1),
           (0,0,0,0,0,0,0,1),(0,0,0,0,1,0,0,1))

while True:
    # 7seg A-G,DP on:0 off:1
    for i in [0,1,2,3,4,5,6,7]:
        Pin(pin_no[i], Pin.OUT).value(pattern[9][i])
    # 7seg com1-4 on:1 off:0
    for l in pin_com:
        Pin(l, Pin.OUT).value(1)
        time.sleep_ms(1)
        Pin(l, Pin.OUT).value(0)

