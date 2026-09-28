import os

os.environ.setdefault(
    "GEMINI_API_KEY",
    "test-key"
)


from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_home_page():

    response = client.get("/")

    assert response.status_code == 200

    assert "EduGenie" in response.text


def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"


def test_api_info():

    response = client.get("/api")

    assert response.status_code == 200

    data = response.json()

    assert data["name"].startswith("EduGenie")

    assert "POST /qa" in data["endpoints"]


def test_empty_question():

    response = client.post(
        "/qa",
        json={
            "question": "",
            "level": "beginner"
        }
    )

    assert response.status_code == 422