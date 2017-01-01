import time
import RPi.GPIO as GPIO

def bcmMode():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)

def myMode():
  bcmMode()

def setupPinOut(pinNumber):
  GPIO.setup(pinNumber, GPIO.OUT)

def pinOn(pinNumber):
  GPIO.output(pinNumber, True)

def pinOff(pinNumber):
  GPIO.output(pinNumber, False)

def cleanup():
  GPIO.cleanup()
