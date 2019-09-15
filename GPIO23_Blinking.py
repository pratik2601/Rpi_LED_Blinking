#simple blinking at GPIO 23

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
# Pin Definitions
ledPin = 23

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)
#initliaze it to LOW
GPIO.output(ledPin, GPIO.LOW)

# Infinite Loop
#try:
while 1:
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(1)

#except KeyboardInterrupt:
#    GPIO.cleanup()

