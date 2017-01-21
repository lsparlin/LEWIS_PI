from gpiozero import Button
import time, sys
import rgb

CONTINUE = True
param_continuous = False
button = Button(20)

if len(sys.argv) > 1:
  param_continuous = True

r = lambda: rgb.redOnly()
y = lambda: rgb.greenOn()
g = lambda: rgb.greenOnly()
c = lambda: rgb.blueOn()
b = lambda: rgb.blueOnly()
p = lambda: rgb.redOn()
w = lambda: rgb.greenOn()
off = lambda: rgb.allOff()

seq = [r, y, g, c, b, p, w, off]

try :
  while CONTINUE:
    seq[0]()
    if param_continuous:
      button.wait_for_release()
    for x in range(1, len(seq)-1):
      button.wait_for_press()
      seq[x]()
      button.wait_for_release()
    if not param_continuous:
      CONTINUE = False
    button.wait_for_press()

except KeyboardInterrupt:
  print("/C Quitting")

finally:
  seq[len(seq)-1]()
