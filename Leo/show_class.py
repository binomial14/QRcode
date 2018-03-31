import RPi.GPIO as GPIO
import time

class Show:
	def show_numbers(self,sold_number):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)

		seg = (4, 17, 27, 22, 23, 24, 25, 18)

		digits = {
    		'.': (1, 1, 1, 1, 1, 1, 1, 0),
   			'0': (0, 0, 0, 1, 0, 0, 0, 1),
    		'1': (0, 1, 1, 1, 0, 1, 1, 1),
    		'2': (0, 0, 1, 0, 1, 0, 0, 1),
    		'3': (0, 0, 1, 0, 0, 0, 1, 1),
    		'4': (0, 1, 0, 0, 0, 1, 1, 1),
    		'5': (1, 0, 0, 0, 0, 0, 1, 1),
    		'6': (1, 0, 0, 0, 0, 0, 0, 1),
    		'7': (0, 0, 0, 1, 0, 1, 1, 1),
    		'8': (0, 0, 0, 0, 0, 0, 0, 1),
    		'9': (0, 0, 0, 0, 0, 1, 1, 1)
			}

		for n in range(0, 8):
    		GPIO.setup(seg[n], GPIO.OUT)

		for n in range(0, 8):
			GPIO.output(seg[n], digits[str(sold_number)][n])


		GPIO.cleanup()
