#https://docs.micropython.org/en/v1.8/esp8266/esp8266/tutorial/network_basics.html

import network

def activeAp():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid='aquionomedarede')
    ap.config(authmode=3, password='aquisuasenha')
    print('Ap mode activate.')