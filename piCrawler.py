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
import consts
import wiki
import os
import logger
import random

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

def scrapeWiki():
    pages = ['python','programming','computer','resistor']
    scraped = []
    while len(pages) > 0:
        GPIO.output(GREEN_LED,GPIO.HIGH)
        nextPage = pages.pop(0)
        if not nextPage in scraped:
            try:
                # write data to file
                dataPath = os.path.join(consts.USB_FOLDER,nextPage+".txt")
                f = open(dataPath,"w+")
                f.write(wiki.getText(nextPage))
                f.close()

                # log the success and grab next pages
                logger.log(nextPage)       
                newLinks = wiki.getLinks(nextPage)
            
                # shuff the links so that it isn't
                #  geared toward alphabetical searches
                random.shuffle(newLinks)
                for p in newLinks:
                    if p in pages:
                        pages.remove(p)
                        index = random.randrange(0,len(pages))
                        pages.insert(index,p)
                    else:
                        pages.append(p)
                
            except:
                logger.log('ERROR: '+nextPage)

            scraped.append(nextPage)
        else:
            logger.log("page already scraped " + nextPage)

        # flip between green and blue to show
        #  when we are scraping a page
        GPIO.output(GREEN_LED,GPIO.LOW)
        GPIO.output(BLUE_LED,GPIO.HIGH)
        time.sleep(10)
        GPIO.output(BLUE_LED,GPIO.LOW)

setupGPIO()
testGPIO()
scrapeWiki()
GPIO.cleanup()
