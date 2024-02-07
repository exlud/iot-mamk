import machine
import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

def calculate_voltage(ad):
    return (ad / 65536) * 3.3

def calculate_temperature(voltage):
    return 27 - ( voltage- 0.706)/0.001721

def append_temperature(sequence, T):
    sequence.pop(0)
    sequence.append(T)

def smooth_temperature(sequence):
    return sum(sequence)/len(sequence)

def sample_temperature():
    ad = adc4.read_u16()
    voltage = calculate_voltage(ad)
    T = calculate_temperature(voltage)
    return T

def display_temperature(temperature):
    text = "{:.2f}".format(temperature)
    oled.fill(0)
    oled.text(text, 0, 0)
    oled.show()

#OLED setup
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
WIDTH =128
HEIGHT= 64
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)


#ADC setup
adc4 = machine.ADC(4)
sequence = []
T = sample_temperature()
sequence.extend([T, T, T, T, T])

while True:
    T = sample_temperature()
    append_temperature(sequence, T)
    T_smoothed = smooth_temperature(sequence)
    display_temperature(T_smoothed)
    
    time.sleep(1)
