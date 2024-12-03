from machine import Pin
import LED_Func

Led = Pin(48, Pin.OUT)

LED_Func.LedNo(Led, 1)
LED_Func.LedOff(Led, 1)
LED_Func.LedNo(Led, 1)
LED_Func.LedOff(Led, 1)