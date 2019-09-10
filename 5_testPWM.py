import Adafruit_BBIO.PWM as PWM

greenLED = "P9_14"
#redLED = "P9_16"

#PWM.start(PWM pin name, dutyCycle (It is val*3.3V) , frequency)
PWM.start(greenLED, 0, 1000)
#PWM.start(redLED, 0, 1000)

#PWM.set_duty_cycle(PWM pin name, dutyCycle)
#PWM.set_duty_cycle(greenLED, DC)

#PWM.stop(myPWM)
#PWM.cleanup()
