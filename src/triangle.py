from src.figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or c + b <= a or a <= 0 or b <= 0 or c <= 0:
            raise ValueError("It is not triangle")
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
