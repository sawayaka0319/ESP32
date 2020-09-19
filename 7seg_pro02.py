# 7seg-2
from machine import Pin
import time

pin_no = [21, 23, 26, 33, 25, 22, 19, 32]  #7segのピン番号
pin_com = [15, 2, 4, 5]   #7segの共通ピン番号
pattern = ((0, 0, 0, 0, 0, 0, 1, 1),(1, 0, 0, 1, 1, 1, 1, 1),(0, 0, 1, 0, 0, 1, 0, 1),
           (0, 0, 0, 0, 1, 1, 0, 1),(1, 0, 0, 1, 1, 0, 0, 1),(0, 1, 0, 0, 1, 0, 0, 1),
           (0, 1, 0, 0, 0, 0, 0, 1),(0, 0, 0, 1, 1, 1, 1, 1),(0, 0, 0, 0, 0, 0, 0, 1),
           (0, 0, 0, 0, 1, 0, 0, 1))
seg7_pin = {}
seg7_compin = {}

# pinの初期化
for i in [0, 1, 2, 3, 4, 5, 6, 7]:
    seg7_pin[i] = Pin(pin_no[i], Pin.OUT)
for l in [0, 1, 2, 3]:
    seg7_compin[l] = Pin(pin_com[l], Pin.OUT)
# 関数定義
def led_seg(pa, pi):
    # 7seg A-G,DP on:0 off:1
    for i in [0, 1, 2, 3, 4, 5, 6, 7]:
        seg7_pin[i].value(pattern[pa][i])
    # 7seg com1-4 on:1 off:0
    seg7_compin[pi].value(1)
    time.sleep_ms(1)
    seg7_compin[pi].value(0)

while True:
    for l in range(9999):
        l0 = int(l / 1000)
        l1 = int((l - l0 * 1000) / 100)
        l2 = int(((l - l0 * 1000)- l1 * 100) / 10)
        l3 = int((((l - l0 * 1000)- l1 * 100) - l2 * 10) % 10)
        led_seg(l0, 0)
        led_seg(l1, 1)
        led_seg(l2, 2)
        led_seg(l3, 3)
