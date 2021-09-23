import pyautogui as pag
import PIL
import time as t
pag.PAUSE = 0.9
схожесть=0.6
print((pag.position()))
link_v = input('Введите ссылку на аккаунт ')
video = int(input('Введите количество видео на которы нужно кинуть жалобы '))
#поисквидео = pag.locateOnScreen('PHOTOS/Поисквидео.png', confidence=0.5)
ссылка = pag.locateOnScreen('PHOTOS/link.png', confidence=схожесть)
жалоба = pag.locateOnScreen('PHOTOS/complain.png', confidence=схожесть)
жестокость = pag.locateOnScreen('PHOTOS/cruelty.png', confidence=схожесть)
отправить = pag.locateOnScreen('PHOTOS/send.png', confidence=схожесть)
безопастность = pag.locateOnScreen('PHOTOS/safety.png', confidence=схожесть)
нарушения = pag.locateOnScreen('PHOTOS/violations.png', confidence=схожесть)
скролл = pag.locateOnScreen('PHOTOS/scroll.png', confidence=схожесть)
пропаганда = pag.locateOnScreen('PHOTOS/propaganda.png', confidence=схожесть)
вниз = pag.locateOnScreen('PHOTOS/down.png', confidence=схожесть)
for x in range(video):
    pag.click(ссылка)
    t.sleep(5)
    pag.moveTo(992, 796)
    pag.click()
    t.sleep(1)
    pag.click(жалоба)
    pag.click(жестокость)
    pag.click(отправить)
    pag.click(жалоба)
    pag.click(пропаганда)
    pag.click(отправить)
    pag.click(жалоба)
    pag.doubleClick(скролл)
    pag.click(безопастность)
    pag.click(отправить)
    pag.click(нарушения)
    pag.click(отправить)
    pag.click(вниз)


