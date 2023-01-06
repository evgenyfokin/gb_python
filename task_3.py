# task_3

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    user_num = int(input("Enter a divisible number: "))
    user_divisor = int(input("Enter a divisor: "))
    if user_divisor == 0:
        raise MyError("Divisor can't be zero!")
    else:
        result = user_num / user_divisor
except ValueError:
    print("You entered not a number!")
except MyError as err:
    print(err)
else:
    print(f"{user_num} / {user_divisor} = {result}")
