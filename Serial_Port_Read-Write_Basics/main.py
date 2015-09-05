################################################################################
# Serial Port Basics
#
# Created by VIPER Team 2015 CC
# Authors: G. Baldi, D. Mazzei
################################################################################

import streams
#creates a serial port and mae it as s to be used for methods calling
s=streams.serial()

while True:
    print("Write some chars on the serial port and terminates with \\n (new line)")
    line=s.readline() #read and return any single characters available on the serial port until a \n is found
    print("You wrote:", line)
    print()
    sleep (300)
      
    
   