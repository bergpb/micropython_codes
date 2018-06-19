#-*-coding: utf8 -*-

import network
import machine
from time import sleep_ms

led = machine.Pin(2, machine.Pin.OUT, value = 1)

def connect():
    ssid = 'suaredewifi'
    password =  'senhadasuarede'
    
    station = network.WLAN(network.STA_IF)
 
    if station.isconnected() == True:
        print('Sucesso ao conectar!')
 
    station.active(True)
    
    station.connect(ssid, password)
 
    while station.isconnected() == False:
        print('.', end='')
        led(0)
        sleep_ms(50)
        led(1)
        sleep_ms(50)
 
    print(station.ifconfig())
