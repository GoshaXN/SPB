import time
import math
import random
from rich import print
while True:
    print('Введите 1 для разложения квадратного уравнения на множители')
    print('Введите 2 для решения квадратного уравнения')
    print('Введите 3 для перевода скорости в разные велечины')
    print('Введите 4 для перевода валют')
    print('Введите 5 для нахождения толщины объемной фигуры')
    print('Введите 6 для работы с теплоемкостью')
    print('Введите 7 для расчета работы')
    print('Введите 8 для расчета мощности')
    x = int(input('Выбрать действие: '))
    if x == 1:
        print('Введите коэффициент A: ')
        A = float(input('='))
        if -100000000 < A < 100000000:
            print('Коэффициент правильный')
        else:
            raise ValueError("Ошибка,  Коэффициент должен находиться от -100000000, до 100000000")
        print('Введите коэффициент B')
        B = float(input('='))
        if -100000000 < B < 100000000:
            print('Коэффициент правильный')
        else:
            raise ValueError("Ошибка,  Коэффициент должен находиться от -100000000, до 100000000")
        print('Введите коэффициент C')
        C = float(input('='))
        if -100000000 < C < 100000000:
            print('Коэффициент правильный')
        else:
             raise ValueError("Ошибка,  Коэффициент должен находиться от -100000000, до 100000000")
        time.sleep(2)
        print('Начало решения')
        print('Решение:')
        D = B**2 - 4 * A * C
        print('Дискриминант равен', D)
        if D < 0:
            print('Рациональных корней нет')
        elif D == 0:
            print('Корень', -B / (2 * A))
        elif D > 0:
            Первыйкорень = (-B + math.sqrt(D)) / (2 * A)
            Второйкорень = (-B - math.sqrt(D)) / (2 * A)
            print('Первыйкорень: ', Первыйкорень)
            print('Второйкорень:', Второйкорень)
            print('Разложение по формуле: A(х - Первыйкорень)(х - Второйкорень')
        if  Первыйкорень < 0 and Второйкорень < 0:
            print(A,'(x +', (Первыйкорень * -1),')(х +', (Второйкорень * -1),')')
        elif Первыйкорень > 0 and Второйкорень > 0:
            print(A,'(х -', Первыйкорень,')(х+', Второйкорень)
        elif Первыйкорень > 0 and Второйкорень < 0:
            print(A,'(x -', Первыйкорень,')(х +',(Второйкорень * -1))
        elif Первыйкорень < 0 and Второйкорень > 0:
            print(A,'(x +',(Первыйкорень * -1),')(х-', Второйкорень)
    elif x == 2:
        print('Решение квадратных уравнений через дискриминант')
        print('Введите коэффициент A: ')
        A = float(input('='))
        if -100000000 < A < 100000000:
            print('Коэффициент правильный')
        else:
            raise ValueError("Ошибка,  Коэффициент должен находиться от -100000000, до 100000000")
        print('Введите коэффициент B')
        B = float(input('='))
        if -100000000 < B < 100000000:
            print('Коэффициент правильный')
        else:
            raise ValueError("Ошибка,  Коэффициент должен находиться от -100000000, до 100000000")
        print('Введите коэффициент C')
        C = float(input('='))
        if -100000000 < C < 100000000:
            print('Коэффициент правильный')
        else:
             raise ValueError("Ошибка,  Коэффициент должен находиться от -100000000, до 100000000")
        time.sleep(2)
        print('Начало решения')
        print('Решение:')
        print('_' * 20)
        D = B**2 - 4 * A * C
        Первыйкорень = (-B + math.sqrt(D)) / (2 * A)
        Второйкорень = (-B - math.sqrt(D)) / (2 * A)
        print('Дискриминант равен', D)
        if D < 0:
            print('Рациональных корней нет')
        elif D == 0:
            print('Корень', -B / (2 * A))
        elif D > 0:
            print('Первыйкорень: ', Первыйкорень)
            print('Второйкорень:', Второйкорень)
    elif x == 3:
        print('Скорость, и ее переводы')
        print('введите скорость')
        speed = float(input('='))
        y = int(input('Выбрать способ перевода: Введите 1 для перевода в км/ч, введите 2 для перевода в м/с'))
        if y == 1:
            speed_kmh = speed / 3.6
            print(speed_kmh)
        elif y ==2:
            speed_ms = speed * 3.6
            print(speed_ms)
    elif x == 4:
        print('Работа с валютой')
        dollar = 72.22
        euro = 87.33
        print('Введите требуемое конвертирование ')
        time.sleep(0.5)
        print('Введите 1 для перевода в рубли доллары или евро')
        print('Введите 2 для перевода в евро или доллары  рубли')
        value_vibor = int(input('>>> '))
        if value_vibor == 1:
            kolichestvo = float(input('Введите количество валюты: '))
            dollarov = kolichestvo / dollar
            print(dollarov,'Долларов')
            euro = kolichestvo / euro
            print(euro,'Евро')
        elif value_vibor == 2:
            kolichestvo = float(input('Введите количество валюты: '))
            rub_dollarov = kolichestvo * dollar
            print(rub_dollarov,'Рублей в долларах')
            rub_euro = kolichestvo * dollar
            print(rub_euro,'Рублей в евро')
    elif x == 5:
        print('Нахождение толщины фигуры объемной')
        plotnost = float(input('Введите плотность материала объекта в г/см³ '))
        mass = float(input('Введите массу в граммах '))
        v = float(input('Введите объем в см³ '))
        print('Введите 1 если ваша фигура это куб')
        print('Введите 2 если ваша фигура это шар')
        print('Введите 3 если ваша фигура это пирамида')
        print('Введите 4 если ваша фигура это параллелепипед')
        print('Введите 5 если ваша фигура это цилиндр ')
        print('Введите 6 если ваша фигура конус')
        vibor_figyri = int(input('>>> '))
        if vibor_figyri == 1:
            l_rebra = float(input('Введите длину ребра в см '))
            s_kyb = 6 *(l_rebra**2)
            tolshina = mass / (s_kyb * plotnost)
            print(tolshina)
        elif vibor_figyri ==2:
            r = float(input('Введите длину радиуса в сантиметрах '))
            s_shar = (4 * math.pi *(r**2))
            tolshina = mass / (s_shar * plotnost)
            print(tolshina)
        elif vibor_figyri ==3:
            l_osnovania = float(input('Введите длину основания в сантиметрах '))
            l_rebra = float(input('Введите длину ребра пирамиды в сантиметрах '))
            l_granei = int(input('Введите количество граней пирамиды '))
            s_piramidi = (((l_rebra**2)- ((l_osnovania / 2)**2))*l_granei)
            tolshina = mass / (s_piramidi * plotnost)
            print(tolshina)
        elif vibor_figyri ==4:
            a = float(input('Введите длину в см '))
            b = float(input('Введите ширину в см '))
            h = float(input('Введите высоту в см '))
            print(mass /((6 *(a * b) + 2 *(a * h))* plotnost))
        elif vibor_figyri == 5:
            r = float(input('Введите радиус в см '))
            h = float(input('Введите высоту в см '))
            print(mass / (((2 *math.pi *(r**2))+ (2 * math.pi * r * h))*plotnost))
        elif vibor_figyri ==6:
            r = float(input('Введите радиус основания в см '))
            l = float(input('введите длину от верхней точки до основания в см '))
            print(mass / ((math.pi * r * l)* plotnost))
    elif x ==6:
        print('Теплоемкость')
        c = float(input('Введите удельную теплоемкость в Дж/кг * °С '))
        t1 = float(input('Введите начальную температуру в °С '))
        t2 = float(input('Введите конечную температуру в °С '))
        mass = float(input('Введите массу в килограммах '))
        t3 = t2 - t1
        Q = c * mass * t3
        print(Q,'Джоулей')
        print('Перевести размерность энергии в более удобную? ')
        prodoljenie = int(input('Введите 1 если да введите 2 если нет '))
        if prodoljenie == 1:
            if 1000 < Q < 1000000:
                print(Q / 1000,'Килоджоулей')
            elif 1000000 < Q < 1000000000:
                print(Q / 1000000,'Мегаджоулей')
            elif Q > 1000000000:
                print(Q / 1000000000,'Гигаджоулей')
    elif x == 7:
        print('Расчет работы')
        mass = float(input('Введите массу в килограммах '))
        s = float(input('Введите расстояние в метрах '))
        g = 10
        f = g * mass
        A = f * s
        print(A,'Джоулей')
        print('Перевести размерность работы в более удобную? ')
        prodoljenie = int(input('Введите 1 если да введите 2 если нет '))
        if prodoljenie == 1:
            if 1000 < A < 1000000:
                print(A / 1000,'Килоджоулей')
            elif A > 1000000 < 1000000000:
                print(A / 1000000,'Мегаджоулей')
            elif A > 1000000000:
                print(A / 1000000000,'Гигаджоулей')
    elif x == 8:
        print('Расчет мощности')
        mass = float(input('Введите массу в килограммах '))
        s = float(input('Введите расстояние в метрах '))
        time = float(input('Введите количество секунд '))
        g = 10
        f = g * mass
        A = f * s
        N = A/time
        print('Перевести размерность мощности в более удобную?')
        prodoljenie = int(input('Введите 1 если да, введите 2 если нет '))
        if prodoljenie == 1:
            if 1000 < N < 1000000:
                print(N / 1000,'Киловат')
            elif N > 1000000 < 1000000000:
                print(N / 1000000,'Мегаватт')
            elif N > 1000000000:
                print(N / 1000000000,'Гигаватт')
