import time
# time.sleep(1) - задержка по времени на вывод в секундах
# Цикл while
i = 1
while i >= 1:
    print("Привет,"+str(i))
    i += 1
    if i >= 6:
        break
print('Программа завершена')
number = 0
while number <= 10:
    number += 1
    if (number % 2) != 0:
        time.sleep(1)
        continue
    print("Чётное число" + str(number))

# Добавление в список
test = [5, 3, 2, 5, 6, 7]
test.append('5')
print('В массиве test  у нас находится ' + str(len(test)) + ' элементов')
# len считает кол-во символов с строке и элементов в списке
print(test)
# Убирает из списка, первое что соответствует поиску
test.remove('5')
print('В массиве test  у нас находится ' + str(len(test)) + ' элементов')
print(test)
# Выводит список с шагом 3
numbers = list(range(0, 10, 3))
print(numbers)
# Вывод каждой цифры в новую строку
numbers = [1, 2, 3, 4, 5]
# Сложный способ

i = 0
length = len(numbers) - 1
while i <= length:
    print(str(numbers[i]) + '-')
    i += 1
    time.sleep(1)
# Простой способ

for elements in numbers:
    print(str(elements) + '+')
    time.sleep(2)
# Третий способ
for a in range(len(numbers)):
    print(str(numbers[a]) + '!')
    time.sleep(2)
# Для выполнения повтора кода
for test2 in range(3):
    print("Привет")
    time.sleep(1)
# Для увеличения списка с помощью добавления другого
numbers.extend(test)
print(numbers)
# Для объединения двух списков в третий
spisok3 = numbers + test
print(spisok3)

# Задача по выводу из списка по индексу

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])

# Просто умножает число на 2


def multiply(number):
    print(number * 2)
    
multiply(5)

# Два способа работы функций
# Первый


def alex(name):
    print("Привет, " + name() + "!")
    
    
def read_name():
    return ":::" + input('Введите ваше имя:') + ":::"


alex(read_name)
# Второй


def alex(name):
    print("Привет, " + name + "!")
    
    
def read_name():
    return ":::" + input('Введите ваше имя:') + ":::"


alex(read_name())

input()
