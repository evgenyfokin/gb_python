from timeit import timeit


def sum_user_nums(calc=0):
    print('Enter nums or finish the process by entering "="')
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


print(timeit('sum_user_nums()', setup='from __main__ import sum_user_nums',
             number=1000000))

"""До оптимизации -> 4.925487957999576"""
