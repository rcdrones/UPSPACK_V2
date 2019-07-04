#!/usr/bin/python3

import time
from upspackv2 import *


if __name__ == "__main__":
    cur_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    start_time = "\nStart time :"+cur_time
    
    with open("log.txt","a+") as f:
        f.write(start_time)
    

    print("UPS single io shutdown DEMO")
    test = UPS2_IO(18)
    try:
        while True:
            time.sleep(1)         
    except KeyboardInterrupt:
        print('User press Ctrl+c ,exit;')
    finally:
        test.cleanup()
    