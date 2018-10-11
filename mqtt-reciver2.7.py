import paho.mqtt.client as mqtt
import time
import struct
import sys
stdi, stdo, stde = sys.stdin, sys.stdout, sys.stderr
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdin, sys.stdout, sys.stderr = stdi, stdo, stde


HOST = "127.0.0.1"
PORT = 1883

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
    client.subscribe("ESP32TEST_9527_Temp")
    client.subscribe("ESP32TEST_9527_XValue")
    client.subscribe("ESP32TEST_9527_YValue")
    client.subscribe("ESP32TEST_9527_ZValue")
    client.subscribe("ESP32TEST_9527_Angle")
    client.subscribe("ESP32TEST_9527_data")


def on_message(client, userdata, msg):

    print(msg.topic+": "+msg.payload.decode("utf-8"))
    print(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))

if __name__ == '__main__':

    

    
    client_loop()
