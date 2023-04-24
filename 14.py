# Создание интернет бота (или автоматизация с помощью веб.браузера)
# Импортируем из модуля авторизации логин, пароль и адрес страницы
from avtorizaciya import login, password, adres
# Имортируем из модуля Селениум вебдрайвер для запуска браузера
from selenium import webdriver
# Импортировал доп.модуль, так как была ошибка с поиском пути
from selenium.webdriver.chrome.service import Service
# Производим импорт ключей для нажатия клавиш внутри браузера
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# Импортируем модуль тайм для задержки вемени и рандом для случайных чисел
import time
import random
# Создаём глобальную переменную Браузер, чтобы работала в нескольких функциях
browser = None


# Добавил костыли из-за сбоя в поиске пути
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Python\\Uroki\\chromedriver.exe')
browser = webdriver.Chrome(options=options, service=g)

# Для В контакте


def login_chrome(login, password, adres):
	# Для этого прописываем, что переменная глобальная внутри каждой функции
	global browser
	# Выбираем браузер хром, указываем путь к файлу вебдрайвера(если он расположен в другой папке) - не работает
	# browser = webdriver.Chrome(executable_path='C:\\Python\\Uroki\\chromedriver.exe')
	# Запускает браузер в максимальном размере
	browser.maximize_window()
	# implicitly_wait даёт задержку перед вводом адресной строки, если браузер долго открывается
	browser.implicitly_wait(5)
	# Вводим адрес страницы
	browser.get(adres)
	# Выставляем время задержки
	time.sleep(random.randrange(1, 3))
	voity_button = browser.find_element(By.XPATH, '//*[@id="quick_login"]/button[1]')
	voity_button.click()
	time.sleep(3)
	_login = browser.find_element(By.XPATH, '//input[@id="index_email"]')
	_login.clear()
	_login.send_keys(login)
	voity_button2 = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/form/button[1]/span/span')
	voity_button2.click()
	_password = browser.find_element(By.XPATH, '//*[@placeholder="Введите пароль"]')
	_password.clear()
	_password.send_keys(password)
	prodolzhit_button = browser.find_element(By.XPATH, '// *[ @ class ="vkuiButton__in"]')
	prodolzhit_button.click()
	time.sleep(2)

	
	# Печечисление индикаторов поиска (только обязательно все большие буквы):
	# id - отрабатывает быстрее, чем xpath
	# name
	# class_name
	# xpath - универсальный поиск, но медленее
	# link_text
	# tag_name
	# css_selector

''' Для учебного сайта
def login_chrome(login, password, adres):
	global browser
	browser = webdriver.Chrome(executable_path='C:\\Python\\Uroki\\chromedriver.exe')
	browser.maximize_window()
	browser.implicitly_wait(5)
	browser.get(adres)
	time.sleep(random.randrange(1, 3))
	# Ищем по зацепку по имени
	_login = browser.find_element(By.NAME, 'user-name')
	# Записываю ещё возможные методы поиска по ID
	# _login = browser.find_element(By.ID, 'user-name')
	# Ищем по XPATH (уникальный локатор - супероружие :))
	
	# Чтобы определить элемент поиска для XPATH нажимаем просмотреть код два раза на нужном элементе,
	# затем нажимаем copy выбираем XPATH, нажимаем ctrl +f, и вставляем в появившееся поле. Затем этот элемент
	# вставляем в свой код в данном случае (//*[@id="user-name"])
	
	# _login = browser.find_element(By.XPATH, '//*[@id="user-name"]')  # Full XPATH
	# Используем уточнение ( какая-то хрень)
	# _login = browser.find_element(By.XPATH, '//input[@id="user-name"]')  # ID XPATH
	# Используем уточнение по любому элементу, если есть = (В конкретном случае по placeholder)
	#_login = browser.find_element(By.XPATH, '//input[@placeholder="Username"]')  # XPATH по любому элементу
	# Очищаем поле логина
	_login.clear()
	# Команда для ввода с помощью клавиш
	_login.send_keys(login)
	# Выставляем случайное время задержки от 1 до 2 секунд, через модуль рандом
	time.sleep(random.randrange(1, 2))
	# Для пароля воспользуемся поиском по CSS_SELECTOR(отвечает за оформление вебстраницы) правой кнопкой copy selector
	_password = browser.find_element(By.CSS_SELECTOR, '#password')  # CSS_SELECTOR
	_password.clear()
	_password.send_keys(password)
	_button_login = browser.find_element(By.XPATH, '//input[@value="Login"]')
	# Для нажатия на кнопку
	_button_login.click()
	print("Клик входа")
	time.sleep(random.randrange(1, 2))
	# Для скролинга
	browser.execute_script("window.scrollTo(0,500)")
	# Проверка успешной авторизации
	# Указываем искомый адрес(url) Важно стереть пробелы
	url = 'https://www.saucedemo.com/inventory.html'
	# Команда показывает на каком адресе сейчас находишься
	get_url = browser.current_url
	# Код для сравнения
	assert url == get_url
	print('GOOD BOY!')
	'''


def search_by_hashtag(hashtag):
	global browser
	# Забиваю переход на страницу с поиском по людям, где подставляю любое имя вместо хэштега
	browser.get(f"https://vk.com/search?c%5Bname%5D=1&c%5Bper_page%5D=40&c%5Bq%5D={hashtag}&c%5Bsection%5D=people")
	# Выбиираю только тех людей, что сейчас находятся на сайте
	seychas_na_sayte_button = browser.find_element(By.XPATH, "//*[@id='marital_filter']/div[2]/div[2]")
	seychas_na_sayte_button.click()
	time.sleep(2)
	# Тыкаю на первую фотку
	# Создал цикл до 20 человек
	a = 1
	while a >= 1:
		try:
			stroka = '//*[@id="results"]/div[%s]/div[1]/a'
			polzovatel = browser.find_element(By.XPATH, stroka % (a))
			polzovatel.click()
			(random.randrange(1, 3))
			try:
				lizevoe_foto = browser.find_element(By.XPATH,
												'//span[@class="AvatarRich AvatarRich--sz-150 AvatarRich--shadow"]')
				lizevoe_foto.click()
				(random.randrange(2, 3))
				like = browser.find_element(By.XPATH,
										'//*[@id="pv_narrow"]/div[1]/div[1]/div/div/div[1]/div[3]/div/div/a[1]/div[1]')
				like.click()
				(random.randrange(1, 3))
				browser.back()
				browser.back()
				a += 1
				print(a)
				time.sleep(1)
				if a >= 226122:
					break
			except:
				browser.back()
				a += 1
				print("Брак" + str(a))
				time.sleep(1)
				if a >= 226122:
					break
		except:
			a = 1
			while a >= 1:
				stroka = '//*[@id="search_more_results"]/div[%s]/div[1]/a'
				polzovatel = browser.find_element(By.XPATH, stroka % (a))
				polzovatel.click()
				(random.randrange(1, 3))
				try:
					lizevoe_foto = browser.find_element(By.XPATH,
														'//span[@class="AvatarRich AvatarRich--sz-150 AvatarRich--shadow"]')
					lizevoe_foto.click()
					(random.randrange(2, 3))
					like = browser.find_element(By.XPATH,
												'//*[@id="pv_narrow"]/div[1]/div[1]/div/div/div[1]/div[3]/div/div/a[1]/div[1]')
					like.click()
					(random.randrange(1, 3))
					browser.back()
					browser.back()
					a += 1
					print(a)
					time.sleep(1)
					if a >= 20:
						a = 2
				except:
					browser.back()
					a += 1
					print("Брак" + str(a))
					time.sleep(1)
					if a >= 20:
						a = 2

	"""# Делаю какую-то херню
	time.sleep(2)
	urls = []
	hrefs = browser.find_element(By.TAG_NAME, 'a')
	for item in hrefs:
		href = item.get_attribute('href')
		print(href)
		urls.append(href)
		print(href)
		"""
	# Для скролинга
	for i in range(1, 4):
		browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		time.sleep(1)


def close_browser():
	global browser
	# Эта команда закрывает текущую вкладку
	browser.close()
	# Эта команда закрывает браузер целиком
	browser.quit()


login_chrome(login, password, adres)
time.sleep(5)
search_by_hashtag('Анастасия')
# Для обновления страницы
browser.refresh()
time.sleep(1000)
close_browser()
