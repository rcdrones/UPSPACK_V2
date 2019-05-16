#!/usr/bin/python3

import tkinter as tk
import re
import serial
import time

ser  = serial.Serial("/dev/ttyAMA0",9600)

def get_data():
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




def reflash_data():
    version,vin,batcap,vout = decode_uart()
#    loc_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    cur_time = time.time()
    cur_time = cur_time - load_time
#    print(cur_time)
    
    
    
    time_var.set("Running: "+str(int(cur_time)) + "s")
    
    
    
    batcap_int = int(batcap)
#    print(type(batcap_int))
    
    if vin == "NG":
        vin_lable.config(bg = "red")
        vin_var.set("Power NOT connected!")
    else:
        vin_lable.config(bg = "green")
        vin_var.set("Power connected!")
                  
    if batcap_int< 30:
        cap_lable.config(bg = "red")
    else:
        cap_lable.config(bg = "green")
    
    
    cap_var.set("Battery Capacity: "+str(batcap)+"%")
    vout_var.set("Output Voltage: "+vout+" mV")

    window.after(1000,reflash_data)

def hit_exit():
    window.destroy()

    

#loc_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#print(loc_time) 
load_time = time.time()


window = tk.Tk()
window.title("UPS GUI demo")
window.geometry("400x200")

time_var = tk.StringVar()
ver_var = tk.StringVar()
vin_var = tk.StringVar()
vout_var = tk.StringVar()
cap_var = tk.StringVar()

version,vin,batcap,vout = decode_uart()
ver_var.set("Smart UPS "+version)

ver_lable = tk.Label( window,
          textvariable = ver_var,
#                      bg = "green",
          font = ("Arial",12),
          width = 20,height = 2)
ver_lable.pack()



time_lable = tk.Label( window,
          textvariable = time_var,
          bg = "green",
          font = ("Arial",12),
          width = 20,height = 2)

time_lable.place(x=10, y=50, anchor='nw')



vin_lable = tk.Label( window,
          textvariable = vin_var,
          bg = "green",
          font = ("Arial",12),
          width = 20,height = 2)

vin_lable.place(x=210, y=50, anchor='nw')


cap_lable = tk.Label( window,
          textvariable = cap_var,
          bg = "green",
          font = ("Arial",12),
          width = 20,height = 2)

cap_lable.place(x=10, y=100, anchor='nw')


vout_lable = tk.Label( window,
          textvariable = vout_var,
          bg = "green",
          font = ("Arial",12),
          width = 20,height = 2)

vout_lable.place(x=210, y=100, anchor='nw')


b1 = tk.Button(window,
  text = "Exit",
  width = 30,height = 2,
  command = hit_exit)
b1.place(x=70, y=150, anchor='nw')


window.after(100,reflash_data)

window.mainloop()

