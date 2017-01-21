from gpiozero import Button
import sys, time
import buzzer

BEEP_PIN=25
button = Button(20)

beepDur=1000
if (len(sys.argv) > 1):
  beepDur=float(sys.argv[1])
if beepDur > 1000:
  print("Max 1000")
  beepDur=1000

beepDur = beepDur / 1000
try:
  while True:
    button.wait_for_press()
    buzzer.beep(BEEP_PIN, beepDur)
    button.wait_for_release()

except KeyboardInterrupt:
  print("\c Quitting")

if len(sys.argv) == 1:
  print("You can enter a beep duration in milliseconds")
