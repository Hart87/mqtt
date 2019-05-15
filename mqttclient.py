import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import datetime
import RPi.GPIO as GPIO
import time

currently = datetime.datetime.now()

#LED
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(19,GPIO.OUT)

def turn_on_led():
    print("LED on...")

    GPIO.output(19,True)
    time.sleep(3)

    print("LED off...")
    GPIO.output(19,False)
    

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("CoreHart/test")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    currently = datetime.datetime.now()
    print(str(currently))
    print(msg.topic+" "+str(msg.payload))
    
    if msg.payload == "yes":
        print("the message is YES :)")
        #Turn on the LED
        turn_on_led()
        #send message to iOS app
        publish.single("CoreHart/reply", "LED powered on", hostname="test.mosquitto.org")

        
        
#Create an MQTT client and attach our routines to it.
client = mqtt.Client()

#run
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()