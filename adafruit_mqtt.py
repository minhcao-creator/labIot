import sys
from Adafruit_IO import MQTTClient
import time
import random

class Adafruit_MQTT:
    AIO_FEED_IDs = ["nutnhan1", "nutnhan2"]
    AIO_USERNAME = "minhcao2000"
    AIO_KEY = "aio_qYHw80uBHuHDIiNWLSmOpZufTQt2"

    def connected(self, client):
        print("Connected ...")
        for feed in self.AIO_FEED_IDs:
            client.subscribe(feed)

    def subscribe(self, client , userdata , mid , granted_qos):
        print("Subscribeb...")

    def disconnected(self, client):
        print("Disconnected...")
        sys.exit (1)

    def message(self, client , feed_id , payload):
        print("Received: " + payload)

    def __init__(self):
        client = MQTTClient(self.AIO_USERNAME , self.AIO_KEY)
        client.on_connect = self.connected
        client.on_disconnect = self.disconnected
        client.on_message = self.message
        client.on_subscribe = self.subscribe
        client.connect()
        client.loop_background()
        counter = 5
        sensor_type = 0
        while True:
            counter = counter - 1
            if (counter <= 0):
                counter = 5
                #TODO
                print("Random data is publising...")
                if sensor_type == 0:
                    print("Temperture...")
                    temp = random.randint(10,20)
                    client.publish("cambien1", temp)
                    sensor_type = 1
                elif sensor_type == 1:
                    print("Humidity...")
                    humi = random.randint(100,700)
                    client.publish("cambien2", humi)
                    sensor_type = 2
                elif sensor_type == 2:
                    print("Light...")
                    light = random.randint(50,70)
                    client.publish("cambien3", light)
                    sensor_type = 0
            time.sleep(1)
            pass

