class Figure:
    def get_area(self):
        raise NotImplementedError("Method must be implemented")

    def get_perimeter(self):
        raise NotImplementedError("Method must be implemented")

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Should be a Figure")
        return self.get_area() + figure.get_area()
