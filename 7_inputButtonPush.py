import Adafruit_BBIO.GPIO as GPIO
from time import sleep

topButton = "P9_11"
bottomButton = "P9_13"

GPIO.setup(topButton, GPIO.IN)
GPIO.setup(bottomButton, GPIO.IN)

while(1):
    if GPIO.input(topButton):
        print "Top button is ON"
    else:
        print "Top button OFF"

    if GPIO.input(bottomButton):
        print "Bottom button in ON"
    else:
        print "Bottom button in OFF"

    if GPIO.input(topButton) and GPIO.input(bottomButton):
        break

    sleep(0.2)

print "Good bye"
GPIO.cleanup()
