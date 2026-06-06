def test_create_notification_log(client, auth_headers, notification_log):
    response = client.post(
        "/notification_logs/",
        json=notification_log,
        headers=auth_headers
    )

    assert response.status_code == 200

def test_read_notification_logs(client, auth_headers):
    response = client.get(
        "/notification_logs/",
        headers=auth_headers
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_notification_log(client, auth_headers, notification_log):
    # First, create a notification log to delete
    create_response = client.post(
        "/notification_logs/",
        json=notification_log,
        headers=auth_headers
    )
    assert create_response.status_code == 200 
    created_log = create_response.json()

    # Now, delete the created notification log
    delete_response = client.delete(
        f"/notification_logs/{created_log['id']}",
        headers=auth_headers
    )
    assert delete_response.status_code == 204