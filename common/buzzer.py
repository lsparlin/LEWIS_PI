import time
import gpio

gpio.myMode()

# Need Max duration because beep is LOUD
MAX_DUR=1

def beep(pinNumber, dur):
  gpio.setupPinOut(pinNumber)
  if dur > MAX_DUR:
    print("ADJUSTED: " + str(dur) + " was adjusted to " + str(MAX_DUR))
    dur = MAX_DUR
  gpio.pinOn(pinNumber)
  time.sleep(dur)
  gpio.pinOff(pinNumber)
