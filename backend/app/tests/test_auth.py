def test_register(client, user):
    response = client.post(
        "/auth/register",
        json=user
    )
    assert response.status_code == 200

def test_login(client, user):
    client.post(
        "/auth/register",
        json=user
    )

    response = client.post(
        "/auth/login",
        json={
            "email": user["email"],
            "password": user["password"]
        }
    )

    assert response.status_code == 200