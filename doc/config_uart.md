# 树莓派串口0配置指南
本文所有配置是基于Raspbian 2019-04-08系统进行编写。[下载链接][download]。
[download]: https://downloads.raspberrypi.org/raspbian_full_latest "Raspbian的官方下载链接"


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








sudo nano /boot/config.txt

pi3-miniuart-bt

ctrl+x -> y ->enter


ls -l /dev

sudo apt-get install minicom
chose y

sudo minicom -D /dev/ttyAMA0 -b 9600

exit:

ctrl+A -> z -> x




------------

git clone https://github.com/rcdrones/UPSPACK_V2.git

sudo apt-get install fcitx fcitx-googlepinyin fcitx-module-cloudpinyin fcitx-sunpinyin