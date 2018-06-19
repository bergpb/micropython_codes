# teste de update

from machine import I2C, Pin
import ssd1306
import json
from time import sleep

i2c = I2C(-1, Pin(5), Pin(4))

display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)

for i in range(100):
    
  if i % 2 == 0:
    display.text('{}'.format(i),0,0) # text, position x, position y
    display.show()
    display.fill(0)
    
  else:
    display.text('res > 0',0,0) # text, position x, position y
    display.show()
    display.fill(0)
  
  sleep(0.1)