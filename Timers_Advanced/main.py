################################################################################
# Timers Advanced Use

# Created by VIPER Team 2015 CC
# Authors: G. Baldi, D. Mazzei
################################################################################

import timers
import streams

#create a serial port with default parameters
streams.serial()

#create new timers
tsec=timers.timer()
tminute=timers.timer()     
tshoot=timers.timer()

seconds=0
minutes=0

#define a function to call when the timer for seconds elapse
def secondpassed():
    global seconds
    seconds +=1
    print(seconds,"  seconds")
    if seconds==60:
        seconds=0

#define a function to call when the timer for minutes elapse
def minutepassed():
    global minutes
    minutes +=1
    print(minutes,"  minutes")
    
#define a function to call when the one shot timer elapse
def shootpassed():
    print("1 second ago was 1:30")
    
#start the timers for minutes and seconds triggers
tsec.interval(1000,secondpassed)
tminute.interval(10000,minutepassed)
    
while True:
    
    if seconds==30 and minutes==1:                               #do a check on passed time to trigger a oneshot timer 
        tshoot.one_shot(1000, shootpassed)                       #this is a oneshot timer, it executes only one time
                
    print("time is:", tminute.get(),":",tsec.get())         #just print the current value sine start or last reset
    sleep(500)                 #run every 1000 millisec