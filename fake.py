import json
import random
import time

import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)
client.loop_start()          # handles the connection in the background

print("Sending fake data...")

alt = 0
while True:
    alt += 10
    data = {"alt": alt, "vel": round(random.random() * 100)}
    client.publish("rocket/telemetry", json.dumps(data))
    time.sleep(0.2)          # 0.2 seconds = 5 messages per second