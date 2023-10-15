#Light Sensor Module.  Digital Output (DO Pin)
#Sensor will only detect presence or absence of light
#It will not show you the intensity of light it detects
from machine import Pin, ADC
from time import sleep
light_sensor=ADC(Pin(28))
while True:
    print(light_sensor.read_u16())
    sleep(1)
          