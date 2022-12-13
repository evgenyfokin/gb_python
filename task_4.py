# task4

user_input = input('Enter some words: ').split(' ')
for i in user_input:
    if len(i) > 10:
        print(i[0:10])
    else:
        print(i)
