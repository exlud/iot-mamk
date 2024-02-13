import network
from time import sleep
from umqtt.simple import MQTTClient
from machine import Pin
import dht
import time

data_pin = Pin(13, Pin.IN, Pin.PULL_UP)
sensor = dht.DHT22(data_pin)

BROKER = "broker.emqx.io"
def connect_mqtt():
    mqtt_client=MQTTClient("", BROKER)
    mqtt_client.connect(clean_session=True)
    return mqtt_client

def read_sensor():
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        return temperature, humidity
    except OSError as e:
        print("Error reading data from the sensor")

def print_sensor_data(temperature, humidity):
    print("Temperature:{}, Humidity:{}".format(temperature, humidity))

# Main program
if __name__ == "__main__":
    # Connect to MQTT
    try:
        mqtt_client=connect_mqtt()
    except Exception as e:
        print(f"Failed to connect to MQTT: {e}")

    # Publish MQTT message
    try:
        while True:
            # Sending a message every 5 seconds.
            topic_temperature = "testtopic/lu/temperature"
            topic_humidity = "testtopic/lu/humidity"
            temperature, humidity = read_sensor()
            print_sensor_data(temperature, humidity)
            mqtt_client.publish(topic_temperature, f"{temperature}")
            mqtt_client.publish(topic_humidity, f"{humidity}")
            sleep(10)
    except Exception as e:
        print(f"Failed to send MQTT message: {e}")