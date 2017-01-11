# import the GPIO and time package
import sys, time
import gpio, buzzer, led

gpio.bcmMode()

RUNNING=True

# setup beep
BEEP_PIN=25
gpio.setupPinOut(BEEP_PIN)

# Main
try:
  lightDur=0.1
  iterations=15
  mode = "rl"
  if (len(sys.argv) > 1):
    lightDur=float(sys.argv[1])
  if (len(sys.argv) > 2):
    iterations=int(sys.argv[2])
  if (len(sys.argv) > 3):
    mode = sys.argv[3]
  
  led.blinkLights(RUNNING, lightDur, iterations, mode, lambda:buzzer.beep(BEEP_PIN, 0.003))
  
except KeyboardInterrupt:
    RUNNING = False
    print("\Quitting")

finally:
    gpio.cleanup()
