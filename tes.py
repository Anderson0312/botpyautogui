import pyautogui
pyautogui.PAUSE = 1
from selenium import webdriver
import time

# Inicializa o navegador (por exemplo, Chrome)
driver = webdriver.Chrome()


# Abre a página da web desejada
driver.get('https://anderson0312.github.io/MyPortifolio/')


# time.sleep(1)

# elemento = driver.find_element_by_id('id_do_elemento')

# print(pyautogui.position())


pyautogui.moveTo(70, 183, 2)

pyautogui.click(70, 183)


print(pyautogui.position())

pyautogui.moveTo(147, 601, 2)

pyautogui.click(147, 601)

# scroll down 10 "clicks"
pyautogui.scroll(-1000)


# element = driver.find_element_by_class_name('form-control')
# element.send_keys('Texto para inserir')

print(pyautogui.position())

time.sleep(1)

pyautogui.moveTo(157, 362, 2)

pyautogui.click(157, 362)

pyautogui.write('Olá, mundo!')