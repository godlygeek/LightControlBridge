# LightControlBridge
Bidirectional serial to HTTP bridge for controlling a matrix of LEDs

This project is designed to run on a Dragino Yun Shield running the Dragino IoT firmware, with the default web server moved from port 80 to 8080 by editing the uhttpd config file.

Status broadcasts (current video, current position) are received from the Arduino over serial, and remembered for future HTTP queries.  Settings changes and commands are received from the HTTP clients and transmitted to the Arduino over serial, and remembered for future HTTP queries.
