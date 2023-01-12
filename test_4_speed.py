from timeit import timeit


def sum_user_numbers():
    user_input = '='
    total = 0
    while user_input != '=':
        total += sum([int(x) for x in user_input.split(' ')])
        user_input = input('Enter your nums: ')
    return print(total)


print(timeit('sum_user_numbers()', setup='from __main__ import '
                                         'sum_user_numbers', number=1000000))

"""После оптимизации -> 2.801369666998653
    Увеличить скорость удалось за счет функции 'sum()'. Встроенные функции 
Python эффективнее, т.к написаны на языке С или С++, 
который более быстрый, чем Python. 
    Увеличению скорости также поспособствовало применение LC"""
