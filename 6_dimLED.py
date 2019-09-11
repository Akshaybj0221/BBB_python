import Adafruit_BBIO.PWM as PWM

#greenLED = "P9_14"
#redLED = "P9_16"


tLED = "P9_14"
bLED = "P9_22"


#PWM.start(PWM pin name, dutyCycle (It is val*3.3V) , frequency)
#PWM.start(greenLED, 0, 1000)
#PWM.start(redLED, 0, 1000)

PWM.start(tLED, 0, 1000)
PWM.start(bLED, 0, 1000)



for i in range(0,5):
    tB = input("Brightness Top LED? (0-7)")
    bB = input("Brightness Bottom LED? (0-7)")
    tBDC=2**tB
    bBDC=2**bB
    if tBDC>100:
        tBDC=100
    if bBDC>100:
        bBDC=100
    PWM.set_duty_cycle(tLED, tBDC)
    PWM.set_duty_cycle(bLED, bBDC)


    #PWM.set_duty_cycle(PWM pin name, dutyCycle)
    #PWM.set_duty_cycle(greenLED, DC)

#PWM.stop(myPWM)
#PWM.cleanup()

PWM.stop(tLED)
PWM.stop(bLED)
PWM.cleanup()


