import os
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

inPin = "P8_17"
GPIO.setup(inPin, GPIO.IN)

pinState = GPIO.input(inPin)

if (pinState == HIGH):
    print "System is shutting down" 
    sleep(1)
    shutdownCmd = 'shutdown'
    os.system(shutdownCmd)


