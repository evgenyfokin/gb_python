# task_2

user_list_length = int(input('Enter the length of the list: '))
user_list = []
i = 0
while i < user_list_length:
    user_list.append(input(f'Enter the {i + 1}-th number: '))
    i += 1

print(f'Original list: {user_list}')
if user_list_length % 2 > 0:
    i -= 2
else:
    i -= 1
while i > 0:
    user_list[i], user_list[i - 1] = user_list[i - 1], user_list[i]
    i -= 2
print(f'New list: {user_list}')
