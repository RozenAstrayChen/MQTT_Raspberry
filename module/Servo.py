import time
import RPi.GPIO as GPIO

# default
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(5)


class Servo(object):
	def __init__(self,pin):
		self.GPIO = GPIO
		self.GPIO.setmode(GPIO.BCM)
		self.GPIO.setup(pin, GPIO.OUT)

		self.pwm = pwm 
		self.pwm = self.GPIO.PWM(pin, 100)
		self.pwm.start(5)

	def __del__(self):
		self.GPIO.cleanup()
		self.pwm.stop()

	def update(self,angle):
		duty = float(angle) / 10.0 +2.5
		self.pwm.ChangeDutyCycle(duty)




