from machine import Pin
import time

def dit():
    led.on()
    time.sleep_ms(500)
    led.off()
    time.sleep_ms(500)

def dah():
    led.on()
    time.sleep_ms(1500)
    led.off()
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
#Default state is off
led = Pin("LED", Pin.OUT, value=0)

#Enter an infinite loop
while True:
  letter_s()
  letter_o()
  letter_s()
  # between messages
  time.sleep_ms(3500)