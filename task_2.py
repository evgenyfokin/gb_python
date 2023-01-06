# task_2

class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return f"Two cells are combined into one containing " \
               f"{self.quantity + other.quantity} parts."

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        if sub > 0:
            return f'Cell difference is {sub}.'
        elif sub < 0:
            return f"Cell difference is {sub * -1}."
        else:
            return "The cells are equal, now we are out of them."

    def __mul__(self, other):
        return f"The product of two cells is " \
               f"{self.quantity * other.quantity}."

    def __truediv__(self, other):
        return f"The division of two cells is " \
               f"{self.quantity // other.quantity}."


my_cell = Cell(17)
your_cell = Cell(15)
print(my_cell + your_cell)
print(my_cell - your_cell)
print(my_cell * your_cell)
print(my_cell / your_cell)
