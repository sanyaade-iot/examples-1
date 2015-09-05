################################################################################
# Light Controlled PWM
#
# Created by VIPER Team 2015 CC
# Authors: L. Rizzello, G. Baldi,  D. Mazzei
###############################################################################

import streams
import pwm
from drivers.toishield import toishield

streams.serial()

# define a function that takes a sensor object as parameter and changes the 
# modulation of the led depending on the last value read by the sensor:
# as currentSample() gets higher, PWM duty cycle gets lower
def changeLEDIntensity(obj):
    global led_pin
    percentage = 1 - obj.currentSample()
    print(int(2040 * percentage))
    #~ 490 Hz
    pwm.write(led_pin,2040,int(2040*percentage),MICROS)

led_pin = LED0.PWM
pinMode(led_pin,OUTPUT)
# set toishield.toFloat as the normalization function for the light sensor
# to get its samples as values between 0 and 1
toishield.light.setNormFunc(toishield.toFloat)
# set changeLEDIntensity as the function to be executed every time a new sample
# is read
toishield.light.doEverySample(changeLEDIntensity)
# start sampling normalized samples
toishield.light.startSampling(200,None,"norm")
