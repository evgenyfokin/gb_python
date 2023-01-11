class NotTooWide:
    def __set__(self, instance, value):
        if value > 100:
            raise ValueError("Hey! We don't do the square roads")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class NotStr:
    def __set__(self, instance, value):
        if isinstance(value, str):
            raise ValueError('It would be adorable to receive a number.')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Road:
    weight = 25
    thickness = 0.05
    length = NotTooWide()
    width = NotStr()

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def result(self):
        total = self.length * self.width * Road.weight * Road.thickness
        return f"{total} kilograms"


# measure = Road(101, 5000)
# measure_2 = Road(99, '5000')
