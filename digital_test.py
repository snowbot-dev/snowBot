import RPi.GPIO as GPIO
import time
sensor_input = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_input, GPIO.IN))
try:
   while True:
      if GPIO.input(sensor_input):
         print('detected')
         time.sleep(.5)
except KeyboardInterrupt:
   GPIO.cleanup()
'''
sudo apt-get update
sudo apt-get install python-dev python-pip
sudo pip install --upgrade distribute
sudo pip install ipython
sudo pip install --upgrade RPi.GPIO
'''
