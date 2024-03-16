# dragonfly

A simple Python program to consume MQTT commands for automation tasks.

This can be used as a remote execution platform for things like Home Assistant. For example, adding the following to your Home Assistant configuration.yaml file will give you a button that plays a sound from the computer running dragonfly when pressed:

```yaml
mqtt:
    - button:
        unique_id: 6720f97a-91b9-4e9e-9fb5-9a0c0fd22a30
        name: "Play sound"
        command_topic: "dragonfly/test/play"
        payload_press: '{"file":"audio/door-chime.wav","volume":"50"}'
```

Obviously you need to be running the Mosquitto MQTT broker in Home Assistant as well as have the audio file available on the computer running dragonfly.

More to come...

## Installation

First, clone the repo and set up the dependencies:

```bash
git clone https://github.com/jgkawell/dragonfly.git
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install paho-mqtt
```

Then, you can run the program with:

```bash
./script/run YOUR_OPTIONS
```

Additionally, you can install the program as a service. First open up the `dragonfly.service` file and modify the options to suit your needs. Then copy the file to the systemd directory and enable the service:

```bash
sudo cp dragonfly.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable dragonfly
sudo systemctl start dragonfly
```

And you can check on the status of the service with:

```bash
sudo systemctl status dragonfly
```
