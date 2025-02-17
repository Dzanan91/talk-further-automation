from support.random_utils import generate_author_payload

def test_create_author(authors_api):
    """
    1) Generate a random author payload
    2) POST /api/v1/Authors
    3) Assert the status code and echoed response
    """
    payload = generate_author_payload()
    
    create_response = authors_api.create_author(payload)
    assert create_response.status_code in [200], f"Create failed: {create_response.status_code}"

    created_author = create_response.json()
    assert created_author["id"] == payload["id"], "ID mismatch"
    assert created_author["firstName"] == payload["firstName"], "firstName mismatch"
    assert created_author["lastName"] == payload["lastName"], "lastName mismatch"

def test_get_author(authors_api):
    """
    1) GET an existing author by ID (e.g., 1) from the default data set
    2) Assert we get a 200 response
    3) Validate the returned structure
    """
    author_id = 1  
    get_response = authors_api.get_author(author_id)
    assert get_response.status_code == 200, f"GET failed: {get_response.status_code}"
    
    author_data = get_response.json()
    assert "id" in author_data
    assert "firstName" in author_data
    assert "lastName" in author_data

def test_delete_author(authors_api):
    """
    1) DELETE an existing author by ID (e.g., 1)
    2) Assert we get a 200  response
    """
    author_id = 1
    delete_response = authors_api.delete_author(author_id)
    assert delete_response.status_code in [200], f"Delete failed: {delete_response.status_code}"
    
    get_response = authors_api.get_author(author_id)
    assert get_response.status_code in [200], f"Unexpected status: {get_response.status_code}"

def test_create_author_invalid_payload(authors_api):
    """
    Test that creating an author with an invalid payload 
    returns an appropriate error code (e.g., 400).
    """
    invalid_payload = {
        "id": None,
    }
    response = authors_api.create_author(invalid_payload)
    assert response.status_code in [400], f"Expected error, got {response.status_code}"
