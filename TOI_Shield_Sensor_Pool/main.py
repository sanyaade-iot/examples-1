################################################################################
# TOI Shield Sensor Pool
#
# Created by VIPER Team 2015 CC
# Authors: L. Rizzello, G. Baldi,  D. Mazzei
###############################################################################

import streams
from drivers.toishield import toishield
from libs.smartsensors import sensorPool

# see Pool Example for sensorPool details

def out_l(obj):
    print("light: ",obj.currentSample())

def out_t(obj):
    print("temperature: ",obj.currentSample())
    
streams.serial()
toishield.light.doEverySample(out_l)  

# to be noticed the use of a preset normalization function 'toishield.toCelsius'
# included in the toishield module
toishield.temperature.setNormFunc(toishield.toCelsius).doEverySample(out_t)
pool = sensorPool.SensorPool([toishield.light,toishield.temperature])
pool.startSampling([1000,1000],[None,None],["raw","norm"])