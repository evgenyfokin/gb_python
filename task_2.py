# task_2

class Road:
    weight = 25
    thickness = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def result(self):
        total = self._length * self._width * Road.weight * Road.thickness
        print(f"{total} kilograms")


measure = Road(20, 5000)
measure.result()
