from machine import Pin
import time
import random
button = Pin(11, Pin.IN, Pin.PULL_UP)
previous = 1
while True:
  current = button.value()
  # fall edge detect
  if current != previous:
    previous = current
    if current == 0:
      print(random.randint(1, 6))
  time.sleep(0.1)
