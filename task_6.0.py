# task_6

from itertools import count


user_num = int(input('Enter the num to start with: '))
for i in count(user_num, 1):
    if i - user_num > 15:
        break
    print(i)
