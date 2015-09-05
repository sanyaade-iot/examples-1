################################################################################
# AnalogRead
# 
# Created by VIPER Team 2015 CC
# Authors: G. Baldi, D. Mazzei
################################################################################

import streams  # import the streams module
import adc      # import the adc driver 

# create a serial stream linked to the serial port
# and open the dedicated connection
streams.serial() 

while True:
    
# Basic usage of analogRead() for acquiring analog signal from a pin   
    value = analogRead(A0)
    print("One sample:",value)

# The complete definition of analogRead() is 
# analogRead(pin, samples=1) 
# For an advanced usage of analogRead() you can edit the default parameters as you need.

#acquire 10 samples with default sampling period    
    value2= analogRead(A0,10)
    print("10 samples with sampling period of 100ms:\n",value2)

#   AnalogRead with callback is not yet supported (coming soon) 
#   value4= analogRead(A0,10,300,ADC_HI_RES, printFun)

    print()
    sleep(300)