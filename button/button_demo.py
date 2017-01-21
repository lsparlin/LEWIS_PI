from gpiozero import Button, PWMLED
import time

ACTIVE_LED = 0

leds=[PWMLED(4), PWMLED(17), PWMLED(13), PWMLED(27), PWMLED(22)]

button = Button(20)
leds[ACTIVE_LED].pulse(.5, .5)

try:
  while True:
    button.wait_for_press()

    leds[ACTIVE_LED].off()
    ACTIVE_LED += 1
    if ACTIVE_LED >= len(leds):
        ACTIVE_LED = 0
    leds[ACTIVE_LED].pulse(.5, .5)

    button.wait_for_release()
  
except KeyboardInterrupt:
    print("\Quitting")


