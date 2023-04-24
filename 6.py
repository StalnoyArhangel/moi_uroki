# Создаём функцию, где "с" имеет уже значение по умолчанию
def summa2(a, b, c=100):
	# return возвращает (выдаёт?) значение
	return a + b + c


# "c" идёт по умолчанию
ab = summa2(10, 20)
print("Сумма a + b =", ab)
# Пользователь сам определил "с".
ab = summa2(2, 30, 1000)
print("Сумма a + b =", ab)

# Классы и объекты.
# Создаём родительский класс


class PereferiyaDlyaKompyutera:
	# Создаём функцию которая сможет вызываться вне класса, для это пишем self в аргументе
	def kategoriya_tovara(self):
		print("Категория товара: Переферия для компьютера")
# Создадим у класса подкласы (или чайлдкклассы)


class Klaviatura (PereferiyaDlyaKompyutera):
	def tovar(self):
		print("Товар: Клавиатура")
	

class Mouse (PereferiyaDlyaKompyutera):
	# Для передачи в класс изначальных параметров, значений через функцию __init__
	def __init__(self, _price):
		# После этого можно создавать переменные, через self.
		self.my_price = _price
		
	def read_price(self):
		# Через f строку не удалось записать вывод (странно)
		print("Цена: %s рублей" % self.my_price)
		
	def write_price(self, _new_price):
		self.my_price = _new_price
		
	def tovar(self):
		print("Товар: Мышь")
	
		
obj1 = Mouse(205.57)
obj1.kategoriya_tovara()
obj1.tovar()
obj1.read_price()
# Для записи новой цены
obj1.write_price(505.73)
obj1.read_price()

obj2 = Mouse(333.15)
obj2.read_price()
