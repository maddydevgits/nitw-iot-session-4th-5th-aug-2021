from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
from arduino import send_to_arduino

client=AWSIoTMQTTClient("new_Client")
client.configureEndpoint('.iot.eu-west-1.amazonaws.com',8883)
client.configureCredentials("root-CA.crt", "private.pem.key","certificate.pem.crt")

client.configureOfflinePublishQueueing(-1) # Infinite Publish Queueing
client.configureDrainingFrequency(2) # Frequency of Data Transfer
client.configureConnectDisconnectTimeout(10) # 10 Seconds
client.configureMQTTOperationTimeout(5) # 5 Seconds

def notification(client,userdata,message):
	print ('Received a new message: ')
  	t=message.payload
  	send_to_arduino(t)
	print (t)
	print ("from topic: ")
	print (message.topic)

client.connect() # Try to connect with AWS IoT Core by using above credentials
print ("MQTT Client is connected to AWS IoT Core")
time.sleep(2)
client.subscribe("device/relay",1,notification)

while True:
	pass

