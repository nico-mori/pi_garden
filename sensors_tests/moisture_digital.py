from gpiozero import DigitalInputDevice
import time

d0_input = DigitalInputDevice(4)

while True:
    if (not d0_input.value):
        print('Moisture reached')
    else:
        print('No water')
        time.sleep(2)    
    
