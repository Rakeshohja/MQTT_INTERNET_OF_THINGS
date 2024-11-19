import paho.mqtt.client as mqtt
import random
import time

# Define MQTT server details
BROKER = 'broker.emqx.io'  # Public EMQX broker
PORT = 8083  # Secure WebSocket port for EMQX
TOPIC = 'RakeshOhja_A00260719/PriyankaPaul_A00287707/HaroldReyes_A00281588'

THRESHOLD = 70


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to EMQX broker over Secure WebSocket")
    else:
        print(f"Failed to connect with result code {rc}")

# Publish sensor values


def publish_values():
    # Create a client instance with WebSocket transport
    client = mqtt.Client(transport="websockets")
    client.on_connect = on_connect
    client.connect(BROKER, PORT, 60)  # Connect to the broker

    client.loop_start()

    try:
        while True:
            value = random.uniform(50, 100)
            client.publish(TOPIC, value)
            print(f"Published (value) to topic {TOPIC}")
            time.sleep(2)
    except KeyboardInterrupt:
        client.loop_stop()
        print("Stopping MQTT")


if __name__ == '__main__':
    publish_values()
