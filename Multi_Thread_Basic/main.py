################################################################################
# Multi-Thread Basics
#
# Created by VIPER Team 2015 CC
# Authors: G. Baldi, D. Mazzei
################################################################################

import streams

#create a serial port with default parameters
streams.serial()

#define a function to be instanced by the various threads
#parameters are passed to the function when the thread is created and then used in the thread loop
#to be continuously executed by a thread a function requires a while true loop otherwise when the function terminates the thread is closed
     
def threadfn(number,delay):    
    
    while True:                    
        print("I am the thread",number)
        print("I run every:",delay,"msec")
        print()                #just add an empty line for console output readability 
        sleep(delay)

#create the various thread using the same function instanced with different parameters        
thread(threadfn,1,500)
thread(threadfn,2,1000)
thread(threadfn,3,1300)
thread(threadfn,4,800)
   
