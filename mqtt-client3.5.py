import paho.mqtt.client as mqtt
import time
import json
import base64
import sys
import importlib,sys 
importlib.reload(sys)
stdi, stdo, stde = sys.stdin, sys.stdout, sys.stderr
sys.stdin, sys.stdout, sys.stderr = stdi, stdo, stde


def client_loop():
    client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    client = mqtt.Client(client_id)    
    client.username_pw_set("username", "password")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.loop_forever()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("application/1/device/2232330000000001/rx")
    client.subscribe("application/1/device/2232330000000002/rx")
    client.subscribe("application/1/device/2232330000000003/rx")
    client.subscribe("application/1/device/2232330000000004/rx")


def on_message(client, userdata, msg):
    
    message = json.loads(msg.payload.decode("utf-8"))
    
    devEUI=message['devEUI']
    deviceName=message['deviceName']
    applicationName=message['applicationName']
    data=base64.b64decode(message['data'])
    client.publish(deviceName+"data" , data , qos=0, retain=False)

    print(deviceName)
    print(applicationName)
    print(data)
    print(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))

if __name__ == '__main__':
   HOST = "127.0.0.1"
   PORT = 1883
   client_loop()
