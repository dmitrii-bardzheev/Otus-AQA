from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("side must be greater than 0")
        super().__init__(side, side)
