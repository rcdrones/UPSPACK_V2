# 上位机软件使用指南

## 下载代码库：
```
cd ~
git clone https://github.com/rcdrones/UPSPACK_V2
```
![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/sw1.png)

## 运行程序：
* 鼠标双击运行，比如进入GUI_py文件夹，双击UPS_GUI_demo.py，会跳出：

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/sw2.png)

直接选*在终端模拟器中执行(T)*,如果选择第一个*执行(E)*，程序会在后台执行，会引起串口资源释放不干净的问题。所以务必选第二个选项。

* 在终端命令行执行程序：
```
cd UPSPACK_V2/
cd GUI_py/
./UPS_GUI_demo.py 
```

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/sw3.png)

## UPS库函数介绍：

![](https://github.com/rcdrones/UPSPACK_V2/raw/master/doc/img/sw4.png)
```python
from upspackv2 import *  #加载UPS库

test = UPS2("/dev/ttyAMA0") 	#建议一个UPS的对象，把实际的端口传给UPS。

version,vin,batcap,vout = test.decode_uart()   #得到软件版本，输入电压是否正常、电池电量、输出电压

```