from module.MQTT_Test import My_MQTT
from module.Rozen_Object import Rozen_Object
import platform
import Adafruit_BMP.BMP085 as BMP085 # Imports the BMP library

Node_Red_Ip = "192.168.0.10"
Node_Red_Port = 1883


if(platform.system() == 'Linux'):
	print('use on ' + platform.system())
	
	sensor = BMP085.BMP085(busnum=2)
	print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature()) # Temperature in Celcius

	MQ = My_MQTT(Node_Red_Ip,Node_Red_Port)
	MQ.Publish(sensor.read_temperature())
	
	#Obj = Rozen_Object(Node_Red_Ip,Node_Red_Port)

elif(platform.system() == 'Darwin'):
	print('use on ' + platform.system() + ' not test Sensor')

	MQ = My_MQTT(Node_Red_Ip,Node_Red_Port)
	MQ.Publish(123)

else:
	print('not use platform on ' + platform.system())
