# UPSPack V2 Product Software and Hardware Usage Guide

![](https://github.com/rcdrones/UPSPACK_V2/wiki/images/ups.JPG)

## Product Description
The Raspberry Pi is an SBC motherboard that is very similar to desktop Linux computer applications. All systems run on the TF memory card that comes with it. However, when the external power is suddenly cut off, the system data (or user data) on the TF card may be lost, resulting in the consequence that the system cannot be started. In addition, because the Raspberry Pi is small in size, in portable applications, a suitable mobile power supply is needed to power the Raspberry Pi. Based on the above considerations, RPi Club has designed this UPSPack V2 product. You can use it as a mobile power source or as an uninterruptible power supply for a Raspberry Pi. In addition, V2 version provides serial communication and single IO communication interface, which can exchange information with the Raspberry Pi motherboard. Let software running on Linux system know about almost all hardware / battery information on UPS. Therefore, when the shutdown is decided, information such as an external power supply abnormality can also be reported to the cloud.


## Battery life test
UPSPack's on-board battery interface is PH2.0 package. The product provides 3 different capacity batteries for customers to choose from. Customers can also access different capacity by themselves: lithium polymer soft pack battery with standard voltage of 3.7V, or 3.7V 18650 battery pack. Note: The input voltage range of the UPS battery interface must be 4.2V or less. (The implication: all battery packs must be connected in parallel, and cells cannot be connected in series). We built different application combinations and got some battery life data. Provide customers with reference to different battery capacities:



| Capacity | Pi4 stand-alone | Pi4 with official 7-inch DSI screen | Pi3B + with 3.5-inch GPIO screen | Pi3B + with 5-inch HDMI screen | Pi3B + with 7-inch HDMI screen | Pi3B + with official 7-inch DSI screen |
| -------- | --------------- | ----------------------------------- | -------------------------------- | ------------------------------ | ------------------------------ | -------------------------------------- |
| 3800mAh  | 4.2h            | 2.3h                                | 4.4h                             | 3.2h                           | 2.0h                           | 4.7h                                   |
| 6500mAh  | 7.5h            | 4.2h                                | 7.0h                             | 5.8h                           | 3.3h                           | 7.7h                                   |
| 10000mAh | 11.6h           | 6.5h                                | 11.6h                            | 9.0h                           | 5.8h                           | 13.0h                                  |

### Remarks:
1. All the above data units are hours.
2. The running system is: Raspbian Buster with desktop and recommended software Version: July 2019 Release date: 2019-07-10. The system does not make any setting changes.
3. The batteries of 3 kinds of capacity are fully charged. After connecting to the Raspberry Pi, use the program to record time. The discharge cut-off point is when the UPS detects that the battery voltage is lower than 2.8V, and the battery protection board is discharged.
4. Download and run UPSPACK_V2 / time_count / RPi_runtime_recoder.py for time recording. After the Raspberry Pi is turned off, connect to the log.txt in the program directory of the other power adapter to check the battery life.


## History
UPSPack V2 is based on UPSPack V1, which adds the ability for the UPS motherboard to communicate with the Raspberry Pi motherboard. In this way, information such as the current battery level on the UPS, external power outages, and whether the system output voltage is normal can be observed. As the software running on the Raspberry Pi system, through the comprehensive information obtained, it can realize the function of software shutdown (to prevent the loss of files on the TF card), and it can also send information such as shutdown or power failure to the designated Email, allowing users to use the phone Get these important reminders. Bring convenience to subsequent disposal.

### Hardware parameters
1. Micro USB input voltage: 5.1V 2-3A. Power adapter adaptive output current.
2. 2 USB-A / 5V GPIO pin headers: The output voltage is 5.1V ± 0.1V, and the maximum total output current of all ports is: 3.0A
3. With 1 UART serial port, baud rate: 9600 8N1
4. With 1 IO output port, high level: indicates that the battery is working normally. Low level: The battery is almost exhausted.
5. The battery output interface package is: PH2.0
6. 4 power LED lights, 1 PMU working status light, 1 external output power light.
7. An external output switch is used to control the external output voltage of the PMU.
8. UPS has on-board resettable fuses, and the three types of batteries have their own lithium battery protection boards. Prevent overcharge and over discharge.

### Mechanical Dimensions  
The mechanical aperture and position of UPSPack V2 and Raspberry Pi 4th / 3rd generation are the same. Therefore, it can be directly mounted on the Pi4 (Pi3) motherboard with M2.5 copper posts.


## Product Usage Guide
! [] (https://github.com/rcdrones/UPSPACK_V2/wiki/images/wire.JPG)
Enter [Wiki] (https://github.com/rcdrones/upspack_v2/wiki) to learn


## Partner
* [Amazon](https://www.amazon.com/MakerFocus-Raspberry-Standard-Expansion-Cellphone/dp/B01LAEX7J0)
* [RICELEE](https://ricelee.com/product/raspberry-pi-ups-lithium-battery-expansion-board)
* [EBAY](https://www.ebay.com/itm/UPS-Raspberry-Pi-Lithium-Battery-Expansion-Board-with-3800mAh-Lithium-Battery-/173685870116?_trksid=p2385738.m4383.l4275.c10)
* [AliExpress](https://www.aliexpress.com/item/UPS-Lithium-Battery-Expansion-Board-with-3800mAh-Lithium-Battery-for-Raspberry-Pi-Durable/32990788550.html)
* If you will like be partnership with us , contact us via email: rcdrones#163.com (# -> @)
