import time
import rgb


r = lambda: rgb.redOnly()
y = lambda: rgb.greenOn()
g = lambda: rgb.greenOnly()
c = lambda: rgb.blueOn()
b = lambda: rgb.blueOnly()
p = lambda: rgb.redOn()
w = lambda: rgb.greenOn()
off = lambda: rgb.allOff()

seq = [r, y, g, c, b, p, w, off]

for x in range(0, len(seq)):
    seq[x]()
    time.sleep(1.5)
