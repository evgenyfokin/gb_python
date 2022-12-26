# task_7

def get_factorial(n):
    for num in range(1, n):
        yield num


result = 1
user_num = int(input('Enter your num: '))
for el in get_factorial(user_num):
    print(el)
    result *= el
print(f'factorial of {user_num}: {result}')
