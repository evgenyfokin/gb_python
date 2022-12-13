# task2

user_num = int(input('Enter a number of month: '))
season_list = {1: [12, 1, 2, 'winter'],
               2: [3, 4, 5, 'spring'],
               3: [6, 7, 8, 'summer'],
               4: [9, 10, 11, 'fall']}
for month in season_list:
    if user_num in season_list.get(month):
        print(season_list.get(month)[3])
