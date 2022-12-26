# task_4

localized_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три',
                  'Four': 'Четыре'}
localized_list = []

with open('task_4_addition.txt', encoding='utf-8') as output_file:
    for i in output_file:
        i = i.split(' ', 1)
        print(i)
        localized_list.append(localized_dict[i[0]] + ' ' + i[1])
    print(localized_list)
    with open('task_4_1_addition.txt', 'w', encoding='utf-8') as input_file:
        input_file.writelines(localized_list)
