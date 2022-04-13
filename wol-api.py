'''
Simple API to wake devices when called.
A dictionary must be saved in 'data.json', which contains an arbitrary two char string ID
for a device as a key, and the corresponding value as the MAC address.
e.g.
{
    "01": "AA:BB:CC:DD:EE:FF",
    "02": "GG:HH:II:JJ:KK:LL"
}
Wake by sending a get command via IFTTT to your external IP address (you'll need a port open) e.g.
http://99.200.200.20:8888/?id=02
Where port 8888 is open to the net and forwarded to port 5000 and your local device.
'''

# Import libraries
import flask
from waitress import serve
from wakeonlan import send_magic_packet
import json

# Show flask version
print('Running flask version: ', flask.__version__)

# Load device data from json file
f = open('data.json')
devices = json.load(f)
f.close()

# Initialise API
app = flask.Flask(__name__)

# Create WOL endpoint
@app.route('/')
def wol():

    # Get API request type
    id = flask.request.args.get('id')
    
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
    serve(app, host='0.0.0.0', port=5000)