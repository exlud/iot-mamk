from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
import sys

#Create the I2C connection
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)

#Initialize the OLED display
WIDTH =128
HEIGHT= 64
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

print("Tell me something and I can echo!")
text = sys.stdin.readline()
text = text[:-1]
remain = len(text)
line = 0
while remain > 0:
    oled.text(text[line*16:line*16+16], 0, line*8)
    remain -= 16
    line += 1

oled.show()

#Clear the screen
button = Pin(11, Pin.IN, Pin.PULL_UP)
import time
while True:
    if button.value() == 0:
        oled.fill(0)
        oled.show()
    time.sleep(0.1)

