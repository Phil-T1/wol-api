'''
Simple API to wake local devices when called.
A dictionary must be saved in 'data.json', which contains an arbitrary two char string ID
for a device as a key, and the corresponding value as the MAC address.
e.g.
{
    "01": "AA:BB:CC:DD:EE:FF",
    "02": "GG:HH:II:JJ:KK:LL"
}
Wake by sending a get request to your WOL server's external IP address e.g.:
http://99.200.200.20:8888/?id=02
Where public port 8888 on your router is open to the net,
and forwarded to local port (default 5000) on your WOL server,
where the device to be woken is labelled id = "02" in the data.json file.

Full instructions in README.md
'''

# Import libraries
import json
import flask
from waitress import serve
from wakeonlan import send_magic_packet

# Choose the port forwarded from your router's IP to your local WOL server
PORT_FORWARDED = 5999

# Show flask version
print('Running flask version: ', flask.__version__)

# Load device data from json file
with open('data.json', encoding='utf8') as f:
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
        status = f'{wol_id} - success!'

    return status

# Run local server
if __name__ == '__main__':
    print('Server started...')
    serve(app, host='0.0.0.0', port=PORT_FORWARDED)
