# task_1

my_dict = {1: 'doctor', 2: 'cashier', 3: 'janitor'}
my_tuple = (5, None, 'string', my_dict)
not_an_array = [5, None, 'string', my_dict]
my_list = [5, None, 'string', my_dict, my_tuple, not_an_array]
for i in my_list:
    print(type(i))
