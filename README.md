# UPSPack V2 产品软硬件使用指南

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/ups.JPG)

## 产品介绍
树莓派是一款SBC主板，本身和台式Linux电脑的应用很相近。所有的系统都跑带自带的TF存储卡上。但是当外部突然断电时，TF卡上的系统数据(或者用户数据)面临丢失的可能，从而导致系统无法启动的恶果。此外树莓派由于本身体积较小，在便携式应用中，就需要一个合适的移动电源对树莓派进行供电。基于以上的考虑，RPi Club设计了这款UPSPack V2的产品，你可以把它当作移动电源来使用，亦可以当作树莓派的不间断供电电源来使用。除此以外，V2版本提供了串口通讯，和单IO通讯的接口，可以和树莓派主板进行信息交互。让跑在Linux系统之上的软件可以得知UPS上几乎所有硬件/电池信息。从而决策关机的时间点，亦可向云端报告外部供电异常等信息。

## 电池的续航测试
UPSPack板载电池接口为PH2.0封装。产品提供了3种不同容量的电池可供客户选择。客户亦可自行接入不同容量：标准电压为3.7V的锂聚合物软包电池，或者是3.7V 18650电池组。注意：输入UPS电池接口的电压范围必须是小于等于4.2V。（言外之意：所有电池组必须是并联关系，不能把电芯串联）。我们搭建了不同的应用组合，得到了一些续航数据。供给客户参考不同的电池容量：


|  容量  |   Pi4单机  |  Pi4搭载官方7寸DSI屏  |  Pi3B+搭载3.5寸GPIO屏  |  Pi3B+搭载5寸HDMI屏  |  Pi3B+搭载7寸HDMI屏  |  Pi3B+搭载官方7寸DSI屏  |
|--------|------------|-----------------------|------------------------|----------------------|----------------------|-------------------------|
|3800mAh |  4.2h     |      2.3h              |   4.4h                |     3.2h             |          2.0h         |        4.7h             |
|6500mAh |   7.5h     |  4.2h                 |   7.0h                 |     5.8h             |          3.3h       |        7.7h              |
|10000mAh |   11.6h      |  6.5h                |   11.6h                 |     9.0h              |          5.8h         |        13.0h             |
### 备注：
1. 以上所有数据单位为小时(hours)。
2. 运行的系统为：Raspbian Buster with desktop and recommended software Version:July 2019 Release date:2019-07-10 ，系统不做任何设置修改。
3. 3种容量的电池完全充满电量，然后接入树莓派后，利用程序进行时间记录。放电截至点为UPS检测到电池电压低于2.8V，电池保护板截至放电为止。 
4. 下载、并运行 UPSPACK_V2/time_count/RPi_runtime_recoder.py 进行时间记录。当树莓派关机后，接入其他电源适配器读取程序目录下的log.txt进行续航时间的查看。


## 历史介绍
UPSPack V2是在UPSPack V1版本的基础上，增加了UPS主板和树莓派主板进行交互通讯的能力。从而可以观测到当前UPS上的电池电量、外部是否停电、系统输出电压是否正常等信息。作为运行在树莓派系统上的软件，通过得到的这些综合性信息，实现软件关机的功能(防止TF卡上的文件丢失）、亦可向指定Email发送关机or停电等信息，让用户在手机上得到这些重要的提醒。为后续处置带来方便。

* 硬件参数
1. Micro USB 输入电压：5.1V 2-3A。电源适配器自适应输出电流。
2. 2个USB-A座/5V GPIO排针口： 输出电压为 5.1V±0.1V  ，所有端口输出电流最大合计为：3.0A 
3. 带1个UART串口，波特率：9600 8N1
4. 带1个IO输出口，高电平：表示电池工作正常。 低电平：表示电池即将消耗完毕。
5. 电池输出接口封装为： PH2.0
6. 4颗电量LED灯，1颗PMU工作状态灯，1颗外部输出电源灯。
7. 1个外部输出开关，用于控制PMU对外输出的电压。
8. UPS板载自恢复保险丝，并且3款电池内部分别自带锂电池保护板。防止过充和过放。 


* 机械尺寸



* 产品使用指南：
进入[Wiki](https://github.com/rcdrones/upspack_v2/wiki)进行学习






## 代码库介绍：
UPS python基于Python3开发，我们把UPS的数据包协议解析、IO口探测封装成了UPS类库，尽可能的减少软件耦合性。有经验的开发者，只需要5分钟稍微熟悉一下demo程序，即可把UPS功能集成到自己的项目内。

* GUI_py文件夹内是基于tkinter库写的UPS上位机程序。可以得到UPS的版本号、电源输入是否正常、电池的电量、UPS输出电压值。

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/tk.png)

* console_py文件夹内是基于控制台输出的程序。功能和GUI程序类似。

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/console.png)

* single_io_py文件夹是利用树莓派任意GPIO口（默认为GPIO_18）接UPS的STA接口，进行电池低压关机操作。*比如你的树莓派UART接口需要用于其他用途，这时候用任意GPIO来探测UPS电池的低压情况，让树莓派在电池没电之前，稳妥的关机。*

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/single.png)

* email警报功能：在UPS关机的时候把email发送到可设置的地址上。[教程](https://github.com/rcdrones/UPSPACK_V2/blob/master/doc/config_email_alert.md)

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/mail1.png)


## 软件教学：
* 树莓派和UPS，通过串口相连。需要确保串口0正确激活，并且正确指向GPIO口上。可用命令ls -l /dev 进行查看，如果看到和下图一样，即表示配置正确，可跳过这一步。

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/14.png)

如果和上图不一致，请查看如下：[教程](https://github.com/rcdrones/UPSPACK_V2/blob/master/doc/config_uart.md)。

* 下载代码库，并运行。[教程](https://github.com/rcdrones/UPSPACK_V2/blob/master/doc/rpi_sw.md)


## 合作伙伴
* [Amazon](https://www.amazon.com/MakerFocus-Raspberry-Standard-Expansion-Cellphone/dp/B01LAEX7J0)
* [RICELEE](https://ricelee.com/product/raspberry-pi-ups-lithium-battery-expansion-board)
* [EBAY](https://www.ebay.com/itm/UPS-Raspberry-Pi-Lithium-Battery-Expansion-Board-with-3800mAh-Lithium-Battery-/173685870116?_trksid=p2385738.m4383.l4275.c10)
* [AliExpress](https://www.aliexpress.com/item/UPS-Lithium-Battery-Expansion-Board-with-3800mAh-Lithium-Battery-for-Raspberry-Pi-Durable/32990788550.html)
* If you will like be partnership with us , contact us via email: rcdrones#163.com (# -> @)

