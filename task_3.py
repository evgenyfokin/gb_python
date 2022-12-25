# task_3

with open('task_3_addition.txt', encoding='utf-8') as file:
    received_data = file.readlines()
    low_salaries = []
    calc = 1
    salary_counter = 0
    for i in received_data:
        line = i.split(' ')
        if float(float(line[1])) < 20000:
            print(f"{calc}) {line[0]}")
            calc += 1
            salary_counter += float(line[1])
    print(f"Average salary: {salary_counter / calc}")
