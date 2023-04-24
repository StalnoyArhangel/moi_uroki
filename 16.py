# Selenium третий сайт
import datetime

from selenium.webdriver import ActionChains
from avtorizaciya3 import login, password, adres
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome(executable_path='C:\\Python\\Uroki\\chromedriver.exe')


def login_chrome(login, password, adres):
	global browser
	browser.maximize_window()
	browser.implicitly_wait(5)
	browser.get(adres)
	time.sleep(random.randrange(1, 2))
	# Чекаем по вкладкам чекбокса
	check_box = browser.find_element(By.XPATH, "//span[@class='rct-checkbox']")
	check_box.click()
	vkladka = browser.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/button')
	vkladka.click()
	time.sleep(random.randrange(1, 2))
	# Меняем адрес, чтобы не парится с переходами
	adres = 'https://demoqa.com/radio-button'
	browser.get(adres)
	time.sleep(random.randrange(1, 2))
	# Нажимаем на радиобаттон, приходится выбирать локатор потому что бывают криворукие разработчики
	radiobutton = browser.find_element(By.XPATH, '//label[@for="yesRadio"]')
	radiobutton.click()
	# Работа с кнопками
	adres = 'https://demoqa.com/buttons'
	browser.get(adres)
	# Создаём новую переменную для работы с хромдрайвером
	action = ActionChains(browser)
	# Вбиваем локатор
	duble = browser.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
	# Используем метод для двойного клика (метод перформ для сохранения результата)
	action.double_click(duble).perform()
	# Для нажатия правой кнопкой мыши
	right_click = browser.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
	action.context_click(right_click).perform()


def close_browser():
	global browser
	browser.close()
	browser.quit()


login_chrome(login, password, adres)
time.sleep(1000)
close_browser()
