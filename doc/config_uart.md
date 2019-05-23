# 树莓派串口0配置指南
本文所有配置是基于Raspbian 2019-04-08系统进行编写。[下载链接](https://downloads.raspberrypi.org/raspbian_full_latest)


## 下载好全新系统，在终端使用ls -l /dev 查看串口设备的指向关系
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/1.png)


## 利用 sudo raspi-config 进行uart的配置。
简单的描述一下过程：选Interfacing Options -> Serial -> No -> Yes -> 显示小节
然后回到主界面 -> 利用TAB键 -> 选到 Finish -> 重启选Yes

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/2.png)
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/3.png)
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/4.png)
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/5.png)
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/6.png)
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/7.png)
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/8.png)
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/9.png)

重启之后，利用ls -l /dev 再次查看串口设备的指向关系
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/10.png)


## 利用dtoverlay，把串口0和串口1的指向进行交换。
首先查看下/boot/overlays，确认有一个叫pi3-miniuart-bt.dtbo的文件。
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/11.png)

命令行打入 sudo nano /boot/config.txt ，在文件的最后加入：pi3-miniuart-bt
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/12.png)

ctrl+x -> Yes -> 回车退出：
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/13.png)

再次用ls -l /dev，查看串口0和串口1的指向关系。主要是查看 serial0 -> ttyAMA0 这个指向要确保和下图一致。
UPS python程序就是和树莓派 /dev/ttyAMA0进行通讯的。
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/14.png)

# 通过minicom串口软件，验证树莓派的串口0和UPS进行正常通信。
## 硬件连线：
首先把UPS和树莓派IO口进行连接：
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/wire.JPG)

相连的5个管脚的定义图：分别是5V(红色)、GND（黑色）、TXD（绿色）、RXD（黄色）、STA（蓝色），蓝色这条信号线，用于single IO warning功能，可接在任意空闲IO上。我们提供的UPS类库中默认定义在BCM.18脚，所以蓝色杜邦线接在下图的位置。
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/pinout.png)

## minicom使用：
Raspbian默认无内置minicom软件，通过 sudo apt-get install minicom 进行下载安装。
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/15.png)


运行：sudo minicom -D /dev/ttyAMA0 -b 9600 
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/16.png)

可以看到UPS发到树莓派上的协议数据包。由于Linux上'\n'只换行，不回到行首。所以minicom上看到的协议，会超出屏幕。这没有关系，我们后面可以利用python来过滤这些信息。
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/17.png)

如果还没看到UPS的数据包，请从本文开头进行步骤对比，一般是中间有步骤漏做导致。如果想退出minicom:
ctrl+A -> z -> x

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/18.png)
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/19.png)


# TIPS：
install chinese 输入法：
sudo apt-get install fcitx fcitx-googlepinyin fcitx-module-cloudpinyin fcitx-sunpinyin

