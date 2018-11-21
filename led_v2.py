#! /usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

print("Ejecucion iniciada...")
        
while True:  
	GPIO.output(11,True)
	GPIO.output(13,False)
	GPIO.output(15,False)
	time.sleep(2)
	GPIO.output(11,False)
	GPIO.output(13,True)
	GPIO.output(15,False)
	time.sleep(2)
	GPIO.output(11,False)
	GPIO.output(13,False)
	GPIO.output(15,True)
	time.sleep(2)  	
    