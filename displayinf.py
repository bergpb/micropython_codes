#-*- coding: utf8 -*-

from machine import I2C, Pin
import ssd1306
import sys
import urequests
import json
from time import sleep, sleep_ms
import machine

i2c = I2C(-1, Pin(5), Pin(4))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.fill(0)

def getAllInformations():
    display.fill(0)
    display.text('...', 50, 30)
    display.show()
    
    res_coins = urequests.get('https://ionicappsapi.herokuapp.com/api/v1/moedas')
    res_temp = urequests.get('http://api.wunderground.com/api/e4c8e67ba47baa9d/conditions/q/Caucaia.json')
    
    display.fill(0)
    display.text('Updated!', 30, 30)
    display.show()
    
    for i in range(30):
        showWeather(res_temp)
        showCoins(res_coins)
        

def showWeather(res_temp):
    forecast = res_temp.json()
    
    weather = forecast['current_observation']['weather']
    temp_c = str(forecast['current_observation']['temp_c'])
    feels_like = forecast['current_observation']['feelslike_c']
    humid = forecast['current_observation']['relative_humidity']
    last_observation = forecast['current_observation']['observation_time_rfc822']
    wind_gust = forecast['current_observation']['wind_gust_kph']
    temp_min = str(forecast['current_observation']['dewpoint_c'])
    temp_max = str(forecast['current_observation']['heat_index_c'])
    
    display.fill(0)
    display.text(weather + '!!', 0, 0)
    display.text('Temp: ' + temp_c + '/' + feels_like, 0, 10)
    display.text('Humid: ' + humid, 0, 20)
    display.text('Wind: ' + wind_gust, 0, 30)
    display.text('Mi/Ma: ' + temp_min + '/' + temp_max, 0, 40)
    display.text('LO: ' + last_observation[17:22], 0, 50)
    display.show()

    sleep(5)
    
def showCoins(res_coins):
    coins = res_coins.json()
    
    dolar = coins['moedas'][0]['valor']
    bitcoin = coins['moedas'][4]['valor']
    euro = coins['moedas'][3]['valor']
    libra = coins['moedas'][5]['valor']
    peso_arg = coins['moedas'][6]['valor']
    
    display.fill(0)
    display.text('Coins!!', 0, 0)
    display.text('D:' + dolar, 0, 10)
    display.text('B:' + bitcoin, 0, 20)
    display.text('E:' + euro, 0, 30)
    display.text('L:' + libra, 0, 40)
    display.text('P:' + peso_arg, 0, 50)
    display.show()
    
    sleep(5)
    