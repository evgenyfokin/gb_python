# task_3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Name: {self.name} {self.surname}')

    def get_total_income(self):
        print(
            f"Total income: {self._income['wage'] + self._income['bonus']}")


dev = Position('Jefferey', 'Smith', 'developer', 4000, 1400)
dev.get_full_name()
dev.get_total_income()
