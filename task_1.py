# task_1) terminal command -> python3 task_1.py 8 500 600
from sys import argv

script_name, working_hours, hourly_charge, bonus = argv
print(f'Salary: {int(working_hours) * int(hourly_charge) + int(bonus)}')
