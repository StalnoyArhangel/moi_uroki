# Пробная программа + проверка
"""
Большой коментарий
на несколько строк
"""

from colorama import init
from colorama import Fore
import random
import numexpr
import time
# s - количество секунд задержки


def pause(s):
    time.sleep(s)
    
    
init()
print(Fore.RED)
name = input("Как вас зовут?")
if bool(name) is True:
    print("Привет,", name)
    pause(1)
    print("Рад вас видеть")
    pause(1)
    print("Меня зовут, Саша")
    pause(1)
let = (
        0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40,
        45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 85, 86, 87, 88,
        89, 90, 95, 96, 97, 98, 99, 100
)
goda = (2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94)
god = (1, 21, 31, 41, 51, 61, 71, 81, 91)
old = input("Сколько вам лет?")
# Эта строка считает являются ли введённые данные числом и выдаёт булево значение.
old.isdigit()
if old.isdigit() is True:
    if 0 < int(old) < 6:
        print("Добро пожаловать, малыш")
    elif 6 <= int(old) < 18:
        print("Добро пожаловать, школота")
    elif 18 <= int(old) < 22:
        print("Добро пожаловать, студент")
    elif 22 <= int(old) < 60:
        print("Добро пожаловать, дорогой товарищ")
    elif int(old) >= 60:
        print("Добро пожаловать, пенсионер")
    elif int(old) == 0:
        print("Не может быть")
    time.sleep(1)
    if int(old) in let:
        print(f"Да,уж {name}  вам уже {old} лет, а вы всё ещё какой-то фигнёй занимаетесь")
    if int(old) in god:
        print(f"Да,уж {name}  вам уже {old} год, а вы всё ещё какой-то фигнёй занимаетесь")
    if int(old) in goda:
        print(f"Да,уж {name}  вам уже {old} года, а вы всё ещё какой-то фигнёй занимаетесь")
else:
    print("Что, так трудно ответить?")
    
pause(1)
print(Fore.BLUE)
# Рандомный бросок

random_number = random.randint(1, 6)
n = 3
while random_number:

    try:
        random_number = random.randint(1, 6)

        if n == 2 or 3:

            user_number = int(input(f"Угадай число(от 1 до 6), Твоё количество попыток '{n}' :"))

            if user_number == random_number:
                print(Fore.GREEN)
                print("Вы угадали! Вы супер круты!")
                break
            else:
                print("Вы не угадали!")
                print(f"Было загадано {random_number}")
            if n < 2:
                print("Вы просрали свои попытки")
                break
        n -= 1
    except ValueError:
        print("Ну как хотите")

print(Fore.MAGENTA)
# Калькулятор
print("А теперь калькулятор")
expr = input("Введите математическое выражение:")


def resultat():
    result = numexpr.evaluate(expr)
    print(f"Результат:{result}")
    
    
def tak_ne_rabotaet():
    print("Так не работает!")
    
    
try:
    resultat()
    while expr:
        expr = input("Введите математическое выражение:")
        try:
            resultat()
        except:
            tak_ne_rabotaet()
except:
    tak_ne_rabotaet()

    while expr:
        expr = input("Введите математическое выражение:")
        try:
            resultat()
        except:
            tak_ne_rabotaet()
print("Программа завершена")
pause(6)
