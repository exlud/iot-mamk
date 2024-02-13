import mip
import network
from time import sleep

# Function to install MQTT
def install_mqtt():
    try:
        mip.install("umqtt.simple")
    except Exception as e:
        print(f"Could not install MQTT: {e}") 

# Main program
install_mqtt()