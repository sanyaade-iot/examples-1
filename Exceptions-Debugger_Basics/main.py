################################################################################
# Exception-Debugger Basics
#
# Created by VIPER Team 2015 CC
# Authors: G. Baldi,  D. Mazzei
###############################################################################

import streams

streams.serial()

while True:
    for x in range(-10,10,1):   #create a for loop ranging the integers between -10 and 10
        
        try:                    #open the Exception monitoring scope
            value=100//x        #when x=0 this will results in a DivisionByZero!
            print(value)
        except Exception as e:  #pass any rised exception as e
            print(e)            #print the content of e for monitoring where the program faults
                                #click on the console X icon for opeing the Viper debugger window        
        sleep(1000)    
      
