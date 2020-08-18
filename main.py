# 起動テスト用
import machine
import time

pin13 = machine.Pin(13, machine.Pin.OUT)
pin19 = machine.Pin(19, machine.Pin.OUT)
pin19.off()

while True:
  pin13.on()
  time.sleep_ms(500)
  pin13.off()
  time.sleep_ms(500)
