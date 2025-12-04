# Hey team, this is the code for Service A.
# It's just a super simple Flask app that returns a JSON message.
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """Serves the home-page and primary API endpoint."""
    # Just a simple JSON response to show the service is up.
    return jsonify({"message": "Hello from Service A! v1.0"})

if __name__ == '__main__':
    # We run on 0.0.0.0 to make it accessible outside the container.
    # Port 5001 is specific to this service.
    app.run(host='0.0.0.0', port=5001)