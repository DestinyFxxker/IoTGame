import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import json
import base64
import struct
import sys
stdi, stdo, stde = sys.stdin, sys.stdout, sys.stderr
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdin, sys.stdout, sys.stderr = stdi, stdo, stde





HOST = "localhost"

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

      

    

    format = '5x 2s 9x'

    Temp = map(eval,struct.unpack(format,data))

    format = '12x 2s 2x'

    Hum = map(eval,struct.unpack(format,data))

    client.publish(deviceName+"_Temp",Temp[0] , qos=0, retain=False)

    client.publish(deviceName+"_Hum",  Hum[0], qos=0, retain=False)

    client.publish(deviceName+"data" , data , qos=0, retain=False)

    print(deviceName)

   # print(devEUI)

    print(data)

    print(Temp[0])

    print(Hum[0])

if __name__ == '__main__':



    client_loop()
