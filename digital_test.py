import RPi.GPIO as GPIO
import time
sensor_input = 4

GPIO.setmode(GPIO.BCM)
<<<<<<< HEAD
GPIO.setup(sensor_input, GPIO.IN)
=======
GPIO.setup(sensor_input, GPIO.IN))

sec = float(input('Interval in seconds: '))
data = [sec]
>>>>>>> ebf36c36096779c0d1707cbe8b73c646294515f6
try:
   while True:
      if GPIO.input(sensor_input):
         print('detected')
<<<<<<< HEAD
         #time.sleep(.5)
      else:
         print('NOPE') 
=======
         data.append(50)
         time.sleep(.5)
      else:
         print('nope')
         data.append(0)
>>>>>>> ebf36c36096779c0d1707cbe8b73c646294515f6
except KeyboardInterrupt:
   f = open('data/digital_test_data.csv', 'w')
   f.write(str(data[1,-1]))
   GPIO.cleanup()

'''
sudo apt-get update
sudo apt-get install python-dev python-pip
sudo pip install --upgrade distribute
sudo pip install ipython
sudo pip install --upgrade RPi.GPIO
'''
