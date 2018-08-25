# LightControlBridge
Bidirectional serial to HTTP bridge for controlling a matrix of LEDs

This project is designed to run on a Dragino Yun Shield running the Dragino IoT firmware, with the default web server moved from port 80 to 8080 by editing the uhttpd config file.

Status broadcasts (current video, current position) are received from the Arduino over serial, and remembered for future HTTP queries.  Settings changes and commands are received from the HTTP clients and transmitted to the Arduino over serial, and remembered for future HTTP queries.

HTTP requests are expected to be received from [a client-side single page web-app](https://github.com/MaddAddaM/LightControlUI).  It is compiled into a single `index.html` file along with its minified Javascript and CSS and served by this application.
