# task_6

from itertools import cycle
from random import randint

your_list = []
i = 0
while i < randint(3, 10):
    your_list.append(randint(0, 5))
    i += 1
print(your_list)

i = 0
cycle_your_list = cycle(your_list)
for j in cycle_your_list:
    print(j)
    i += 1
    if i == 20:
        break
print(f"It's been {i} circles")
