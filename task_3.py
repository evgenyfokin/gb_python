import re

pattern = 'regular[а-я]expression'
for i in ['attribute', 'класс', 'функция', 'type']:
    if re.match('[a-z]', i):
        print(f"'{i}' is good for byte converting!")
    else:
        print(f"'{i}' is not suitable for prefix 'b'")
