#Ex8a. the light sensor will give out reading
#based on the light intensity of the location
#65535 being total darkness
#0 being total brightness
#these values depends on the light sensor which can be tweaked
from machine import Pin, ADC
from time import sleep
light_sensor=ADC(Pin(28))
relay=Pin(16,Pin.OUT)

while True:
    reading=light_sensor.read_u16()
    
    #based on what you get from reading
    #turn the street lights on or off
    #refer to light_sensor_analog.py for reference
    
    sleep(1)
          