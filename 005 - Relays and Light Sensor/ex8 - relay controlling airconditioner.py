#Ex8 Partially completed
#for example, if you set the threshold temp of
#30 degrees to turn on the air conditioner
from machine import Pin
from time import sleep
import dht

temp_sensor = dht.DHT11(Pin(14))
relay=Pin(16,Pin.OUT)

while True:
    temp_sensor.measure()
    temperature = temp_sensor.temperature()
    
    
    if temperature > 30:
        #activate the air conditioner
        
    else:
        #deactivate the air conditioner
    
    
    sleep(1)
