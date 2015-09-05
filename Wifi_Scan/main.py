################################################################################
# VIPER wifi scan
#
# Created by VIPER Team 2015 CC
# Authors: G. Baldi, D. Mazzei
################################################################################

# import streams & socket
import streams
import socket

# import the cc3000 wifi driver
from drivers.wifi.cc3000 import cc3000
# import the wifi interface
from wireless import wifi

streams.serial()

# init the cc3000 drivers: works on arduino compatibles and Particle Core.
# The driver automatically registers itself to the wifi interface
# so the wifi module can use the cc3000 without your intervention 
cc3000.auto_init()

# a list of security strings
wifi_sec=["Open","WEP","WPA","WPA2"]
try:
    print("Scanning for 15 seconds...")
    # start scanning for 15000 milliseconds
    res = wifi.scan(15000)
    
    # if everything goes well, res is a sequence of tuples
    # each tuple contains:
    # -ssid: the name of the network
    # -sec: the security type of the network, from 0 to 3
    # -rssi: the strength of the signal, from 0 to 127
    # -bssid: the mac address of the access point
    for ssid,sec,rssi,bssid in res:
        print(ssid,"::",wifi_sec[sec],":: strength ",rssi*100/127)
except Exception as e:
    print(e)