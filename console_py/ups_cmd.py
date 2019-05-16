#!/usr/bin/python3

import serial
import re

ser  = serial.Serial("/dev/ttyAMA0",9600)
    
def get_data():

    global ser
    
    while True:
        count = ser.inWaiting()
        
        if count !=0:
            recv = ser.read(100)
##            recv_string = recv.decode(encoding='utf-8')
            
##            print("----------")
##            print(recv)
##            print("----------")
            return recv
        

def decode_uart():
    uart_string = get_data()
#    print(uart_string)
    
    data = uart_string.decode('ascii','ignore')
#    print(data)
    pattern = r'\$ (.*?) \$'
    result = re.findall(pattern,data,re.S)
    
    tmp = result[0]
    
    pattern = r'SmartUPS (.*?),'
    version = re.findall(pattern,tmp)
    
    pattern = r',Vin (.*?),'
    vin = re.findall(pattern,tmp)
    
    pattern = r'BATCAP (.*?),'
    batcap = re.findall(pattern,tmp)
    
    pattern = r',Vout (.*)'
    vout = re.findall(pattern,tmp)
    
#    print(version)
#    print(vin)
#    print(batcap)
#    print(vout)
    
    return version[0],vin[0],batcap[0],vout[0]
  
    


def main():
    version,vin,batcap,vout = decode_uart()
    print("--------------------------------")
    print("       UPS Version:"+version)
    print("--------------------------------")
    
    i = 1
    
    while True:
        version,vin,batcap,vout = decode_uart()
        
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
#        print(type(i))
     
  


if __name__ == "__main__":
    main()

