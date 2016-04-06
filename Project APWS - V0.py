# This code will trigger the solenoid valve for required regular intervals

import RPi.GPIO as GPIO 	     #Import GPIO library
import time		             #Import time library
GPIO.setmode(GPIO.BCM)    	     #Set GPIO pin numbering 

valve = 18                           #Associate pin 18 to valve

while True :
  GPIO.output(valve, True)           #Set valve as OPEN

  time.sleep(30)                     #Delay of 30 seconds (adjust as required) for water to fill in to pots

  GPIO.output(TRIG, False)           #Set valve as Close

  time.sleep(14400)                  #Delay of 14400 seconds (adjust as required) wait time between fill in of pots with water 

  GPIO.output(TRIG, False)           #Set TRIG as LOW

# Further extension is to add a manual switch to operate the solenoid valve
