# task_4

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print(f"{self.name} goes")

    def stop(self):
        return print(f"{self.name} stops")

    def turn(self, direction):
        return print(f"{self.name} turning {direction}")

    def show_speed(self):
        return print(f'Your speed is {self.speed} km/h')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Your speed is {self.speed} km/h')
        if self.speed > 90:
            return print(f"Impressive! Your {self.name} is a really fast one")
        else:
            return print(f"Haha, is all u r capable of!? Your {self.name} - "
                         f"is a bucket")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Your speed is {self.speed} km/h')
        if self.speed > 60:
            return print(f"U r not allowed to move so fast in such type of "
                         f"transport. Your {self.name} is a town car.")
        else:
            return print(f"It's appropriate for such type of "
                         f"transport. Your {self.name} is a town car.")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Your speed is {self.speed} km/h')
        if self.speed > 40:
            return print(f"U r not allowed to move so fast in such type of "
                         f"transport. Your {self.name} is a work car.")
        else:
            return print(f"It's appropriate for such type of "
                         f"transport. Your {self.name} is a work car.")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def horn(self):
        if self.is_police:
            print(f"Whoop-whoop")
        else:
            print(f"Beeeeep")


cooper = TownCar(59, 'gray', 'mini', False)
cooper.show_speed()
cooper.go()
cooper.turn('left')
cooper.stop()
print()

lada = PoliceCar(11, 'blue', 'granta', True)
lada.horn()
lada.go()
lada.turn('right')
lada.stop()
print()

kamaz = WorkCar(64, 'black', 'kamaz', False)
kamaz.show_speed()
print()

nissan = SportCar(150, 'orange', 'skyline', False)
nissan.show_speed()
