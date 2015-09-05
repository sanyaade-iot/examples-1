################################################################################
# Viper Time API
#
# Created: 2015-08-17 16:44:58.640097
#
################################################################################

# import streams & socket
import streams
import socket

# import the cc3000 wifi driver
from drivers.wifi.cc3000 import cc3000
# import the wifi interface
from wireless import wifi

# import the http module
import requests

streams.serial()


# init the cc3000 drivers: works on arduino compatibles and Particle Core.
# The driver automatically registers itself to the wifi interface
# so the wifi module can use the cc3000 without your intervention 
cc3000.auto_init()

# use the wifi interface to link to the Access Point
# change network name, security and password as needed
print("Establishing Link...")
try:
    wifi.link("Network-Name",wifi.WIFI_WPA2,"Wifi-Password")
except Exception as e:
    print("ooops, something wrong while linking :(", e)
    while True:
        sleep(1000)

# let's try to connect to timeapi.org to get the current UTC time        
for i in range(3):
    try:
        print("Trying to connect...")
        # we need to impersonate a web browser: as easy as setting the http user-agent header
        user_agent = {"user-agent":"Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405"}
        # got get that time!
        # url resolution and http protocol handling are hidden inside the requests module
        response = requests.get("http://www.timeapi.org/utc/now",headers=user_agent)
        # let's check the http response status: if different than 200, something went wrong
        print("Http Status:",response.status)
        # if we get here, there has been no exception, exit the loop
        break
    except Exception as e:
        print(e)


try:
    # check status and print the result
    if response.status==200:
        print("Success!!")
        print("-------------")
        print("And the result is:",response.content)
        print("-------------")
except Exception as e:
    print("ooops, something very wrong! :(",e)
    