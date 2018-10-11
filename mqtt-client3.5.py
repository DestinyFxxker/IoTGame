import paho.mqtt.client as mqtt
import time
import json
import base64
import struct
import sys
import importlib,sys 
importlib.reload(sys)
stdi, stdo, stde = sys.stdin, sys.stdout, sys.stderr
sys.stdin, sys.stdout, sys.stderr = stdi, stdo, stde



HOST = "127.0.0.1"
PORT = 1883

def client_loop():
    client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    client = mqtt.Client(client_id)    
    client.username_pw_set("loraroot", "62374838")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.loop_forever()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("application/3/device/223233aa66ac6668/rx")
    client.subscribe("application/1/device/2232330000000002/rx")
    client.subscribe("application/1/device/2232330000000003/rx")
    client.subscribe("application/1/device/2232330000000004/rx")


def on_message(client, userdata, msg):
    
    message = json.loads(msg.payload.decode("utf-8"))
    
    devEUI=message['devEUI']
    deviceName=message['deviceName']
    applicationName=message['applicationName']
    data=base64.b64decode(message['data'])

    list = [1] 
    for i in range(0,len(data),4):
        stream=[data[i],data[i+1],data[i+2],data[i+3]]
        value = struct.unpack('f', bytearray(stream))[0]
        list.append(value)
    
    typecode=list[0]
    
    if typecode==1:
        client.publish(deviceName+"_Temp", json.dumps({"devEUI":devEUI,"value":list[1]} ,sort_keys=True), qos=0, retain=False)
        client.publish(deviceName+"_XValue", json.dumps({"devEUI":devEUI,"value":list[2]} ,sort_keys=True), qos=0, retain=False)
        client.publish(deviceName+"_YValue", json.dumps({"devEUI":devEUI,"value":list[3]} ,sort_keys=True), qos=0, retain=False)
        client.publish(deviceName+"_ZValue", json.dumps({"devEUI":devEUI,"value":list[4]} ,sort_keys=True), qos=0, retain=False)
        client.publish(deviceName+"_Angle", json.dumps({"devEUI":devEUI,"value":list[4]} ,sort_keys=True), qos=0, retain=False)
        client.publish(deviceName+"data" , data , qos=0, retain=False)
    if typecode==2:
        client.publish(deviceName+"_Temp", json.dumps({"devEUI":devEUI,"value":list[1]} ,sort_keys=True), qos=0, retain=False)
        client.publish(deviceName+"_Humidity", json.dumps({"devEUI":devEUI,"value":list[2]} ,sort_keys=True), qos=0, retain=False)

    text = '%s' % (list)   
    print(deviceName)
    print(text)
    print(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))

if __name__ == '__main__':

    

    
    client_loop()
