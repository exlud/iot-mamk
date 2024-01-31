# By default, characters are 8x8 pixels including space
# outter rectangle: 128*64
# inner rectangle for 6 characters: 48*8
# offset: (64-24)*(32-4) = 40*28

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

#Create the I2C connection
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
#Initialize the OLED display
WIDTH =128
HEIGHT= 64
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

#Button
button = Pin(11, Pin.IN, Pin.PULL_UP)

#States
previous = 1
displayFlag = 0

while True:
  current = button.value()
  if current != previous:
    previous = current
    if current == 0:
        if displayFlag == 0:
            oled.text("Lu DAI", 40, 28)
            oled.show()
            displayFlag = 1
        else:
            oled.fill(0)
            oled.show()
            displayFlag = 0
  time.sleep(0.1)

