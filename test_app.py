import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ── Basic arithmetic (as required by spec) ──────────────────────────────────

def test_home():
    """Required spec test: basic arithmetic sanity check."""
    assert 1 + 1 == 2


# ── Route tests ───────────────────────────────────────────────────────────────

def test_home_route(client):
    """GET / returns 200 with expected keys."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert "status" in data
    assert data["status"] == "running"


def test_health_route(client):
    """GET /health returns 200 and healthy status."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_add_route(client):
    """GET /add/<a>/<b> returns correct sum."""
    response = client.get("/add/3/7")
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 10


def test_add_large_numbers(client):
    """Addition works with large numbers."""
    response = client.get("/add/100/200")
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 300


def test_add_zeros(client):
    """Addition works with zeros."""
    response = client.get("/add/0/0")
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 0