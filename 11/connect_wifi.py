import network
from time import sleep

def scan_wlan():
    aps = wlan.scan()
    for ap in aps:
        ssid = ap[0].decode("utf-8")
        if ssid != '':
            ssids.append(ssid)

def select_wlan():
    for index, value in enumerate(ssids):
        print(f"{index}: {value}")
    number = int(input("Choose a Wi-Fi by number: "))
    return ssids[number]

# Function to connect to WLAN
def connect_wlan(ssid):
    password = input("Input Password:")
    wlan.connect(ssid, password)
    # Attempt to connect once per second
    while not wlan.isconnected() == True:
        print("Connecting... ")
        sleep(1)
    # Print the IP address of the Pico
    print("Connection successful. Pico IP:", wlan.ifconfig()[0])

# Main program
ssids = []
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
scan_wlan()
ssid = select_wlan()
connect_wlan(ssid)