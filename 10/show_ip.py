from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

#Create the I2C connection
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
#Initialize the OLED display
WIDTH =128
HEIGHT= 64
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

import network
wlan = network.WLAN(network.STA_IF)
oled.fill(0)
oled.text("IP Address:", 0, 0)
oled.text(wlan.ifconfig()[0], 0, 8)
oled.show()

 


