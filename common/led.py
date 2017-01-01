import gpio
import time

def blinkLights(stillRunning, mapOfLights, duration, iterations, mode, fOnLight):
  iterRange = range(0, iterations)
  if mode == "lr":
    iterRange = range(iterations, 0, -1)
  if mode == "alt":
    iterRange = range(0, iterations*2, 2)
  
  for i in iterRange:
      if not stillRunning:
        break
      current = mapOfLights[ (i % len(mapOfLights)) + 1 ]
      gpio.pinOn(current)
      if fOnLight != None:
        fOnLight()
      time.sleep(duration)
      gpio.pinOff(current)
      time.sleep(0.025)
