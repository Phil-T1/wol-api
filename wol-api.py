# Get libraries
from flask import Flask, request

# Initialise API
app = Flask(__name__)

# Return student list
@app.route('/',methods=['POST'])
def home():
    output = request.args.get('status')
    return output

# Run local server
if __name__ == "__main__":
    app.run(debug=True)