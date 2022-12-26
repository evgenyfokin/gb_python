# task_5

def sum_user_nums(calc=0):
    print('Enter nums or finish the process 'f'by entering "="')
    total = calc

    def get_sum(result):
        nums = input('Enter: ')
        if nums == '=':
            return print(f'The sum is {result}')
        for i in nums.split(' '):
            result += int(i)
        print(f'The sum is {result}')
        sum_user_nums(result)
    get_sum(total)


sum_user_nums()
