from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle
import pytest
# python -m pytest

                                            # Тесты для круга
def test_circle():
    c = Circle(10)
    assert c.r == 10


@pytest.mark.parametrize("r", [0, -10])
def test_circle_invalid(r):
    with pytest.raises(ValueError):
        Circle(r)


def test_circle_area(circle):
    assert circle.get_area() == pytest.approx(314.159265358978)


def test_circle_perimetr(circle):
    assert circle.get_perimeter() == pytest.approx(62.831853071796)


def test_circle_gtr(circle):
    assert circle.add_area(Circle(5)) == pytest.approx(392.699081698724)


                                        # Тесты для прямоугольника


def test_rect():
    r = Rectangle(10, 20)
    assert r.side_a == 10
    assert r.side_b == 20


@pytest.mark.parametrize("s1, s2", [(5, -5), (0, 10), (0, 0)])
def test_rect_invalid(s1, s2):
    with pytest.raises(ValueError):
        Rectangle(s1, s2)


def test_rect_area(rect):
    assert rect.get_area() == 150


def test_rect_perim(rect):
    assert rect.get_perimeter() == 50


def test_rect_add(rect):
    assert rect.add_area(Circle(10)) == pytest.approx(464.15926535898)


                                            # Тесты для квадрата


def test_sqr():
    s = Square(30)
    assert s.side_a == s.side_b == 30


@pytest.mark.parametrize("s", [0, -15])
def test_sqr_invalid(s):
    with pytest.raises(ValueError):
        Square(s)


def test_sqr_area(sqr):
    assert sqr.get_area() == 625


def test_sqr_perim(sqr):
    assert sqr.get_perimeter() == 100


def test_sqr_add(sqr):
    assert sqr.add_area(Rectangle(5, 10)) == 675


                                        # Тесты для треугольника


def test_trngl():
    t = Triangle(5, 6, 8)
    assert t.a == 5 and t.b == 6 and t.c == 8


@pytest.mark.parametrize("a, b, c", [(0, 0, 0), (5, 0, 10), (-4, 10, 8), (-5, -6, -8), (5, 5, 12)])
def test_trngl_invalid(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)


def test_trngl_area(trngl):
    assert trngl.get_area() == pytest.approx(14.9812382665786)


def test_trngl_perim(trngl):
    assert trngl.get_perimeter() == 19


def test_add_invalid(trngl):
    with pytest.raises(ValueError):
        trngl.add_area(10)