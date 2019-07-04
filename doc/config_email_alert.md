# 利用Email发送UPS断电提醒的消息

## 原理：
UPS经常会在无人坚守的情况下进行工作，如果由于外部市电突然断电，UPS就会开始消耗电池电能。当电池电能消耗完毕前，树莓派会自动关机。如果我们能把关机的时间点通过互联网通知网管，那不是更好吗？
UPS通过IO口和树莓派进行互联，树莓派就能时时刻刻知道UPS上的电池信息。当UPS上的电池快没电了，树莓派可以把当前关机的时间戳通过email方式发到互联网上。网管可通过手机或者PC上接收到这个警报信息。

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/mail1.png)

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/mail2.png)

## 如何做？

1. 首先把UPS和树莓派IO口进行连接：

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/wire.JPG)

相连的5个管脚的定义图：分别是5V(红色)、GND（黑色）、TXD（绿色）、RXD（黄色）、STA（蓝色），蓝色这条信号线，用于single IO warning功能，可接在任意空闲IO上。我们提供的UPS类库中默认定义在BCM.18脚，所以蓝色杜邦线接在下图的位置。

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/pinout.png)

2. 进入single_io_py/文件夹，用编辑器打开upspackv2.py，把10-11行进行相应的修改

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/mail_before.png)

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/mail_after.png)

3. 最后运行single_io.py
