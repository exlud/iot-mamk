# Description

Write a program that reads temperature and humidity values from the DHT22 sensor and publishes the messages
over the local MQTT connection. The messages should have a separate topic for humidity and temperature data,
and you should use your name as the top-level topic. Example topic: “/saana/temperature”. The MQTT messages
should be sent once every 5 seconds. Subscribe to your own topic on an MQTT client on your own computer.
