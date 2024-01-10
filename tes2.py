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


# Iterar sobre os IDs e armazená-los em uma variável
for index, row in planilha.iterrows():
    id_selecionado = row['email']
    
    # Aqui você pode realizar as operações que deseja com o ID selecionado
    # Por exemplo, imprimir o ID selecionado
    print("ID selecionado:", id_selecionado)
    
    # Ou então, fazer alguma operação com o ID selecionado
    
    # Para sair do loop após o primeiro ID selecionado, remova o 'break' abaixo
    break  # Remove essa linha se deseja percorrer todos os IDs