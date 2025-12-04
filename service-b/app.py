# This is Service B.
# Very similar to Service A, but it serves some different data
# on a different route and port.
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')
def get_data():
    """Serves some sample data."""
    # Just a different route and response to distinguish it from Service A.
    return jsonify({"service": "Service B", "data": [1, 2, 3, 4, 5]})

if __name__ == '__main__':
    # Running this service on port 5002.
    app.run(host='0.0.0.0', port=5002)