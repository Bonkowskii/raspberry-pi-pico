from machine import ADC, Pin
import time

led1 = machine.Pin(15, machine.Pin.OUT)
led2 = machine.Pin(14, machine.Pin.OUT)
led3 = machine.Pin(13, machine.Pin.OUT)
ldr = ADC(26)
while True:
    light = ldr.read_u16()
    print("jasnosc:", light)
    time.sleep(0.5)
    if light>25000:
        led1.value(0)
        led3.value(0)
        led2.value(1)
    elif 25000>light>20000:
        led1.value(0)
        led2.value(0)
        led3.value(1)
    else:
        led1.value(1)
        led2.value(0)
        led3.value(0)  

