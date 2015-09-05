###############################################################################
# Led Blink
#
# Created by VIPER Team 2015 CC
# Authors: G. Baldi, D. Mazzei
###############################################################################

# D0 to D127 represent the names of digital pins

# On most Arduino-like boards Pin D13 has an on-board LED connected.
# Initialize a digital pin as an output to drive the connected LED.

pinMode(D13,OUTPUT)

# loop forever
while True:
        digitalWrite(D13,HIGH)  # turn the LED ON by making the voltage HIGH
        sleep(1000)             # wait for a second
        digitalWrite(D13,LOW)   # turn the LED OFF by making the voltage LOW
        sleep(1000)             # wait for a second
