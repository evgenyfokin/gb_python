from chardet import detect


def convertor(file):
    with open(file, 'rb') as my_file:
        content_in_bytes = my_file.read()
        detected = detect(content_in_bytes)
        encoding = detected['encoding']
        content = content_in_bytes.decode(encoding)
    with open(file, 'w', encoding='utf-8') as my_file:
        my_file.write(content)


convertor('test_file.txt')

with open('test_file.txt', encoding='utf-8') as reading_file:
    print(reading_file.read())
