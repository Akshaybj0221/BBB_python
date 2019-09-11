import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM


from time import sleep


commandButton = "P9_11"
GPIO.setup(commandButton, GPIO.IN)

potVal="P9_33"
ADC.setup()

pwmLED="P9_14"
PWM.start(pwmLED, 0, 1000)


while(1):
    analogRead = ADC.read(potVal)
    dutyCycle = 101**analogRead-1
    print("The Potentiometer value is:", analogRead, "%", "   |   Dutycycle: ", dutyCycle)
    PWM.set_duty_cycle(pwmLED, dutyCycle)
    sleep(0.2)
    if GPIO.input(commandButton):
        print "Bye Bye"
        break

