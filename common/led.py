import gpio
import time

def myColors():
  white=4
  yellow=17
  red=13
  green=27
  blue=22
  colorMap={1:white, 2:yellow, 3:red, 4:green, 5:blue}
  gpio.setupPinOut([white, yellow, blue, red, green])
  return colorMap

def myRgbColors():
  red=26
  green=19
  blue=6
  colorMap={1:[red,green,blue], 2:[red, green], 3:[red], 4:[green], 5:[blue]}
  gpio.setupPinOut([red, green, blue])
  return colorMap

def blinkLights(stillRunning, duration, iterations, mode, fOnLight):
  mapOfLights = myColors()
  mapOfRgb = myRgbColors()

  iterRange = range(0, iterations)
  if mode == "lr":
    iterRange = range(iterations, 0, -1)
  if mode == "alt":
    iterRange = range(0, iterations*2, 2)
  
  for i in iterRange:
      if not stillRunning:
        break
      mapLocation = (i % len(mapOfLights)) + 1
      current = mapOfLights[mapLocation]
      currentRgb = mapOfRgb[mapLocation]
      gpio.pinOn(current)
      gpio.pinOn(currentRgb)
      if fOnLight != None:
        fOnLight()
      time.sleep(duration)
      gpio.pinOff(current)
      gpio.pinOff(currentRgb)
      time.sleep(0.025)
