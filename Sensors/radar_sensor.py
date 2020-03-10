import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)          # Note uses BCM instead of BOARD!!!
GPIO.setup(9, GPIO.IN)         # Read output from PIR motion sensor

while True:
    reading = GPIO.input(9)
    if reading is not None:                 # When output from motion sensor is LOW
        print("Radar Value", reading)
        time.sleep(.75)
    else:
        print('ERROR: READ NONE')
        break
