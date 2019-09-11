import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

ADC.setup()

commandButton = "P9_11"
GPIO.setup(commandButton, GPIO.IN)

analogPin="P9_33"


while(1):
    potVal = ADC.read(analogPin)
    print("The Potentiometer value is:", potVal*1.8, "V  |  ", potVal, "%")
    sleep(0.5)
    if GPIO.input(commandButton):
        print "Bye Bye"
        break

