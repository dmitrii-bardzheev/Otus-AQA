# python -m pytest tests_api/test_jsonplaceholder_api.py -v
import pytest
import requests

HEADERS = {
    'Content-type': 'application/json; charset=UTF-8',
}
URL = "https://jsonplaceholder.typicode.com"
DATA = {
    "title": 'foo',
    "body": 'bar',
    "userId": 1
}


def test_create_post_pshdr():
    response = requests.post(f"{URL}/posts", json=DATA, headers=HEADERS)
    assert response.status_code == 201, response.status_code
    data = response.json()
    assert isinstance(data, dict)
    assert all(key in data for key in ["userId", "id", "title", "body"])
    assert all(DATA[item] == data[item] for item in ["userId", "title", "body"])


def test_get_pshdr1():
    response = requests.get(f"{URL}/users/1/albums")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_get_pshdr():
    response = requests.get(f"{URL}/posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert all(key in data[0] for key in ["userId", "id", "title", "body"])


@pytest.mark.parametrize("num", [1, 5, 10, 50])
def test_get_pshdr_num(num):
    response = requests.get(f"{URL}/posts/{num}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) > 0
    assert all(key in data for key in ["userId", "id", "title", "body"])
    assert data["id"] == num


@pytest.mark.parametrize("num", [1, 5, 10, 50])
def test_get_pshrd_com(num):
    response = requests.get(f"{URL}/posts/{num}/comments")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert all(all(key in item for key in ["postId", "id", "name", "email", "body"]) for item in data)
    assert all(item["postId"] == num for item in data)
    assert all(isinstance(i["id"], int) for i in data)


