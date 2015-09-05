################################################################################
# Sensor Driven Multi-Blink
#
# Created by VIPER Team 2015 CC
# Authors: G. Baldi, D. Mazzei
################################################################################

#This examples require a analog sensor and three LEDs or an RGB LED
import streams
import adc

#create a serial port stream with default parameters
streams.serial()

#set the A1 pin as analog input and D8, D9, D10 as outputs for driving the LEDs. 
pinMode(A1,INPUT_ANALOG)
pinMode(D10,OUTPUT)
pinMode(D9,OUTPUT)
pinMode(D8,OUTPUT)

#creates two arrays for storing global variables to be used in the blinking threads
freq=[1,1,1]        
pin=[D8,D9,D10]    

#define the generic blinking function to be used for driving the LEDs
#this function takes as input the index identifying the LED then use the global freq and pin arrays to dynamically drives the LEDs
def blink(Npin,value):
    global freq
    global pin 
    while True:
        print(pin[Npin],freq[Npin])        
        digitalWrite(pin[Npin],HIGH)
        sleep(freq[Npin])
        digitalWrite(pin[Npin],LOW)
        sleep(freq[Npin])

#define an analog sensor sampling function that acquire the raw data and convert it in the three LED frequencies        
def sampling():
    global freq
    while True:
        value = analogRead(A1)
        freq[0] = value//10
        freq[1] = freq[0] * 2
        freq[2] = freq[0] * 4
        sleep(50)

#launch the four threads        
thread(sampling)
thread(blink,0,0)
thread(blink,1,1)
thread(blink,2,2)

#The main loop is used only for printing out at reasonable speed the calculated frequencies in term of waiting times 
while True:
    print("Wait times are", freq)
    sleep(500)
