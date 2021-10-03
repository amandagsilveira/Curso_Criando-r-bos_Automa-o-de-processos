from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd

print('Iniciando o robô...\n')
arq = open('resultado.txt', 'w')
dominios = []
#para ler do excel
worksheet = xlrd.open_workbook('planilha_teste.xls')
sheet = worksheet.sheet_by_index(0)
for linha in range(0, 10):
    dominios.append(sheet.cell_value(linha, 0))

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://registro.br/')


for d in dominios:
    pesquisa = driver.find_element_by_id('is-avail-field')
    pesquisa.clear()  # limpa a barra de pesquisa
    pesquisa.send_keys(d)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)

    resultados = driver.find_elements_by_tag_name('strong')
    #import pdb; pdb.set_trace()
    texto = f'Domínio {d} {resultados[4].text}\n'
    arq.write(texto)

arq.close()
driver.close()

