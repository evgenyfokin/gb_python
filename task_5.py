# task_5

income = int(input("Income: "))
expenses = int(input("Expenses: "))
result = income - expenses
if result < 0:
    print(f'Unprofitable ({result});')
else:
    print(f'Profitable ({result}); Benefit: {result / income * 100}%')
    