import os
from dotenv import load_dotenv
from source.nasa_api_requests import nasa_neows_request

load_dotenv()

NASA_API_KEY = os.getenv('NASA_API_KEY')

## TESTS ##
def test_search_asteroids_with_sucess():
    # Arrange:
    query_parameters = f"api_key={NASA_API_KEY}"
    # Act:
    response = nasa_neows_request(query_parameters)
    # Assertion:
    assert response.status_code == 200  # Validation of status code
    data = response.json()
    # Assertion of body response content:
    assert len(data) > 0
    assert data["element_count"] > 0

def test_search_asteroids_with_query_parameters_empty():
    # Arrange:
    query_parameters = ""
    # Act:
    response = nasa_neows_request(query_parameters)
    # Assertion:
    assert response.status_code == 403

def test_search_asteroids_with_start_date():
    # Arrange:
    query_parameters = f"api_key={NASA_API_KEY}&start_date=2023-11-10"
    # Act:
    response = nasa_neows_request(query_parameters)
    # Assertion:
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data["element_count"] > 0

def test_search_asteroids_with_end_date():
    # Arrange:
    query_parameters = f"api_key={NASA_API_KEY}&start_date=2024-03-05&end_date=2024-03-10"
    # Act:
    response = nasa_neows_request(query_parameters)
    # Assertion:
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data["element_count"] > 0

def test_search_asteroids_in_valid_range():
    # Arrange:
    query_parameters = f"api_key={NASA_API_KEY}&start_date=2023-11-09&end_date=2023-11-10"
    # Act:
    response = nasa_neows_request(query_parameters)
    # Assertion:
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data["element_count"] > 0

def test_search_asteroids_in_invalid_range():
    # Arrange:
    query_parameters = f"api_key={NASA_API_KEY}&start_date=2023-11-19&end_date=2023-11-10"
    # Act:
    response = nasa_neows_request(query_parameters)
    # Assertion:
    assert response.status_code == 400

def test_search_asteroids_in_invalid_token():
    # Arrange:
    query_parameters = "api_key=INVALID_TOKEN"
    # Act:
    response = nasa_neows_request(query_parameters)
    # Assertion:
    assert response.status_code == 403