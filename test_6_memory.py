from memory_profiler import profile
import numpy as np
from collections import Counter


@profile()
def my_origin():
    my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

    new_list = [i for i in my_list if my_list.count(i) == 1]
    print(new_list)


my_origin()
"""Оригинальное решение."""


@profile()
def my_numpy():
    my_list = (item for item, count in
               Counter(np.array(
                   [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11])).items()
               if count == 1)
    for i in my_list:
        print(i)


my_numpy()

"""NumPy использует массивы одного типа данных и интегрированные механизмы 
обработки. Стандартный же способ использования массивов с помощью 
списков или кортежей требует больше памяти, ввиду потенциального нахождения в 
них значений различных типов данных."""
