import pyautogui as pag
import time as t

pag.FAILSAFE = False
print(pag.position())
print(pag.size())
pag.PAUSE = 0.5
l = 2
v_len1 = int(input('количество видео 1 аккаунта '))
v_len2 = int(input('количество видео 2 аккаунта '))
v_len3 = int(input('количество видео 3 аккаунта '))
v_len4 = int(input('количество видео 4 аккаунта '))
v_len5 = int(input('количество видео 5 аккаунта '))
a_end = int(input('Выключить компьютер после работы? 1-да 2-нет'))
v_complaint = map(int, input('Введите какие жалобы использовать:'
                             '1) Жестокость 2) Пропаганда 3)Безопастность 4)Оскорбление 5) Порнография и нагота').split())


def cruelty():
    pag.moveTo(993, 224)  # жалоба
    pag.click()
    pag.moveTo(632, 628)  # жестокость и шок контент
    pag.click()
    pag.moveTo(1116, 962)  # отправить жалобу
    pag.click()
    t.sleep(l)


def hatred():
    pag.moveTo(993, 224)  # жалоба
    pag.click()
    pag.moveTo(992, 728)  # ропаганда ненависти
    pag.click()
    pag.moveTo(1116, 962)  # отправить жалобу
    pag.click()
    t.sleep(l)


def minor():
    pag.moveTo(993, 224)  # жалоба
    pag.click()
    pag.moveTo(1314, 880)  # скрол вниз
    pag.click()
    pag.moveTo(638, 603)  # безопастность несовершеннолетних
    pag.click()
    pag.moveTo(1116, 962)  # отправить жалобу
    pag.click()
    pag.moveTo(640, 525)  # нарушения несовершеннолетних
    pag.click()
    pag.moveTo(1116, 852)  # отправить жб
    pag.click()
    t.sleep(l)


def insult():
    pag.moveTo(993, 224)  # жалоба
    pag.click()
    pag.moveTo(634, 829)  # оскорбление
    pag.click()
    pag.moveTo(1128, 952)  # отправить жб
    pag.click()
    pag.moveTo(999, 597)  # прочее
    pag.click()
    pag.moveTo(1113, 840)  # отправить жб
    pag.click()
    t.sleep(l)


def nudity():
    pag.moveTo(993, 224)  # жалоба
    pag.click()
    pag.moveTo(990, 825)  # нагота и порнография
    pag.click()
    pag.moveTo(1120, 956)  # отправить жалобу
    pag.click()


def complains_all():
    def compain():
        pag.moveTo(983, 859)  # видео
        pag.click()

    if v_complaint == 1:
        cruelty()
    elif v_complaint == 2:
        hatred()
    elif v_complaint == 3:
        minor()
    elif v_complaint == 4:
        insult()
    elif v_complaint == 5:
        nudity()
    pag.moveTo(1041, 665)  # листать вниз
    pag.click()


for x in range(v_len1):
    pag.moveTo(1753, 17)  # свернуть
    pag.click()
    pag.moveTo(1112, 763)  # 1ссылка
    pag.click()
    t.sleep(5)
    complains_all()
if v_len2 == 0:
    raise ValueError("Скрипт завершен")
elif v_len2 > 0:
    def next_link():
        pag.moveTo(1753, 17)  # свернуть
        pag.click()
        pag.moveTo(997, 812)  # 2ссылка
        pag.click()
        t.sleep(5)


    for x in range(v_len2):
        complains_all()
if v_len3 == 0:
    raise ValueError("Скрипт завершен")
elif v_len3 > 0:
    pag.moveTo(1753, 17)  # свернуть
    pag.click()
    pag.moveTo(1017, 869)  # 3ссылка
    pag.click()
    t.sleep(5)
    for x in range(v_len3):
        complains_all()
if v_len4 == 0:
    raise ValueError("Скрипт завершен")
elif v_len4 > 0:
    pag.moveTo(1753, 17)  # свернуть
    pag.click()
    pag.moveTo(996, 919)  # 4ссылка
    pag.click()
    t.sleep(5)
    for x in range(v_len4):
        complains_all()
if v_len5 == 0:
    raise ValueError("Скрипт завершен")
elif v_len5 > 0:
    pag.moveTo(1753, 17)  # свернуть
    pag.click()
    pag.moveTo(992, 971)  # 5ссылка
    pag.click()
    t.sleep(5)
    for x in range(v_len5):
        complains_all()
if a_end == 1:
    pag.moveTo(0, 1079)  # выключение
    pag.click()
    pag.moveTo(28, 980)  # кнопка
    pag.click()
    pag.moveTo(123, 848)
    t.sleep(0.1)
    pag.click()
    pag.click()
    pag.click()
else:
    raise ValueError("Скрипт остановлен")
