# task_5

from random import randint

with open('task_5_addition.txt', 'w', encoding='utf-8') as new_file:
    for i in range(5, randint(5, 13)):
        new_file.write(f'{str(randint(1, 100))} ')

with open('task_5_addition.txt', 'r', encoding='utf-8') as f_obj:
    str_list = f_obj.readline().split()
    acc = 0
    for i in str_list:
        acc += int(i)
    print(f'The sum: {acc}')
