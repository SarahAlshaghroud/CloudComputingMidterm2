import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json


broker_address="10.20.1.95"
# This is the Publisher
client = mqtt.Client()
x = {"StudentID":201520, "Name":"Sarah","Surname":"Alshaghroud","Telephone":"0556543","Grade":100}
y = json.dumps(x)
topic = "se443/midterm2"
if (client.connect(broker_address,1883,60) == 0):
	print ("Connected succesfully to "+broker_address)
	
client.publish(topic, y)
print ("Published in "+topic+", msg = "+y)
client.disconnect()