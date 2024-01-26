from machine import Pin
import time

def dit():
    led.toggle()
    time.sleep_ms(500)
    led.toggle()
    time.sleep_ms(500)

def dah():
    led.toggle()
    time.sleep_ms(1500)
    led.toggle()
    time.sleep_ms(500)

def letter_s():
    dit()
    dit()
    dit()
    time.sleep_ms(1500)

def letter_o():
    dah()
    dah()
    dah()
    # break between letters
    time.sleep_ms(1500)


#Create a pin instance for the LED
led = Pin("LED", Pin.OUT)
#Bring it to off state
if led.value() == 1:
    led.toggle()

#Enter an infinite loop
while True:
  letter_s()
  letter_o()
  letter_s()
  # between messages
  time.sleep_ms(3500)