# Description
For this exercise you need to wire a push button to your Pico board. Make sure your Pico board is not powered before making any wiring changes.
1. Attach a push button over the junction of the breadboard so that there are two pins on both sides of the
junction.
2. Connect the bottom left pin of the push button to ground (GND) on pin 18 on the Pico W.
3. Connect the top left pin of the push button to pin GP15 on the Pico W.
4. ~~The connection should look as follows:~~
5. The following program sets up pin 15 as an input pin and enters a loop where the status of the button is
  checked on each round. If the button is pressed, “Button was pressed” is printed out to the console. Copy
  and run the program in Thonny to investigate how it works.

  ```python
  from machine import Pin
  import time
  button = Pin(15, Pin.IN, Pin.PULL_UP)
  while True:
  if button.value() == 0:
  	print("Button was pressed")
  time.sleep(0.1)
  ```
6. Modify the program so that it detects each button press exactly once. Add a variable that counts the
button presses and change the print to show how many times the button was pressed.
