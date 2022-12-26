# task_4

user_num = int(input("Enter your number: "))
biggest_num = user_num % 10
while user_num > 9:
    user_num //= 10
    if user_num % 10 > biggest_num:
        biggest_num = user_num % 10
print(f'The biggest number: {biggest_num}')
