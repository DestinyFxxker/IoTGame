import paho.mqtt.client as mqtt
import time
import struct
import sys
import base64
import json
stdi, stdo, stde = sys.stdin, sys.stdout, sys.stderr
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdin, sys.stdout, sys.stderr = stdi, stdo, stde


def client_loop():
    client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    client = mqtt.Client(client_id)    
    client.username_pw_set("heltec", "62374838")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.loop_forever()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("application/2/device/223233aa66ac6668/rx")
#    client.subscribe("application/2/device/223233aa66ac6668/tx")

def on_message(client, userdata, msg):
    s = json.loads(msg.payload.decode("utf-8")) # - {'altitude', 'longitue', 'latitude'}
    s.pop('altitude', None)
    s.pop('latitude', None)
    s.pop('longitude', None)
    print("ADD: " + msg.topic + " " + str(msg.qos) + " " + json.dumps(s)) #json.dumps(s, indent=4))
    if (msg.topic.endswith("/rx") and 'data' in s):
        m = base64.b64decode(s['data'])
        print("fport: " + str(s['fPort']) + " msg: [" + m + "]")
        print("loraSNR: " + str(s['rxInfo'][0]['loRaSNR']) + " rssi: " + str(s['rxInfo'][0]['rssi']))
        r = {}
        r['reference'] = "test_some"
        r['confirmed'] = True
        r['fPort'] = s['fPort']
        r['data'] = base64.b64encode('ABC')
#        r['data'] = base64.b64encode("answer " + m.split(" ")[0])
        print(m)
        print(r['data'])
        client.publish(msg.topic.replace("/rx", "/tx"), json.dumps(r))

if __name__ == '__main__':
 
  HOST = "127.0.0.1"
  PORT = 1883
  client_loop()
