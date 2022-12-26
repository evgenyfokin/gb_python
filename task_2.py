# task_2

def show_user_data(email, surname, birthday, current_city, name, phone):
    return (f'name: {name}; surname: {surname}; birthday: {birthday};'
            f' current city: {current_city}, email: {email}, phone: {phone}')


print(show_user_data(surname='Smith', phone='+0(101)0111010', name='Jeffrey',
                     email="jeffrey.smith@gb.com", current_city='Istanbul',
                     birthday='04.24.1996'))
