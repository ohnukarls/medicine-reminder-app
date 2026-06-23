import pytest
from fastapi.testclient import TestClient
from app.main import app
import uuid

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def user():
    return {
        "email": f"{uuid.uuid4()}@example.com",
        "username": f"user_{uuid.uuid4().hex[:8]}",
        "password": "password123"
    }

@pytest.fixture
def medication(client, auth_headers):
    response = client.post(
        "/medications/",
        json={
            "medication_name": "Tylenol",
            "dosage": "500mg",
            "instructions": "Take one tablet every 6 hours"
        },
        headers=auth_headers
    )
    assert response.status_code == 200
    return response.json()

@pytest.fixture
def adherence_log(medication):
    return {
        "medication_id": medication["id"],
        "taken_at": "2024-01-01T08:00:00Z",
        "status": "taken"
    }

@pytest.fixture
def schedule(client, medication, auth_headers):
    response = client.post(
        "/schedules/",
        json={
            "medication_id": medication["id"],
            "recurrence_pattern": "daily",
            "reminder_time": "2024-01-01T08:00:00Z",
            "timezone": "UTC"
        },
        headers=auth_headers
    )

    assert response.status_code == 200
    return response.json()

@pytest.fixture
def notification_log(schedule):
    return {
        "schedule_id": schedule["id"],
        "status": "sent",
        "message": "Reminder sent successfully"
    }

@pytest.fixture
def auth_headers(client, user): 
    # Register
    client.post(
        "/auth/register",
        json=user
    )

    # Login
    login_response = client.post(
        "/auth/login",
        json={
            "email": user["email"],
            "password": user["password"]
        }
    )

    token = login_response.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }
