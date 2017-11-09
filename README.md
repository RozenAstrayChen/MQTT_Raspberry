# MQTT on Raspberry Pi
工研院Raspberry pi課程使用

## BMP180
Using the Adafruit BMP Python Lib
```shell==
sudo apt-get update
sudo apt-get install git build-essential python-dev python-smbus
git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd Adafruit_Python_BMP
sudo python setup.py install
```
[follw this pdf](https://cdn-learn.adafruit.com/downloads/pdf/using-the-bmp085-with-raspberry-pi.pdf)

### If you havn't GPIO driver , [clone this](https://github.com/adafruit/Adafruit_Python_GPIO) 

## Commend
build this project
```
make all
```
clean project build
```
make clean
```
use scp copy to your target
```
make scp
```

## Tutorial

### step 1.
[pinout reference](https://thepihut.com/blogs/raspberry-pi-tutorials/18025084-sensors-pressure-temperature-and-altitude-with-the-bmp180)

### step 2.
should enable raspberry i2c interface
```shell==
sudo raspi-config
```
select __5. interface options__,and enable __i2c__.
if you can't find __5. interface options__,you can select __advance options__

Ok,after enable i2c. Detecting i2c 
```shell==
i2cdetect -l
``` 
So you can find interface
```shell==
i2c-1	i2c       	bcm2835 I2C adapter             	I2C adapter
```
Listening i2c adderss
```shell==
i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --      
```
If you find address in mapping.That is BMP180 has been detected by your Raspberry Pi and you can try:
```shell==
git clone https://github.com/RozenAstrayChen/MQTT_Raspberry.git
cd MQTT_Raspberry
make
```



## MQTT