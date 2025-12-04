# Unit test for Service B.
# Same principle as the test for Service A, but we're checking the /data route.
import pytest
from app import app as flask_app # Import our app instance

@pytest.fixture
def client():
    """Configures the app for testing and provides a test client."""
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_data_endpoint(client):
    """Tests the /data endpoint."""
    # Make a GET request to the /data route
    response = client.get('/data')
    
    # Check for a 200 OK status
    assert response.status_code == 200
    
    # Check for the correct JSON payload
    assert response.json == {"service": "Service B", "data": [1, 2, 3, 4, 5]}