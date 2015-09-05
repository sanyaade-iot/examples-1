################################################################################
# Interrupt Basics
#
# Created by VIPER Team 2015 CC
# Authors: G. Baldi, D. Mazzei
################################################################################

import streams

#create a serial port stream with default parameters
streams.serial()

#define where the button and the LED are connected
#in this case the BTN0 label will be replaced by the compiler according to the board definition
#change this definition to connect external buttons on any other board digital pin 
buttonPin=BTN0 
ledPin=D13  #where the onboard LED is connected on most Arduino-like boards

#configure the pin behaviour for driving the LED and reading form the button  
pinMode(buttonPin,INPUT_PULLUP)
pinMode(ledPin,OUTPUT)

#define the function to be called when the button is pressed
def pressed():
        print("touched!")
        digitalWrite(ledPin,HIGH) #just blink the LED for 100 millisec when the button is pressed
        sleep(100)
        digitalWrite(ledPin,LOW)

#attach an interrupt on the button pin and call the pressed function when it fall
#having the button pin a PULLUP configuration we can assume that pressing the button the signal goes to GND so it falls  
#opposite behaviour can be obtained with the equivalent "rise" interrupt function onPinRise(pin,fun)
onPinFall(buttonPin,pressed)



