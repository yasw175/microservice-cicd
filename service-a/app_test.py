# Just a basic smoke test for our Service A endpoint.
# This ensures the app is configured correctly and the route returns what we expect.
import pytest
from app import app as flask_app # Import our app instance

@pytest.fixture
def client():
    """Configures the app for testing and provides a test client."""
    # This sets up a test "client" we can use to make virtual requests
    # to our app without having to run a full web server.
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Tests the / endpoint."""
    # Make a GET request to the home ('/') route
    response = client.get('/')
    
    # Check that we get a 200 OK status code
    assert response.status_code == 200
    
    # Check that the JSON payload is exactly what we expect.
    assert response.json == {"message": "Hello from Service A! v1.0"}