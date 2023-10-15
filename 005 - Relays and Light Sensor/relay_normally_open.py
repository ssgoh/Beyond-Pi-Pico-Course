from machine import Pin
relay=Pin(16,Pin.OUT)

#NORMALLY OPEN
relay.value(0) # to turn on relay

input('Hit Enter to Continue')

relay.value(1) # to turn off relay
