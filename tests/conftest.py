import pytest
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.fixture
def circle():
    return Circle(10)


@pytest.fixture()
def rect():
    return Rectangle(10, 15)


@pytest.fixture()
def sqr():
    return Square(25)


@pytest.fixture()
def trngl():
    return Triangle(5, 6, 8)