# task_4

def my_func(x, y):
    if x <= 0:
        return '"x" must greater than 0'
    if y >= 0:
        return '"y" must less than 0'
    i = 1
    result = x
    while i < y * -1:
        result *= x
        i += 1
    return 1/result


print(my_func(int(input('Number to be powered: ')),
              int(input('Degree: '))))
