import pandas as pd
import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import Font
from openpyxl.chart import BarChart, Reference
import string

import pyautogui
pyautogui.PAUSE = 1
from selenium import webdriver
import time


planilha = pd.read_excel("MOCK_DATA.xlsx")

print(planilha.head())

# Inicializa o navegador (por exemplo, Chrome)
driver = webdriver.Chrome()


# Abre a página da web desejada
driver.get('https://anderson0312.github.io/MyPortifolio/')


# Iterar sobre os IDs e armazená-los em uma variável
for index, row in planilha.iterrows():
    id_selecionado = row['email']
    
    pyautogui.moveTo(70, 183, 0.2)

    pyautogui.click(70, 183)

    print(pyautogui.position())

    pyautogui.moveTo(147, 601, 0.2)

    pyautogui.click(147, 601)

    # scroll down 10 "clicks"
    pyautogui.scroll(-1000)


    time.sleep(0.2)

    pyautogui.moveTo(157, 362, 0.2)

    pyautogui.click(157, 362)

    pyautogui.write(id_selecionado)
    # Aqui você pode realizar as operações que deseja com o ID selecionado
    # Por exemplo, imprimir o ID selecionado
    print("ID selecionado:", id_selecionado)
    
    # Ou então, fazer alguma operação com o ID selecionado
    
    # Para sair do loop após o primeiro ID selecionado, remova o 'break' abaixo
    break # Remove essa linha se deseja percorrer todos os IDs