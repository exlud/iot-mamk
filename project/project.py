from machine import Pin
import time
import dht
from umqtt.simple import MQTTClient

# use button to fake an input event of PIR sensor
# return:
#   1: no humuan body approximate
#   0: human body approximate
pir = Pin(11, Pin.IN, Pin.PULL_UP)
def scan_pir():
    return pir.value()

# light control
# turn on when human approximate
# turn off when no human approximate
# remain on for at least 3 seconds
light = Pin(19, Pin.OUT, Pin.PULL_UP)
def turn_on_light():
    light.on()
def turn_off_light():
    light.off()
remain = 0

# temperature sensor DH22
data = Pin(13, Pin.IN, Pin.PULL_UP)
sensor = dht.DHT22(data)
def scan_temperature():
    sensor.measure()
    temperature = sensor.temperature()
    humidity = sensor.humidity()
    return temperature, humidity

# data publish
BROKER = "broker.emqx.io"
mqtt_client=MQTTClient("", BROKER)
def init_data_channel():
    mqtt_client.connect(clean_session=True)

def publish_data(temperature, humidity):
    topic_temperature = "testtopic/lu/temperature"
    topic_humidity = "testtopic/lu/humidity"
    mqtt_client.publish(topic_temperature, f"{temperature}")
    mqtt_client.publish(topic_humidity, f"{humidity}")

# main process, scheduled in time slot
slot = 0
init_data_channel()
while True:
    # light control start
    if(scan_pir() == 0):
        remain = 30
    if(remain > 0):
        turn_on_light()
    else:
        turn_off_light()
    remain = remain - 1
    # light control end
    
    # data collect/publish start
    if(slot == 5):
        temperature, humidity = scan_temperature()
        publish_data(temperature, humidity)
    
    # TODO: temperature control
    #if(slot == 9):
    #    http get the target temperature
    #    lazy comparator, to control cooling or heating
    
    # schedule 30 time slot
    slot = slot + 1
    slot = slot % 30
    time.sleep_ms(100)