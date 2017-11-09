# SubscriberTest.py
import paho.mqtt.client as mqtt
#import paho.mqtt as paho
import time

class My_MQTT():
	def __init__(self,ip,port):
		self.client = mqtt.Client()
		self.ip = ip
		self.port = port
		self.client.on_connect = self.On_Connect
		self.client.on_message = self.On_Message

	def __del__(self):
		self.client.stop()

	def On_Connect(self, client, userdata, flag, rc):
		print("Connect with result code "+ str(rc))
		client.subscribe("Servo")

	def On_Message(self, client, userdata, msg):
		print(msg.topic + " " + str(msg.payload))

	def Edit_Ip(self,ip):
		self.ip = ip
	def Edit_Port(self,port):
		self.port
	# Test connect and use subscribe to test it work
	def Test_Connect(self):
		self.client.connect(self.ip, port=self.port, keepalive=60)
		self.client.loop_forever()

	def Subscribe(self,topic):
		client.subscribe(topic)
		
	def Publish(self,topic,data):
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
				loop_time = loop_time+1
			else:
				self.client.loop_stop(force=False)
				break



