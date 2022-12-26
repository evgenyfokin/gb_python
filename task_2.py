# task_2

with open('task_2_addition.txt', encoding='utf-8') as file:
    received_data = file.readlines()
    print(f'The amount of lines: {len(received_data)}.')
    for i in received_data:
        line_list = i.split(' ')
        print(f"{received_data.index(i) + 1} line contains "
              f"{len(line_list)} words.")
