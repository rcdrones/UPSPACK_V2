#!/usr/bin/python3

from upspackv2 import *


test = UPS2("/dev/ttyAMA0")
version,vin,batcap,vout = test.decode_uart()
print("--------------------------------")
print("       UPS Version:"+version)
print("--------------------------------")

i = 1

while True:
    version,vin,batcap,vout = test.decode_uart()
    
    print("-%s-" %i)
    
    if vin == "NG":
        print("USB input adapter : NOT connected!")
    else:
        print("USB input adapter : connected!")
    print("Battery Capacity: "+batcap+"%")
    print("UPS Output Voltage: "+vout+" mV")
    print("\n")
    
    i = i+1
    
    if i == 10000:
        i = 1

