from module.MQTT_Test import My_MQTT
import platform
from  Adafruit_BMP.BMP085 import BMP085 # Imports the BMP library


class Rozen_Object(My_MQTT,BMP085):
	#def __init__(self,ip,port,BMP085_I2CADDR= 0x77,BMP085_STANDARD = 1,**kwargs):
		#super(My_MQTT, self).__init__()
		#My_MQTT.__init__(self, ip, port)
		#BMP085.__init__(self)

	def test():
		print('hi')
