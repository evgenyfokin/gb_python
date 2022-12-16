# task_1

def divide(num, divider):
    if divider == 0:
        return print("U can't divide by zero!")
    else:
        if num % divider > 0:
            return num / divider
        else:
            return num // divider


print(divide(int(input('Enter a divisible numb: ')),
             int(input('Enter a divider: '))))
