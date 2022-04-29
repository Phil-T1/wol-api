wol_api

Created 29-Apr-2022
By Phil Tegg

SUMMARY:
A simple REST API flask app to run on an internet-facing WOL Server that will turn on
local devices by sending them magic packets.

SECURITY FIRST:
This app requires that you expose a device on your network to the internet, please ensure
you understand the security risks before using this.
Anybody can send a request to your device if they know its address.

Instructions:
(1) A WOL Server is required for this project. I use a Raspberry Pi that has this app running 24/7,
    waiting for a HTTP request to wake any devices on your local network.

(2) Forward a public-facing port on your router to a local port for your WOL Server (local port is 5000 in the code),
    exposing the WOL Server to the internet for HTTP requests.
    You'll need to do this in your router port forwarding settings.
    ONLY USE IF YOU UNDERSTAND THAT EXPOSING A DEVICE DIRECTLY TO THE INTERNET IS A SECURITY RISK.
    ANYBODY CAN SEND A REQUEST TO YOUR DEVICE AT YOUR IP ADDRESS.

(3) In the wol_api.py file, set the PORT_FORWARDED value to the port number you have forwarded
    from your router to your WOL server (the default is 5000).

(4) Create a data.json file in the main directory using a text editor.
    Add a dictionary of device IDs (any strings you like) and MAC addresses, for example:
{
	"01": "00:00:00:00:00:00",
	"02": "11:11:11:11:11:11"
}

(5) Run the app
Test the app in your browser, for example, if your public port is 8888 and the device to be woken has
id = "02" in the data.json then enter in the address bar:
http://99.200.200.20:8888/?id=02

(6) Consider IFTTT
I created an IFTTT applet to send a get request that can be triggered from Alexa (I say "Trigger work" wake
my work laptop). IFTTT is free for five applets and it only takes seconds to create them.
