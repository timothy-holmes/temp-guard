import pytest
import app # the package starting from the base dir /temp-guard

@pytest.fixture
def client():
    return app.app.test_client()

def test_index_endpoint(client):
    index_page_response = client.get('/')
    assert index_page_response.status_code == 200

def test_404_error(client):
    response = client.get('/blahblahtypo')
    assert response.status_code == 404

def test_current_temp_endpoint(client):
    temp = client.get('/current-temp').json['temp']
    assert temp >= 0 and temp < 2000

def test_critical_temp_endpoint(client):
    trip_points = client.get('/trip-points').json
    assert trip_points == {
        'ActiveTripPoint': 500,
        'PassiveTripPoint': 1000,
        'CriticalTripPoint': 1500
    }
