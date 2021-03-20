#!/usr/bin/env python3
import RPi.GPIO as GPIO
import random
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization
p.ChangeDutyCycle(12)
time.sleep(1.05)
GPIO.cleanup()
