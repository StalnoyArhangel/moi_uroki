# Для редактирования вывода, где sep-пробел между кортежем, а end - меняет перевод строки.
print("Привет друг!", "Приветствую тебя!", sep="***", end="    ")
print(5, 9, 0, sep="+")
# Внесение изменений в документ с помощью print
f = open('test2.txt', 'w')
print("Доброе утро дорогой друг!", file=f)
# Внесение записи с помощью метода write, где \n для перевода строки
f.write("Этот метод не добавляет перевод строки\n")
f.close()
# Цикл for выводит значения для переменной в перечень по строчно из заданной области
# Заданная область - range - создаёт кортеж с начальным значением, до конечного, и шагом( по умолчанию 1)
for xren in range(0, 6):
	print(xren)
# Заданная область - может быть представлена и списком
fruits = ['Лимоны', 'Яблоки', 'Киви', 'Ананас', 'Клубника']
for xren in fruits:
	print(xren)
# Вывод перечня через range
fruits = ['Лимоны', 'Яблоки', 'Киви', 'Ананас', 'Клубника']
for a in range(len(fruits)):
	print(fruits[a])
# Для переменной можно задать условие на вывод перечня
chisla = [-1, 8, 95, -67, 77, -55]
for xren in chisla:
	if xren > 0:
		print(xren)
# Если цикл for весь пройден, можно поставить условие
for xren in chisla:
	if xren == 77:
		print("Мы нашли 77!")
		# Прерывает вывод перечня при нахождении исходного числа, иначе выполнится else
		break
	print(xren)
# Выполняет условие если поиск по списку пройден полностью
else:
	print("Мы не нашли 77! Прости")
# Для прохода всех значений по прямоугольной области (таблице)
for x in range(0, 5):
	for y in range(0, 5):
		print(x, y, sep="x")
# Цикл for для подсчёта денег
kapital = 4333423
dohod = 292163
rashod = 165342
ostatok = kapital
for god in range(0, 5):
	ostatok = ostatok + (dohod - rashod * 1.2)
	print("Год %s Осталось денег %s" % (god, ostatok))
# dir позволяет получить информацию об объекте
morgan = 'пират'
print(dir(ostatok))
print(dir(morgan))
# Методы any и all
spisok2 = [True, False, True]
if all(spisok2):
	print("Все элементы True")
else:
	print("Не все элементы True")
if any(spisok2):
	print("Хотя бы один элемент True")

chisla2 = [1, 15, 50, 100, 200]
if any(number > 50 for number in chisla2):
	print("В списке есть число больше 50")
# list преобразует строку в список по буквенно
print(list("Привет друзья"))
