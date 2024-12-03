import time

def LedNo(LedPin = None, Timer = 1):
    if LedPin is None:
        print("LedPin is None")
        return
    LedPin.value(1)
    time.sleep(Timer)
    return

def LedOff(LedPin = None, Timer = 1):
    if LedPin is None:
        print("LedPin is None")
        return
    LedPin.value(0)
    time.sleep(Timer)
    return