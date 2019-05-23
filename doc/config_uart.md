# 树莓派串口0配置指南
本文所有配置是基于Raspbian 2019-04-08系统进行编写。[下载链接][download]。

[download]: https://downloads.raspberrypi.org/raspbian_full_latest "Raspbian的官方下载链接"


## 下载好全新系统，在终端使用ls -l /dev 查看串口设备的指向关系
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/1.png)







dao 9

ls -l /dev

10


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