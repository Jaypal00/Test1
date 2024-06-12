from fastapi.testclient import TestClient
from run import app

client = TestClient(app)

def test_add_success():
    response = client.post("/add", json={"numbers": [[1, 2], [3, 4]]})
    assert response.status_code == 200
    assert response.json() == {"result": [3,7]}

def test_add_empty():
    response = client.post("/add", json={"numbers": []})
    assert response.status_code == 200
    assert response.json() == {"result": [0]}

def test_add_invalid():
    response = client.post("/add", json={"numbers": [1, 2, 'abc']})
    assert response.status_code == 500
