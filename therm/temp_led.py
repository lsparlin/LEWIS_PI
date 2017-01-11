
import time, math
import RPi.GPIO as GPIO
import rgb

GPIO.setmode(GPIO.BCM)

RUNNING = True
led_list = [4, 17, 13, 27, 22]
temp_low = 70
temp_high = 85
a_pin = 23
b_pin = 24

GPIO.setup(led_list, GPIO.OUT)
for x in range(0, len(led_list)):
    GPIO.output(led_list[x], False)

adjustment_value = 0.385

def resistance_reading():
    total = 0
    for i in range(1, 100):
        # Discharge the capacitor
        GPIO.setup(a_pin, GPIO.IN)
        GPIO.setup(b_pin, GPIO.OUT)
        GPIO.output(b_pin, False)
        time.sleep(0.01)

        # Charge the capacitor until out GPIO pin 
        # reads HIGH or aprox 1.65 volts
        GPIO.setup(b_pin, GPIO.IN)
        GPIO.setup(a_pin, GPIO.OUT)
        GPIO.output(a_pin, True)
        t1 = time.time()
        while not GPIO.input(b_pin):
            pass
        t2 = time.time()

        # Record the time taken to add to our total
        # for an eventual average calculation
        total = total + (t2 - t1) * 1000000
    # Average our time readings
    reading = total / 100
    # Convert our average to a resistance 
    resistance = reading * 6.05 - 939
    return resistance

def temp_reading(R):
    B = 3977.0 
    R0 = 9500.0
    t0 = 273.15
    t25 = t0 + 25.0
    # Steinhart-Hart equation
    inv_T = 1/t25 + 1/B * math.log(R/R0)
    T = (1/inv_T - t0) * adjustment_value
    return T * 9.0 / 5.0 + 32.0

# Main loop
try:
    while RUNNING:
        # Getting thermistor temperature
        t = temp_reading(resistance_reading())

        # print temp
        print(t)

        # turn off leds
        for x in range(0, len(led_list)):
            GPIO.output(led_list[x], False)
        
        if t <= temp_low:
            t = temp_low
        if t >= temp_high:
            t = temp_high

        num_leds = int(round(((t-temp_low) / (temp_high-temp_low))*5))
        if num_leds < 1:
            num_leds = 1
        for x in range(0, num_leds):
            GPIO.output(led_list[x], True)
        if num_leds >= 4:
            # candle is ignited
            rgb.redOnly()
        else :
            # candle is out
            rgb.blueOnly()

        time.sleep(0.3)
    
except KeyboardInterrupt:
    RUNNING = False
    print("\Quitting")

finally:
    GPIO.cleanup()
