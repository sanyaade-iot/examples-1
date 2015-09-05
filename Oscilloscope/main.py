###############################################################################
# VIPER oscilloscope
#
# Created by VIPER Team 2015 CC
# Authors: G. Baldi, D. Mazzei
###############################################################################

import streams
import adc
   
streams.serial()

while True:
    value = analogRead(A4)
    conv = value*80//4095
    print("|","#"*conv," "*(80-conv),"|")
    sleep(200)
    