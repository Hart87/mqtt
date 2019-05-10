import paho.mqtt.publish as publish

publish.single("CoreHart/test", "yes", hostname="test.mosquitto.org")
print("Publisher done...")