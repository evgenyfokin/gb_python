# task_3

def my_func(num_1, num_2, num_3):
    if num_1 > num_2 & num_1 > num_3:
        if num_2 > num_3:
            return f'The sum of two biggest nums: {num_1 + num_2}'
        else:
            return f'The sum of two biggest nums: {num_1 + num_3}'
    else:
        return f'The sum of two biggest nums: {num_2 + num_3}'


num1, num2, num3 = int(input('Enter the 1-st num: ')), \
                   int(input('Enter the 1-st num: ')), \
                   int(input('Enter the 1-st num: '))

print(my_func(num1, num2, num3))
