from fastapi.testclient import TestClient
import uuid
from app.main import app

client = TestClient(app)

email = f"{uuid.uuid4()}@example.com"

def test_register():
    response = client.post(
        "/auth/register",
        json={
            "email": f"{uuid.uuid4()}@example.com",
            "username": f"user_{uuid.uuid4().hex[:8]}",
            "password": "password123"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "User created successfully"

def test_login():
    response = client.post(
    "/auth/login",
    json={
        "email": email,
        "password": "password123"
    }
)