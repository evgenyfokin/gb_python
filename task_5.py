# task_5

user_num = int(input('Enter your number: '))
default_list = [user_num, 7, 5, 3, 3, 2]
i = 0
while i < len(default_list) - 1:
    if default_list[i] < default_list[i + 1]:
        default_list[i], default_list[i + 1] = default_list[i + 1], \
                                               default_list[i]
    i += 1
print(default_list)