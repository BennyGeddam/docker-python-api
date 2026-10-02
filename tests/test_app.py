import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_returns_message(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello from Benny Agent Docker API"}


def test_health_is_healthy(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_info_has_name_and_version(client):
    response = client.get("/info")
    data = response.get_json()
    assert response.status_code == 200
    assert data["name"] == "docker-python-api"
    assert data["version"] == "1.0"


def test_unknown_route_returns_404(client):
    response = client.get("/does-not-exist")
    assert response.status_code == 404
