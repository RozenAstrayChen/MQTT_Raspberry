# MQTT on Raspberry Pi
工研院Raspberry pi課程使用

## Commend
這些指令在 __專案根目錄下__ 執行，將會執行 __Makefile裡面的命令__。如果只需要編譯請執行 ```make all```
- build this project
```
make all
```
- clean project build
```
make clean
```
- use scp copy to your target
```
make scp
```

## BMP180
請先安裝 Adafruit BMP Python Lib
```shell==
sudo apt-get update
sudo apt-get install git build-essential python-dev python-smbus
git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd Adafruit_Python_BMP
sudo python setup.py install
```
[接角請參照這份文件](https://cdn-learn.adafruit.com/downloads/pdf/using-the-bmp085-with-raspberry-pi.pdf)

### 如果沒有Rpi的 GPIO Lib 請安裝此套件, [clone this](https://github.com/adafruit/Adafruit_Python_GPIO) 

## 教學

### i2c 部分
__請先完成上面BMP180部分後__，啟動 Rpi 的 i2c
```shell==
sudo raspi-config
```
選擇 __5. interface options__,在選擇 __i2c__.
如果沒有找到 __5. interface options__,選擇 __advance options__

接下來在執行 偵測i2c 
```shell==
i2cdetect -l
``` 
你可以發現i2c介面
```shell==
i2c-1	i2c       	bcm2835 I2C adapter             	I2C adapter
```
監聽 i2c 地址
![](https://i.imgur.com/cVJXEz2.jpg)

如果發現 i2c 地址，則代表已經有偵測到感測器，接下來下載專案
```shell==
git clone https://github.com/RozenAstrayChen/MQTT_Raspberry.git
cd MQTT_Raspberry
make
```

### Node Red
先更新和安裝npm 套件
```shell==
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:gias-kay-lee/npm
sudo apt-get update
sudo apt-get install nodejs npm node-semver
```
確認 npm版本
```shell==
npm -v
```
### Mosquitto MQTT Broker
- Mosquitto 主要功能是將 MQTT port 打開，如果沒有執行，則會造成 Node Red connted boker failed
安裝：
```shell==
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
sudo apt-get update
sudo apt-get install mosquitto
sudo apt-get install mosquitto-clients
```
執行:
```shell==
sudo service stop mosquitto
sudo service start mosquitto #see note later
```
如果執行失敗，代表mosquitto 不在 bin 裏，則執行
```shell==
sudo /etc/init.d/mosquitto start 
```
若需要關掉
```shell==
sudo /etc/init.d/mosquitto stop 
```
檢查是否開啟 MQTT Broker
![](https://i.imgur.com/IIEyBwT.jpg)

開機自動啟動 Mosquitto，需重新開機。如果沒有自動開啟請參考此[連結](https://forums.debiancn.org/t/mosquitto-1-4-10/393/8) 
```shell==
systemctl enable mosquitto
sudo reboot
```

- [其他請參考](http://www.steves-internet-guide.com/install-mosquitto-broker/)

### Node Red


node red clipboard in __Clipboard.txt__