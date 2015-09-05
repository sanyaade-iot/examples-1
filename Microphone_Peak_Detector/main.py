
################################################################################
# Electrect Microphone Peak Detector
#
# Created by VIPER Team 2015 CC
# Authors: L. Rizzello, G. Baldi,  D. Mazzei
###############################################################################

import streams
# import toishield module
from drivers.toishield import toishield
        
# define a function that takes a sensor object as parameter and checks the
# maximum peak to peak extension of the signal in a preset window
# if the extension is over the threshold prints a message   
def detectSound(obj):
    if (obj.resetMinMaxCounter == obj._observationWindowN):
        extension = obj.staticMax - obj.staticMin
        if (extension > 1000):
            print("!!!")
        obj.staticMax, obj.staticMin = -4096, 4096
        obj.resetMinMaxCounter = 0
    else:
        c = obj.currentSample()
        if (c > obj.staticMax):
            obj.staticMax = c
        elif (c < obj.staticMin):
            obj.staticMin = c
        obj.resetMinMaxCounter += 1


streams.serial()

# set three new attributes to the toishield.microphone object
toishield.microphone.staticMin = 4096
toishield.microphone.staticMax = -4096
toishield.microphone.resetMinMaxCounter = 0

# set 'detectSound' as the function to be applied to the object at every sampling
# step
toishield.microphone.doEverySample(detectSound)
# start sampling at 22 microseconds ( ~45 kHZ ) with a window length of 500 that 
# sets the lowest detectable frequency at ~90 Hz 
toishield.microphone.startSampling(22,500,"raw",MICROS)


while True:
    print(toishield.microphone.currentSample())
    sleep(200)