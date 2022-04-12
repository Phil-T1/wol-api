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

# Get libraries
from flask import Flask, request
from wakeonlan import send_magic_packet
import json

# Load device data
f = open('data.json')
devices = json.load(f)
f.close()

print(devices['01'])

# Initialise API
app = Flask(__name__)

# Return student list
@app.route('/',methods=['POST'])
def home():
    # Get API request type
    id = request.args.get('id')
    
    # Default error message
    action = 'Error 404 - no action taken'
    
    # If ID listed with MAC address in json then wake device
    if id in devices:
        mac = devices[id]
        send_magic_packet(mac)
        action = id + ' - success!'

    return action

# Run local server
if __name__ == "__main__":
    app.run(debug=True)