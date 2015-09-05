################################################################################
# Viper App - TOI Shield
#
# Created: 2015-08-29 00:17:06.795078
#
################################################################################

import streams


import pwm
from drivers.toishield import toishield
from wireless import wifi
from drivers.wifi.cc3000 import cc3000_tiny as cc3000
# and also import the viperapp module
from libs.apps import viperapp


streams.serial()


# save the template.html in the board flash with new_resource
new_resource("template.html")

# connect to a wifi network
try:
    cc3000.auto_init()

    print("Establishing Link...")
    wifi.link("Network-Name",wifi.WIFI_WPA2,"Wifi Password")
    print("Ok!")        
except Exception as e:
    print(e)


#### ViperApp Setup    

# :: Javascript to Python ::
# the following function will be called when the template button is pressed
# it plays an "A" of one second on the buzzer
def buzz():
    pwm.write(toishield.buzzer_pin,2272,1000,MICROS,440)

# :: Python to Javascript ::
# the following function sends messages to the mobile app
# labelling them as "data" events

# configure the viper app with a name, a descripton and the template url
vp = viperapp.ViperApp("TOI Shield","TOI Shield Test","resource://template.html",True)

# everytime Javascript generates the event "buzzer" the function buzz is called
vp.on("buzzer",buzz)

# run the ViperApp!
vp.run()



#### Main thread

# since vp.run starts a new thread, you can do whatever else you want down here!

while True:
    # let's gather data
    # convert numbers to int, no support for float on the mobile app yet
    light = int(toishield.light.getFloat()*100)
    sound = int(toishield.microphone.getFloat()*100)
    temperature = int(toishield.temperature.getCelsius())
    touch = digitalRead(toishield.touch_pin)
    # send a tuple to the app
    vp.notify("data",(light,sound,temperature,touch))
    sleep(1000)


