## Contents
----------
- [The Overview](#the-overview)
- [Features](#features)
- [Contact me](#contact-me)
- [Information](#information)
- [Issue report template](#issue-report-template)

# The Overview
----------
- This script is used to replace the work that telegraf can't do base64 decoding on json files.
- This is a python script that receives the message from the port1883 MQTT broker.
- Send the decoded data back to the mqtt broker, then subscribe to the new topic via telegraf's mqtt plugin, and send it to influxdb (8086).

# Features
----------
- In the client script base64 decoding of the "data" part of the json file from the device.
- And reconfigures the message back to port 1883.
- along with a recive script to detect if the message has returned to the mqtt broker.
- Support python2.7 and 3.x+.

# Information
----------
![](https://github.com/solotaker/IoTGame/blob/master/IOT.png)
[HelTecDevice](http://www.heltec.cn/proudct_center/internet_of_things/)

# Contact me
----------
- [mail](mailto:1327270611@qq.com)

# Issue report template
----------
[for reference](https://github.com/solotaker/IoTGame/issues).     
  
