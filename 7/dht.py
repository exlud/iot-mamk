from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import dht
import time
data_pin = Pin(13, Pin.IN, Pin.PULL_UP)
sensor = dht.DHT22(data_pin)

#Create the I2C connection
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
#Initialize the OLED display
WIDTH =128
HEIGHT= 64
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

def read_sensor():
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        print_sensor_data(temperature, humidity)
        display_sensor_data(temperature, humidity)
    except OSError as e:
        print("Error reading data from the sensor")

def print_sensor_data(temperature, humidity):
    print("Temperature:{}, Humidity:{}".format(temperature, humidity))
    
def display_sensor_data(temperature, humidity):
    text1 = 'Tempera: {}'.format(temperature)
    text2 = 'Humidity: {}'.format(humidity)
    oled.fill(0)
    oled.text(text1, 0, 0)
    oled.text(text2, 0, 8)
    oled.show()

while True:
    read_sensor()
    time.sleep(1)