import pytest


def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru")
    parser.addoption("--status_code", default=200)

@pytest.fixture()
def url(pytestconfig):
    return pytestconfig.getoption("--url")

@pytest.fixture()
def status_code(pytestconfig):
    return int(pytestconfig.getoption("--status_code"))