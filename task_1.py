# task_1

with open("task_1_addition.txt", 'w', encoding='utf-8') as file:
    user_input = 'plug'
    while user_input != '':
        user_input = input('Enter something: ')
        file.write(f'{user_input}\n')
