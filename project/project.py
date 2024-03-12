from machine import Pin
import time
import dht
from umqtt.simple import MQTTClient
import urequests

# use button to fake an input event of PIR sensor
# return:
#   1: no human body approximate
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

# temperature control
margin = 1 # margin window +/-, centered at the target temperature
heating = Pin(4, Pin.OUT, Pin.PULL_UP)
cooling = Pin(5, Pin.OUT, Pin.PULL_UP)
def heating_up():
    heating.on()
    cooling.off()
def cooling_down():
    heating.off()
    cooling.on()
def suspend():
    heating.off()
    cooling.off()
# we want to achieve the same temperature as in Marseille
# fr/marseille
# br/rio-de-janeiro
# is/reykjavik
def target():
    r = urequests.get("https://meteocast.net/temperature/br/rio-de-janeiro/")
    anchor = r.content.find(b'tempnow')
    div = r.content[anchor:anchor + 180]
    r.close()
    anchor2 = div.find(b'bibi') + 6
    inner = div[anchor2:anchor2+5]
    non_printable_index = 0
    for byte in inner:
        if (byte < 32 or byte > 127):
            break
        non_printable_index += 1
    
    content = inner[:non_printable_index]
    temperature = int(content.decode('utf-8'))
    
    return temperature

target = target()

# 1 for heating
# 0 for cooling
def init_direction():
    temperature, humidity = scan_temperature()
    if(temperature < target):
        direction = 1
    else:
        direction = 0

direction = init_direction()
suspend()

# data publish
BROKER = "broker.emqx.io"
mqtt_client=MQTTClient("", BROKER)
def init_data_channel():
    mqtt_client.connect(clean_session=True)

init_data_channel()

def publish_data(temperature, humidity):
    topic_temperature = "testtopic/lu/temperature"
    topic_humidity = "testtopic/lu/humidity"
    mqtt_client.publish(topic_temperature, f"{temperature}")
    mqtt_client.publish(topic_humidity, f"{humidity}")

# main process, scheduled in time slot
slot = 0
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
    
    if(slot == 9):
        print(temperature)
        print(target)
        print(direction)
        if(direction == 1): # heating
            if(temperature > (target + margin)):
                cooling_down()
                direction = 0
            else:
                if(temperature > target):
                    suspend()
                else:
                    heating_up()
        else: # cooling
            if(temperature < (target - margin)):
                heating_up()
                direction = 1
            else:
                if(temperature < target):
                    suspend()
                else:
                    cooling_down()
    
    # schedule 30 time slot
    slot = slot + 1
    slot = slot % 30
    time.sleep_ms(100)