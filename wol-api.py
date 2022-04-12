'''
Simple API to wake devices when called.
A dictionary must be saved in 'data.json', which contains an arbitrary two char string ID
for a device as a key, and the corresponding value as the MAC address.
e.g.
{
    "01": "AA:BB:CC:DD:EE:FF",
    "02": "GG:HH:II:JJ:KK:LL"
}
'''

# Import libraries
from flask import Flask, request
from wakeonlan import send_magic_packet
import json

# Load device data from json file
f = open('data.json')
devices = json.load(f)
f.close()

# Initialise API
app = Flask(__name__)

# Create WOL endpoint
@app.route('/')
def wol():

    # Get API request type
    id = request.args.get('id')
    
    # Default error message
    status = 'Error 404'
    
    # If ID listed with MAC address in json then wake device
    if id in devices:
        mac = devices[id]
        send_magic_packet(mac)
        status = id + ' - success!'

    return status

# Run local server
if __name__ == "__main__":
    app.run(host='0.0.0.0', ssl_context=('certificate.pem', 'private-key.pem'), port=5000)