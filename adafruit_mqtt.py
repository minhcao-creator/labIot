import sys
from Adafruit_IO import MQTTClient
import time
import random
from simple_ai import *
from uart import *


class Adafruit_MQTT:
    AIO_FEED_IDs = ["nutnhan1", "nutnhan2"]
    AIO_USERNAME = "minhcao2000"
    AIO_KEY = "aio_vVmk453IGGDbowXlKuUyncbIKCWc"

    def connected(self, client):
        print("Connected ...")
        for feed in self.AIO_FEED_IDs:
            client.subscribe(feed)

    def subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribeb...")

    def disconnected(self, client):
        print("Disconnected...")
        sys.exit(1)

    def message(self, client, feed_id, payload):
        print("Received: " + payload)
        if feed_id == 'nutnhan1':
            if payload == '0':
                writeData("1")
            else:
                writeData("2")
        if feed_id == 'nutnhan2':
            if payload == '0':
                writeData("3")
            else:
                writeData("4")

    def __init__(self):
        client = MQTTClient(self.AIO_USERNAME, self.AIO_KEY)
        client.on_connect = self.connected
        client.on_disconnect = self.disconnected
        client.on_message = self.message
        client.on_subscribe = self.subscribe
        client.connect()
        client.loop_background()
        # counter = 5
        # sensor_type = 0
        counter_ai = 5
        pre_label_ai = ""
        while True:
            # counter = counter - 1
            # if (counter <= 0):
            #     counter = 5

            #     print("Random data is publising...")
            #     if sensor_type == 0:
            #         print("Temperture...")
            #         temp = random.randint(10, 20)
            #         client.publish("cambien1", temp)
            #         sensor_type = 1
            #     elif sensor_type == 1:
            #         print("Humidity...")
            #         humi = random.randint(100, 700)
            #         client.publish("cambien2", humi)
            #         sensor_type = 2
            #     elif sensor_type == 2:
            #         print("Light...")
            #         light = random.randint(50, 70)
            #         client.publish("cambien3", light)
            #         sensor_type = 0

            counter_ai = counter_ai - 1
            if counter_ai <= 0:
                label_ai = image_detector()
                counter_ai = 5
                if label_ai != pre_label_ai:
                    client.publish("ai", label_ai)
                    pre_label_ai = label_ai
            readSerial(client)
            time.sleep(1)
