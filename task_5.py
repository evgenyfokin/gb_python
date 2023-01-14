import subprocess
import chardet

for resource in ['ya.ru', 'youtube.com']:
    ARGS = ['ping', resource]
    PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
    i = 0
    '''Вынужден ввести счетчик, поскольку "ping" в терминале macOS бесконечен и
    завершается только после нажатия шортката ^+Z'''
    for line in PING.stdout:
        result = chardet.detect(line)
        print(line.decode(result['encoding']))
        i += 1
        if i > 4:
            break
