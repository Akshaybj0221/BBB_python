#import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from time import sleep


commandButton = "P9_11"
GPIO.setup(commandButton, GPIO.IN)

pwmLED="P9_14"
PWM.start(pwmLED, 0, 1000)

buttonPress = 0

while(1):
    if GPIO.input(commandButton):
        buttonPress += 1
        print "Button Pressed!"

    if buttonPress > 10:
        buttonPress = 0
        print "Bye Bye!"
        PWM.set_duty_cycle(pwmLED, 0)
        GPIO.cleanup()
        break

    dutyCycle = 1.5864**buttonPress-1
    print("Total number of times the button is pressed: ", buttonPress, "%", "   |   Dutycycle: ", dutyCycle)
    PWM.set_duty_cycle(pwmLED, dutyCycle)
    sleep(0.2)

