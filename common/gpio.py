import time
import RPi.GPIO as GPIO

def gcmMode():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)

def myMode():
  gcmMode()

def setupPinOut(pinNumber):
  GPIO.setup(pinNumber, GPIO.OUT)

def pinOn(pinNumber):
  GPIO.output(pinNumber, True)

def pinOff(pinNumber):
  GPIO.output(pinNumber, False)

def cleanup():
  GPIO.cleanup()
