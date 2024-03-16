import argparse
import os
import ssl
import json

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")

def on_message(client, userdata, msg):
    print(f"Recieved message {str(msg.payload)} on topic {msg.topic}")
    match msg.topic.split('/')[-1]:
        case 'play':
            play(msg.payload)
        case 'volume':
            volume(msg.payload.decode('utf-8'))
        case _:
            print('Unknown command')

def play(message):
    msg = json.loads(message)
    volume(msg['volume'])
    os.system(f"aplay {msg['file']}")

def volume(volume):
    os.system(f"amixer sset Master {volume}%")

parser = argparse.ArgumentParser()
parser.add_argument('-N', '--name', required=True)
parser.add_argument('-H', '--host', required=True, help='MQTT broker host (e.g. mqtt.local or 192.168.X.Y)\n')
parser.add_argument('-U', '--username', required=False, default=None)
parser.add_argument('-P', '--password', required=False, default=None)
parser.add_argument('-T', '--port', required=False, type=int, default=1883, help='Using port 8883 will enable TLS\n')
args, unknown = parser.parse_known_args()


mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.username_pw_set(args.username, args.password)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
if args.port == 8883:
    mqttc.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=None, tls_version=ssl.PROTOCOL_TLSv1_2)

mqttc.connect(args.host, args.port, 60)
mqttc.subscribe(f'dragonfly/{args.name}/#', 2)

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting
mqttc.loop_forever()
