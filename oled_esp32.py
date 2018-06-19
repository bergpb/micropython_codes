import ssd1306_mod
from time import sleep
from machine import I2C, Pin

i2c = I2C(-1, Pin(22), Pin(21)) # slc sda
oled = ssd1306_mod.SSD1306_I2C(128, 64, i2c)

msg = 'hello world'

def scroll_up_to_down(oled, msg):
    for y in range(0, 12, 1):
        sleep(0.01)
        oled.scroll(0, y) # coordenadas x e y

        if y == 11:
            oled.text(msg, 0, 0)
    oled.show()

scroll_up_to_down(oled, msg)