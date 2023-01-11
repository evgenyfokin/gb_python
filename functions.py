def divide(num, divider):
    try:
        if num % divider > 0:
            return num / divider
        else:
            return num // divider
    except ZeroDivisionError:
        return "U can't divide by zero!"


def my_func(num_1, num_2, num_3):
    if num_1 > num_2 & num_1 > num_3:
        if num_2 > num_3:
            return f'The sum of two biggest nums: {num_1 + num_2}'
        else:
            return f'The sum of two biggest nums: {num_1 + num_3}'
    else:
        return f'The sum of two biggest nums: {num_2 + num_3}'


def show_user_data(email, surname, birthday, current_city, name, phone):
    return (f'name: {name}; surname: {surname}; birthday: {birthday};'
            f' current city: {current_city}, email: {email}, phone: {phone}')


your_func = my_func

my_gen = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
