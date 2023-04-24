# Создал новый файл по Селениуму, чтобы не перегружать код (коментарии смотреть в 14 файле)
import datetime

from selenium.webdriver import ActionChains
from avtorizaciya2 import login, password, adres
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
browser = None

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Python\\Uroki\\chromedriver.exe')
browser = webdriver.Chrome(options=options, service=g)


def login_chrome(login, password, adres):
	global browser
	# browser = webdriver.Chrome(executable_path='C:\\Python\\Uroki\\chromedriver.exe')
	browser.maximize_window()
	browser.implicitly_wait(5)
	browser.get(adres)
	time.sleep(random.randrange(1, 3))
	# Ищем по зацепку по имени
	_login = browser.find_element(By.NAME, 'user-name')
	# Очищаем поле логина
	_login.clear()
	# Команда для ввода с помощью клавиш
	_login.send_keys(login)
	time.sleep(random.randrange(1, 3))
	# Стирает символ
	_login.send_keys(Keys.BACKSPACE)
	time.sleep(random.randrange(1, 3))
	_login.send_keys(Keys.BACKSPACE)
	time.sleep(random.randrange(1, 3))
	# Вводим любой текст, с помощью этой конструкции можно проверять программу на изменение данных
	_login.send_keys("er")
	# Выставляем случайное время задержки от 1 до 2 секунд, через модуль рандом
	time.sleep(random.randrange(1, 2))

	# Для пароля воспользуемся поиском по CSS_SELECTOR(отвечает за оформление вебстраницы) правой кнопкой copy selector
	_password = browser.find_element(By.CSS_SELECTOR, '#password')  # CSS_SELECTOR
	_password.clear()
	_password.send_keys(password)
	_button_login = browser.find_element(By.XPATH, '//input[@value="Login"]')
	# Используем клавишу вместо кнопки войти
	_password.send_keys(Keys.RETURN)
	# Для нажатия на кнопку
	# _button_login.click()
	# print("Клик входа")
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
	filter = browser.find_element(By.XPATH, "//select[@data-test='product_sort_container']")
	filter.click()
	print("Нажатие на фильтр")
	time.sleep(3)
	# Нажимает кнопку на клавиатуре вниз
	filter.send_keys(Keys.DOWN)
	# Нажимает кнопку выполнить
	filter.send_keys(Keys.RETURN)
	# Создаём переменную для работы с браузером (приходится скачивать ещё один модуль)
	action = ActionChains(browser)
	# Привязываю элемент который надо найти (храним наш локатор)
	krasnaya_futbolka = browser.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-onesie"]')
	time.sleep(2)
	# Переходим к элементу куда надо навестись и делаем скриншот (вместо скролинга)
	action.move_to_element(krasnaya_futbolka).perform()
	# Находим кнопку скрытого меню
	menu = browser.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
	menu.click()
	print('нажатие меню')
	time.sleep(2)
	link_about = browser.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
	link_about.click()
	print("Нажатие на кнопку Эбаут")


def close_browser():
	global browser
	browser.close()
	browser.quit()


login_chrome(login, password, adres)
# Для подтверждения выполненной работы делаем скриншот (название скрина, формат)
# Чтобы скриншот не перезаписывался добавим дату и время скрина в название
now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = "Sreenshot" + now_date + ".png"
# Вставляем путь сохранения скиншота
browser.save_screenshot('D:\\Python\\Uroki\\Sreen\\' + name_screenshot)
browser.back()
print("Возврат на предыдущую страницу")
time.sleep(2)
browser.forward()
print("Вернулись впеёд")
time.sleep(1000)
close_browser()
