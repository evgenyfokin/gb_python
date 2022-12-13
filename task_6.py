# task_6

result = int(input("First day result: "))
goal = int(input("Your goal: "))
day = 1
while result < goal:
    result += result * 0.10
    day += 1
print(f"You'll reach it in {day} days")
