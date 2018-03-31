#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Use physical pin numbers
GPIO.setmode(GPIO.BOARD)
# Set up header pin 22 (GPIO25) as an input
buttonPin = 22
print "Setup Pin 22"
GPIO.setup(buttonPin, GPIO.IN)
prev_input = 0

while True:
  #take a reading
  input = GPIO.input(buttonPin)
  #if the last reading was low and this one high, print
  if ((not prev_input) and input):
    print("Button pressed")
  #update previous input
  prev_input = input
  #slight pause to debounce
  time.sleep(0.05)
