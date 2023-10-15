from machine import Pin
relay=Pin(16,Pin.OUT)

#NORMALLY CLOSED
relay.value(1) # to turn on relay

input('Hit Enter to Continue')

relay.value(0) # to turn off relay