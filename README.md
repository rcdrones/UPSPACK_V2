# UPSPack V2 产品软硬件使用指南

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/ups.jpg)

## 硬件资料

* 硬件参数

* 产品使用说明

* 机械尺寸

## 代码库介绍：
由于到了2019年，python3势不可挡，所以UPS的上位机全部是基于python3进行开发的。如果你用python2运行出错，请在代码中酌情更改。

* GUI_py文件夹内是基于tkinter库写的UPS上位机程序。可以得到UPS的版本号、电源输入是否正常、电池的电量、UPS输出电压值。

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/tk.png)

* console_py文件夹内是基于控制台输出的程序。功能和GUI程序类似。

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/console.png)

* single_io_py文件夹是利用树莓派任意GPIO口（默认为GPIO_18）接UPS的STA接口，进行电池低压关机操作。*比如你的树莓派UART接口需要用于其他用途，这时候用任意GPIO来探测UPS电池的低压情况，让树莓派在电池没电之前，稳妥的关机。*

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/console.png)

### 预先配置串口
树莓派和UPS，通过串口相连。需要确保串口0正确激活，并且正确指向GPIO口上。可用命令ls -l /dev 进行查看，如果看下和下图一样，即表示正确。

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/14.png)

如果没有配置，请查看如下：[教程](https://github.com/rcdrones/UPSPACK_V2/blob/master/doc/config_uart.md)。

### python demo程序使用教程

## 购买途径