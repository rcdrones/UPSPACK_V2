#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import os,sys

shutdown_check_pin = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(shutdown_check_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def RPI_shutdown(channel):
    print("detect bat LOW, system will shutdown in 10s!")
    for i in range(10,0,-1):
        print(i,end = ' ',flush=True)
        time.sleep(1)
        
    print("\nexecute System shudown!\n")
    os.system("sudo shutdown -t now")
    sys.exit()
    
GPIO.add_event_detect(shutdown_check_pin, GPIO.FALLING, callback= RPI_shutdown,bouncetime=1000)


def cleanup():
    print("clean up GPIO.")
    GPIO.cleanup()


def main():
    print("UPS single io shutdown DEMO")
    try:
        while True:
            time.sleep(1)         
    except KeyboardInterrupt:
        print('User press Ctrl+c ,exit;')
    finally:
        cleanup()
    

if __name__ == "__main__":
    main()