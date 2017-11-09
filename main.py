from module.MQTT_Test import My_MQTT
from module.Rozen_Object import Rozen_Object
import platform
import time

Node_Red_Ip = "localhost"
Node_Red_Port = 1883

if(platform.system() == 'Linux'):
	import Adafruit_BMP.BMP085 as BMP085 # Imports the BMP library
	from module.Servo import Servo
	print('use on ' + platform.system())
	#BMP085 test
	"""
	sensor = BMP085.BMP085()
	print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature()) # Temperature in Celcius
	#MQTT test
 
	MQ = My_MQTT(Node_Red_Ip,Node_Red_Port)
	MQ.Publish(sensor.read_temperature())

	#Servo test

	servo = Servo(18)
	while(True):
		i = input("input angle: ")
		servo.update(i)
		time.sleep(1)
	"""
	obj = Rozen_Object(Node_Red_Ip,Node_Red_Port,18)
	obj.Start_Up_Temp("Temp",obj.read_temperature())
	
elif(platform.system() == 'Darwin'):
	print('use on ' + platform.system() + ' not test Sensor')

	#MQ = My_MQTT(Node_Red_Ip,Node_Red_Port)
	#MQ.Publish("Temp",123)
	obj = Rozen_Object(Node_Red_Ip,Node_Red_Port,18)
	obj.Start_Up_Temp("Temp",122)

else:
	print('not use platform on ' + platform.system())
