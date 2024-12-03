import time

def LedNo(LedPin = None, Interval = 1):
    if LedPin is None:
        print("LedPin is None")
        return
    LedPin.value(1)
    print("Led is ON")
    time.sleep(Interval)
    return

def LedOff(LedPin = None, Interval = 1):
    if LedPin is None:
        print("LedPin is None")
        return
    LedPin.value(0)
    print("Led is OFF")
    time.sleep(Interval)
    return