                # Guia Padrão da Mega-Sena
""" ##############################################################
                Você deve formar um jogo com:
1) 3 Números Pares e 3 Números Impares. Ex: 04 03 15 17 34 38
2) Jogar em 3 ou 4 quadrantes diferentes
3) Duas dezenas com inicio igual e duas diferentes. Ex: (10 12) (25 27) 47 58
4) Um número que se repete no final da dezena. Ex: 12 22
5) Opcional: Um par de Números invertidos. Ex: 03 30
6) Um número em atraso 0 e outro em atraso máximo (Consultar Tabela Gerada).
    ############################################################## """

# Web Scrapping com Python + Selenium

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import json

# 1. Pegar conteúdo HTML a partir da URL
url = "https://estatisticasdamegasena.com.br/megasena/estatisticas"

options = Options()
options.headless = True
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get(url)

# 1.1 Garantir que o servidor esteja carregado em 10 segundos
time.sleep(2)

# 1.2 Simular Cliques na Plataforma
rota_click1 = "/html/body/div/div/div[2]/div[1]/div/div[2]/div/div/a[5]"
rota_click2 = "/html/body/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/label/select/option[4]"
rota_click3 = "/html/body/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/table/thead/tr/th[6]"
driver.find_element_by_xpath(rota_click1).click()
time.sleep(2)
driver.find_element_by_xpath(rota_click2).click()
time.sleep(2)
driver.find_element_by_xpath(rota_click3).click()

# 1.3 Após o clique pegar o elemento que a gente quer
rota_table = "/html/body/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/table"
element = driver.find_element_by_xpath(rota_table)
html_content = element.get_attribute('outerHTML')

# 2. Parsear o conteúdo HTML - BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

# 3. Estruturar o conteúdo em um Dataframe - Pandas
data = pd.read_html(str(table))[0]

# 3.1 Tratar dados da tabela
data.drop('Último sorteio', inplace=True, axis=1)
data.drop('A cada x sorteios', inplace=True, axis=1)
data.drop('%', inplace=True, axis=1)
data.drop('Qtd', inplace=True, axis=1)
print(data)

# Opcional. Transformar os dados em um dicionário próprio
# Opcional. Converter e salvar em um arquivo JSON

driver.quit()