from machine import Pin
import LED_Func

Led = Pin(48, Pin.OUT)

LED_Func.LedOn(LedPin = Led, Interval = 1)
LED_Func.LedOff(LedPin = Led, Interval = 1)
LED_Func.LedOn(LedPin = Led, Interval = 1)
LED_Func.LedOff(LedPin = Led, Interval = 1)
