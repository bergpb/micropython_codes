import machine
from machine import Pin
from time import sleep_ms

led = machine.Pin(2, Pin.OUT, value=1)

for i in range(5):
    led(0)
    sleep_ms(50)
    led(1)
    sleep_ms(50)
 