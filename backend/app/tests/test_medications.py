def test_create_medication(client, medication, auth_headers):    
    response = client.post(
        "/medications/",
        json=medication,
        headers=auth_headers
    )

    assert response.status_code == 200

def test_read_medications(client, auth_headers):
    response = client.get("/medications/", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_medication(client, medication, auth_headers):        
    create_response = client.post(
        "/medications/",
        json=medication,
        headers=auth_headers
    )

    medication_id = create_response.json()["id"]

    updated_medication = {
        "medication_name": "Ibuprofen",
        "dosage": "200mg",
        "instructions": "Take after meals"
    }

    update_response = client.put(
        f"/medications/{medication_id}",
        json=updated_medication,
        headers=auth_headers
    )

    assert update_response.status_code == 200

def test_delete_medication(client, medication, auth_headers):
    create_response = client.post(
        "/medications/",
        json=medication,
        headers=auth_headers
    )

    medication_id = create_response.json()["id"]

    delete_response = client.delete(f"/medications/{medication_id}", headers=auth_headers)
    assert delete_response.status_code == 204
