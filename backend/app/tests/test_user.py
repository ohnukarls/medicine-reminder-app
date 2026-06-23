import uuid

def test_read_user(client, auth_headers):
    response = client.get("/users/me", headers=auth_headers)
    assert response.status_code == 200

def test_update_user(client, auth_headers, user):
    new_user = user.copy()
    new_user["username"] = f"user_{uuid.uuid4().hex[:8]}"
    new_user["email"] = f"{uuid.uuid4()}@example.com"
    response = client.put("/users/me", json=new_user, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["username"] == new_user["username"]
    assert response.json()["email"] == new_user["email"]
     
def test_delete_user(client, auth_headers):
    response = client.delete("/users/me", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["message"] == "Account deleted successfully"