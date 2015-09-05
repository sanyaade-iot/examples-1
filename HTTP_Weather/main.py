################################################################################
# Viper Weather
#
# Created by VIPER Team 2015 CC
# Authors: G. Baldi, D. Mazzei
################################################################################



# import streams & socket
import streams
import socket

# import json parser, will be needed later
import json

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

# let's try to connect to openweathermap.org to get some weather info
# for this example to work you need a openweathermap API key
# if you don't have one, you can get one for free here: http://openweathermap.org/price

# type here your API key!
# or you can use ours...however, if our calls quota is exceded 
# the example won't work :(
api_key = "bd4ba90e2b397e24a925e436a9d8fed9"
        
for i in range(3):
    try:
        print("Trying to connect...")
        # to get weather info you need to specify a correct api url
        # there are a lot of different urls with different functions
        # they are all documented here http://openweathermap.org/api
        
        # let's put the http query parameters in a dict
        params = {
            "APPID":api_key,
            "q":"Pisa"   # <----- here it goes your city
        }
        
        # the following url gets weather information in json based on the name of the city
        url="http://api.openweathermap.org/data/2.5/weather"
        # url resolution and http protocol handling are hidden inside the requests module
        response = requests.get(url,params=params)
        # if we get here, there has been no exception, exit the loop
        break
    except Exception as e:
        print(e)


try:
    # check status and print the result
    if response.status==200:
        print("Success!!")
        print("-------------")
        # it's time to parse the json response
        js = json.loads(response.content)
        # super easy!
        print("Weather:",js["weather"][0]["description"],js["main"]["temp"]-273,"degrees")
        print("-------------")
except Exception as e:
    print("ooops, something very wrong! :(",e)



