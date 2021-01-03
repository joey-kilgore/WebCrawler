# This is a python web crawler to run continuously
#   on a raspberry pi
# The wiring setup is as follows
#   pin | connected to
#    3  | Green LED (with 220Ohm R to ground)
#    5  | Red LED (with 220Ohm R to ground)
#    7  | Blue LED (with 220Ohm R to ground)
#    24 | 3 terminal switch (connected to 5v and ground)
#    26 | Passive Buzzer (connected to ground)

import RPi.GPIO as GPIO
import time

# define pins
GREEN_LED = 3
RED_LED = 5
BLUE_LED = 7
SWITCH = 24
BUZZER = 26

def setupGPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GREEN_LED,GPIO.OUT)
    GPIO.setup(BLUE_LED,GPIO.OUT)
    GPIO.setup(RED_LED,GPIO.OUT)
    GPIO.setup(SWITCH,GPIO.IN)
    GPIO.setup(BUZZER,GPIO.OUT)

def testGPIO():
    # First we will flash all 3 LEDs
    # flash green
    GPIO.output(GREEN_LED,GPIO.HIGH)
    GPIO.output(RED_LED,GPIO.LOW)
    GPIO.output(BLUE_LED,GPIO.LOW)
    time.sleep(0.5)
    # switch to red
    GPIO.output(GREEN_LED,GPIO.LOW)
    GPIO.output(RED_LED,GPIO.HIGH)
    time.sleep(0.5)
    # switch to blue
    GPIO.output(RED_LED,GPIO.LOW)
    GPIO.output(BLUE_LED,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(BLUE_LED,GPIO.LOW)

setupGPIO()
testGPIO()
GPIO.cleanup()
