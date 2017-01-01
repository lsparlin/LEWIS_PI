import sys, time
import buzzer

BEEP_PIN=25

beepDur=.1
if (len(sys.argv) > 1):
  beepDur=float(sys.argv[1])

buzzer.beep(BEEP_PIN, beepDur)

if len(sys.argv) == 1:
  print("You can enter a beep duration in seconds")
