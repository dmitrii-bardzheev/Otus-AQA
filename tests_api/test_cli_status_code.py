import requests


def test_cli(url, status_code):
    assert requests.get(url).status_code == status_code