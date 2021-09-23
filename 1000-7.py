import time
import random
random_smile  = [('（Ω Д Ω）'),
						       ('ಥ‿ಥ'),
						   	('˚‧º·(˚˃⌓˂)‧º·˚') ,
						   	('(╯︵╰)'),
						   	('Ó╭╮Ò')]
print('.......Я')
time.sleep(1.5)
print('.......Гуль')
time.sleep(1.5)
print('Лелеле ми дай')
time.sleep(0.71)

x = 1000 - 7

while x > 7:
    time.sleep(0.04)
    print(f"{x} - 7 = {x-7}")
    x -= 7
print(random.choice(random_smile))
