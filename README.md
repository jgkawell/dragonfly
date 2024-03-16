# dragonfly

A simple Python program to consume MQTT commands for automation tasks.

This can be used as a remote execution platform for things like Home Assistant. For example, adding the following to your Home Assistant configuration.yaml file will give you a button that plays a sound from the computer running dragonfly when pressed:

```yaml
mqtt:
    - button:
        unique_id: 6720f97a-91b9-4e9e-9fb5-9a0c0fd22a30
        name: "Play sound"
        command_topic: "dragonfly/test/play"
        payload_press: "audio/sound.wav"
```

Obviously you need to be running the Mosquitto MQTT broker in Home Assistant as well as have the audio file available on the computer running dragonfly.

More to come...
