def test_create_schedule(client, schedule, auth_headers):
    response = client.post(
        "/schedules/", 
        json=schedule,
        headers=auth_headers
    )

    assert response.status_code == 200

def test_read_schedules(client, auth_headers):
    response = client.get(
        "/schedules/",
        headers=auth_headers
    )

    assert response.status_code == 200

def test_update_schedule(client, schedule, auth_headers):
    # First, create a schedule
    create_response = client.post(
        "/schedules/",
        json=schedule,
        headers=auth_headers
    )

    assert create_response.status_code == 200
    schedule_id = create_response.json()["id"]

    # Then, update the schedule
    updated_schedule = {**schedule, "name": "Updated Schedule Name"}
    update_response = client.put(
        f"/schedules/{schedule_id}",
        json=updated_schedule,
        headers=auth_headers
    )

    assert update_response.status_code == 200


def test_delete_schedule(client, schedule, auth_headers):
    # First, create a schedule
    create_response = client.post(
        "/schedules/",
        json=schedule,
        headers=auth_headers
    )

    assert create_response.status_code == 200
    schedule_id = create_response.json()["id"]

    # Then, delete the schedule
    delete_response = client.delete(
        f"/schedules/{schedule_id}",
        headers=auth_headers
    )

    assert delete_response.status_code == 204