from module.MQTT_Test import My_MQTT
import platform
import time
if(platform.system() == 'Linux'):
	from  Adafruit_BMP.BMP085 import BMP085 # Imports the BMP library
	from module.Servo import Servo

class Rozen_Object(My_MQTT,BMP085,Servo):
#class Rozen_Object(My_MQTT,Servo):
#class Rozen_Object(My_MQTT):
	def __init__(self,ip,port,pin,mode = 1,addr = 0x77,**kwargs):
		My_MQTT.__init__(self, ip, port)
		BMP085.__init__(self, mode, addr, **kwargs)
		Servo.__init__(self, pin)
		
		self.client.on_message = self.On_Message

	# Receive message and judgment how topic data you need
	def On_Message(self, client, userdata, msg):
		print("Rozen " + msg.topic + " " + str(msg.payload))
		if(str(msg.topic) == "Servo"):
			self.Servo_control(msg.payload)
			pass
		elif(str(msg.topic) == "Infrared"):
			#your code and if you add code need remove `pass`
			pass

	def Servo_control(self,value):
		if(platform.system() == 'Linux'):
			self.update(value)
	def Infrared_control(self,value):
		#your code and if you add code need remove `pass`
		pass

	def Start_Up_Temp(self,topic,data):
		loop_time = 0;
		self.client.connect(self.ip, port=self.port, keepalive=60)
		"""
		These functions implement a threaded interface to the network loop. 
		Calling loop_start() once, before or after connect*(), runs a thread in the background to call loop() automatically. 
		This frees up the main thread for other work that may be blocking. This call also handles reconnecting to the broker. 
		Call loop_stop() to stop the background thread. The force argument is currently ignored.
		"""
		self.client.loop_start()
		while True:
			time.sleep(1)
			self.client.publish(topic, data)
			if(loop_time != 10):
				#loop_time = loop_time+1
				pass
			else:
				self.client.loop_stop(force=False)
				break


