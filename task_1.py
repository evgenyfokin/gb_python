# task_1

class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for i in self.my_list:
            print(i)
        return ''

    def __add__(self, other):
        for row in self.my_list:
            new_row = []
            for i in row:
                new_row.append(i * 2)
            print(new_row)


my_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_matrix)
my_matrix + my_matrix
