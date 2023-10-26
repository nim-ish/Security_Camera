import RPi.GPIO as GPIO
import time
import picamera
from time import sleep
import paho.mqtt.client as mqtt



#pir sensor
PIR_PIN=4
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN,GPIO.IN)

#led

#LED_PIN=17
##GPIO.setmode(GPIO.BCM)
#GPIO.setup(LED_PIN,GPIO.OUT)

#Buzzer

buzzer_pin= 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin,GPIO.OUT)
#camera
camera=picamera.PiCamera()
camera.resolution=(1280,720)
camera.rotation=180

#MQTT Configuration
mqtt_broker_address ="broker.hivemq.com"
mqtt_topic="group8/house/intruder"

#MQTT Setup
mqtt_client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("Connected to MQTT Broker")
	else:
		print(f"Connection to MQTT broker failed with code {rc}")
	
mqtt_client.on_connect = on_connect
mqtt_client.connect(mqtt_broker_address, 1883, 60)

#Main Loop
try:
	while True:
		if GPIO.input(PIR_PIN):
			print("Motion Detected")
			#GPIO.output(LED_PIN, GPIO.HIGH)
			GPIO.output(buzzer_pin, GPIO.HIGH)
			timestamp= time.strftime("%Y%m%d-%H%M%S")
			filename="motion_"+timestamp+".h264"
			camera.start_recording(filename)
			camera.wait_recording(3)
			camera.stop_recording()
			#GPIO.output(LED_PIN, GPIO.LOW)
			GPIO.output(buzzer_pin, GPIO.LOW)
			print("Video captured:",filename)
			time.sleep(5)
			
			
			#Publish a message to MQTT
			mqtt_client.publish(mqtt_topic, "Intruder detected in the house!")
		time.sleep(0.5)
except KeyboardInterrupt:
	pass
finally:
	camera.close()
	GPIO.cleanup()
