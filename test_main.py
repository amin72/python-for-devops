from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_api():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. Call /search or /wiki"}


def test_phrase_api():
    response = client.get("/phrase/Barack Obama")
    assert response.status_code == 200
    assert response.json() == {
        "results": [
            "barack hussein obama ii",
            "bə-rahk hoo-sayn oh-bah-mə",
            "august",
            "american politician",
            "44th president",
        ]
    }
