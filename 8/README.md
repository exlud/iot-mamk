# Description

The Raspberry Pi Pico board has an internal analog temperature sensor. Write a program that reads the
temperature values and prints both the AD value and the temperature values to the console once every 2
seconds.
To calculate the temperature value, you must first convert the digital AD value to voltage.
• Resolution: 16 bits
• Reference voltage: 3.3 V
The you need to use the transfer function for the sensor to calculate the temperature:
𝑇 = 27℃ − (𝑉𝑜𝑢𝑡 − 0.706 𝑉 ) / 1.721 𝑚𝑉/℃

What is the smallest detectable change in temperature measured by the sensor?
