
################################################################################
# Toishield basic
#
# Created by VIPER Team 2015 CC
# Authors: L. Rizzello, G. Baldi,  D. Mazzei
###############################################################################

import streams
import adc
from drivers.toishield import toishield

streams.serial()

# toishield defines pin names in a board indipendent manner
# let's use them to read raw sensors values

while True:
    print(" Microphone:",adc.read(toishield.microphone_pin))
    print("      Light:",adc.read(toishield.light_pin))
    print("Temperature:",adc.read(toishield.temperature_pin))
    print("      Touch:",digitalRead(toishield.touch_pin))
    # aux pins are also accessible!
    print("       AUX1:",adc.read(toishield.aux1.ADC))
    print("-"*40)
    sleep(500)
    
# this scripts runs on every supported board, without a single change...cool isn't it? :)