# python -m pytest tests_api/test_openbrewery_api.py -v
import pytest
import requests
URL = "https://api.openbrewerydb.org/v1/breweries"

def test_general():
    page_amount = 5
    response = requests.get(URL, params={"per_page": page_amount})
    data = response.json()
    assert response.status_code == 200, f"Expected code 200, received {response.status_code}"
    assert isinstance(data, list), f"The type of data is {type(data)}"
    assert len(data) == page_amount, f"The length of the list is {len(data)}"



@pytest.mark.parametrize("city", ["moscow", "boston", "houston"])
def test_by_city(city):
    response = requests.get(URL, params={"by_city": city})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list), f"The type of data is {type(data)}"
    assert len(data) > 0, f"The length of the list is less than 1"
    assert all(map(lambda x: x.lower() == city, [i["city"] for i in data])), f"Incorrect city {city}"


@pytest.mark.parametrize("type_brew", ["micro", "regional", "brewpub"])
def test_by_type(type_brew):
    response = requests.get(URL, params={"by_type": type_brew})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list), f"The type of data is {type(data)}"
    assert len(data) > 0, f"The length of the list is less than 1"
    assert all(item["brewery_type"] == type_brew for item in data)

