
################################################################################
# Buzzer with PWM
#
# Created by VIPER Team 2015 CC
# Authors: G. Baldi, D. Mazzei
################################################################################

import streams
import pwm

#create a serial port stream with default parameters  
streams.serial()

# the pin where the buzzer is attached to
BUZZER =D8.PWM 

pinMode(BUZZER,OUTPUT) #declare pin 'BUZZER' to be an output:
frequency=100          #define a variable to be incremented for changing the played tone frequency

while True:
    period=1000000//frequency #we are using MICROS so every sec is 1000000 of micros. // is the int division, pwm.write period doesn't accept floats
    print("frequency is", frequency,"Hz")
    
    #set the period of the buzzer and the duty to 50% of the period
    pwm.write(BUZZER,period,period//2,MICROS)
        
    # increment the frequency every loop
    frequency = frequency + 20 
        
    # reset period
    if frequency >= 5000:
        frequency=100
        
    sleep(100) 