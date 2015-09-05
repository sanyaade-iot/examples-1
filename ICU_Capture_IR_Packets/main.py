################################################################################
# ICU Capture IR Packets
#
# Created by VIPER Team 2015 CC
# Authors: L. Rizzello, G. Baldi, D. Mazzei  
################################################################################

import icu
import streams
import pwm

streams.serial()

ir_pin = D2.ICU #This is the pin where the TOI Shield IR receiver is connected on Arduino boards.

def IR_capture():
    while True:
        print("Capturing...")
        # starts capturing from the chosen pin (which must be an icu pin) setting
        # a trigger (in this case capture will start when the pin first goes from
        # HIGH to LOW), the max number of samples to be collected (a sample represents the
        # interval in microseconds passed between a change from a LOW to a HIGH
        # value on the pin or viceversa) and a maximum time window in ms after that the function exits 
        
        # Values chosen for this example come from NEC IR (used by LG) specification.
        # Play with these for fitting your remote protocol
        x = icu.capture(ir_pin,LOW,67,68,pull=HIGH)
        print(x,"\n captured n samples:",len(x))
               
    
# captures in a different thread
thread(IR_capture)

while True:
    print("alive!")
    sleep(1000)