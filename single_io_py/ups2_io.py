#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import os,sys


class UPS2_IO:
    def __init__(self,bcm_io=18):
        self.shutdown_check_pin = bcm_io
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.shutdown_check_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.shutdown_check_pin, GPIO.FALLING, callback= self.RPI_shutdown,bouncetime=1000)


    def RPI_shutdown(self,channel):
        print("detect bat LOW, system will shutdown in 10s!")
        for i in range(10,0,-1):
            print(i,end = ' ',flush=True)
            time.sleep(1)
            
        print("\nexecute System shudown!\n")
        os.system("sudo shutdown -t now")
        sys.exit()
    

    def cleanup():
        print("clean up GPIO.")
        GPIO.cleanup()  
    

if __name__ == "__main__":
    print("This is UPS v2 single IO class file.")
    
#    test = UPS2_IO(18)
#    try:
#        while True:
#            time.sleep(1)         
#    except KeyboardInterrupt:
#        print('User press Ctrl+c ,exit;')
#    finally:
#        cleanup()