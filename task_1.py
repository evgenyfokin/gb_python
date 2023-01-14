my_list = ['разработка', 'сокет', 'декоратор']

for i in my_list:
    print(f"{i} => {type(i)}")
    encoded = i.encode('unicode-escape').decode('utf-8')
    print(f"{encoded} => {type(encoded)}")
    print('\n')
