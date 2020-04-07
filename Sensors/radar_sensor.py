import RPi.GPIO as GPIO
import time


def main():
    interval = .75
    runtime = 20
    pin_num = 9
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)                              # Note uses BCM instead of BOARD!!!
    GPIO.setup(pin_num, GPIO.IN)                        # Read output from PIR motion sensor
    data = collect_data(interval, runtimes, pin_num)    # collects the data from the radar

    if data != -1:
        save_data_to_csv(data, 'test.csv', '../data/') # saves the data to a file


def collect_data(interval, runtime, pin_num):
    '''
    params
    interval in seconds can be an int or float
    runtime how long you want to collect data (if runtime = -1 it will continue until you C-c out)
    
    data will only be collected if interval < runtime, interval > 0, and runtime != -1

    ret
    data is interval at idx 0 then collected data is at data[1:]
    if data is not collected retruns -1
    '''
    if runtime < interval or interval < 0:
        print('runtime must be greater than or equal to the runtime')
        return -1
    elif runtime == -1:
        while True:
            reading = GPIO.input(pin_num)
            if reading is not None:                 # When output from motion sensor is LOW
                print("Radar Value", reading)
                time.sleep(interval)
            else:
                print('ERROR: READ NONE')
                break
    else:
        data = [interval]
        t = 0
        while runtime > t:
            reading = GPIO.input(pin_num)
            if reading is not None:                 # When output from motion sensor is LOW
                print("Radar Value", reading)
                data.append(reading)
                time.sleep(interval)
                t += interval
            else:
                print('ERROR: READ NONE')
                break


def save_data_to_csv(data, name, path):
    '''
    params
    data should be a list
    name is a string of what you want the file to be named
    path is a string where you want the csv file to be saved

    ex: save_data_to_csv([3,2,1], text.csv, ../data/) will save a file named test.csv
    to the dir the is 1 dir back and then into the data dir and it will contain 3,2,1
    '''
    f = open(path+name,'w')
    data = str(data)[1:-1]
    f.write(data)

    
if __name__=='__main__':
    main()


