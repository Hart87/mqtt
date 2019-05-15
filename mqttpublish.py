import paho.mqtt.publish as publish
import datetime

currently = datetime.datetime.now()
print(str(currently))
publish.single("CoreHart/test", "yes", hostname="test.mosquitto.org")
print("Publisher done...")

publish.single("CoreHart/reply", "this worx", hostname="test.mosquitto.org")
print("Publisher done...")