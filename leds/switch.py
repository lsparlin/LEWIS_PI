import sys
import gpio

gpio.myMode()

if (len(sys.argv) > 1):
  ledNode=int(sys.argv[1])
  switch=True
  if (len(sys.argv) > 2):
    switch=(sys.argv[2] in ["True", "true", "on", "On", "1"])
  gpio.setupPinOut(ledNode)
  if switch:
    gpio.pinOn(ledNode)
  else:
    gpio.pinOff(ledNode)

elif len(sys.argv) == 1:
  print("Please enter LED node number to illuminate FOLLOWED BY switch")
