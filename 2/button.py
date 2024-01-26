from machine import Pin
import time
button = Pin(11, Pin.IN, Pin.PULL_UP)
previous = 1
count = 0
# detect fall edge
while True:
  current = button.value()
  if current != previous:
    previous = current
    if current == 0:
      count = count + 1
      print(count)
  time.sleep(0.1)