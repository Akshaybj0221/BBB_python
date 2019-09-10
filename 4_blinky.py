import Adafruit_BBIO.GPIO as GPIO
from time import sleep

redLED = "P8_8"
greenLED = "P8_10"
GPIO.setup(redLED,GPIO.OUT)
GPIO.setup(greenLED,GPIO.OUT)

delay = input("Please enter the time between each blink in seconds: ")
freq = input("Please enter the number of times you want the LED's to blink: ")

for i in range(0,freq):
    GPIO.output(redLED, GPIO.HIGH)
    GPIO.output(greenLED, GPIO.HIGH)
    sleep(delay)
    GPIO.output(redLED, GPIO.LOW)
    GPIO.output(greenLED, GPIO.LOW)
    sleep(delay)

#Clean up all the GPIO pins status
GPIO.cleanup()


