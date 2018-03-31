import RPi.GPIO as GPIO
import time

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

c = 0

while True:

    for n in range(0, 8):
        GPIO.output(seg[n], digits[str(9 - c % 10)][n])

    time.sleep(.3)

    for n in range(0, 8):
        GPIO.output(seg[n], GPIO.HIGH)

    time.sleep(.3)

    c += 1

GPIO.cleanup()