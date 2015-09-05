###############################################################################
# Hello Viper
#
# Created by VIPER Team 2015 CC
# Authors: G. Baldi, D. Mazzei
###############################################################################

# import the streams module, it is needed to send data around
import streams

# open the default serial port
streams.serial()  

# loop forever
while True:
    print("Hello Viper!")   # print automatically knows where to print!
    sleep(1000)