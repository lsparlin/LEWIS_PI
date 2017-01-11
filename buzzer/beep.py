import sys, time
import buzzer

BEEP_PIN=25

beepDur=1000
if (len(sys.argv) > 1):
  beepDur=float(sys.argv[1])

beepDur = beepDur / 1000
buzzer.beep(BEEP_PIN, beepDur)

if len(sys.argv) == 1:
  print("You can enter a beep duration in milliseconds")
