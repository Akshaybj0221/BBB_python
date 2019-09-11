import os
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

powerButton = "P9_11"
GPIO.setup(powerButton, GPIO.IN)

pinState = GPIO.input(powerButton)

while (1):
    if GPIO.input(powerButton):
        print "System is shutting down"
        sleep(1)
        GPIO.cleanup()
        shutdownCmd = 'echo temppwd | sudo -S shutdown now'
        os.system(shutdownCmd)
        sleep(0.2)

