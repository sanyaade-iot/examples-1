################################################################################
# Viper UDP pinger
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

# use the wifi interface to link to the Access Point
# change network name, security and password as needed
print("Establishing Link...")
try:
    wifi.link("Network-Name",wifi.WIFI_WPA2,"Wifi-Password")
    # get our ip
    myip = wifi.link_info()[0]
    # convert myip to a tuple with the socket.ip_to_tuple function
    # "x.y.z.w" becomes (x,y,z,w)
    ip_tuple = socket.ip_to_tuple(myip)
    # generate a broadcast address to port 9999
    # (it's ok and easier to generate it as a 5 number tuple)
    broadcast = (ip_tuple[0],ip_tuple[1],ip_tuple[2],255,9999)
    print(myip,ip_tuple,broadcast)
    # create an UDP socket and bind it to port 9999
    sock = socket.socket(type=socket.SOCK_DGRAM)
    sock.bind(9999)
except Exception as e:
    print("ooops, something wrong while linking :(", e)
    while True:
        sleep(1000)

        
# this function will be used as a thread
# sending every 2 seconds a message to all
# the udp sockets listening on port 9999 
def ping():
    while True:
        print("Sending")
        sock.sendto("Hello Viper!",broadcast)
        sleep(2000)
        
# launch it!
thread(ping)

# in the main thread we listen for incoming udp packets
while True:
    print("Receiving pings")
    try:
        # revfrom returns both the packet data and the address of the sender
        data,address = sock.recvfrom(32)
        # since we bind to 9999 we also receive the packets we send
        # check for it by comparing just the ip address (without the port)
        if address[0]!=myip:
            print("Received ping from",address,"=>",str(data))
        else:
            print("Received ping from myself!")
    except Exception as e:
        print(e)
# uplink this script to more than one board and check
# the ping ch