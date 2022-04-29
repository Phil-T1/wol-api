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
import json
import flask
from waitress import serve
from wakeonlan import send_magic_packet

# Choose the port forwarded from your router's IP to your local WOL server
PORT_FORWARDED = 5000

# Show flask version
print('Running flask version: ', flask.__version__)

# Load device data from json file
f = open('data.json', encoding='utf8')
devices = json.load(f)
f.close()

# Initialise API
app = flask.Flask(__name__)

# Create WOL endpoint
@app.route('/')
def wol():
    '''
    Endpoint for WOL request.
    id = 1 or id =2 is passed in a http request, and the corresponding MAC address is read from the
    data.json file.
    A magic packet is then sent locally to the device's MAC address.
    '''

    # Get API request type
    wol_id = flask.request.args.get('id')

    # Default error message
    status = 'Error 404'

    # If ID listed with MAC address in json then wake device
    if wol_id in devices:
        mac = devices[wol_id]
        send_magic_packet(mac)
        status = wol_id + ' - success!'

    return status

# Run local server
if __name__ == "__main__":
    print('Server started...')
    serve(app, host='0.0.0.0', port=PORT_FORWARDED)
    