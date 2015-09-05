################################################################################
# Input Capture Unit 
#
# Created by VIPER Team 2015 CC
# Authors: G. Baldi, D. Mazzei
################################################################################

import pwm 
import icu
import streams

#create the serial port using default parameters  
streams.serial()

#define a pin where a button is connected, you can use the Nucleo button pin as input or change it with any other digital pin available
buttonPin=BTN0 #this is the pin where the button is connected, for the various supported board VIPER automatically translates it on the board button specific pins

#define a pin where the ICU is used. D2 works with Arduino footprint boards while on Particle boards D0 can be used 
captPin=D2.ICU  #On Arduino like boards
#captPin=D0.ICU  #On Particle boards

#define the Pin where the PWM is controlled. D13 works with Arduino footprint boards where the LED1 is also connected
#while on Particle boards A4 can be used
pwmPin=D13.PWM #On Arduino like boards 
pwmPin=A4.PWM #On Particle boards

#set the pin as input with PullUp, the button will be connected to ground
pinMode(buttonPin, INPUT_PULLUP)

#define a function for printing capture results on the serial port
def print_results(y):
    print("Time ON is:", y[0],"micros")
    print("Time OFF is:",y[1],"micros")
    print("Period is:", y[0]+y[1], "micros")
    print()
    
#define a global variable for PWM duty cycle and turn on the PWM on board LED (Pin 13)

duty=10
pwm.write(pwmPin,100, duty,MICROS) #pwm.write needs (pn, period, duty, time_unit)

#define the function to be called for changing the PWM duty when the button is pressed
def pwm_control():
    global duty
    duty= duty+10
    pwm.write(pwmPin, 100, duty,MICROS)
    if duty>=100:
        duty=0
    print("Duty:", duty, "millis")
    
#Attach an interrupt on the button pin waiting for signal going from high to low when the button is pressed.
#The interrupt if triggered call the pwm_control function
onPinFall(buttonPin, pwm_control)

while True:
    #define an icu capture on pin 2 to be triggered when the pin rise.
    #this routine acquires 10 steps (HIGH or LOW states) or terminates after 50000 micros, the time unit is MICROS
    #this is a blocking function, icu.capture can be also instanced as non blocking using call-back, refer to the doc for more info
    x = icu.capture(captPin,HIGH,10,50000,MICROS)
    print("alive")
    # x is a list of steps lengths in microseconds, pass it to the printing function for showing on the serial console
    print_results(x)
    
    sleep(1000)
    
