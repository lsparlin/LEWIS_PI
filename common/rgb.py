import gpio
import sys, time

gpio.bcmMode()

red=26
green=19
blue=6
gpio.setupPinOut([red, green, blue])

def redOn():
  gpio.pinOn(red)

def redOnly():
  redOn()
  gpio.pinOff([green, blue])

def redOff():
  gpio.pinOff(red)

def greenOn():
  gpio.pinOn(green)

def greenOnly():
  greenOn()
  gpio.pinOff([red, blue])

def greenOff():
  gpio.pinOff(green)

def blueOn():
  gpio.pinOn(blue)

def blueOnly():
  blueOn()
  gpio.pinOff([red, green])

def blueOff():
  gpio.pinOff(blue)

def allOff():
  gpio.pinOff([red, green, blue])
