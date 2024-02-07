import machine
import time

def calculate_voltage(ad):
    return (ad / 65536) * 3.3

def calculate_temperature(voltage):
    return 27 - ( voltage- 0.706)/0.001721

adc4 = machine.ADC(4)

T1 = calculate_temperature(calculate_voltage(14147))
T2 = calculate_temperature(calculate_voltage(14148))
print("Temperature Resolution:{}".format(T1 - T2))

while True:
    ad = adc4.read_u16()
    voltage = calculate_voltage(ad)
    T = calculate_temperature(voltage)
    
    text = "AD value: {} Temperature value: {:.2f}".format(ad, T)
    print(text)
    
    time.sleep(2)