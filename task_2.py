# task_2

user_time = int(input("Enter number of seconds: "))
hours = user_time // 3600
minutes = user_time // 60
seconds = user_time % 60
print(f"{hours}:{minutes}:{seconds}")