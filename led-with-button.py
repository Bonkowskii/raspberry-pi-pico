import utime
from machine import Pin

led_pin = machine.Pin(16, machine.Pin.OUT)
led_pin1= machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(15, Pin.IN, Pin.PULL_DOWN)

def blink():
    led_pin.value(1)
    utime.sleep(0.1)
    led_pin.value(0)
    utime.sleep(0.1)

def blink1():
    led_pin1.value(1)
    utime.sleep(0.1)
    led_pin1.value(0)
    utime.sleep(0.1)
    
while True:
    if button.value() ==1:
        print(button.value())
        blink()
    print(button.value())
led_pin.value(0)
led_pin1.value(0)


