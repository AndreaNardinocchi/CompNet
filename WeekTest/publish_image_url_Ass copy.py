from sense_hat import SenseHat
import paho.mqtt.client as mqtt
from urllib.parse import urlparse
from datetime import datetime
from capture_image import capture_image
from upload_image import upload_image

sense = SenseHat()
IMAGE_PATH="./images/sensehat_image.jpg"

# parse mqtt url for connection details
URL = urlparse("mqtt://broker.emqx.io:1883/AndreaNardinocchi/home/cameras/cam1")
BASE_TOPIC = URL.path[1:]

# MQTT event callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
         print("Connected successfully")
    else:
        print(f"Connection failed with code {rc}")

def on_publish(client, userdata, mid):
    print(f"Message ID: {mid} published successfully")

def on_disconnect(client, userdata, rc):
    print("Disconnected from MQTT broker")
    if rc != 0:
        print("Unexpected disconnection. Reconnecting...")
        client.reconnect()

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

# check if useame and password in the url (there isn't in this basic example)
if (URL.username):
    mqttc.username_pw_set(URL.username, URL.password)
# Connect
mqttc.connect(URL.hostname, URL.port)
mqttc.loop_start()

def publish_message():
    # Get the current time
    current_time = datetime.now()
    #Function to publish the message to the MQTT topic
    message = f"Photo taken at {current_time:%H:%M} | url: {upload_image(IMAGE_PATH)}"
    mqttc.publish(BASE_TOPIC, message)
    print("Message published:", message)
    
def photo():
  #  if event.action == "pressed":
    capture_image(IMAGE_PATH)
    upload_image(IMAGE_PATH)   
    print("Image captured using SenseHAT button and uploaded to https://polar-polar-dianella.glitch.me/!")
    publish_message()

# Taking picture
photo()
print("Great job!")
while True:
    pass  # Keep the script running to detect button presses