import Adafruit_BBIO.GPIO as GPIO
from time import sleep

outPin = "P8_17"
GPIO.setup(outPin,GPIO.OUT)

for i in range(0,5):
    GPIO.output(outPin, GPIO.HIGH)
    sleep(1)
    GPIO.output(outPin, GPIO.LOW)
    sleep(1)

#Clean up all the GPIO pins status
GPIO.cleanup()


