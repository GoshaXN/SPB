import random
import time

while True:
    print('Введите 1 для генератора пароля')
    print('Введите 2 для генератора номера телефона')
    x = int(input('>>>'))
    if x == 1:
        abc = 'abcdefghijklmnopqrstuvwxyz'
        ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        special = '_-'
        parol = abc + ABC + numbers + special
        print('Генератор сложных паролей')
        len_pass = int(input('Введите длинну пароля '))
        raz = int(input('Введите количество рандомных паролей '))
        for i in range(raz):
            time.sleep(raz * 0.001)
            print(''.join(random.sample(parol, len_pass)))
    elif x == 2:
        numbers = '0123456789'
        nachala = ['8910',
                   '8915',
                   '8916',
                   '8917',
                   '8919',
                   '8985',
                   '8986',
                   '8903',
                   '8905',
                   '8906',
                   '8909',
                   '8962',
                   '8963',
                   '8964',
                   '8965',
                   '8966',
                   '8967',
                   '8968',
                   '8969',
                   '8980',
                   '8983',
                   '8986',
                   '8925',
                   '8926',
                   '8929',
                   '8936',
                   '8999',
                   '8901',
                   '8958',
                   '8977',
                   '8999',
                   '8995',
                   '8996',
                   '8999',
                   '8911',
                   '8912',
                   '8917',
                   '8919',
                   '8981',
                   '8982',
                   '8987',
                   '8988',
                   '8989',
                   '8904',
                   '8921',
                   '8922',
                   '8927',
                   '8929',
                   '8931',
                   '8932',
                   '8937',
                   '8939',
                   '8999',
                   '8900',
                   '8901',
                   '8902',
                   '8904',
                   '8908',
                   '8950',
                   '8951',
                   '8952',
                   '8953',
                   '8995',
                   '8991',
                   '8995',
                   '8996',
                   '8999']
        print('Генератор номеров')
        raz = int(input('Введите количество рандомных  номеров телефонов '))
        for i in range(raz):
            time.sleep(0.001)
            print(random.choice(nachala) + ''.join(random.sample(numbers, 7)))
