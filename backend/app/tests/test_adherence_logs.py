def test_create_adherence_log(client, adherence_log, auth_headers):
    response = client.post(
        "/adherence_logs/",
        json=adherence_log,
        headers=auth_headers
    )

    assert response.status_code == 200
    assert response.json()["status"] == adherence_log["status"]

def test_read_adherence_logs(client, auth_headers):
    response = client.get(
        "/adherence_logs/",
        headers=auth_headers
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_adherence_log(client, adherence_log, auth_headers):
    # Create log
    create_response = client.post(
        "/adherence_logs/",
        json=adherence_log,
        headers=auth_headers
    )

    assert create_response.status_code == 200
    log_id = create_response.json()["id"]

    # Update log
    updated_log = adherence_log.copy()
    updated_log["status"] = "missed"

    update_response = client.put(
        f"/adherence_logs/{log_id}",
        json=updated_log,
        headers=auth_headers
    )

    assert update_response.status_code == 200
    assert update_response.json()["status"] == "missed"

def test_delete_adherence_log(client, adherence_log, auth_headers):
    # Create log
    create_response = client.post(
        "/adherence_logs/",
        json=adherence_log,
        headers=auth_headers
    )

    assert create_response.status_code == 200
    log_id = create_response.json()["id"]

    # Delete log
    delete_response = client.delete(
        f"/adherence_logs/{log_id}",
        headers=auth_headers
    )

    assert delete_response.status_code == 204

