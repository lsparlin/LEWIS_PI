import gpio

gpio.bcmMode()

usedPins=[4,17,13,27,22,25,6,19,26]

gpio.setupPinOut(usedPins)

gpio.pinOff(usedPins)

gpio.cleanup()
