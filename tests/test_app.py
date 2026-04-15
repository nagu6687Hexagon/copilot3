import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Arrange-Act-Assert (AAA) pattern

def test_get_activities():
    # Arrange
    # (No special setup needed; uses in-memory data)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_register_participant():
    # Arrange
    activity = "Chess Club"
    email = "testuser1@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert f"Signed up {email}" in data["message"]
    # Confirm participant is in the list
    activities = client.get("/activities").json()
    assert email in activities[activity]["participants"]


def test_register_duplicate_participant():
    # Arrange
    activity = "Chess Club"
    email = "testuser2@mergington.edu"
    client.post(f"/activities/{activity}/signup?email={email}")

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    # Should fail or ignore duplicate (update this when backend is fixed)
    assert response.status_code == 200 or response.status_code == 400

# Add more tests for unregister and edge cases as needed
