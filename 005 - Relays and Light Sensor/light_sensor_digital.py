#Light Sensor Module.  Digital Output (DO Pin)
#Sensor will only detect presence or absence of light
#It will not show you the intensity of light it detects
from machine import Pin, ADC
from time import sleep
light_sensor=Pin(15)
while True:
    print(light_sensor.value())
    sleep(1)
          